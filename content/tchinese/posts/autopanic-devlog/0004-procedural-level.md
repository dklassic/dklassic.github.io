---
title: "04. 挑戰程序性產生關卡"
date: 2022-10-17T10:10:00+08:00
draft: false
tags: ["自動混亂"]
---

大部分情況下提到類 Rogue，大概就會跟隨機產生關卡綁在一起吧。
當時最讓我印象深刻的隨機關卡就是《Bad North》，一般 2D 作品都只能使用普通的 Tileset 拼貼，但《Bad North》可以產生出有地形起伏、全 3D 的關卡。

因此我就開始研究 Oskar Stålberg 的一些演講，相關內容可以回頭參考我寫的[基礎篇]({{< ref "/0001-wave-function-collapse" >}})與[實用篇]({{< ref "/0002-wfc-tips" >}})。

總之當時的實驗成果大概像這樣：

![rim condition](/images/posts/autopanic-devlog/0004/1.png)
![tower](/images/posts/autopanic-devlog/0004/2.png)



但當然我也很快地發掘這樣的設計並沒有真的很有意義，只是形狀獨特，沒有對應複雜的填充內容的話，看起來也就只有形狀獨特而已。而 Oskar Stålberg 也為《Bad North》設計了超過兩百片拼貼的板塊才能達到那個複雜的獨特視覺，這就不是完全沒有實用建模能力的我能達成的事情。

後來關卡設計的邏輯就發生了大改，換個講法，完全放棄進行關卡設計。