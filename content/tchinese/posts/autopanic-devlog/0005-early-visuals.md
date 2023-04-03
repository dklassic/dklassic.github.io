---
title: "05. 初期的視覺探索"
date: 2022-10-18T10:00:03+08:00
draft: false
tags: ["自動混亂"]
---

《自動混亂》的視覺探索花了不少時間，實際上最終版的場景設計要到 2022 年巴哈姆特 ACG 創作大賽前夕才完成。

這裡就流水帳地解釋過去：

![dynamic lighting](/images/posts/autopanic-devlog/0005/1.png)

> 在開發初期就確定要盡量實作動態光源

![ambient occlusion](/images/posts/autopanic-devlog/0005/2.png)

> 一開始試過純粹靠配色與 Ambient Occlusion 的版本

![outline](/images/posts/autopanic-devlog/0005/3.png)

> 後來被抱怨物件之間的邊緣難以辨識，所以做了外框線的測試
> 
> 這個版本用了好一陣子

![particle decoration](/images/posts/autopanic-devlog/0005/4.png)

> 後來開始花更多時間去研究其他高科技主題的作品，然後嘗試使用粒子系統去隨機散佈場景的裝飾
> 
> 上圖是測試模仿《Transistor》配色的成品，老實說粒子系統意外能做滿多有趣的功能

![particle](/images/posts/autopanic-devlog/0005/5.png)
![particle in motion](/images/posts/autopanic-devlog/0005/6.gif)

> 中途曾經有過大幅仰賴粒子系統的版本

![floor piece 1](/images/posts/autopanic-devlog/0005/7.png)
![floor piece 2](/images/posts/autopanic-devlog/0005/8.jpg)
![floor piece 3](/images/posts/autopanic-devlog/0005/9.jpg)

> 接著開始探索一些光線、地板板塊來裝飾關卡

![tower top](/images/posts/autopanic-devlog/0005/10.png)

> 原本最終戰是要在高塔的頂端進行戰鬥

總之這一波初期的探索，雖然還沒有成功走向終點，但是也讓我確立了幾個重點：

- 動態光線的視覺效果很好，能多動態就要盡量做
- 因為沒有可靠的建模能力，所以不要花時間在嘗試增加幾何密度，不如著重在乾淨的幾何與模型
- 選擇好的配色就可以帶來十足的效果