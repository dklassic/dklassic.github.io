---
title: "視覺設計 3－著色器與它們的產地"
date: 2022-12-18T18:40:01+08:00
draft: false
tags: ["自動混亂","遊戲設計"]
---

上兩篇都處理了大方向的視覺設計討論，這篇就來精細說明某一些著色器的具體實作。

但首先我們來提一下這個柱子。

# 偽造倒影

![pillar](/images/posts/autopanic-devlog/0015/1.png)

總之嗯，這東西呃。不是倒影。

他只是一個往下長的版本，然後畫在所有東西上面：

![fake reflection](/images/posts/autopanic-devlog/0015/2.png)

比起純粹的精細度，玩家對於光影表現更加敏感，會大幅增加體感品質。實際上我確實也可以用其他方式嘗試正確顯示出倒影，但是都比不上直接塞兩張紙卡在底下來得簡單有效。

這個把戲早在《潛龍諜影 2》就已經被使用，他們直接延伸場景到地底下：

![mgs2 fake reflection 1](/images/posts/autopanic-devlog/0015/3.jpg)
![mgs2 fake reflection 2](/images/posts/autopanic-devlog/0015/4.jpg)

也因此可以在不存在光線追蹤能力的硬體上，產生看起來很高品質的倒影。因為實際上就是底下直接放一個東西 XDDDDD

總之雖然很好笑，但看起來體感品質就莫名其妙提升了。

![actual](/images/posts/autopanic-devlog/0015/5.png)

> 真正的樣貌，障礙物看不出來在空間中的深度、相對位置

![faked](/images/posts/autopanic-devlog/0015/6.png)

> 加入了假造的倒影後，就突然變得很厲害，也解決了空間感的問題

# <abbr title="Shader">著色器</abbr>們

那我們接下來流水帳，首先一圖流展示遊戲裡面有什麼重要的著色器視覺表現：

![everything all at once](/images/posts/autopanic-devlog/0015/7.gif)

所有重要的著色器都在這了，自己找吧（誤

## 建築物

之前早在東京都專案登場過的建築物著色器，自然而然很適合被沿用過來當裝飾品使用。

基本原理就是在建築物上產生方格，根據物件的世界位置做隨機判定，決定窗戶顏色、色溫傾向、亮度等等。

實作方式有點瘋狂，大概不是全世界最好的做法，而且當時使用 Shader Graph 製作所以完全是蜘蛛網：

![building](/images/posts/autopanic-devlog/0015/8.png)

有興趣的話我之前有公布過一次[舊版](https://github.com/dklassic/Unity-Simple-Building-Triplanar-Shader)。其實功能組反而比我現在使用的還要豐富，只是可能沒辦法直接延用到新版 Unity，要自行克服一下繁雜的移植工程。

## 流動光點

基本上就是隨時間流動的 Voronoi，搭配之前東京都專案的視角自動對應顏色判定製作而成。

雖然實作上很簡陋，但因為景深會解決一切的問題所以就算了。

![car light](/images/posts/autopanic-devlog/0015/9.png)

## 體積雲霧

非常土炮的體積雲霧，基本上直接放一個倒置的 Fresnel，接著吃一個立體雜訊去扭曲邊緣，然後就當作我搞定了。

實際的配置是直接使用粒子系統打出大量的 Sphere Mesh 然後配上這個著色器的材質使用。

實務上為了搭配景深使用，刻意做成了一個從側面看起來會很醜的版本，但加上景深之後細節就恰到好處。

![volumetric cloud](/images/posts/autopanic-devlog/0015/10.png)
![volumetric cloud actual](/images/posts/autopanic-devlog/0015/11.png)

> 這個設定值側拍長起來超醜，但一過景深就會看起來很漂亮

## 地板

其實沒什麼好提的，基本上就是根據世界位置去採樣一個 Gradient Noise，然後用某種形式去製造動態。

例如最上面的地板動態是這樣製作的：

![floor tile](/images/posts/autopanic-devlog/0015/12.png)


就這樣水了一篇，好耶！（不是