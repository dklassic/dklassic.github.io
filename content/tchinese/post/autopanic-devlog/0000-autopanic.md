---
title: "00. 開發定位"
date: 2022-10-14T04:02:38+08:00
draft: false
tags: ["自動混亂"]
---
或許應該要再另外講清楚，接下來開始連載的開發日誌，性質上比較是給「想要開發遊戲」的人看的。因此內容會寫得滿繁複的，大概不是很適合純粹的玩家看 XD

總之就，開始囉（？）

![old thumbnail](/images/posts/autopanic-devlog/0000/1.png)
![combat action](/images/posts/autopanic-devlog/0000/2.gif)


自動混亂是一個「完全敘事表現的極簡風雙搖桿射擊遊戲」，並且有一些類 Rogue 要素。

之所以在任何表現機會都強調是「帶有類 Rogue 要素」，而不是直接稱為一款「類 Rogue」，基本上還是希望不要引起錯誤的玩家期待。畢竟身為新手單人開發者，所能提供的內容量恐怕是難以跟市面上成熟的類 Rogue 作品相比。

就結果而論，現在遊戲內有 20 種武器型態、20 種主要能力與 40 種次要能力，整體來說也刻意著重在差異性，所以應該已經算是可以搭配出多元玩法的數字了。但一旦要跟其他作品比，跟動輒上百種能力、武器的作品比就顯得相形失色。

不過真要問我會不會想要擴充更多要素，其實也還好。選擇的能力都姑且有合理的差異性，至少對我自娛來說已經能提供夠多元的遊戲性了。而且如果陷入內容量迷思使得平衡作業更難進行的話，最後造成開發困難就本末倒置了。

總之要說明整個開發過程，還是要先來了解清楚整個遊戲的定位。

# 故事結構

主角必須在 AI 夥伴的協助下，登上設施的頂層，弄清楚到底發生了什麼事。

# 目標

玩過《十三機兵防衛圈》後我對於戰鬥的視覺設計感到敬佩。在一款明明是機器人戰鬥的作品中，戰鬥中並沒有寫實的機器人表現，而是使用簡約的符號象徵性代表。戰鬥介面的視覺設計簡單到我覺得自己都能做出來，但依然有足夠的高科技格調而不顯簡陋。

但戰鬥設計本身實在是太......對不起這個渾厚的故事也對不起這個很棒的視覺設計。即便是困難模式下也在完全沒有輸過半場戰鬥的情況下結束了整個遊戲，讓人不免有些失望感。

當時在設計雙搖桿射擊遊戲的我，認為這是個意外容易製作，也可以輕易帶來爽快感的遊戲型態。也因此我想要試著做一款有著《十三機兵防衛圈》戰鬥視覺的雙搖桿射擊遊戲，就是這樣！

事後往類 Rogue 要素發展又是另一回事了。但因為早早就訂下了「完成近乎不可能的挑戰」這個核心概念，所以往類 Rogue 發展似乎也算理所當然。

# 開發紀錄

這次必須像這樣事後慢慢補述開發記錄，除了因為開發中的我就懶以外，畢竟身為一個零知識的新手，開發路上充滿著各種混亂情境。

也唯有在接近完工的現在，我才能整理清楚思緒寫出個結構完整的紀錄。

# 視覺設計

由於我沒有 3D 建模知識，也沒有什麼過人的美術才能可以利用，所以遊戲早早就決定要以向量圖形與基本 3D 模型來處理。

這個決策也回頭影響到了我的遊戲設計本身。有時候我會想到一個有趣的設計，但最後僅僅因為「找不到能被簡單表現出來的方式」而放棄。雖然有時候會有點不甘心，但事後看來這讓我的開發過程非常專注在絕有效的部分，而因此少走了不少冤枉路。

這樣的理解算是受到[《Portal》的演講](https://youtu.be/c2YRVWZupwo)影響（印象中音質有點糟糕，聽的時候小心爆音），神作級的《Portal》也不過是總共有七個人參與過（不是全程參與）的專案，因為限制而必須直接使用《Half Life 2》的素材製作。然而這件事情也因此讓他們建立起了「同個世界觀下的作品」的概念，而最終產品更是各方限制下，單純照著有限的路線走而最後誕生了大家津津樂道的神作。

雖然受限聽起來很糟糕，以創作者來說或許覺得很不自由，然而在有限的路線中規劃最佳選擇的概念，或許就像過去的作曲家就在鋼琴的 88 個琴鍵上完成無限的歌曲是一樣的。因為受限而反而能專注在真正重要的地方。

# 完全敘事表現

會決定做這個設計是有著複雜的緣由的。因為《A Short Hike》讓我理解了比起遊戲的內容量，我更重視遊戲帶來的「圓滿感」。我因此假設了任何遊戲只要能成功做出圓滿感，無論遊戲內容的長短，都應該能讓所有人玩得滿意，而不會出現什麼遊戲時數未滿兩小時就想要退費的情形。

而我也自我假設說我並不會想要在一款遊戲上開發太久，希望能早早完成到商業上可行的程度就推出。因此我想說如果先完成一個「最小可行產品（Minimum Viable Product）」，接著將各方要素都準備到恰好提供充足的圓滿感，形成「最小完全產品（Minimum Complete Product）」的話，就可以用很快的節奏推出商業上可行的產品。

如果能證明這個手法是有效的，開發者就不再需要打內容戰，像 3A 工作室現在忙著打內容量軍備競賽而造就一系列缺乏意義的遊戲設計。縮短開發時間、增加作品成功機會，然後快速一款一款地迭代，就不會發生小開發者花多年製作一款遊戲大爆死，然後就再起不能的窘境。

但講起來簡單，做起來難，要怎樣做到「恰到好處的圓滿」實在沒有什麼方針可循。於是我想到了一個唯一有跡可循的方式，那就是做出一款所有要素之間都「完全自圓其說」的作品，一個任何遊戲中要素都被設計過，甚至開發手段本身都被設計成遊戲的一環的作品。

也因此誕生了這個非常複雜的「完全敘事表現」的概念，企圖要做出一款所有看得見的要素都實際存在於故事中的作品。

不過我也從 3 個月的目標時間做到了 30 個月了，所以這個理論可能還得再慢慢驗證清楚。下一款會更好！

# Unity 3D

我使用 Unity3D 開發。整個開發過程中只使用了 DOTween（漸進變化套件）和 Shapes（向量圖形繪製套件）兩個第三方套件，除了一些從網路上找到的實用程式碼片段以外，任何其他系統都是自己撰寫完成的。

不使用第三方套件除了因為怕仰賴別人寫的東西，如果出錯的話自己難以察覺跟修改。另一方面也是想著說，如果我可以在幾乎不仰賴套件的情況下完成這款遊戲，就或許可以讓未來的開發者知道這樣做也是沒問題的。



總之對於遊戲的定位就講到這裡，下一篇提一下《自動混亂》的原型！