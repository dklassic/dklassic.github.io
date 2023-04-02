---
title: "07. 介面系統"
date: 2022-10-19T10:10:01+08:00
draft: true
tags: ["自動混亂"]
---

雖然沒有特別想要完全手刻介面系統，但當時的我先選擇要相信 Unity 新的 Input System。稍稍不幸的是這個 Input System 當時跟 Unity 自己的 UI 相關系統並不是配合得很好，於是我自然而然得設計一套客製的 UI 系統。

總之受到《Recompile》這部作品的影響，我決定放棄標準的圖形介面，而是刻意採用純文字顯示的介面。雖然我不會作 ASCII 動畫，然後為了要支援中文的正常顯示導致有一些設計無法施行，我認為相關的限制反而可以讓我更專注在其他重要的事情上。

回過頭來，當時我切實地需要一套 UI 系統，因為光是要生成敵人出來測試，就必須要仰賴 UI 系統。所以我先做了一個這樣的敵人生成工具：


如此一來，我終於不需要反覆拖拉，在編輯器跟遊戲內交替操作。
這個系統後續被擴張到可以輕易支援各種介面的顯示，我只要使用很簡單的程式碼宣告介面的構成，就可以產生出像這樣的介面：
```
protected override void InitializeUI()
{
    systemWindow ??= NewWindow("ui_system", DefaultSetup);
    AddButton("ui_system_Resume", systemWindow, () => CloseMenu(true, false));
    AddButton("ui_system_Visual", systemWindow, () => OpenSubMenu(0));
    AddButton("ui_system_Audio", systemWindow, () => OpenSubMenu(1));
    AddButton("ui_system_Control", systemWindow, () => OpenSubMenu(2));
    AddButton("ui_system_Language", systemWindow, () => OpenSubMenu(3));
    AddButton("ui_system_Accessibility", systemWindow, () => OpenSubMenu(4));
    exitUI = AddButton("ui_system_Exit", systemWindow, () => OpenSubMenu(7));
}
```


完成了這樣可用性極高的介面系統後，我就可以輕易地為了各種測試用途製作對應的遊戲內介面：


其實如果認真想起「介面」一詞，本來就是人與機器之間的互動手段。所以為了要設計好遊戲，先設計好一套能輕鬆拿來設計遊戲的介面似乎是很理所當然的事情。