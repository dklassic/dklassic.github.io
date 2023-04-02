---
title: "08. 敵人翻新與程序性動畫"
date: 2022-10-20T10:00:25+08:00
draft: false
tags: ["自動混亂"]
---

# 敵人翻新

敵人的翻新過去曾經寫過一篇文解釋[低效能需求的區域性碰撞迴避 AI]({{< ref "/0004-low-cost-ai" >}})，所以在這邊就只講剩下的部分。

![enemy roaming](/images/posts/autopanic-devlog/0008/1.gif)

我希望《自動混亂》更像是個要被解開的謎題，而不是純粹的反應力大戰。希望玩家可以學清楚敵人的所有反應，然後在了解過後就能把各個房間的敵人配置都當作一個要被解開的戰鬥難題應對。

因此《自動混亂》選擇使用了<abbr title="Attack Pattern">攻擊樣板</abbr>式的設計，敵人會從多個可以使用的樣板選出一種，然後樣板開始執行之後就只會完全重現整個線性過程：

![enemy pattern](/images/posts/autopanic-devlog/0008/2.png)

一開始的指令數很少，後來為了配合更多的行為設計，不得不持續追加新的指令，簡單舉例：

![commands](/images/posts/autopanic-devlog/0008/3.png)

而在敵人經過翻新之後，我就可以使用一個 Scriptable Object 去設定個別敵人的性質，再由一個共用的 Enemy Prefab 去生成所有敵人。

![enemy setting](/images/posts/autopanic-devlog/0008/4.png)

敵人行為設計完之後，再來就是配合敵人行為的「程序性動畫」。

# 程序性動畫

由於人力有限所以沒辦法製作傳統動畫，程序性動畫變成了唯一選項（或者是完全不做動畫啦，但那不太可能）。

遊戲中廣義的程序性動畫有：

- 使用者介面動畫
- 泛用動畫
- 移動動畫

## 介面動畫

使用者介面動畫比較簡單，主要是使用程式驅動一些遮罩的變化，來支援多種介面出現、消失的顯示手段。

![ui animation](/images/posts/autopanic-devlog/0008/5.gif)

## 泛用動畫

泛用動畫則大多是用 DOTween 套件直接完成，例如說受到攻擊時的反應，就可以直接寫：
```csharp
icon.DOPunchRotation(damageForce / unitSize, 0.5f, 10, 0)
```

![hit reaction](/images/posts/autopanic-devlog/0008/6.gif)

而武器造成的後座力動畫則可以直接這樣寫：
```csharp
recoilTarget.DOPunchPosition(recoilForce / unitSize, recoilDuration, 1)
```

![rifle recoil](/images/posts/autopanic-devlog/0008/7.gif)
![shotgun recoil](/images/posts/autopanic-devlog/0008/8.gif)

如此一來就可以輕易完成正確考慮一些物理性質的泛用程序性動畫。

## 移動動畫

而最後移動動畫的部分可以去參考以前寫過的[程序性動畫實作雜談]({{< ref "/0005-procedural-animation" >}})。基本上是一系列「被動式動畫系統」的實作，會直接根據物件的位移去決定行動方式（移動腳、轉前導輪），完成之後就可以做出完全獨立於角色行動的動畫，讓角色移動不會被動畫干擾回去。

![procedural animation](/images/posts/autopanic-devlog/0008/9.gif)

總之在完成了程序性動畫之後，整個遊戲的動態性就增強很多，看起來越來越像是個有在邁向終點的作品了！