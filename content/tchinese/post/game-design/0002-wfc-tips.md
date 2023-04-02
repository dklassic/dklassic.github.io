---
title: "Wave Function Collapse 實用技巧"
date: 2020-12-29T14:23:49+08:00
draft: false
tags: ["遊戲設計"]
---

[上篇]({{< ref "/0001-wave-function-collapse" >}})大致上講述了 Wave Function Collapse 的基本概念。如果照著做的話大概可以做出像這樣的東西：

![early-result](/images/posts/game-design/0002/pF36Ds5.png)

無論基本方塊有多少，這時候都已經可以無限量自動產生出關卡結構。但是像這樣的關卡顯然還過於格狀粗糙，遠遠不到可以實用的程度。

# 精緻化手段

在這裡分享我研究 Wave Function Collapse 期間得出的兩個主要精緻化手段：

## 邊界條件的多樣化與精細化

![divide-more](/images/posts/game-design/0002/AxfjDPK.png)

簡單點就是像我這樣。

多樣化在於原本邊界條件是牆壁與地板，在這裡多加了圍欄。而精細化在於原本邊界條件只分成兩部分，在這裡則是直接切割為了四部分。




## 轉接器

![adapter](/images/posts/game-design/0002/l6Ggkre.png)

簡單來說是一個允許邊界條件之間轉換的零件。

由於這樣的零件存在，就可以讓所有邊界條件隨時切換，讓關卡版面不至於太死板。

發揮以上兩點之後就有辦法自動產生像這樣的盤面：

![result1](/images/posts/game-design/0002/BjvB2iC.png)
![result2](/images/posts/game-design/0002/d5NUnEo.png)
![result3](/images/posts/game-design/0002/H78iV51.png)
![result3](/images/posts/game-design/0002/tZWCzfs.png)

雖然由於使用的是簡單的方塊，當然還是看起來很醜。但結構已經看起來不像是具備特定意圖的設計師擺放出來的樣子了。在人造建築上可能是稍嫌奇怪，但如果將這樣的東西使用在天然島嶼（例如說就像 Bad North 那樣），效果可以說是一流。

而如果是單純產生房間形狀的話，應該也可以輕易製作出像 Ape Escape 的關卡結構。


# 反思

而從八月到九月之間研究完 Wave Function Collapse 之後，其實到現在十二月底我的個人專案又回歸到了手拉關卡。接下來的部分就是要講述這樣的轉變背後的理由：

## 能大量產生不代表能無腦產生

Wave Function Collapse 雖然允許用極低的努力做出極大化的成果，然而這個成果仍然是正比於一開始製作的板塊（規則）總量。

Oskar Stalberg 的 Bad North 雖然使用了 Wave Function Collapse 進行關卡產生，但是他也製作了超過 300 個基本板塊才能夠呈現出看似每個都完全獨特的島嶼。

## 有設計目的的意義大於純粹的關卡總量

雖然關卡產生的總量是可以無上限的，但是並不代表絕對能有效表現關卡想要考驗玩家的目的。能夠達成目的的關卡價值遠大於純粹的關卡總量。

為了要驗證關卡能夠達成目的，實際上還是得付出更多的時間對於產生規則進行微調。

也因此雖然當時研究出 Wave Function Collapse 自覺得很得意，但回頭看來其實我的遊戲設計並不需要用無上限的關卡量來堆疊。

Hades 的開發團隊也提到說雖然他們不是沒有打算做隨機產生關卡，但是為了要讓一個關卡有多樣的變化，所花的時間已經夠他們設計一面全新的關卡了。而甚至我玩了很久才意識到 Hades 的關卡並不是隨機產生的，代表說就算不仰賴關卡量也能是個好的類 Rogue 遊戲。

但是對於機制極為簡單的遊戲循環來說， Wave Function Collapse 還是能明顯帶來各種好處。例如 Oskar Stalberg 不算是遊戲的 Townscape，以及 Bad North 這樣比較好限制條件產生出好關卡的遊戲。

總之大概就是這樣提供參考（？