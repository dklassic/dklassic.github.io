---
title: "速度感的表現"
date: 2022-08-13T12:00:04+08:00
draft: true
tags: ["遊戲設計"]
---

原文是回覆 Unity3D 板上板友提問的內容「想問一下有關Nier/原神 跑步的動作 實現問題」。最近決定將幾篇回答內容寫得比較完整的文章整理起來，用更泛用的方式翻寫一遍。比起給別人看更像是讓自己筆記起來，知道自己在這個時候的想法。

本文是一篇關於構成「衝刺感、速度感、加速感」常見元素的文章。

基本上衝刺感的目標就是：讓人覺得發生了加速。
只是觀察速度很快的東西本身並不會讓人感受到衝刺感，而是觀察到加速才會。
舉例來說......相對於地表是靜止的一個人，其實也是相對地球核心大概以每小時 1674 公里的速度被地球自轉甩動著，同時又被太陽公轉、銀河系核心公轉用超高速甩動著。然而在地表的人顯然不覺得自己正在以極高速移動中。

扯遠了。

基本上就是要對人展現出物理狀態（Sell Physicality），因此就算準備了一個慢跑跟和世界紀錄百米衝刺一樣的跑步動畫做切換，也不代表玩家一定就能感受到衝刺感。相反地如果能清楚展現狀態的變化，就算其實速度很慢也會讓人有衝刺的感覺。
因此要讓人感覺的衝刺的關鍵就是要讓人感受到加速，具體實作手段大多都是可以調整鏡頭達成，而反而不是動畫本身，這邊有點流水帳地提大量的選項：

關於鏡頭能有的表現
彈簧鏡頭
不要把鏡頭鎖死在相對角色固定距離，而是讓鏡頭像是被角色用一個彈簧拉著。
這樣子玩家可以更清楚地看到角色相對場景的移動狀態，同時感受到鏡頭需要加速追著角色跑的物理性質。
要注意需要將鏡頭稍微瞄向角色面對的角度，而不是單純看向角色，不然玩家會看不清楚移動目標。

增加鏡頭晃動幅度
模仿鏡頭追角色的辛苦程度產生的額外晃動會讓人有速度比較快的錯覺，但要抓準幅度跟頻率免得引起動態暈。
參考實作：戰爭機器的衝刺動作，實際速度很慢但是卻很有速度感。
增大鏡頭的視角大小（FOV）
衝刺時增加視角大小可以讓玩家更清楚地看見角色相對於場景的位置變化，更能讓人感受到速度感。
另一方面角色在超高速移動時，擴大視角大小也比較方便看清楚環境去做移動。
在畫面邊緣加入速度線（Speed line）效果
速度線真正的意義是：模仿動態模糊的表現。簡單來說攝影機是有快門速度的，並不是拍攝瞬間靜止的樣貌。如果物體移動太快就會變成模糊的視覺，而對移動中的鏡頭，離鏡頭物理距離最近的地方（像是最接近的地面）相對移動速度會比較快，因此在畫面邊緣才會有動態模糊的效果。
當然可以直接加入鏡頭移動造成的模糊，但應該滿多玩家不太喜歡鏡頭動態模糊的表現；相對的加入假造的速度線可以產生鏡頭邊緣動態模糊的錯覺，進而增加速度感。


關於其他能有的表現
加入加速動畫
發生加速的期間，角色會用相對大的力道踩踏，所以如果你仔細看《尼爾：人工生命》、《原神》的動畫，他的角色在從慢跑改成衝刺的瞬間會做出身體更往前傾的動作版本。
相較之下完成加速後的穩定跑步，傾角就沒那麼大。
排排站比較：

加入加速特效
畢竟目標是「傳達加速的力道」，所以除了加入衝刺加速動畫以外，只要能讓玩家「感覺很用力」就好。所以如果增加像是現實世界很用力的時候會發生的視覺效果，就可以達到暗示玩家的效果。
例如說加速期間會向後飛濺沙塵，簡單點甚至不做動畫，單純在轉入衝刺時向後飛濺沙塵就好。
另一個很常用，現實世界也很好類比的就是像是撞開了靜止的空氣產生衝擊波，現實世界最好的例子就是戰鬥機突破音障的瞬間。


以上提供參考。

其中有鏡頭的部分是從這篇演講「Vehicle Feel Masterclass: Balancing Arcade Accessibility with Simulation Depth」出來的，雖然這篇是講載具，但是其實對人物也非常適用。
如果沒時間的話，推薦看 27:22～29:22 一段他示範改變鏡頭性質會影響到速度感的例子。

總之展現衝刺感、加速感、速度感的手段千奇百怪，上面表列的這些也只是常用的手段。其實其中一些也就是好好地展現物件在現實世界會有的狀態時就能讓人感受到速度感（例如說模仿鏡頭動態模糊、現實世界的加速的物理狀態）。
可以自己實驗看看哪些比較符合想像，再去使用就好，不一定要全都做，也沒有說不做上面這些就展現不了速度感。

但總之有嘗試做這些東西的話，就算是一個方塊也或許能展現出速度感：