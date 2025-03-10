---
title: "絕對有保證的遊戲爽感"
date: 2022-11-14T01:08:39+08:00
draft: false
tags: ["自動混亂","遊戲設計"]
---

2013 年，Vlambeer 的 Jan Willem Nijman 進行了一個演講，名為「[The art of screenshake](https://youtu.be/AJdEqssNZ-U)」。

影片觀看數達到 31 萬，應該就足以說明這部影片對整個遊戲界的影響力有多大。要記得這影片應該是只有遊戲從業人員才會看的，31 萬也許只是有中等觀看次數的 YouTube 影片，但實質上的意義可能是很大量的遊戲從業者都受到這部影片的影響。

《自動混亂》的遊戲機制，基本目標就是要爽。沒了。

我沒有什麼要做出獨特遊戲機制的想法，但最低標準就是要一套玩家無論怎樣玩都會很爽的射擊遊戲機制。

2020 年 11 月 28 日的我看了這部影片，然後就想說......等等，不是照著這部影片一步一步做就會做出怎樣玩都會很爽的遊戲嗎？

![view history](/images/posts/autopanic-devlog/0012/1.png "歷史性的一刻，一個禮拜後遊戲體驗就有了無限倍的強化")

總之基本上只要看一遍這個影片，就可以做出玩起來體驗很好的遊戲。就算不是射擊遊戲，有很多概念都可以被直接沿用。總之《自動混亂》的遊戲性完全奠基於這個設計，可以說是看完這部影片人人都能抄一份《自動混亂》出來了（？

處理前：

![before](/images/posts/autopanic-devlog/0012/2.gif)

處理後：

![after](/images/posts/autopanic-devlog/0012/3.gif)

但說起來都簡單，終究比不上實際體驗一遍，所以我做了這個測試版本讓大家親身玩玩看這些效果的差異：

[下載連結](https://www.dropbox.com/s/1gfqygt95or83wv/%E8%87%AA%E5%8B%95%E6%B7%B7%E4%BA%82%E9%81%8A%E6%88%B2%E7%88%BD%E6%84%9F%E5%B1%95%E7%A4%BA.zip?dl=0)

想要抄出一份《自動混亂》，不如作者本人直接教大家怎麼抄（？？？

可以先去玩玩看再來詳細看說明，也可以先看完說明再去玩，都行。

當然更重要的是，這邊的設計都是以「讓玩家爽」為前提，所以如果前提就是要「不讓玩家爽」的話，這邊的設計就未必適用。兩個設計方向都是可行的，這篇文章**不是**告訴你「讓玩家爽」才是正確的。

但如果你想要讓玩家爽，卻意外造成玩家不爽的話，那這篇文章就可以給你一些設計要素參考。

以下逐一加入要素介紹：

1. 首先是基本的樣子

![step 1](/images/posts/autopanic-devlog/0012/4.gif)

2. 基本動畫

    總之有動畫會比沒動畫好，這邊舉例是加上了腳。

![step 2](/images/posts/autopanic-devlog/0012/5.gif)


3. 降低敵人擊殺時間

    過高的敵人擊殺時間會降低爽感。

    即便是以難度著稱的魂系遊戲一般的敵人也都很脆。

![step 3](/images/posts/autopanic-devlog/0012/6.gif)

4. 高射速
    
    高射速永遠比較爽。

![step 4](/images/posts/autopanic-devlog/0012/7.gif)

5. 提升敵人數量

    即便是同樣的戰鬥時間，大量低血量敵人戰鬥起來，通常比少量高血量敵人體驗還要好。

6. 更大的子彈

    現實世界的子彈很小顆，但記得我們不是現實世界，要爽就要大顆的子彈。

    即便是擬真槍戰作品，實際上也會讓子彈能被玩家清晰看見，好像每一發都是打曳光彈一樣。現實世界中的子彈如果擊發出去，可是肉眼完全追不上的。

![step 6](/images/posts/autopanic-devlog/0012/8.gif)


7. 槍口焰
    
    嗯，記得做。

![step 7](/images/posts/autopanic-devlog/0012/9.gif)


8. 更快的子彈

    飛得快就是爽。不過要注意碰撞判定問題，以免子彈直接穿過敵人。

![step 8](/images/posts/autopanic-devlog/0012/10.gif)

9. 準度低一點

    筆直的彈道很無聊，增加隨機性看起來會更豐富。

![step 9](/images/posts/autopanic-devlog/0012/11.gif)

10. 命中特效

    打中了敵人記得噴一些東西出來。

![step 10](/images/posts/autopanic-devlog/0012/12.gif)

11. 受擊反應

    敵人受到攻擊時產生反應很重要。

![step 11](/images/posts/autopanic-devlog/0012/13.gif)

12. 敵人擊退

    讓玩家可以擊退敵人的話，也會讓敵人的行動產生額外的隨機性。也會增加一些戰術考量。

![step 12](/images/posts/autopanic-devlog/0012/14.gif)

13. 場地永久性

    盡量殘留可以讓玩家看到自己豐功偉業的要素，像是讓敵人的屍體留存。

![step 13](/images/posts/autopanic-devlog/0012/15.gif)

14. 鏡頭平滑跟隨

    拜託不要卡死在角色背後固定距離，要像綁著彈簧一樣拉著走。

    完全貼死：
    ![step 14-1](/images/posts/autopanic-devlog/0012/16.gif)

    平滑跟隨：
    ![step 14-2](/images/posts/autopanic-devlog/0012/17.gif)

15. 鏡頭晃動

    晃起來會增加爽感，但要注意晃動的方式並不是「隨便晃」，而是要有規律地推動鏡頭。

    《自動混亂》的做法是鏡頭會往玩家射擊的反方向推動。

![step 15](/images/posts/autopanic-devlog/0012/18.gif)


16. 玩家擊退

    同敵人可以被擊退，玩家也可以被自己擊退，增加變化性。

    《自動混亂》中，設計上是只有一種武器會造成玩家自己被擊退。

![step 16](/images/posts/autopanic-devlog/0012/19.gif)


17. 打擊暫停

    藉由暫停整個遊戲來強調打擊的力道，要小心別過頭會讓玩家反而感到不耐煩。

    以《自動混亂》為例，我實作的方式不是暫停，而是  1/10 流速的慢動作。我的慢動作時間是根據武器的威力計算，並且隨著連續發動會降低長度。

    不過這個效果 Gif 應該很難看出來，建議實際實行起來檢視。

    沒有打擊暫停：
    ![step 17-1](/images/posts/autopanic-devlog/0012/20.gif)

    有打擊暫停，命中瞬間有三幀的慢動作：
    ![step 17-2](/images/posts/autopanic-devlog/0012/21.gif)

18. 槍枝擊退動畫

    同樣可以強調武器的威力、打擊的力道。

    《自動混亂》中會考慮武器的傷害來決定擊退／後座力的程度。

![step 18](/images/posts/autopanic-devlog/0012/22.gif)

19. 敵人隨機爆炸
    
    讚啦！

![step 19](/images/posts/autopanic-devlog/0012/23.gif)




總之就是這樣，歡迎大家下載試玩交流，把我從別人偷來的設計也一起偷走，大家一起賺大錢（？？？？