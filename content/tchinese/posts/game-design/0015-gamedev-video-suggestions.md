---
title: "GDC 與遊戲開發相關影片推薦"
date: 2023-04-14T21:52:01+08:00
draft: false
tags: ["雜記"]
---

趁著 GDC 逐字稿補完計畫，決定趁此機會流水帳地推薦一些我這幾年覺得非常實用遊戲開發相關演講們。

原本是想說要整理一些中文共筆內容再開放大家一起使用討論，但總之後來在自己的專案推進度就有點自顧不暇的情況下，就只能無限期擱置了。以至於現在預計要撰文介紹的影片清單都已經累積到上百部了（死臉

![watch later](/images/posts/game-design/0015/1.png)

總之呃，趁這次機會讓我簡單介紹所有影片，然後就終於可以裝死把這個清單清空啦！

如果有人考慮要將這個清單另外存取下來的話，可以找這篇文章的 [md 原始檔](https://raw.githubusercontent.com/dklassic/dklassic.github.io/master/content/tchinese/posts/game-design/0015-gamedev-video-suggestions.md)應該會比較方便！

也記得正常狀況下這不是要人一口氣吞完的內容，看清楚目次，找自己有興趣的分類再往下著手才對 XD

**那就開始囉！**

# 美術製程

- https://youtu.be/DBqa7Um28m8 - Building a Living World from Ancient Ruins in Assassin's Creed Odyssey - Assassin's Creed Odyssey - 完整講述整個有點暴力的世界製作流程 XD
- https://youtu.be/x30j-PUN1G4 - Art Directing VFX for Stylized Games - Fortnite - 一個關於怎麼設計風格化美術的詳細指引。這時候的 Fortnite 還不是大逃殺遊戲呢！
- https://youtu.be/8_KBjd0iaCU - 2D Animation at Klei Entertainment - Shank, Mark of the Ninja - 詳盡解說了 Klei 作為的 2D 動畫製程。
- https://youtu.be/z-5djm1pRpU - The GDC 2015 Live 2D Animation Demo - Skullgirls - 一個現場展示 Skullgirls 動畫繪製過程的影片。
- https://youtu.be/bEIX-EQNZuQ - Cinematic Environment Production for Uncharted 4 - Uncharted 4 - 一個詳細展示多個遊戲中過場動畫的設計過程的演講。
- https://youtu.be/DFM5zbekZ7c - Procedural Generation of Cinematic Dialogues in Assassin's Creed Odyssey - Assassin's Creed Odyssey - 一個關於遊戲內容爆量的 AC Odyssey 使用怎樣的流程程序性生成對話場面的演講。

# 視覺設計

- https://youtu.be/aMcJ1Jvtef0 - 8 Bit & '8 Bitish' Graphics-Outside the Box - NA - 一個關於 8 Bit 與 8 Bit 風的美術概念差異，以及一個用色塊循環可以不需要做逐幀動畫就能創造出複雜美術的手段。
- https://youtu.be/A_Gni_2ecd4 - The Art of The Witness - The Witness - 一個探索風格化視覺，並甚至與建築事務所合作設計場景美術的過程。
- https://youtu.be/o7wFPkGmWdI - The Elementary Particles - Dishonored 2 - 一個分析基礎視覺特效設計構成的演講，非常詳盡。

# 渲染相關

- https://youtu.be/-w7wUs30OXk - Dev Diaries: Ray Tracing in World of Tanks - World of Tank - 光線追蹤實作技術演講，基本上是個對光線追蹤標準實作的詳盡演講，可以當作光線追蹤技術本身的教戰影片看。
- https://youtu.be/mDlmQYHApBU - Minecraft With RTX: Crafting a Real-Time Path-Tracer for Gaming - Minecraft - 一個詳盡講述 Minecraft Pathtracer 怎麼實作的演講。
- https://youtu.be/qnxCcY0WDAk - Achieving High-Quality, Low-Cost Skin: An Environment Approach - Final Fantasy XV - 基本上討論如何使用環境系統中的重複貼圖機制（Tiling）應對皮膚上毛細孔的問題，可以降低整體貼圖容量而不影響表現（同時會降低設計單一面孔的時間）。
- https://youtu.be/TUFcerTa6Ho - Star Citizen's Next-Gen Tech: Micro-Level Detail - From Battle Damage To Particle Effects + More - 採用的粒子系統使用的是 SDF 進行模擬，而不是直接用 CPU 進行碰撞判定，所以可以轉為 GPU 進行快速模擬；衣物使用重複的紋路做 Tiling，實作方式很類似上篇的皮膚做法，讓衣服可以快速更換底部紋路就產生不同的材質、性質與感受，還有很多其他低成本製作高品質成果的工具組。

# 關卡設計

- https://youtu.be/LFsMenc5Q8I - Applying 3D Level Design Skills to the 2D World of Hyper Light Drifter - Hyper Light Drifter - 關卡設計師將 3D 關卡設計經驗轉化為 2D 關卡設計，著重在用安全區域引導玩家，以及反過來破壞安全區域來挑戰玩家的設計。
- https://youtu.be/CEn44ZN4RLQ - Set this Game in Order: Organizing Hundreds of Levels and Mechanics - Pig Eat Ball - 主要在討論怎樣預先跟玩家溝通關卡特性，使得關卡越來越難的時候玩家仍然能夠應對這些預先已經溝通好的特性，進而完成關卡的挑戰。
- https://youtu.be/ythxeTIGZIc - Invisible Intuition: Blockmesh and Lighting Tips to Guide Players - Uncharted 4 - 描述在使用白模進行關卡設計時，可以考慮使用的玩家指引提示物，同時藉由顏色與實際美術設計師溝通場景性質；另一方面則是使用光線作為玩家指引，以及使用光線為模型帶來更好的觀感。
- https://youtu.be/CkHGuHd9BgU - Designing Unforgettable Titanfall Single Player Levels with Action Blocks - Titanfall 2 - 完成遊戲機制之後，先設計一堆讓人感到有趣的「遊戲片段」，再將這些遊戲片段轉化成具體遊戲內容的開發過程。
- https://youtu.be/hc8_W2PERZE - Level Design in Hitman: Guiding Players in a Non-Linear Sandbox - Hitman (2016) - 一個以 Hitman 第一季內容（教學跟巴黎關）為例，說明怎樣教導玩家遊玩這款沙盒遊戲。
- https://youtu.be/Bix1nLgneR4 - Building New York in Marvel's Spider-Man: It's Still Just Level Design - Marvel's Spider-Man - 詳細解釋這款遊戲中如何進行關卡設計流程，也舉了前作 Sunset Overdrive 的流程進行對比。

# 動畫

- https://youtu.be/LNidsMesxSE - Animation Bootcamp: An Indie Approach to Procedural Animation - Overgrowth - 一個以少到只有兩個 Keyframe 等級也可以靠各種形式的 Damping 就做出非常具備物理性的高品質動畫手段。神片。
- https://youtu.be/Ox2H3kUQByo - Unsynced: The Last of Us Melee System - The Last of Us - 原作的近戰動畫相關演講，基本上在講述就算動畫銜接性低，或者物理上空間不對，只要讓玩起來好就行的設計。
- https://youtu.be/BghECmeLda0 - Analysing the AI of The Last of Us Part II - The Last of Us Part 2 - 續作的近戰動畫相關演講，可惜 CJCAT 的演講原檔沒公開，但這篇 AI and Games 的介紹滿詳盡的，也與上一篇有點承襲關係。
- https://youtu.be/BYyv4KTegJI - Inertialization: High-Performance Animation Transitions in Gears of War - Gears of War 4 - 一個基於動作慣性讓角色持續動作的方式，目的是為了不要同時載入兩段動畫，對記憶體耗費太大，但也因此產生更加自然的切換動畫。
- https://youtu.be/zEYITZUHpo4 - 2019 Animation Tricks of the Trade - NA - 大大雜燴超實用動畫設計知識。
- https://youtu.be/o1tti636Kag - Animation Bootcamp: 2018 Tricks of the Trade - NA - 大雜燴超實用動畫設計知識。
- https://youtu.be/VIgHW4ddHLc - 2017 Animation Bootcamp: Tricks of the Trade - NA - 再一個雜燴超實用動畫設計知識。
- https://youtu.be/_1j5Tf6ulII - The Best Animation Tricks of the Trade (For 2016) - NA - 又一個大雜燴超實用動畫設計知識。
- https://youtu.be/50mIKB-NACU - Animation Bootcamp: Bringing Life to the Machines of Horizon Zero Dawn - Horizon Zero Dawn - 基本上描述了整個機器人的設計靈感，以及一些細項問題的處理方式。由於 Horizon Zero Dawn 幾乎都是啟發自動物的設計，所以大部分最後的解決方式也是從動物中取得。
- https://youtu.be/50mIKB-NACU - Player Traversal Mechanics in the Vast World of Horizon Zero Dawn - Horizon Zero Dawn - 著重在處理一些動畫上的滑步問題。
- https://youtu.be/uikbLyi-cug - Parkour: How to Improve Freedom of Movement in First-Person Games in 20 Simple Steps - Dying Light - 二十個小手段來處理玩家跑酷問題，裡面有解釋了特定設計問題上為什麼採用特定解決辦法的思考流程。非常實用導向，所以解決辦法有很多單純視角差的暴力手段。例如說裡面提到了動態暈眩問題，而最後的處理方式就是盡量讓鏡頭移動的狀況滑順。
- https://youtu.be/o-QLSjSSyVk - Character Control with Neural Networks and Machine Learning - NA - 一個使用神經網路驅使狀態機，不再需要設定一堆聖誕樹的做法，反之要在標記資料上下功夫。
- https://youtu.be/7S-_vuoKgR4 - Physics Animation in Uncharted 4: A Thief's End - Uncharted 4 - 整體重要要素是關於將部分的肢體做「Ragdoll」的設計，讓肢體可以適時地受到物理拉扯、環境影響而產生晃動、變形，看起來更有真實性。
- https://youtu.be/er4SgnjDYMI - Motion Capture Performance: An Actor's Approach - NA - 一個關於動作捕捉的雜談，非常詳盡描述動作捕捉演出者能怎樣幫助動畫師做出高品質的動畫。
- https://youtu.be/KSTn3ePDt50 - Motion Matching, The Future of Games Animation... Today - For Honor - 明確講述怎樣實作 Motion Matching 的演講。
- https://youtu.be/XjMKbElVNmg - Freeform Animation Rigging: Evolving the Animation Pipeline - NA - 一個 Unity 講述一個不需要有骨架專家的情況下就可以在不破壞骨架系統的情況下更方便調整動畫的工具。
- https://youtu.be/6TB62YKHwRQ - Animating Dauntless: Slaying AAA Animation on the Indie Scale - Dauntless - 提到一個小團隊怎樣用人類動作捕捉跟程序性動畫來實現高品質動畫的方式，其中一個特點是用人類來做動物的 Mocap 時，不要想說要類比骨骼，而是要想說類比體重分布的轉換。
![weight](/images/posts/game-design/0015/2.png)


# 程序性生成

- https://youtu.be/0bcZb-SsnrA - Wave Function Collapse in Bad North - Bad North - 非常詳盡的 Wave Function Collapse 實作過程。
- https://youtu.be/krxmNpqKxtI - Procedural Islands of 'Dauntless' - Dauntless - 使用 Houdini 藉由設定環境（植被、地形）自然互動的演變程序性產生浮空島的演講。
- https://youtu.be/wavnKZNSYqU - Between Tech and Art: The Vegetation of Horizon Zero Dawn - Horizon Zero Dawn - 以少到只有三人的環境美術團隊就可以根據規則系統、生態密度圖就產生出複雜而不會讓玩家感到有重複感的大規模環境。
- https://youtu.be/ToCozpl1sYY - GPU-Based Run-Time Procedural Placement in Horizon: Zero Dawn - Horizon Zero Dawn - 基本上是讓上面那篇演講可以成功的背景技術。
- https://youtu.be/hqXZhnrkBdo - Star Citizen's Next-Gen Tech In-Depth: World Generation, Galactic Scaling + More! - 主要在講利用濕度、溫度以及高度三張示意圖完成星球生成，然後同時可以設定屬性範圍讓美術擺放素材，會自動出現在星球相似屬性的位置，額外有趣的是會自動化變更素材的顏色讓整體看起來比較一致。
- https://youtu.be/4aw9uyj9MAE - Procedurally Crafting Manhattan for Marvel's Spider-Man - Marvel's Spider-Man - 完整的講述了城市的生成方式，提到了邊界處理的應對、岔路處理的手段。還有現實世界的紐約其實只有一條小巷存在，所以他們得人為製造小巷的事情。
- https://youtu.be/WumyfLEa6bU - Practical Procedural Generation for Everyone - No Man's Sky - 一個非常詳盡關於程序性生成可以使用的工具組解說，密度超高。
- https://youtu.be/C9RyEiEzMiU - Building Worlds in No Man's Sky Using Math(s) - No Man's Sky - 接續前影片，更多的程序性生成工具組。
- https://youtu.be/LCJlBs1B46M - Lucen: Indie gamedev with Houdini and UE4 - Lucen - 雖然是未上市遊戲，但是是關於一個單人開發者試著使用 Houdini 工具的各種不同程序性生成手段來製作一款開放世界遊戲的手段詳細介紹影片。

# 遊戲設計

- https://youtu.be/zyVTxGpEO30 - Practical Creativity - NA - 一個在講述可以用非常實用導向的方式進行遊戲設計建構的演講，非常詳盡又實用，推薦直接看比較好理解。
- https://youtu.be/qie4My7zOgI - Player-Driven Stories: How Do We Get There? - NA - 以 Portal 和 Red Dead Redemption 為例，討論系統、遊玩機制、故事結合在一起，就可以讓玩家感覺到自己藉由遊戲機制參與到劇情中的方法。
- https://youtu.be/8uE6-vIi1rQ - Cursed Problems in Game Design - League of Legends - 重點在講「不可解問題」，也就是「被官方承諾要解決卻有根本衝突的兩個問題」，以及設計上要努力讓玩家雖然不會直接被官方阻止，但是卻會因為難度較高而放棄的手段，藉此讓玩家不容易走向產生衝突的型態。
- https://youtu.be/JyuR2fKvQ20 - To Err is to Play: Human Error and Game Design - NA - 一個詳盡地分析人類失誤能對遊戲設計帶來怎樣影響的講座。
- https://youtu.be/vid5yZRKzs0 - Why Dark Souls Is The 'Ikea' Of Games - NA - 一個很有趣的譬喻 XD
- https://youtu.be/kBSB2X4Sbak - The Freedom Fallacy: Understanding Player Autonomy in Game Design - NA - 主要提到避免讓玩家感到困擾（有想做的事情卻做不到）的遊戲設計，並且對於許多遊戲應對玩家自由度的方式進行分析。
- https://youtu.be/CWi5gjxdh4o - Devil May Cry 5: Creating a Standout Action Game - Devil May Cry 5 - 提到了幾個比較廣泛的劇情場面，對照到遊戲內的特定劇情解釋影響力的來源，然後有非常多小項目說明如何讓玩家感覺到「有趣」。
- https://youtu.be/aIb-Lt7WX_s - Reinventing God of War - God of War - 提到了怎樣將遊戲機制以及遊戲故事融合為一的設計流程。
- https://youtu.be/nJParAVA1TM - Why Make Games? Lessons from Frostpunk and This War Of Mine - Frostpunk, This War of Mine - 這兩款遊戲都共同呈現了嚴肅的主題、精省的呈現手段等面貌，在這部影片裡面個別從遊戲原型討論到最後的樣貌，以及他們為什麼選擇這樣的主題。還有 This War of Mine 的所有人物圖像是工作室成員與大樓警衛的照片。
- https://youtu.be/D2ChyzAIzS0 - Theme Oriented Design: The Case of Phantom Doctrine - Phantom Doctrine - 主要概念是雖然遊戲機制並不是嶄新的設計，但是在遊戲主題上發揮功夫吸引玩家。
- https://youtu.be/0ymAdeWrsYM - Unravel: Using Empathy as a Game Mechanic - Unravel - 以人際互動、人與人的連結與遊戲機制本身融合為主軸進行的遊戲設計，讓玩家的同理畫為遊戲機制。
- https://youtu.be/OfSpBoA6TWw - Dead Cells: What the F*n!? - Dead Cells - 一個關於如何讓玩家享受困難的遊戲的演講。實務內容是一些遊戲中其實有很多幫助玩家作弊的設計，但因為有這些作弊讓玩家比較不容易感到無力，而可以享受遊戲的困難的部分。
- https://youtu.be/LtBNffzWhf4 - How Dead Cells Secretly Stops You From Dying - Dead Cells - 可以當作上面的演講的簡略版。
- https://youtu.be/0pBvMIUk1nQ - Cultist Simulator: Designing an Experimental Game for Commercial Success - Cultist Simulator - 主要重點在於跟玩家建立起互信關係協助調整遊戲方向。
- https://youtu.be/IB28lsqUT3Q - The Living World of The Witcher 3: The Wild Hunt - The Witcher 3 - 一個關於遊戲內數值經濟的平衡與一些經濟學上機制設計干擾玩家決策的設計。
- https://youtu.be/6UTcj-BQ7Qs - Breaking the Rules of Game Design - NA - 主要是遊戲構成要素會帶來玩家期待，破壞這個期待本身也是一項遊戲設計工具。
- https://youtu.be/kX8Jn3XPoWQ - Taking an Axe to God of War Gameplay - God of War - 完整分析戰鬥設計的各方面。
- https://youtu.be/uKwi_5nePZg - The Making of Divinity: Original Sin 2 - Divinity: Original Sin 2 - 內容比較廣泛，大致上從工作室構成、QA 流程設計、翻譯等多種面向都有提到。
- https://youtu.be/c2YRVWZupwo - Integrating Narrative into Game Design: A Portal Post-Mortem - Portal - 講述在團隊極小的情況下 Portal 是怎樣結合遊戲性跟敘事產生出這款作品，幾乎可以說是所有遊戲設計都是為了限制而產生的。
- https://youtu.be/P4Um97AUqp4 - 'FTL: Faster Than Light' Postmortem: Designing Without a Pitch - FTL Faster Than Light - 詳盡說明了整個 FTL 開發過程的演講，有設計，有募資，有社群互動的討論。
- https://youtu.be/s_I07Iq_2XM - Into the Breach Design Postmortem - Into the Breach - 大致上整體分析了開發過程的決策，裡面有很多簡化遊戲系統的參考。
- https://youtu.be/7rqfbvnO_H0 - Slay the Spire: Metrics Driven Design and Balance - Slay the Spire - 詳細地說明從搶先體驗到實際上市期間的開發過程與遊戲平衡拿捏方式。
- https://youtu.be/U4uH1ynH3Rs - Open-Ended Puzzle Design at Zachtronics - NA - Zachtronics 擅長製作近似現實環境的工具謎題，例如說製作晶片、破解網站，在這裡完整地用訪談的方式討論為什麼會設計出這樣的遊戲，以及製作過程如何進行。
- https://youtu.be/7R-x9NSBS2Y - The Design of Subnautica - Subnautica - 完整講述整個 Subnautica 的遊戲結構以及為什麼會發展出這樣的設計（甚至包含了意料之外的設計）。
- https://youtu.be/JFaOYYSxSEA - Classic Game Postmortem - Another World - 一個關於經典遊戲 Another World 的設計完整分析。
- https://youtu.be/0xVYVP0hxME - Weaving 13 Prototypes into 1 Game: Lessons from Edith Finch - What Remains of Edith Finch - 詳盡講述遊戲原型轉為實際遊戲的過程，開發期間基本上就是分開做了 13 個小遊戲原型然後最後塞成一個遊戲作品。
- https://youtu.be/QyMsF31NdNc - Breaking Conventions with The Legend of Zelda: Breath of the Wild - The Legend of Zelda Breath of the Wild - 詳盡說明曠野之息全方面設計的演講，真的很詳盡。
- https://youtu.be/r4-O_7wSyAQ - Dealing with Scope Change in Heat Signature and Gunpoint - Heat Signature, Gunpoint - 詳細說明 Heat Signature 的設計（過度擴張）理念。
- https://youtu.be/A7ejh3YUbac - How We Created Mark of the Ninja Without (Totally) Losing Our Minds - Mark of the Ninja - 主要在討論遊戲機制（遊戲片段）為主的開發方式，並且維持工作室的正常經營。著重在要建立能被測試考驗的假說。
![mark of the ninja](/images/posts/game-design/0015/3.png)

# 遊戲數學

- https://youtu.be/J5qnnxFoBss - Math for Game Programmers: Dark Secrets of the RNG - NA - 舉例說明純粹機率與絕對機率性質，開發者可以用絕對機率確保使用者不會真的賽到很悲劇的純機率而感到不公平。
- https://youtu.be/mr5xkf6zSzk - Math for Game Programmers: Fast and Funky 1D Nonlinear Transformations - NA - 一個各種不同形式的多元數學操作的演講，主要用意是要拿來作一些 Easing 效果。
- https://youtu.be/hG9SzQxaCm8 - Math for Game Programmers: Building a Better Jump - NA - 一個講述各種不同形式的跳躍相關數學工具的講座，可以藉此來操作不同的跳躍操作特性。


# 遊戲 AI

- https://youtu.be/ygNRNru1B_s - Eos is Alive: The AI Systems of Final Fantasy XV - Final Fantasy XV - 雖然背景音樂有夠大聲，但大致提到了如何應對單一 AI 的動畫系統，同時又設計一個比較廣泛的 AI 分配系統來驅動個別 AI 行動。
- https://youtu.be/VoXSJBVqdek - Taking Back What's Ours: The AI of Dishonored 2 - Dishonored 2 - 非常鉅細靡遺，甚至到描述資料結構設計的程度的演講。主要在討論怎樣讓多名 NPC 可以定位環境，避免 NPC 行為過於無意義。整個設計延伸到潛行與搜索、相對應對話系統以及動畫系統等面向。
- https://youtu.be/lbyGzzcKg9U - Raising Atreus for Battle in God of War - God of War - 基本上逐一地提出兒子的各種設計面向，以及各種投機設計讓兒子更有戰鬥的參與感。有很多關於怎樣讓兒子傳送到位，讓玩家不會覺得兒子是個累贅的設計。
- https://youtu.be/Qq_xX1JCreI - AI Arborist: Proper Cultivation and Care for Your Behavior Trees - NA - 大致上提到 Behavior Tree 的好處與壞處，並且分析一些可行的改變。
- https://youtu.be/tAbBID3N64A - AI-driven Dynamic Dialog through Fuzzy Pattern Matching - Left 4 Dead - 追蹤遊戲內要素的動態對話系統，讓遊戲中的人物可以理解遊戲中的情境來進行對應的對話。
- https://youtu.be/wj-2vbiyHnI - Do You Copy? Dialog System and Tools in Firewatch - Firewatch - 基本上是延伸自上面的演講的實作。
- https://youtu.be/RO2CKsl2OmI - Behavior is Brittle: Testing Game AI - NA - 一個關於測試遊戲 AI 的有趣一小時雜談。
- https://www.gdcvault.com/play/1020338/The-Last-of-Us-Human - The Last of Us: Human Enemy AI - The Last of Us - 關於作品 AI 決策手段的詳細說明。
- https://youtu.be/G8W7EQKBgcg - Authored vs. Systemic: Finding a Balance for Combat AI in Uncharted 4 - Uncharted 4 - 同樣這一系列息息相關的內容 XD，主要內容集中在講泛用戰鬥 AI 跟特製場面 AI 的平衡，其中有些他們持續認為實用的小技巧，像是讓敵人交替開火的設計方式。
- https://www.gdcvault.com/play/1029277/Picking-a-Good-Spot - Picking a Good Spot: Naughty Dog's Post System - The Last of Us Part 1 - 剛好是延續前幾篇演講的後續延伸。
- https://youtu.be/c06DZ81Tbmk - Hacking into the Combat AI of Watch Dogs 2 - Watch Dogs 2 - 詳盡解釋了 AI 如何理解環境、選取掩體、進行環境互動的方式。
- https://youtu.be/HzhDjbsXA9s - AI & Animation in Assassin's Creed Brotherhood - Assassin's Creed Brotherhood - AC Brotherhood 的群眾系統，雖然以現在來說有點古老，但是如果要寫一個群眾系統的話還是很可以拿來參考的骨幹。
- https://youtu.be/pUXS9snrZE4 - Can You See Me Now? Building Robust AI Sensory Systems - NA - 一個關於能如何建構一個讓 AI 能根據各種感官應對玩家輸入的系統的演講。
- https://youtu.be/Rz2cNWVLncI - Massive Crowd on Assassin's Creed Unity: AI Recycling - Assassin's Creed Unity - 一個完整講述 AC Unity 中如何將 AI 分成多層級、作層級切換，並且為各層級的具體實作說明的演講。因此才有辦法達成該遊戲中極誇張的 NPC 數量。
- https://youtu.be/a09vnDjmY_E - Virtual Insanity: Meta AI on Assassin's Creed: Origins - Assassin's Creed Origins - 一個講述 AC Origins 中的 Meta AI 如何驅使超大範圍人群行動的設計，讓 AI 試著理解環境並且努力完成其需求。也有關於環境資料結構、測試手段的說明。

# 遊戲物理

- https://youtu.be/prXuyMCgbTc - Exploring the Tech and Design of Noita - Noita - 詳盡說明物理性極強的 Noita 的物理運作方式跟一些最佳化手段。
- https://youtu.be/SKXqWcaoTGE - The Science of Off-Roading: Uncharted 4's 4x4 - Uncharted 4 - 算是非常完整地呈現如何設計一台四輪驅動車的整體過程，同時又不是完全執著於物理模擬級的表現讓玩家玩得開心。
- https://youtu.be/mHWFzo2no94 - Vault, Slide, Mantle: Building Brink's SMART System - Brink - 關於 Brink 自動跑酷系統詳盡說明實作的演講。
- https://youtu.be/SHinxAhv1ZE - Physics for Game Programmers: Understanding Constraints - NA - 一個詳盡的遊戲物理系統的實作，另外 CJCAT 也有兩個演講在講同樣的內容「遊戲物理約束 [part 1](https://www.ptt.cc/bbs/GameDesign/M.1586764005.A.DDE.html)、[part 2](https://www.ptt.cc/bbs/GameDesign/M.1601107542.A.38B.html)」。

# 遊戲程式

- https://youtu.be/RDCCyrC1sto - Beyond Framerate: Taming Your Timeslice Through Asynchrony - NA - 一個以分散執行時機降低 CPU 瞬間超載的演講，著重在非同步運算的管理。
- https://youtu.be/KDhKyIZd3O8 - Marvel's Spider-Man: A Technical Postmortem - Marvel's Spider-Man - 一個非常詳盡的開發期間遭遇的技術問題的說明演講。

# 敘事設計

- https://youtu.be/WBF2RyeEOlA - What Wikipedia Doesn't Know Can Hurt You: Writer Research Skills - NA - 大致上在說明作為腳本家撰寫故事時該注意甚麼、能從怎樣的來源獲得資訊，以及該怎樣注意使用這些資訊。
- https://youtu.be/HZft_U4Fc-U - Narrative Sorcery: Coherent Storytelling in an Open World - Sorcery - 一個有趣的敘事設計結構，來確保開放世界框架下不會導致故事難以設計，確保永遠都會講出邏輯上合理的故事。
- https://youtu.be/3eYHtDGOM8U - Creating Interactive Film Scripts for 3D Adventures with Ink - Heaven's Vault - 一個介紹開源敘事設計語言 Ink 的具體實用效果。

# 音樂音效配音

- https://youtu.be/U4FNBMZsqrY - DOOM: Behind the Music - DOOM - 由業界傳奇的 Mick Gordon 講述音樂的製作方式，大致上在討論說「要使用不同的音樂製作手段，才能夠產生不同的音樂」、「如果使用相同的手段，即便達到業主的要求，也依然只是有不同風味的相同音樂」還有具體提出他的回饋式音樂系統設計的方式。
- https://youtu.be/sZ8gOm3t40E - Tacoma: An Experimental VO Production Postmortem - Tacoma - 各方面都有討論，從錄音室的配置方式到如何引導配音員的手段。
- https://youtu.be/NfRtRldvnkA - Zen and the Art of Game Audio Maintenance - Horizon Zero Dawn - 一個關於創作心態與遊戲音效開發的有趣演講。
- https://youtu.be/FEK8Ggg2xxQ - Data Driven Granular Synthesis for Video Games - NA - 一個有趣的，可以自動分析聲音樣本不同層級，並且用以組合出豐富音效的工具展示，潛在可以成為一個永遠不會聽起來單調的音效系統基礎。
- https://youtu.be/Rz7WwwlDjOA - Next Level Creature Sound Design - Elder Scrolls Online, Alien Isolation, Total War: Warhammer - 一個非常詳盡的生物音效設計演講，清楚展示多層級的特效鍊對音效各步驟產生了什麼影響。還有人類為生物配音的能力其實超強，方便命令，遠比對動物實際錄音容易。

# 工具開發

- https://youtu.be/KRJkBxKv1VM - Creating a Tools Pipeline for Horizon: Zero Dawn - Horizon Zero Dawn - 非常細節導向的工具開發方針跟部分內容實作。
- https://youtu.be/Iqmg4gblreo - Geometry in Milliseconds: Real-Time Constructive Solid Geometry - NA - 一個關於 CSG Tool 性質介紹的演講。
- https://youtu.be/VRm3d0TqMq4 - Level Design Workshop: Improving Tool Design Through Editor Triage - NA - 一個關於多種工具使用者體驗設計概念的形式舉例的演講。

# 行銷、社群、市場分析

- https://youtu.be/uy0Dfr-mnUY - Know Your Market: Making Indie Games That Sell - Life Goes On - 一個詳盡分析說明為什麼這款遊戲沒有獲得成功的演講，裡面講述了非常多分析手段。
- https://youtu.be/mrZlSDngwH8 - The Diary of a Modern PR Campaign: How to Plan Your Game's Promotion - NA - 一個詳盡展示遊戲宣傳可以如何分階段，並每階段能做什麼事情的扎實演講。
- https://youtu.be/zctUBJ-kBe8 - The Power of an Embedded Community Platform to Inform, Engage, Educate and Retain - NA - 一個詳細說明能怎樣構成一個讓玩家願意遊玩遊戲的社群環境的演講。

# 專案管理

- https://youtu.be/4DWdnoLosZ8 - Embracing Ambiguity: How to Do Good Work When You Don't Know What to Do - NA - 一個討論遊戲開發過程中，模糊性的存在，以及要能判斷這些模糊性是否會成為開發上的困難的手段。
- https://youtu.be/amlwcI8dh_g - Three Steps to Becoming a Better Artist Immediately - NA - 雖然看起來是關於美術的演講，但真正的演講內容集中在怎樣與人正確溝通出需要的目標，對於怎樣具體溝通美術有很好的範例。

# 雜項

- https://youtu.be/f786ak3GKQo - The Portal Locomotion of Budget Cuts - Budget Cuts - 詳盡講述怎樣應對玩家做出意料之外的行為來設計一個傳送門的機制。
- https://youtu.be/C7307qRmlMI - 50 Game Camera Mistakes - Journey - 一個非常詳盡的鏡頭問題與解方演講，最大的體悟是太多遊戲都自然而然使用第三人稱跟隨鏡頭設計，但實質上並沒有意義反而增加很多困難。
- https://youtu.be/4BuvKotqpWo - Efficient Texture Streaming in Titanfall 2 - Titanfall 2 - 貼圖串流技術說明，非常技術導向的演講，無法摘要 XD 但現在的硬體速度來說可能有點過時了。
- https://youtu.be/-VZTudg6ifg - Design vs. Story: How Uncharted: The Lost Legacy Addressed the Elephant in the Room - Uncharted: The Lost Legacy - 主要討論是他們為什麼決定要建構大象場面，以及他們如何持續修改場景設計合理化這個設計的具體過程。
- https://youtu.be/WjPiJn9dkxs - The Surge 2: Behind The Scenes - The Evolution Of The Fledge Engine - The Surge 2 - 關於 The Surge 2 客製引擎的設計的詳盡雜談。
- https://youtu.be/cV5HArLYajE - Everyone Watching This Is Fired: Tips for Game Industry Programmers - NA - 一個關於遊戲開發心態的雜談。
- https://youtu.be/XKMj2aYfnWI - The State & Future of AR Games: Rose-Colored Glasses - NA - 討論 AR 遊戲的限制與發展，主要提到的內容是物件辨識問題、低延遲問題，以及如何拿來幫助人類生活發展而不是造成阻礙。
- https://youtu.be/7z_EIjNG0pQ - High Dynamic Range Color Grading and Display in Frostbite - NA - 一個詳盡的關於 HDR 的演講，不過已經有點過時了。
- https://youtu.be/9FAXAgRrOSE - Art Direction Bootcamp: Building a Creative Future with Artificial Intelligence - NA - 人工智慧對創作的輔助，有點 2019 年預測現在 AI 的進步跟可能帶來的幫助的演講 XD
- https://youtu.be/4Z0aUEBp_Os - Deterministic vs. Replicated AI: Building the Battlefield of For Honor - For Honor - 為了多電腦同時同步對戰結果而設計的 Deterministic 式遊戲邏輯計算方式，雖然結果而論電腦之間直接連線的機制後來被廢除。
- https://youtu.be/HrZWGGl5duk - Prototype Through Production: Pro Guitar in Rock Band 3 - Rock Band 3 - 從 Rock Band 3 看現實操作轉遊戲內容的過程。
- https://youtu.be/48Ymh4Ge5j8 - Boss Up: Boss Battle Design Fundamentals and Retrospective - NA - 一個詳盡統整分析頭目戰設計的演講。
- https://www.slideshare.net/HEXADRIVE/final-fantasy-hd-hd - FINAL FANTASY 零式HDにみる 新しいHDリマスター - Final Fantasy Type-0 HD - 因為是個關於將 PSP 遊戲重製為 PS4 遊戲的演講，所以機本身可以當作橫跨兩個世代的遊戲技術大統整。
- https://youtu.be/XPPtLNkVPWY - Game Design Tools: For When Spreadsheets and Flowcharts Aren't Enough - NA - 字面上的，表格、流程圖以外，多種遊戲設計工具分析說明優劣。
- https://youtu.be/wWt29xdW_kA - Battletoads Tech Talk: The challenge of 11 game modes - Battletoads - 一個非常詳盡說明這款遊戲如何做各種類型的最佳化的演講，Unity 開發者特別適用。