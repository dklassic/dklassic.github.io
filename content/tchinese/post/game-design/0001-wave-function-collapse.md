---
title: "Wave Function Collapse 隨機關卡產生系統"
date: 2020-12-24T16:08:37+08:00
draft: false
tags: ["遊戲設計"]
---

因為自己在做遊戲的緣故，開始研究各種省錢（？）的開發手段，趁等待的空檔打一篇教學文簡易積積陰德。其中最重要的一個就是關卡編輯與自動化關卡產生。

總之因為沒有時間與人力製作從頭製作關卡，所以不如想個辦法自動化產生關卡。

這部分目前最實用的手段就叫做 Wave Function Collapse。

可能很多人的印象最深刻的例子是來自這個 [Github 專案 mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)，我個人則是從 Oskar Stålberg 2018 年的演講入坑的：
{{< youtube 0bcZb-SsnrA >}}
從這邊聽個大概，似懂非懂很難理解，剩下很多片段都是在實作過程中才理解。

最後得到的結論就是 Wave Function Collapse 聽起來很厲害，但具體意義就是「有設定好條件的暴力解」，只要掌握這個精隨什麼都很好實作。



# 具體的實作方法

總之 Wave Function Collapse 比較簡單的做法是對規則形狀的物件做。為了方便舉例就以方形舉例。

## 定義單位方塊的屬性

例如在我的實作測試中作了一個簡單的牆壁、地板組合，單元如下：

![basic blocks](/images/posts/game-design/0001/KnZSeeI.png)

接著要詳細實作規則定義，基本上就是定義要有怎樣的 Tag 的物件才能接上。

![connectivity](/images/posts/game-design/0001/bGUxUDkl.jpg)

以這邊的例子來說就是要把牆壁的區域對接、地板的區域對接。

就寫個 Script 來定義這些屬性。

## 生成環境

首先當然是產生一些 Empty Game Object 來存放各個單元。

就把預先做好的單元在每個格子都塞好一份：

![environment](/images/posts/game-design/0001/rhw1pObl.jpg)
![setup](/images/posts/game-design/0001/uXcaEj1l.jpg)

上圖塞四份是因為我懶得紀錄各個單元的旋轉版本，所以就直接複製四份。雖然應該算是沒效率四倍，但是因為好寫又沒有即時的需求就這樣做了。

也因為複製四倍這種因素，產生過程中都直接把 Renderer 關好關滿。

## 開始<abbr title="Collapse">崩塌</abbr>

這邊是個循環，基本過程就是：

1. 尋找<abbr title="Entropy">熵</abbr>最低的格子

    簡單來說就是可選選項最少的格子。如果機率都一樣的話就用隨機。

2. 崩塌該格

    基本上是隨機崩塌，也就是從可選選項中隨機選一個出來用。

3. 更新鄰居的熵

    因為將一格的未來確定之後，附近鄰居可以與該格接起來的選項就變少了。所以要更新選項、熵值。

所以每做一個循環就會像這樣：

- 執行前

![before](/images/posts/game-design/0001/bcqgiEcl.jpg)

- 執行後

![after](/images/posts/game-design/0001/srRPTd5l.jpg)

會崩塌一格，並且讓週邊鄰居的可能性變少。

接著就無限執行循環直到每一格的未來都決定好：

![full](/images/posts/game-design/0001/K42uSg4.gif)

實作上就是如此的樸實無華。

# 延伸議題

此外的延伸議題有：

## 錯誤應對

簡單來說根據你單塊選項、銜接規則的設計，可能會出現某個位置完全沒有選項能與週邊銜接。這時候有兩種做法。
- 正解－回溯變更

    簡單來說就是既然有問題，就試著讓前一步變成別的方塊看看。

    這部分最好多一些輔助，像是「隨著錯誤次數越多，回溯的步數也增加」。根據隨機機率，早晚會生出一個可以完全解開的版本。
- 懶人－錯誤偵測與重來

    簡單來說就是只偵測錯誤，而撞到錯誤就重來。

    這個方法實作上比較簡單，但是比較沒效率。而且根據規則寫得完備程度越差，撞到錯誤而必須重來的次數可能也會增加，是個危險的做法。

    而隨著方塊的總量越多，單次產生所需要的時間也越來越長，為了避免大量的時間都被浪費在重新產生，寫個踏實的歷史步驟紀錄系統也比較重要。

## 可用程度偵測

根據關卡需求，可能要寫一些自動化的條件來偵測關卡的可用程度。

例如說各方塊通行區域的連通程度等等，加深自動化的有效性。

也同樣可以在可用程度過低的時候直接重新產生，不用浪費時間，更不用人力檢查。

## 預先設計條件加強可用程度

以我遊戲需求，我只寫了確保邊緣一定是牆壁的機制。但延伸可以考慮的面向就包含：

- 整張地圖的連通程度（有沒有房間被隔開無法通行）
- 可通行區域的面積

這些當然都是寫偵測比較簡單，要寫出可靠的解法比較難。

就看專案需求來決定要走好寫但是產生過程比較困難，或者是確保可以產生出來但比較難寫的版本。

## 三維化

目前我寫的版本只用了兩維，不過其實三維的概念也是一模一樣的，只是邊界銜接條件精細度可能要寫比較多。事前準備稍微複雜點但概念還是一致。

## 多核心化

老實說我還不太確定怎樣平行化比較好 XD


總之大概是這樣，老實說整個過程做起來還是很簡單，我弄出第一個可以產生的程式只花了十個小時左右。不過過程中還是各種想要尋求細節實作的部分都沒在網路上看到。

另一個我雖然沒有開來看但是有開源的 [Github 專案 marian42/wavefunctioncollapse](https://github.com/marian42/wavefunctioncollapse) 或許值得參考一下。

剛好有人問，我就順手寫了一份 Pseudo Code 提供參考：
```
MainFunction()
function
    TotalEntropy = Infinite
    while(TotalEntropy > unitList.Count)
        unitList.GetMinEntropy().Collapse()
        TotalEntropy = unitList.TotalEntropy()
    endwhile
endfunction


GetMinEntropy()
function
    minEntropy = Infinite
    for(unit in unitList)
        if(unit.Entropy < minEntropy)
            minEntropy = unit.Entropy
        endif
    endfor
    candidateList = new List
    for(unit in unitList)
        if(unit.Entropy = minEntropy)
            candidateList.Add(unit)
        endif
    endfor
    return candidateList[Random.Range(candidateList.Count)]
endfunction

Collapse()
function
    index = Random.Range(Possibilies.Count)
    for(possibility in Possibilies)
        if(possibility.Index != index)
            possibility.Remove()
        endif
    endfor
    Entropy = 1
    for(neighbor in neighbors)
        neighbor.UpdatePossibility()
    endfor
endfunction

UpdatePossibility()
function
    changed = false
    for(possibility in Possibilies)
        for(neighbor in neighbors)
            for(npossibility in neighbor.Possibilities)
                if(not npossibility.Compatible(possibility))
                    possibility.Remove()
                    changed = true
                endif
            endfor
        endfor
    endfor
    if(changed)
        UpdateEntropy()
        for(neighbor in neighbors)
            neighbor.UpdatePossibility()
        endfor
    endif
endfunction

UpdateEntropy()
function
    count = 0
    for(possibility in possibilities)
        if(!possibility.Removed)
            count = count + 1
        endif
    endfor
    Entropy = count
endfunction

TotalEntropy()
function
    count = 0
    for(unit in unitList)
        count = count + unit.Entropy
    endfor
endfunction
```