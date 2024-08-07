---
title: "10. 重新出發前的長假－輕鬆玩的小專案"
date: 2022-10-22T15:25:06+08:00
draft: false
tags: ["自動混亂"]
---

總之因為差點把自己燃燒殆盡，所以說好要在搞定最重要的骨幹後就先放幾個月的長假再說。

所以長假要幹什麼呢？當然是寫更多遊戲啦！

# Enemy Within

我先寫了一個簡單的小遊戲，基本想法是要做一個單人版的《阿瓦隆》。主要原因還是因為跟朋友玩了《桌遊模擬器》後，覺得遊戲虛擬空間中重現現實桌遊的物理性質，其實意外地很有趣。
這個小專案的目的有：

- 試著用 Unity 的 HDRP 示範場景內建的素材快速拼湊出乍看之下好像還行的視覺
- 測試一些穩定性比較低的物理互動看有沒有辦法帶來樂趣

![enemy within selection](/images/posts/autopanic-devlog/0010/1.gif "選擇要出任務的人，看結果")

![enemy within vote](/images/posts/autopanic-devlog/0010/2.gif "《阿瓦隆》每次出任務的投票系統當然也要做")

![enemy within throw](/images/posts/autopanic-devlog/0010/3.gif "不是直接把卡片瞬移過去，而是用物理系統丟到桌上")

總之這個實驗讓我得出了兩個結論：

- 能有效善用 HDRP 的話，可以很輕易地做出看起來很潮的畫面感
- 使用物理系統執行的東西，雖然可靠性很低，但是這種隨機性的物理互動會帶來動態的視覺密度提升

後者的概念是「比起增加模型的精細度，讓物件會變化本身就是一種視覺密度、品質的提升」。

但當然以物理系統來說會有穩定性的問題，像是為了要確保所有卡片能夠正確丟上桌面必須做一些反覆的測試跟額外的保證系統。

總之簡單測試下還不錯，後來就沒有執著於真的要寫完遊戲邏輯的部分了。不過這樣整理起來，如果有準備一些各有特色的人物頭像，似乎就可以當有效的作品使用。


# Taipei Bus Drift
基本上是個半搞笑的作品，就是，「台北公車司機開車像在開賽車」，其實應該是全台灣都有這狀況吧 XD

最當初是發現有個 [Blender 套件](https://github.com/domlysz/BlenderGIS)可以自動擷取 Open Street Map 的資料，然後就瞬間發想出要寫一個關於這樣的遊戲：

> 「在台北開公車，跑公車路線，載乘客然後當氮氣加速把乘客噴射出去」的賽車遊戲

這個小專案的目的有：

- 繼續測試 HDRP 能帶來乍看之下視覺品質的效果
- 測試一個據說實作起來很簡單的賽車操控機制
- 看看能不能直接拉入一些現實世界的資料來輔助設計

所謂實作起來很簡單的賽車操控機制就是，與其模擬真實車輛的運作方式，把車子當作一顆球去推動這個球的移動簡單又有效。可以參考這個影片：[Mario Kart's Drifting | Mix and Jam](https://youtu.be/Ki-tWT50cEQ)。

![sphere collision](/images/posts/autopanic-devlog/0010/4.png "移動運算使用的 Collider 是普通的球體的情況下，物理計算基本上很穩定，不用考慮各種真實車輛的物理問題")

順帶一提也是為什麼我[對速度感的表現稍微有些研究心得]({{< ref "/0008-speed" >}}) XD

![bus movement](/images/posts/autopanic-devlog/0010/5.gif)
![bus route](/images/posts/autopanic-devlog/0010/6.gif)

總之其實算是一個不錯的挑戰，公車路線的抓取跟產生賽道是我朋友寫的程式 XD

以結果而論，單純仰賴一些 HDRP 內建的視覺性質，像是 SSR 的實作等等的確可以迅速產生乍看之下很有效的視覺，這個概念本身也有一些不錯的遊戲性質，像是：

> 公車路線通常不會彎曲，理論上作為賽道其實沒有太大意義；但是如果為了取得公車站乘客進行氮氣加速的話，就可以讓玩家依然有一些決策空間。

總之要延伸這個主題做出一個簡單的惡搞作品似乎還算容易，還可以完成一條公車路線就可以客製化外觀成那個路線的公車的樣子（？

不過也有一些額外問題要克服：

- 公車站 GPS、Open Street Map 資料是不準確的，所以不太可能一氣呵成弄出實用的遊戲地圖
- 直接使用公車路線還是有點太枯燥，也許必須自製路線或加入其他障礙、加成效果來提升趣味
- 公車路線不是每條都有經過城市範圍，必須挑選
- Open Street Map 標記的台北建築資料不夠完整，要嘛人工處理，要嗎得取得更完整的資料（像是[台北市政府的建築套繪圖](https://addr.gov.taipei/M2019/indexPwd.aspx#)完整度跟準確性都會高很多）
- 資料繁多，站點位置、物件必須動態生成管理，不然資源需求會太高

總之因為沒有很確定的專案未來，所以這個公車的小專案就做到這裡為止擱置了。

但這時候我一時好奇查了一下，發現東京的 Open Street Map 標記超完整，讓我萌生了一個想法：

> 也許我可以快速地做出一款在假想的東京開車的作品？

結論是顯然不太能，但是個有趣的挑戰，下篇就講這個。