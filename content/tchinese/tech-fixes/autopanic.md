---
title: "《自動混亂》技術問題指引"
date: 2022-05-10T19:07:26+08:00
draft: false
enableComments: false
showTip: false
---

**如果你遊玩《自動混亂》時遭遇到技術問題，請先閱讀這篇文章**

感謝你遊玩我的遊戲！如果讓你沒辦法好好享受可就糟了，所以我準備了一些潛在可能可以解決你遭遇問題的手段：

# 請確保你有最新的顯示卡驅動程式

如果你在遊戲中遭遇到任何問題，請先確認你已經安裝最新的顯示卡驅動程式。許多問題都可以靠取得對應廠商最新的驅動程式解決，而你可以在這裡取得最新的驅動程式：

- **AMD 顯示卡**: [https://www.amd.com/zh-hant/support](https://www.amd.com/zh-hant/support)
- **NVIDIA 顯示卡**: [https://www.nvidia.com/Download/index.aspx?lang=tw](https://www.nvidia.com/Download/index.aspx?lang=tw)
- **Intel 顯示卡**: [https://www.intel.com.tw/content/www/tw/zh/download-center/home.html](https://www.intel.com.tw/content/www/tw/zh/download-center/home.html)

# 驗證遊戲檔案

有時候在下載遊戲更新時，可能會發生錯誤。這樣的錯誤可能會導致遊戲無法正常執行，或者是遊戲中出現奇怪的畫面錯誤。如果你遭遇的問題是這樣的，可以試著驗證透過遊戲啟動器驗證你的安裝狀況，並且取代掉缺少或損壞的檔案：

**Steam 平台：**
1. 在「收藏庫」右鍵點擊《**自動混亂**》
2. 選擇「內容...」，然後點選 「本機檔案」分頁
3. 選擇「驗證遊戲檔案的完整性...」

你也可以嘗試完全解除安裝並重新安裝遊戲。同時可能會需要重新啟動電腦才能發揮效果。

# 如果你沒辦法正常啟動遊戲，或者是看見黑色的畫面

請考慮你的系統狀況並且依序嘗試適用的解決方案：

1. Windows 與 Proton 使用者： 

    目前遊戲有推出 Vulkan 和 32 位元版的考慮。如果啟動遊戲時有相關選項，你應該可以先嘗試看看這兩個啟動選項。

2. 如果你使用的是 Steam，請嘗試停用你的 Steam 內嵌介面：
    1. 在「收藏庫」右鍵點擊《**自動混亂**》
    2. 選擇「內容...」
    3. 關閉「在遊戲時啟用 Steam 內嵌介面」

3. 如果你曾經執行遊戲成功過，試著到你登陸檔備份並且刪除你的設定資料：

    `Computer\HKEY_CURRENT_USER\Software\ChosenConcept\Autopanic`

    **注意** 這與遊戲的保存紀錄無關。單純是把一些相關系統設定復原回預設設定。

4. 試著用「系統管理員」權限執行 Steam：
    1. 如果 Steam 還在執行中的話請關閉
    2. 找到 Steam 的執行檔
    3. 右鍵點擊執行檔
    4. 選擇「以系統管理員身分執行」

5. 試著下載並安裝[最新的 Visual C++可轉散發套件](https://learn.microsoft.com/zh-tw/cpp/windows/latest-supported-vc-redist?view=msvc-170)，某些狀況下可能會沒有正確安裝。

6. 從你的 PC 上移除掉所有非必要的 USB 或者藍芽裝置。

7. Windows 8 使用者：如果你看到了 D3DCompiler_47.dll 遺失的錯誤，可以在[這裡](https://wikidll.com/microsoft/d3dcompiler_47-dll)下載安裝。

8. Proton 使用者：請參照以下連結確認你的顯示卡有沒有設定正確
    [https://github.com/ValveSoftware/Proton/wiki/Requirements#amdintel](https://github.com/ValveSoftware/Proton/wiki/Requirements#amdintel)

    「Arch Linux - Intel Graphics Drivers - Modesetting VS Intel」
    [https://www.youtube.com/watch?v=zEhAJMQYSws](https://www.youtube.com/watch?v=zEhAJMQYSws)

# 如果遊戲無法啟動，或者是存讀檔無法進行

請考慮你的系統狀況並且依序嘗試適用的解決方案：

1. 特定防毒軟體可能會造成這種性質的問題。如果你看到錯誤訊息說「警告：無法存檔」或者「警告：無法讀檔」的話，這很有可能就是原因出處。要解決這個問題，就得在你的防毒軟體裡加入白名單，或者是直接關閉。

2. 確保以下路徑存在：

    `文件\Saved Games\Autopanic`

    並且 Windows Defender 與存取受控制的資料夾中允許使用相關資料夾：[允許 app 存取受控制的資料夾](https://support.microsoft.com/zh-tw/windows/%E5%85%81%E8%A8%B1-app-%E5%AD%98%E5%8F%96%E5%8F%97%E6%8E%A7%E5%88%B6%E7%9A%84%E8%B3%87%E6%96%99%E5%A4%BE-b5b6627a-b008-2ca2-7931-7e51e912b034)

3. OneDrive 和 Google Drive 的同步系統有可能會干擾存檔。請參照這篇文章的第五步驟進行（英文：[https://windowsreport.com/access-is-denied-windows-10/](https://windowsreport.com/access-is-denied-windows-10/)）以關閉 OneDrive 對遊戲存檔資料夾的同步。

# 如果遭遇到了卡頓、停頓、延遲、幀率低落或效能問題

《**自動混亂**》**因為敵人 AI 的運作方式是個對<abbr title="CPU">中央處理器</abbr>需求很高的遊戲。常態的低電壓裝置（例如說舊世代的 Intel、AMD U 系列核心）可能會跑得不太好，但整體來說遊戲很能善用多核心的性質。

也有其他你可以改進遊戲體驗的方式：

- 在「顯示」→「進階」啟用「動態解析度」
- 降低解析度可以稍微緩解一些 CPU 需求
- 調整幀率限制可以維持穩定的遊玩環境

如果前述選項都沒有幫助，而你認為你的裝置比最低測試過的還要好，可以依序嘗試以下操作：

1. 確保你有最新的顯示驅動程式。
2. 試著在遊戲中切換各類型全螢幕顯示與幀率限制設定。
3. 如果你有啟用 Nvidia G-Sync 或 AMD FreeSync，請停用並且依適用狀況啟用 AMD Anti-Lag。
4. Windows 與 Proton 使用者：如果這些選項後來有實裝的話，請在啟動遊戲時嘗試使用 Vulkan 與 32 位元版。
5. 關閉其他執行中的程式。
6. 如果適用的話，在你的顯示卡控制面板中找尋「最大效能優先」、「快速垂直同步」等相關選項並且嘗試啟用。
7. 確保沒有對 Autopanic.exe 啟用 Windows 7 相容模式。
8. 停用所有內嵌介面，像是 Steam 或 GeForce 等。
9. 物理上停用所有次要顯示裝置。
10. 如果你使用的是 Nvidia 顯示卡，請參照這篇文章指引（英文：[https://www.techadvisor.co.uk/how-to/pc-components/how-set-default-graphics-card-3612668/](https://www.techadvisor.co.uk/how-to/pc-components/how-set-default-graphics-card-3612668/)）並且確保遊戲是在使用對應顯示卡，而不是使用內建的顯示晶片。
11. 除此之外，確保你的 Windows 效能設定在執行《**自動混亂**》時是處於「高效能模式」。確保遊戲執行的螢幕是連接在 Nvidia 顯示卡上的。

**注意**：如果你找不到選擇顯示卡的選項，你可能要在系統 BIOS 中調整。在 BIOS 中停用 Intel HD 顯示晶片並且確保使用 PCIe 裝置作為預設的顯示裝置，不要使用「自動」。

# 如果高解析度下還是看起來很模糊

大概是動態解析度造成的，可以在`顯示` → `進階`中停用。

動態解析度在遊戲執行初期過於卡頓時會被自動啟動，實作方式有點積極但為了確保玩家有穩定的體驗還是值得使用。

# 如果你有多個螢幕卻無法切換顯示

設計上刻意禁止在全螢幕模式下切換螢幕。

因為在全螢幕模式下的切換會造成太多詭異的問題，所以得請你先切換至無邊框或者是視窗化模式再切換螢幕。

# 滑鼠與手把輸入問題

如果你時不時遭遇到輸入偵測方面的問題，請將所有連接的手把都斷開連結。

《**自動混亂**》面對無線、藍芽遊戲手把時可能會有一些連接問題，而除此之外如果有任何問題，也可以嘗試在設定選單中關閉手把震動功能，可能會解決問題。

如果你在使用滑鼠時有額外的問題，像是瞄準的速度不如預期，可以試著這樣設定：在系統選單的`輔助`中，將`使用滑鼠瞄準`改為`只用滑鼠`。大部分狀況下應該這樣就可以解決問題。

如果你的手把沒有辦法被遊戲偵測到，請嘗試斷開所有手把連結，確保「裝置管理員」中沒有任何手把。接著將你的主要手把重新連接並再次嘗試。要注意這款遊戲隨時都會偵測所有手把的輸入。

你也可以嘗試調整 <abbr title="Steam Input">Steam 輸入</abbr>，無論是開啟或是關閉都有可能帶來正確的手把偵測。

同時也有一些已知問題：

- DualShock 4 和 DualSense 手把的觸控板按鍵在啟用 Steam 輸入時都會被顯示（並且實際上對應到）Share 按鈕。但如果你關閉 Steam 輸入的話，就會被正確顯示為觸控板按鍵。

# 音效問題

如果你遭遇到遊戲音效的問題，請先確定你的音效驅動程式是最新版：

- 開啟 Windows 的「裝置管理員」
- 展開「音訊輸入與輸出」的裝置清單
- 右鍵點選你的音效裝置，並且選擇「更新驅動程式」

如果音效詭異地中途被斷開，可以嘗試將遊戲選單中任何非最大值的音效設定調整到最大值，並且使用你的系統音量設定來控制音量。

同時也可以注意，如果你使用的手把是 DualShock 4 或 DualSense，由於手把上有音效裝置，可能會劫走音效輸出。請注意確認系統的音效輸出是不是被設定在手把的音效裝置上。

# 如果你的存檔進度發生預料之外的損壞

如果有什麼事情導致你的存檔進度遺失，或者是存檔本身消失，還是有機會拿回你的紀錄。

如果你的存檔消失或者可能損毀而沒有辦法正確載入遊戲，請示著重新安裝遊戲。如果依然無效的化，請參照以下步驟：

- 在 **Windows** 上，前往「\Documents\Saved Games\Autopanic」
    1. 將「save.dat」重新命名為「save.dat.old」備用
    2. 根據**修改日期**排序，並且找到最新的備份存檔
        - 例如會叫做：「save.dat.bak1」、「save.dat.bak2」
    3. 將該存檔重新命名為「save.dat」
    4. 打開遊戲，看能不能順利載入
    5. 如果沒用的話，可以從**第一步**重來，去試試看下一個最近期的備份存檔能否使用

如果你已經檢查所有備份存檔都沒有用，請前往 Steam 的**技術支援**討論區留言，我會盡力幫你處理存檔問題。

# 如果全都沒幫助

如果在這裡沒有找到任何解決辦法，請在 Steam 的**技術支援**討論區或者 Discord 的 **#自動混亂零式-技術支援** 頻道請求協助。
同時也請提供以下檔案：

1. Windows 使用者，請提供你的 [DxDiag](https://support.microsoft.com/zh-tw/windows/%E9%96%8B%E5%95%9F%E4%B8%A6%E5%9F%B7%E8%A1%8C-dxdiag-exe-dad7792c-2ad5-f6cd-5a37-bf92228dfd85)

2. 你的 Player.log，位置參考以下

Windows：
`Users\[Username]\AppData\LocalLow\ChosenConcept\Autopanic\Player.log`

感謝你的閱讀。希望這篇文章能幫助你快點找到解決辦法。