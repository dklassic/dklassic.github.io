---
title: "視覺設計 2－色彩後製"
date: 2022-12-18T18:20:01+08:00
draft: false
tags: ["自動混亂","遊戲設計"]
---

上一篇已經準備好了整個遊戲的基本視覺要素，也可以說是已經完成了整個視覺設計。
但其實還有非常重要的最後一步，重要到必須要獨立一篇來解釋：色彩後製。

不過在那之前我們先岔開來提一下一個不同但又有點相關的議題。

# 照相寫實與寫實的差異

照相記錄下來的是客觀事實，但攝影師的工作可不是只要擺好按下快門就結束了。攝影師所觀測到的主觀畫面與被記錄下來的客觀事實是會有偏差的，這就是「白平衡」的運作，攝影師除了必須調整照片到與自己主觀看見的「白色」一致以外，也要將顏色的走向調整成自己腦中所看見的樣貌才真正完成了攝影作品。

這樣講感覺有點混亂，不過我們直接換個名詞來迅速解釋吧 XD 基本上就是「寫實」與「照相寫實」的差異。

例如說之前有人用 UE5 做了一個日本車站，看起來很符合「<abbr title="Photorealism">照相寫實</abbr>」：

![ue5 station](/images/posts/autopanic-devlog/0014/1.png "Lorenzo Drago 使用 UE5 製作的日本車站")

寫實畫家的作品看起來很符合「<abbr title="Realism">寫實</abbr>」：

![painting](/images/posts/autopanic-devlog/0014/2.png "William Bouguereau 繪製的 The Story Book")

應該沒有人會覺得能用 UE5 渲染出第一張圖，就會導致能畫出第二張圖的價值變低吧 XD

這就是為什麼照相的發明沒有破壞掉寫實作畫的價值，因為人追求的寫實其實是「腦海中看到的寫實」，而不是純粹被客觀記錄下來的「照相寫實」。同樣的，攝影師拍出了「客觀寫實」，也依然得想辦法調整為自己腦海中看到的樣貌才算作品的完成：

![painterly photo](/images/posts/autopanic-devlog/0014/3.png "Joanna Kustra 所拍攝的如畫般的照片")

有空推薦看一下這篇文「[Creating Painterly 3D Scenes: preparing assets for NPR](https://shahriyarshahrabi.medium.com/creating-painterly-3d-scenes-preparing-assets-for-npr-8d6c726cc34f)」整理得更好 XD

總之離了點題，我們回來。

# 色彩後製

色彩後製有很多功用，我個人認為最重要的有三個：

- 情緒傳達
- 統一視覺性質
- 改變視覺表現的便宜手法

第一點應該不用多說，提一下下面兩點。

曾經看過一個音效師提到他製作遊戲音效時都會幫遊戲定義一個基本的效果器鏈，這樣就算出處來自不同地方的素材，也會乍聽之下有一些一致的性質。統一的畫面後製可以幫助各種不同的視覺要素看起來更一致，不一定要真的全都自己手工製作才能達到。

而無須執著於為不同情境設計完全獨特的素材，純粹改變色彩後製隨之而來的情緒變化，就已經是很有效的視覺體驗改變。

例如說，我們看一次色彩後製前的樣貌：

![before](/images/posts/autopanic-devlog/0014/4.png)

雖然不至於有什麼重大問題，但角色、場地的物件、燈源與背景，看起來似乎都像是活在不同的世界。

然而讓我們加入色彩後製：

![after](/images/posts/autopanic-devlog/0014/5.png)

僅僅進行了色彩的後製就可以讓整體畫面的和諧度提升，並且帶來了完全不同的情緒。

色彩後製的學問、流派很多，在這裡簡單介紹我的作法，但比起遵循這個方法，還是自行去探索適合自己的，最重要的是反覆實驗出自己會喜歡的類型比較重要 XD

我採用的作法與影視的作法比較接近，最重要的第一步驟是：大幅降低對比度。

![lower contrast](/images/posts/autopanic-devlog/0014/6.png)

影視業最常用的做法就是以所謂的 SLog2、SLog3 拍攝，拍出來的畫面會長這樣：

![slog](/images/posts/autopanic-devlog/0014/7.jpg "Gerald Undone Sony A1 評測影片")

這樣做可以確保不會產生過曝、曝光不足的畫面，保留整體畫面細節。

例如說如果我沒做這部的話，同樣的色彩調整下我的遊戲畫面會變成這樣：

![plain change](/images/posts/autopanic-devlog/0014/8.png)

可以看到許多畫面細節被壓縮掉，例如說右上角原本有看起來很大片的光線，變成了黑色一團。大幅降低對比度再進行調整可以避免這種現象的發生。

總之從基礎的畫面讓我們降低對比度：

![lower contrast](/images/posts/autopanic-devlog/0014/9.png)

很好，細節都保留起來了！

接著決定 Lift、Gamma、Gain 三部分的顏色去改變整個畫面的情緒。

在色彩後製上有時候又會改以 Shadows、Midtones、Highlights 的形式調整，分別對應的就是暗部、中間調、亮部的顏色配置。兩者雖然計算方式不盡相同，但想要調整的目的類似。
關於 Lift、Gamma、Gain 對於不同亮度範圍的影響參考這張圖（從[這裡](https://www.getop.com/post/%E9%80%99%E4%BA%9B%E5%90%8D%E7%A8%B1%E5%88%B0%E5%BA%95%E6%9C%89%E4%BB%80%E9%BA%BC%E4%B8%8D%E5%90%8C%EF%BC%9F)撿來的）：

![Lift, Gamma, and Gain](/images/posts/autopanic-devlog/0014/10.png)

總之我想要當個假文青，所以我選擇幫亮部跟陰影都上藍青色的顏色：

![Lift](/images/posts/autopanic-devlog/0014/11.png "暗部顏色調整結果")

![Gain](/images/posts/autopanic-devlog/0014/12.png "亮部顏色調整結果")

![Combined](/images/posts/autopanic-devlog/0014/13.png "合成")

但這樣藍藍青青的，畫面實在有點不太平衡，所以我在中間調使用了紅紫色，去平衡回去整個畫面：

![Gamma](/images/posts/autopanic-devlog/0014/14.png "中間調顏色調整結果")

![Combined Gama](/images/posts/autopanic-devlog/0014/15.png "合成")

這樣總算畫面變得比較舒服了！帶點冷冽的氣息但又不會變得超陰陰鬱鬱的。

不過亮度這下有點暗啊，我們來平衡回去吧：

![Brighten](/images/posts/autopanic-devlog/0014/16.png)

這就完成了！

總之沒有想到日常拍照、影片後製學到的東西居然就這樣順利地成為了遊戲開發可以用上的知識（汗