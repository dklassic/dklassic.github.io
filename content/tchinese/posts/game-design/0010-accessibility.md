---
title: "無關遊戲卻至關重要的輔助設計"
date: 2022-08-19T22:31:29+08:00
draft: false
tags: ["遊戲設計"]
---

設計出好玩的遊戲、做出精彩的視覺、準備精緻的樂曲、寫出動人的故事，一般來說想著遊戲設計的時候多半想著的是這些內容。但無論遊戲本身做得再好，如果玩家沒有辦法順利享受到就本末倒置了。

這些無關遊戲卻至關重要的遊戲設計遍地都是，在大部分開發中卻很容易就會被忽視。舉個最切實的例子：製作出全世界最好看的遊戲，但是只有頂尖的電腦才能夠順利執行。如此一來無論遊戲內容有多堅實，都變得毫無意義。

在《自動混亂》開發收尾的期間，大部分工作內容都是如此：著重在降低玩家因為跟遊戲內容無關的理由而可能會遭遇的挫敗感。這篇文章是趁機整理一下自己做了哪些內容，順便整理出一些相關資源（Unity 為主）以供他人或自己未來備考。

以下流水帳：

# 效能相關

效能的主題不外乎是考慮玩家使用各種不同強度的硬體，為了讓玩家無論使用什麼硬體都能順暢執行而必須在程式撰寫上盡量使用效能需求最低的寫法。細項能做的最佳化太多而難以逐一提起，在這邊想特別提兩件事：

## 最佳化使用硬體

《自動混亂》雖然乍看之下是款視覺很簡單的遊戲，但是因為一些因素實際上意外地吃效能：

- 採用完全無接縫的關卡表現
- 能夠即時應對玩家動作反應的 AI
- 大量留存於場地上具備物理互動能力的物件

因此不得不全力善用玩家硬體，例如說：

- 使用多核心去做大量 Raycast 判定（參考 [Raycast Command](https://docs.unity3d.com/ScriptReference/RaycastCommand.html)）
- 沒有迫切需求的場域就將工作分散在好幾個 frame 執行（參考[時間切割](http://allenchou.net/2021/05/time-slicing-chinese/)）
- 物件脫離玩家視野之後就盡快處理掉
- 使用所謂的 Object Pooling 的方式去降低反覆生成、破壞物件的資源需求（參考 [ObjectPooling](https://docs.unity3d.com/ScriptReference/Pool.ObjectPool_1.html)）

## 動態解析度

> 參考 [Dynamic Resolution Sample](https://github.com/Unity-Technologies/DynamicResolutionSample)

動態解析度即是根據遊戲執行狀況，持續改變解析度來確保 FPS 可以達到指定值。對於相較沒有反應需求的遊戲來說可能不算重要，但是《自動混亂》的戰鬥節奏非常快，我想要盡量確保玩家不會受到影響。

然而動態解析度雖然聽起來像是無敵解，也要注意兩件事：

- Unity 只有在使用 DX12、Vulkan 兩種圖形 API 的情況下才能使用動態解析度，但兩者的表現都不如 DX11 穩定
- 要在 DX11 實現必須用稍微迂迴點的 Render Texture 去應對
- 動態解析度基本上只能解決 GPU 效能不足的問題，解決不了 CPU 效能不足的問題

![Dynamic Resolution](/images/posts/game-design/0010/1.png)

基本原理就是看看 GPU、CPU 計算需要的時間，發現越算越久的時候就降低解析度。另外編輯器內 GPU 時間偵測有問題所以顯示為 0。

# 體驗改良相關

體驗改良相關的內容雖然比較不容易影響到遊戲本身的體驗，但對於追求最佳體驗不想要被其他事物干擾的玩家來說，仍然是非常重要的設計。

## 顯示器選擇

> 參考 [Screen.MoveMainWindowTo](https://docs.unity3d.com/ScriptReference/Screen.MoveMainWindowTo.html) 與[官方範例](https://github.com/Unity-Technologies/DesktopSamples/tree/master/MoveWindowSample/)

雖然讓玩家視窗化後手動搬動是個選項，但是完全比不上遊戲內官方原生的自動搬動系統。

Unity 在 2021.2.0a16 之後支援了官方的 MoveMainWindowTo 系統，自動搬動系統也可以方便不是即時讀取現在資訊更新的開發者手動更新解析度、幀率設定等相關選項，降低玩家必須要反覆重開遊戲的困擾。

## 解析度設定

> 參考 [Resolutions](https://docs.unity3d.com/ScriptReference/Screen-resolutions.html) 但這文件有夠爛

允許玩家自由地調整解析度，尤其是當開發者使用的螢幕如果限定特定比例（16:9）或解析度（1920x1080）時，很容易會寫出意外限制玩家的結果。例如說忽視了不同比例的螢幕的視覺體驗，或者單純因為沒想到而不允許玩家使用更高的解析度。

Unity 的解析度也實際上會同步提供所有支援的「螢幕更新率」，最理想的情況下是把螢幕更新率與解析度分開設定，而不是一股腦地將所有解析度塞在一起，構成非常長的清單。

## 全螢幕設定

> 參考 [Fullscreen Mode](https://docs.unity3d.com/ScriptReference/FullScreenMode.html)

螢幕可以用「視窗化」、「無邊框視窗」、「全螢幕」三種設定。雖然大部分想像中玩家都應該會使用方便的「視窗化」與效能最好的「全螢幕」，但是「無邊框視窗」可以允許有全螢幕的畫面，卻仍可以自由使用 Alt-Tab 等切換功能快速切換螢幕。相較之下「全螢幕」在進行切換時會有相當長的延遲。

值得注意的是 MacOS 有自己獨特的「無邊框視窗」設定叫做 Maximized Window。

## 幀率限制設定

> 參考 [VsyncCount](https://docs.unity3d.com/ScriptReference/QualitySettings-vSyncCount.html) 跟 [TargetFrameRate](https://docs.unity3d.com/ScriptReference/Application-targetFrameRate.html)

比起很高但是不穩定的 FPS，較低但是穩定的 FPS 可以提供比較好的遊戲體驗。提供幀率限制設定選項，也可以幫助硬體不夠好的玩家還是能藉此有合理的遊玩體驗。

Unity 的實作方式上有兩種：
- Vsync Count 是開啟垂直同步的情況下，強迫遊戲以完整更新率、1/2 更新率、1/3 更新率或 1/4 更新率執行。以 60Hz 螢幕為例，分別代表鎖定在 60FPS、30FPS、20FPS 以及 15FPS。
- TargetFrameRate 是在垂直同步關閉的情況下，嘗試要求遊戲以指定更新率執行。這個寫法的好處是能指定任意更新率。
    
    對於擁有 FreeSync/GSync 的螢幕來說，可能比起只有完整更新率與 1/2 更新率這種情況下更實用（例如說 120Hz 螢幕只使用 Vsync 實作等於只有 120FPS 或 60FPS 可用，但使用這個方式就可以指定 100FPS 發揮 FreeSync/GSync）。

《自動混亂》會根據偵測到的螢幕最高更新率去給指定值：

![Frame cap](/images/posts/game-design/0010/2.png)

不過 Unity 有時候會偵測到奇怪的數字，所以無法被 4 整除的時候就只顯示 1/2、1/3、1/4 更新率。

## 螢幕比例鎖定

> 參考一種[很簡潔的實作方式](https://forum.unity.com/threads/how-to-force-black-bar-widescreen.21238/#post-6428252)

根據基本實作方式不同，可能要在意的是「解除比例鎖定」的選項。《自動混亂》實作時因為想要盡量開放像 21:9、32:9 這種超寬螢幕的體驗，所以主要實作傾向讓所有螢幕比例都能照實使用。

也因此必須另外實作一個機制讓想要確保體驗正常的人（例如說我沒辦法保證 1:1 螢幕的介面不會壞掉），可以強制鎖定在 16:9 的畫面。

![ratio lock](/images/posts/game-design/0010/3.png)

雖然我的遊戲原則上允許自由比例，但是大多設計還是以 16:9 為基礎製作的，所以加入鎖定為 16:9 的選項。

## 音量設定

最理想情況下是分開總音量、音樂、音效、配音的設定，甚至在調整的時候會有參考音效播放輔助確認成果而不需要來回切換。

## 雜訊效果
《自動混亂》使用後製雜訊效果來提升乍看之下的視覺品質。然而雖然有乍看之下的體驗提升，使用的效能也不高，雜訊效果的存在會導致想要錄影的人的影片大小暴增。
允許關閉雜訊效果可以讓內容創作者的生活好過很多。

## 高動態範圍的螢幕輸出

> 參考 [HDROutputSettings](https://docs.unity3d.com/ScriptReference/HDROutputSettings.html)

使用高動態範圍渲染可以讓遊戲的亮、暗處不會直接失去所有細節。對於支援 HDR 並且擁有更高鋒值亮度螢幕的玩家，能夠開啟「高動態範圍的螢幕輸出」就可以看到更加亮眼的畫面表現。

在 Built-in 渲染流程中，需要使用 Post Processing Tonemapper 開啟 High Dynamic Range，在 PlayerSetting 裡面允許輸出 HDR 畫面，最後使用程式的 HDROutputSettings.main.available 確認螢幕支援與否，並且用 HDROutputSettings.main.RequestHDRModeChange(true) 開啟。

## 亮度設定

每個螢幕的亮度校正都不太一樣，所以開放玩家可以自行調整畫面亮度可以大幅改善一些玩家的體驗。

我的實作方式是使用 Post Processing Tonemapper 的 Exposure 去調整。

## 符合目前操作裝置的按鍵圖示
玩家可以使用的遊玩裝置很多，如果能夠配合玩家使用的裝置去改變圖示的話，會讓玩家的體驗好很多。

基本情況下至少建議包含 Xbox 手把，很理想的情況下可以再考慮納入 PS 手把、NS 手把。

網路上目前最有名的範用圖示是[全平台都有包含的這個](https://thoseawesomeguys.com/prompts/)，我個人則是使用這個[字體檔案](https://github.com/Shinmera/promptfont/)來處理。

![button prompt](/images/posts/game-design/0010/4.png)

使用正確的圖示顯示能讓玩家體驗更好。

# 輔助性功能

輔助性功能想要幫助的是生理上需要協助才能正常遊玩的人，也就是「沒有這些功能就可能會有人完全玩不了」。

## 畫面震動

畫面震動是一種能幫助很多遊戲體驗提升的手段，《自動混亂》的打擊感相當程度源於畫面震動效果。

但不是所有人都喜歡，尤其對很多人來說可能會造成額外的頭暈。允許玩家開關相關效果會比較好。

## 色盲輔助

> 參考[色盲模擬器](https://www.color-blindness.com/coblis-color-blindness-simulator/)跟文章 [Purple and orange are the solution](https://montoliu.naukas.com/2021/11/18/color-blindness-purple-and-orange-are-the-solution/)

根據遊戲內容不一定需要實作。《自動混亂》因為有部分遊戲機制跟顏色有關，因此額外製作了一個粗淺的輔助系統。實際上也可以外掛濾鏡，但效果通常不是很好，最好從一開始就做好顏色的控制。

如果有遊戲機制需要仰賴顏色的話，不妨有空的時候確認一下各種色盲會不會有識別困難。甚至能開放自訂顏色會更好。

《自動混亂》中門的顏色會影響判斷，雖然極度簡陋，但比起直接看不出差異還是有幫助：

![color blind](/images/posts/game-design/0010/5.png)

## 高對比度用色

主要是幫助色弱與輕度盲人仍然能享受遊戲。《自動混亂》實作的方式是使用 Post Processing Tonemapper 強制降低背景亮度，並且改變特定物件的用色強化識別度：

![high contrast](/images/posts/game-design/0010/6.png)

《自動混亂》本來對比度就很高，而左圖是進一步降低背景亮度的結果。

但更理想的情境可能是像《最後生還者 2》的實作：

![high contrast](/images/posts/game-design/0010/7.webp)

## 自訂按鍵

> 參考 [LoadBindingOverridesFromJson](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.1/api/UnityEngine.InputSystem.InputActionRebindingExtensions.html)、[SaveBindingOverridesAsJson](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.1/manual/ActionBindings.html)、[PerformInteractiveRebinding](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.1/manual/ActionBindings.html)，都要在頁面另外搜尋關鍵字，還有文件寫超爛 XD

不是每個人都能接受用 WASD 操控，每個使用者也可能根據各自的身體狀況有偏好的操作方式。

如果按鍵可以允許玩家完全重新分配的話，能夠讓所有人都更好享受遊戲內容。

《自動混亂》的操作系統使用 Unity 新的 Input System，其中有個功能叫做 LoadBindingOverridesFromJson 可以快速地載入設定，並且有 PerformInteractiveRebinding 能直接讀取玩家所另外按下的按鍵。最後可以使用 SaveBindingOverridesAsJson 存成字串。

建議偵測玩家使用的是手把還是鍵鼠，分開兩種裝置類型的設定值。

## 手把震動

手把震動聽起來是個小功能，但是對於握力偏低的使用者來說，能夠完全關閉或調整強度都會有幫助。

## 手把輔助瞄準

> 參考 [Designing a Better Aim Assist for 2D Games](https://youtu.be/yGci-Lb87zs)

就是，輔助瞄準，畢竟手把很難瞄準。能另外開放強度調整，讓玩家有關閉的選項也很好。

## 鍵鼠／手把操控切換與裝置特定功能

讓玩家可以自動偵測使用的裝置很好，而相關機制可能也會失靈，所以能同步加入完全只使用特定操作裝置的功能會比較好。

至於裝置特定功能想要提的是在《自動混亂》中，因為鍵盤滑鼠移動只能使用 WASD，導致玩家衝刺方向受到八方向的限制。因此加入了一個選項叫做「往滑鼠方向衝刺」，讓有需要的玩家可以使用。

# 結語

這些非常零碎的功能雖然都與遊戲本身毫無關聯，實作起來也算是相當曠工費時。但是作為遊戲開發者，最糟糕的情形莫過於因為無關遊戲內容的原因導致玩家無法享受遊戲。例如說因為 Bug 的存在會導致玩家沒有辦法專心享受過場動畫，因為這些細小的問題而破壞掉玩家的體驗就得不償失了。也因此為了盡量讓所有玩家都能順利享受，這些功能的正確實作就非常重要。

我自己是做起來其實還挺開心的，但查資料也算是花了不少時間。於是決定寫一篇文章來記錄自己做了些什麼，並且整理了一些資源，幫助自己，也看看有沒有機會幫助他人。

以上提供參考。