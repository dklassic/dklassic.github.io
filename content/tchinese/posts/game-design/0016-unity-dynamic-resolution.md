---
title: "Unity Built-in RP 動態解析度實作與 FSR2 實裝"
date: 2023-09-01T09:00:01+08:00
draft: false
tags: ["Unity"]
---

昨天突然意外在調查別的東西時，解開了我困擾近一年的一個問題，趕快寫下來紀錄。解決這個問題的同時，也讓我順勢可以加上原本已經打算捨棄掉的 FSR2 實裝。

# 問題

《[自動混亂](https://store.steampowered.com/app/1274830)》因為有很多奇怪的設計，我希望最大限度降低玩家對作品周邊要素的困擾，來增加玩家能享受遊戲本體的可能性。周邊的困擾太多的話可能會被轉嫁成對遊戲本身的厭惡，進而放大對特定設計的難以接受。

因此對三件事情特別在意處理：

- 效能需求：讓玩家盡量用怎樣的硬體都能跑得順
- 玩家體驗：不在我設計意圖內的遊戲設計，都以盡量優惠玩家為主
- 輔助功能：除了面對生理性要素的輔助，盡量允許玩家用他們想要的方式遊玩

總之《自動混亂》效能部份上整體來說算輕量，不過為了盡量提供幫助，試圖實作了「動態解析度」的機制。去年 11 月完成的動態解析度系統算是殘缺的，為了迴避特定的問題而加上了不理想的設計，這件事情後面會特別提到。

# 動態解析度

動態解析度顧名思義，解析度可以隨需求動態產生變化。由於大部分 GPU 負擔都跟解析度直接正比相關，實作動態解析度的話就等同於有個無條件避免 GPU 過度負載的機制。雖然最理想的情況下當然是對遊戲做好極端的最佳化，但動態解析度可以當作最後的防線。

Unity 有對鏡頭內建動態解析度系統，但是除了要求要使用 DX12、Vulkan 這兩個都還不太穩定的 Graphics API 以外（或者是在家用主機有對應的 API），實際上他的運作原理是完全的謎。

[我遊戲的渲染設計]({{< ref "/0013-rendering-pipeline" >}})上用了多個鏡頭堆疊，UI 是使用 Screen Space Camera 顯示，自然而然想說「只要不要勾選 UI 鏡頭的 Allow Dynamic Resolution 應該就可以維持 UI 在原生解析度」但是大錯特錯。實際上只要 depth 最低的鏡頭啟用就會影響到剩下的鏡頭，反過來說最下面的沒啟用上面的就全都啟動不了的詭異狀況。

這問題也另外有多層面的影響，並不是只是透過這個官方支援的 DRS 做法才會有問題，而是看來是整個渲染流程的問題。
目前我知道 Scale 鏡頭解析度的方式有這幾種：
- **ScalableBufferManager**，就是官方的 DRS 主要實作手段，啟用 Allow Dynamic Resolution 的鏡頭會被這個影響
- **Camera Rect**，在 OnPreRender 降低 Rect 大小，然後在 OnRenderImage 的時候改回原始大小
上面這兩個都會有那個最下面的鏡頭調整就會影響到上面所有鏡頭的情境。
- **Render Texture**，就是手動調整 Render Texture 大小來配合；如果有在 Render Texture 上勾選 Dynamically Scalable 的話，ScalableBufferManager 也會自動 Scale

總之以下提兩個可以確保 UI 不會被影響手段：

- **UI 使用 ScreenOverlay**：就是這麼簡單，改用 ScreenOverlay 的話 UI 就不會被底層鏡頭影響到。
- **使用 Render Texture 顯示遊戲畫面**：在 UI 鏡頭放著 Render Texture 顯示，我這邊因為渲染設計會用到超過標準亮度的值，目前沒有看到任何 Render Texture 的格式可以正確儲存結果，變成如果我要用這個方式的話得重新設計渲染方式。

兩個方法都對我來說會有點困擾（一個要重新設計遊戲畫面渲染方式，一個要重新設計 UI 的互動與渲染方式），所以從去年 11 月實作完就就一直在掛心著調查有沒有解套方案。而就在昨天終於找到處理方式了。

## Unity 的 Camera Stack Link

在調查無關的事情時，意外得知了 Unity 有個行為：會自動將設定一致 Viewport 的鏡頭 Link 起來，在黑箱中把分散的鏡頭綁成一個 Camera Stack。因而導致了只要調整底層就會同步改變頂層鏡頭的結果。

也就是說......將 Viewport 微妙地設定不同就行了。我將三個鏡頭分別設定為 W=1、1.000001、0.999999 之後，這個問題就迎刃而解了。

謝了，Unity，謝了。

## 調整解析度的判定

當然有了調整解析度的手段，再來就是要怎麼判斷該增加或者減少解析度了。

我的實作方式是直接參考[官方的範例](https://github.com/Unity-Technologies/DynamicResolutionSample)，在降低解析度上算激進，但畢竟我把動態解析度當成最後防線同時又允許玩家自由開關，所以就以範例的演算法為主。簡單來說 GPU 負載如果逐漸增加，而且上一幀的費時快要比目標時間長的時候，就逐步降低解析度；反之則增加。

其中官方的範例中提供了可以使用 [`UnityEngine.Rendering.FrameTimingManager`](https://docs.unity3d.com/ScriptReference/FrameTimingManager.html) 來取得 GPU 費時的資訊，但是只有在 DX12、Vulkan 跟 Metal 上能取得所需要的資訊。為了能增加可用性，我為了 DX11 實作了 根據 `Time.unscaledDeltaTime` 判斷的版本（也就是 GPU time 與 CPU time 較長的那一個），但當然就不一定能正確應對 GPU 負載調整渲染壓力，可能會在 CPU 負載高的時候誤判。

# FSR2 實裝

因為昨晚意外解決了前述的問題，讓我的遊戲可以順便把 FSR2 也實裝進來，驗證一下成效。使用的實作來源是這個[開源專案 FSR2Unity](https://github.com/ndepoel/FSR2Unity)。

除了同動態解析度一樣是降低解析度換取 GPU 壓力降低而不會對 CPU 瓶頸有所幫助以外，FSR2 因為目標同時有反鋸齒與提升體感解析度的效果，會附帶額外的計算壓力。這個計算壓力會隨著目標解析度的提升而大幅增加，可以參考[這張官方的大表](https://github.com/GPUOpen-Effects/FidelityFX-FSR2#performance)理解一下額外的需求大約是多少。

以下直接以成果來解說一下觀察到的性質。

## Ultra Performance（3x 縮放）

720p 原生：

![720p native](/images/posts/game-design/0016/720.png)

720p -> 2160p FSR2：

![720p FSR](/images/posts/game-design/0016/720FSR2.png)

效果非常顯著，反鋸齒成效跟看起來有更高解析度的感覺都有做到。當然遠遠看起來不像是 2160p 原生影像，但體感品質是遠高於 720p 的。

至於因為使用的是超低原生解析度（1/9 面積），GPU 負載就顯著降低。

## Quality（1.5x 縮放）

1440p 原生：

![1440p native](/images/posts/game-design/0016/1440.png)

1440p -> 2160p FSR2：

![1440p FSR](/images/posts/game-design/0016/1440FSR2.png)

到這程度就可以說是見仁見智。1440p 當 2160p 看本來就還行，FSR2 的性質就沒那麼顯著的優勢：

- 有反鋸齒，但因為時域性性質看起來總是偏糊一點
- 沒有顯著的提高解析度的感覺
- 效能不算真的有省
- 但是也有時域穩定性

## Ultra Quality（1.3x 縮放）

用到這程度的時候，FSR2 的大致性質是：

- 總效能需求已經比原生更高了
- 視覺品質應該能算是客觀比原生好
- 有時域穩定性
- 比較不會有 TAA 的糊感

Quality 跟 Ultra Quality 可以當個比原生 Unity TAA 更好的選項了，甚至可以嘗試硬實作類 DLAA＝1x 解析度去跑 FSR2，應該可以弄出很高品質但也超貴的成果。

## 算是結論

總之應該是可用性非常高了。

尤其我的做法類似動態解析度中會介面維持原生，我只有底層鏡頭渲染背景用 FSR2、遊戲邏輯相關物件都用原生，就會在正常視距更難發現品質差異。

不過每個專案性質還是會產生出不太一樣的結果，如果有試著在自己專案玩出有趣的差異求分享 XD

自動混亂的例子中因為幾乎極簡風設計使得畫面整體偏乾淨，FSR2 的視覺成果非常顯著，就算是動態下也看起來非常乾淨；對於其他專案，尤其是第一人稱的視角下就很難在動態下也取得如此顯著的視覺品質提升。

## 題外討論

這個 FSR2 實作支援用 `ScalableBufferManager` 進行 FSR2 動態解析度組合技，試著實裝起來其實成效也不錯，基本上會達到解析度調整時幾乎看不出來的效果。

但是在我的實作下 ScalableBufferManager 會很開心地做一些我意料之外的 RT Scaling，導致視覺錯誤出現，所以就放棄實裝，謝了 Unity。