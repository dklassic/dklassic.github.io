---
title: "簡單更新"
date: 2023-07-09T20:44:11+08:00
draft: false
tags: ["自動混亂","雜記"]
---

感覺該來點更新，整理一下最近做了些什麼 XD

我還在研究怎樣改善戰鬥系統，這部分大概要看靈感如何，所以總之就慢慢推進。除此之外做了一些小改良。

# 邊緣標示效果

![rim indication](/images/posts/autopanic-devlog/0021/1.gif)

我一直打算要做一個這樣的效果，簡單展現為什麼不會掉落平台。之前做過的嘗試效果都不太好，不過這次可不一樣，因為我終於掌握了著色器的使用方式。

![rim quad](/images/posts/autopanic-devlog/0021/5.png)

這次我單純在邊緣都加上一些 quad，然後用一個 LevelManager 來持續將玩家的位置餵給<abbr title="global shader keyword">全域著色器關鍵字</abbr>，接著就在著色器內讀取出來，並且根據距離更新透明度。除此之外，我綜合使用了世界位置 XZ 以及 UV 的 V 值，來讀取 3D Voronoi Noise，確保我不需要在整個邊緣都使用完整的 quad 也可以做出連續的視覺效果。

至於為什麼是使用世界位置 XZ 以及 UV 的 V 值而不是直接使用世界位置的 XYZ 呢？是因為我想在這邊做慣例的假造倒影，但是如果我直接使用世界位置的 Y 值的話，會讓確保倒影確實顯示成相反紋路比較麻煩。所以單純使用 UV 的 V 值，並且讓假造倒影的 UV 顛倒，就可以輕易完成這個處理。

![rim reflection](/images/posts/autopanic-devlog/0021/6.png)

# 光線陰影

沒什麼東西，簡單來說就是讓光線可以打出陰影，並且幫特定物件設定只會打出陰影的 Mesh Renderer。

![shadow casting light](/images/posts/autopanic-devlog/0021/2.gif)

不過有趣的是，我在使用 spot light 上遭遇了一些神祕的問題。我的遊戲空間使用上非常的大，最高在 Y 值會到達 40,000 左右，在相對高的高度下， spot light 的陰影會開始有閃爍現象。這個問題大概是慣例的精度問題，但至於為什麼 point light 沒有這問題，卻只在 spot light 上有就不太確定了。

總之我就直接把所有 spot light 都換成 point light，反正視覺效果沒差太多。

# 傷害數值

![damage number](/images/posts/autopanic-devlog/0021/4.gif)

這算是這次更新中對我來說比較爭議的措施，不過最後而言我覺得應該是得留下來。

我之前不想要實作傷害數值的原因，是因為我認為傷害數值會影響到我的極簡風視覺。不過只能說實作後，讓確認自己的戰鬥輸出簡單很多，所以我決定就留下這功能並且預設開啟，但是有選項可以關掉。

# 音效文字

![audio caption](/images/posts/autopanic-devlog/0021/3.gif)

這算是個小意外。

我一直都有這個小功能可以幫助我確認我的音效狀況，不過仔細一想這功能根本可以直接被搬來當作音效文字顯示，總之就拿來用用看 XD

不過也不是說能直接把除錯版直接用下去，不然畫面會整個變成一團亂，所以我還得做一些額外處理：

- 幫音效的名字改名，讓文字更能被理解（或精簡掉不必要的資訊）。
- 音效現在各自會有對應的「重要度」，讓比較不重要的音效文字會有比較低的不透明度。

總之這次就這樣，繼續推進度。