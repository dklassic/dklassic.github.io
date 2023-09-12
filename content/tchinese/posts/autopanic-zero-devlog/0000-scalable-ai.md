---
title: "規模化 AI 設計"
date: 2022-12-18T10:00:23+08:00
draft: false
tags: ["自動混亂零式","遊戲設計"]
---

《自動混亂》的設計重點之一是「恰到好處」，體現在戰鬥設計上就有：

- 限縮遊戲環境，以房間制進行
- 限制敵人登場數量
- 比起完全可靠的機制，只要玩家看不出有問題就好

《自動混亂：零式》則要面對原作十倍以上的敵人數量級。

![autopanic](/images/posts/autopanic-zero-devlog/0000/1.jpg "《自動混亂》中，關卡板塊最多規劃到 8x8 的程度，同時登場敵人最多八個")

![autopanic zero](/images/posts/autopanic-zero-devlog/0000/2.jpg "《自動混亂：零式》的敵人總量顯著多很多")

製作《自動混亂：零式》時，目的已經先被決定了：極大量敵人的戰鬥。也因此不存在什麼繞路手段，就只能直球對決面對。

總之這邊介紹一下為了《零式》的大量敵人做了什麼調整，而這樣的設計又為原作帶來了怎樣的回饋。我們先來重新介紹一下原作的敵人 AI 邏輯。

# 《自動混亂》的 AI 運作流程與統一管理化架構

原作的敵人 AI 基本上可以拆為：`Enemy`、`EnemyController` 與 `EnemyBehavior` 三個要素：

- `Enemy` 定義最基本的可互動性，以《自動混亂》來說就是互相傷害的互動與血量、狀態的紀錄為主
- `EnemyController` 驅動實際的移動、視覺的表現
- `EnemyBehaviour` 字面上負責決定角色接下來的行動，例如使用武器、決定移動與轉向

`Enemy` 因為只有狀態紀錄，是個純資料的存在。而另外兩組程式各自跑在自己 Update() 裡進行更新，也不算有特別的理由，畢竟這就是最常態的 Unity 程式寫法，自然而然寫成了這樣。

除此之外還有一些獨立要素一樣自己跑在自己的 Update() 裡，像是：

- 控制角色圖像的程式（圖像生成、圖像變化、圖像的閒置動畫）
- 控制程序性動畫的程式

總之雖然沒有整理得很乾淨，但應該算是簡單好懂也能順利執行的程式。不過實際上使用 Unity 的 Update() 進行更新的效率並不是很高，對於總量不多的遊戲來說難以注意到，但一旦將 Update() 的數量級大增，效率之差就會顯現出來。（參考[官方自己的測試結果](https://blog.unity.com/engine-platform/10000-update-calls)）

此外，使用 Update() 更新的話就難以預期這些程式的執行順序，對於某些強耦合的系統來說會構成問題。將之執行順序管理起來會對於長遠來說程式可靠性更有幫助。

之前本來就實作了一個 `EnemyManager` 來統一管理敵人的生成與破壞，也因此改在這邊統一管理所有元件的更新：

![manager](/images/posts/autopanic-zero-devlog/0000/3.png)

原先交給 `EnemyBehaviour` 更新的周邊環境碰撞偵測獨立拉出來一項為 EnemyVectorUpdate()，這邊就不多解釋運作方式，可以參考過去寫過的[低效能需求 AI 介紹]({{< ref "/0004-low-cost-ai" >}})。

然後把一些視覺相關的更新都統一包進去給 `EnemyController` 一起更新，畢竟我遊戲中大多數視覺更新都跟移動機制本身有關，所以交給負責移動的 `EnemyController` 統一更新也算合適。

# 多核心化

由於我的 AI 基本上仰賴大量 Raycast 掌握環境狀態，所以讓 100 個敵人 AI 隨機閒晃更新起來會長這樣：

![original](/images/posts/autopanic-zero-devlog/0000/4.png)

單顆核心直接被橘色的 Raycast 塞滿，在原作可能還好，但對於大量敵人的《零式》就是個問題了。在閱讀過 cjcat 的「[延遲蒐集結果](http://allenchou.net/2021/05/delayed-result-gathering-chinese/)」後，我決定嘗試將 Raycast 改以 Job 執行，善用現代處理器的多核心。

首先將每個敵人各自的更新方式多執行緒化：

![threaded](/images/posts/autopanic-zero-devlog/0000/5.png)

可以看到下面一排零碎的橘色片段，證明了這些 Raycast 確實成功交給了多個核心去分開執行。

看起來執行時間反而比較長可以有幾種解讀方式：

- 單純測試環境隨機性造成
- 過少的 Raycast 指令數去交給 Job 執行可能成本反而比單核心執行高

由於差距之大，後者的影響顯然比較大。總之繼續進一步設法整併所有敵人的 Raycast 一次發出所有指令：

![combined](/images/posts/autopanic-zero-devlog/0000/6.png)

這樣就總算降低了需求！這個 Update 從 2.29ms 降為 1.87ms 大概節省了 18% 的時間，實際意義則是原本要用 0.42ms 執行的計算被降低為 0.035ms！而這個節省幅度也會隨著敵人數、進行的 Raycast 數量而增加。

例如將敵人的 raycast 精度從 10 個方向提升為 20 個方向時，節省幅度就變成 3.21ms→2.34ms 的 27%，計算從 0.87ms 降為 0.073ms：

![larger request](/images/posts/autopanic-zero-devlog/0000/7.png)
![larger request combined](/images/posts/autopanic-zero-devlog/0000/8.png)


總之雖然對於原作的敵人規模來說實用度沒那麼高，但如果玩家的電腦配置是低時脈多核心的情境，多少還是可以有一些幫助吧（？）

能看著誇張的敵人數量在畫面上漫遊卻繼續以高幀率執行也是相當的舒壓 XD

![swarm](/images/posts/autopanic-zero-devlog/0000/9.gif)