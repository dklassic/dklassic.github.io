---
title: "早早失敗（Fail Fast）"
date: 2024-07-13T10:00:23+08:00
draft: false
tags: ["自動混亂"]
---

2023 年底的時候，我做出了要無限期延後《自動混亂》開發的決定。會做出這個決定的本質還是得歸究於我個人對自己的遊戲的理解，並沒有與我預期的開發時辰對應到。講簡單點，這樣下去《自動混亂》不可能照著原定開發時辰跑，如果硬是照著跑的話最終成品大概也是個會讓人充滿遺憾的產物。

追根究柢得從《自動混亂》的根源想起，畢竟最最最當初這只不過是一個練習作品，是我第一次寫 C#，是看著網路上的雙搖桿射擊遊戲教學做出來的東西。而突然的就從練習作品變成了一個完整的遊戲規格，怎麼想都過於瘋狂。這樣的規格轉變下很明顯地遊戲的各方面都很不成熟，一方面自然得歸究於我欠缺大量的能力，另一方面則是時間限制（我還是得做工作養活自己呢！）。

不過既然這樣走下去不是個辦法，我就需要一個全新的計畫，我需要「早早失敗（Fail Fast）」。

# 早早失敗（Fail Fast）

「早早失敗」是一個遊戲開發者經常給新手的建議，英文講起來滿順，寫成中文感覺有點怪怪的但總之概念有到吧！也已經開發多年不能再以新手自居的我，完全認同這個概念。通常大概是這樣說的：

> 不要第一款就做出你夢想中的大遊戲，先做好幾款小遊戲。這些遊戲全都會失敗但沒關係，你會因此而慢慢學到怎樣做出那款夢想中的大遊戲。

做遊戲很難，而**完成**遊戲就更是指數級的難。如果打算第一款就直接做出世界上最棒的遊戲，物理上大概也不會做不到但會因此消耗顯著更多的時間去製作，《自動混亂》就已經是個很好的例子。而在這樣的夢想遊戲開發過程中，大部分的專案最後大概就是走向滅亡，就算成功的專案也滿多會把開發者的靈魂直接燒乾然後世界上就出現一堆做出一款傑作就再無新作的開發者。

過去幾個月，我偶爾還是會就很突然地收到新玩家的訊息，他們玩了《自動混亂》的試玩版然後覺得這是他們玩過最棒的遊戲，必須要跟我說聲謝謝。這些聲音多少強化了我對《自動混亂》設計理論的信心，我認為即便拖了四年《自動混亂》依然會是世界上獨一無二的遊戲。我真的很希望能用最理想的樣貌將它呈現出來，而同時我也要避免用會把自己殺死的方式來完成，所以我需要來進行我的版本的「早早失敗」。

《自動混亂》的設計理論奠基於超多個非常大膽的假設，所以如果我要在最終成品中順利發揮這些理論，我就應該要先把我的假設全都驗證完畢。而我手邊正好有隨手做出來拿去 G8 遊戲展驗證過一次的《自動混亂：零式》，就覺得這大概是個很棒的出發點。我要把《零式》做成一款我認為可以上市的作品，然後就丟出去，而這個過程會被拿來驗證我一部分的理論。

《零式》無庸置疑會失敗，會是常見的 90% 沒玩家沒收入的 Steam 遊戲。一款來自未知開發者的遊戲，就算實際上是世界上最棒的遊戲（當然這不是事實），也不會被人看見。不過即便是這麼稀少的曝光下，也還是有人會意外挖到它，而這些人就會讓我知道我有沒有做對。

![一名玩家稱讚《零式》的圖片](/images/posts/autopanic-devlog/0025/0001.png "到底怎麼辦到居然有發現我的遊戲，總之真的是大感謝！")

我會做一些快速修正應對顯著問題，但接著我就會趕快往下跑了。如果這些小遊戲真的其實很棒的話，未來遲早會再次被人看見的。我要繼續做下一款遊戲，再下一款，直到我能夠摸清楚我所有的疑慮。每一款都會讓我更接近完整呈現《自動混亂》所需要的能力。

# 下一步？

《自動混亂》獲得參展 BitSummit 的資格，所以我要去京都玩一趟然後希望可以跟世界各地酷炫的開發者見個面！也許我們也能在那裡見？