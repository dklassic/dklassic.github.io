---
title: "自動建置系統與自動版本標記系統"
date: 2023-06-01T12:20:11+08:00
draft: false
tags: ["自動混亂", "遊戲設計"]
---

最近《自動混亂》進入比較大規模的對外設計驗證階段，頻繁切換各種不同功能組的需求也開始大增。時不時就會發生不小心輸出錯誤的版本，然後上傳之後讓測試者感到困惑。

也因此，是時候該製作自動建置系統了。不得不說這也是進 SIGONO 一輪之後才學到可以做的事情，如果我持續自力開發的話大概不一定會想到要做 XD

# 自動建置系統的需求

![feature toggle](/images/posts/autopanic-devlog/0018/2.png)

《自動混亂》目前有數個經常會頻繁切換開關的功能組：

- Debug Start Up－不會正常載入，而是顯示一個快速切換遊戲狀態的工具選單，進入各種遊戲狀態。

![debug start up](/images/posts/autopanic-devlog/0018/3.png)

- Allow Debug Tool－可以開關使用除錯工具。
- Allow In Game Logger－預設開啟一個測試用的資訊欄。
- Allow Incompatible Save－目前沒有寫版本間的存檔轉移機制，所以看狀況需要直接清除舊存檔。
- Skip Tutorial Setting－遊戲的最開始的設定選單全部都跳過的小功能。
- Allow Steamwork－沒有在上面的圖片中，因為 Steamwork 的運作機制很容易干擾編輯器內的操作，所以只有我很需要在編輯器內測試的時候才會手動改程式碼開啟，否則編輯器內一律不開，並且在對外編譯版本時看狀況輸出。

總之應該可以看出一些排列組合了：

- 個人測試用途的話全都會用上
- 給外部測試者時，會正常載入，但也還是會允許除錯工具的使用以防萬一
- 要測試對外釋出版，但又想要做額外的測試驗證時，會把測試用資訊欄強制打開
- 想要直接打包一個壓縮檔，不希望觸動 Steam 機制時，會特地關掉輸出版的 Steamwork 支援

這麼多排列組合撇除我自己會記錯的問題以外，偶爾測試修正後沒有正確勾選對應選項就輸出也是時常發生的事情。這件事情當然小規模還好，但因為擴大了平行測試對象的總量，各方切換的手忙腳亂就開始堆積起來。

於是這種人為操作的問題，就全都交給程式解決。

# 自動建置系統

![auto builder](/images/posts/autopanic-devlog/0018/1.png)

總之目標就是做出上圖這樣的一個一鍵輸出工具，避免人為失誤的可能性。

這個流程基本上要仰賴幾個東西：

- UnityEditor.BuildPipeline.BuildPlayer－簡單來說就是可以直接觸發建置的函式。
- UnityEditor.PlayerSettings.SetScriptingDefineSymbols－可以修改編輯器 PlayerSettings 內 Define Symbol 設定的函式。

沒了 XD

總之流程就是：

1. 根據版本類型，觸發 Define Symbol 的修改
2. 建置
3. 復原回去原本的 Define Symbol 設定

不過中間還是卡了很多怪東西像 `BuildTarget` 跟 `BuildTargetGroup` 的差異等等，姑且只是零碎的文件查詢，沒有啥大問題。

如此一來就可以一鍵完成版本建置，再也不怕自己手殘。各版本差異就交給 Define Symbol 去處理。覺得 Define Symbol 很容易寫歪的話，其實也還可以放一個 ScriptableObject Asset 來負責管理這些功能。

# 自動版本標記系統？

標題講了一半，所以另一半這是什麼？簡單來說就是如何讓我的懶病能繼續發揮作用的輔助系統。

《自動混亂》是個體量很小的遊戲，無論是設計上還是素材上，建置出來的遊戲容量打包壓縮只在 70MB 至 80MB 之間。在 Unity 2021 LTS 上，Mono 的建置時間是 20 秒，改用 IL2CPP 則是一分鐘。有試著建置的人應該都知道這時間有多短跟遊戲容量有多小 XDDDDD

隨之而來的是我的測試迭代很快，測試者遭遇的問題幾乎可以瞬間修復完，不會受到建置時間、上傳時間干擾。不過有著高速的迭代時間，卻持續遭遇另一個問題：我不知道這個版本到底是哪個版本。

Steam 的上傳機制對於使用者端收到通知要更新並不是即時的，除非使用者手動驗證檔案不然會馬上推成最新的版本。而就算驗證了，也難以知曉到底是不是真正的最新，我們需要其他資訊。Unity 有內建一個相關功能，也就是遊戲版本，可以用 `Application.version` 調度出來。但問題是.....快速迭代的我一點都不想要手動幫每次的版本都要打開 Project Settings 來增加版本號 XDDDDDD

於是，就可以來挪用 Git，版本管理的資訊。

# Commit SHA

像 Git 這樣的版本管理軟體，會持續記錄我們每次 Commit 的內容存在根目錄的 .git 資料夾內，並且為了驗證這些內容的正確性，會幫我們標記一個 SHA 值。

在每次打版本時都讀取目前的 SHA 值，就實務上可以達到紀錄現在的具體程式位置。

![Commit](/images/posts/autopanic-devlog/0018/5.png)

最右側就是可以直接對照出現在程式版本的 SHA 值，最後實務上則在遊戲畫面上顯示以下資訊：

```C#
$"v{手動紀錄的程式版本} {現在的 Git 分支} ({現在的 Commit Short SHA（只有完整 SHA 的前幾位數）})\n" +
$"{建置的版本設定} [{目標平台}]\n" +
$"@ {打版本當下的時間}";
```

![SHA](/images/posts/autopanic-devlog/0018/4.png)

如此一來，不只我個人的所有紀錄現在開始都內建了「這是什麼時候做的？」的效果，外部測試者傳截圖給我的時候我也立刻就知道所回報的問題到底我是修了還沒成功，還是根本就玩到還沒修正的版本。

# 延伸

自動建置都出來了下個正常步驟就是用程式上傳 Steam。許多人應該都因為遊戲容量而已經被迫要做這件事（Steamwork 限制網頁上傳只能小於 2GB），但總之因為《自動混亂》容量很小，就一直偷懶沒做 XD

而如果有一台多餘的電腦的話，也可以直接設立一個輸出流程，請獨立的電腦去負責完成遊戲的建置與上傳。

但總之現階段就先讓我再偷懶一下吧 XD