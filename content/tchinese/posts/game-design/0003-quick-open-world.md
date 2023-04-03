---
title: "工作流程研究：快速世界建構"
date: 2021-03-29T19:16:23+08:00
draft: false
tags: ["遊戲設計"]
---



# 前言
開放世界應該對於很多人來說是某種夢想與浪漫。然而小團隊在資源上不太可能器及多大的規模，自動地圖產生機制的設計又可能太難。
今年二月初因為從手上的專案暫時休息，也算當作一個練習，我決定摸索看看有什麼流程可以讓廣大世界的製作能夠簡單達成，用最低限度的資源製作某種大規模場景。

雖然這篇裡面用的工具是 Unity，但是純粹工具組跟流程應該是可以適用於任何引擎。

# 目標
在這邊要為目標「使用最低資源製作大規模場景」做更明確的定義，以了解這項實驗的可用之處與限制：
- 最低資源

    不花費任何金錢，甚至以不撰寫任何程式為目標，意即近乎沒有技術知識也能處理。
- 大規模場景

    能近乎無人工的情況下製作某種程度上可用的場景，開放世界關卡不是唯一目標。

所以某方面來說這個流程並不會讓你閉著眼睛就做出一款 3A 大作，但有可能作為有效的基礎，幫助你進行地圖的建設或者是一個大規模背景的製作。
同時因為主要是流程上的探討，基本上不會花時間詳述實作細節，但是所有提到的工具應該都有不少網路上提供的教學，只是沒有人整併起來整個流程。

# 流程

Open Street Map 是一個由社群之力建構的完全開放任何用途的地圖，這個流程基本上奠基於 Open Street Map 的資料。由於 OSM 也有 3D 建築形狀的標記，所以就代表我們可以直接從中取出建築跟道路的資訊。

## 建築

建築資訊可以藉由 Blender 的工具 [Blender-GIS](https://github.com/domlysz/BlenderGIS) 取得，可以取得的模型大約像這樣：

![buildings](/images/posts/game-design/0003/1.png)

基本大多是純粹的建築描框，甚至有些因為沒有高度標示而只能隨機產生。

使用 [Blender-OSM](https://gumroad.com/l/blender-osm) 的話能選擇建築的屋頂形式：

![roof](/images/posts/game-design/0003/2.png)

如果進一步使用的是 [Blender-OSM 付費版](https://gumroad.com/l/blosm)的話，這個版本作者有額外附上建築材質：

![texture](/images/posts/game-design/0003/3.png)

我則因為想要對於建築的表現有更多的控制權，我選擇另外寫了一個 Unity HDRP/URP 用的可控簡易[建築外觀 Shader](https://github.com/dklassic/Unity-Simple-Building-Triplanar-Shader)：

![custom shader](/images/posts/game-design/0003/4.jpg)
![building result](/images/posts/game-design/0003/5.png)

應該還算騙：

![moving across](/images/posts/game-design/0003/6.gif)
![flying across](/images/posts/game-design/0003/7.gif)
![day night cycle](/images/posts/game-design/0003/8.gif)

## 道路
Blender-GIS 跟 Blender-OSM 同樣都可以取得道路資訊，差異是 Blender-GIS 只會取得曲線，Blender-OSM 會直接給出一個 Mesh，因此先用這邊延續下去。

從 Blender-OSM 可以取得的 Mesh 資訊大約像這樣：
![road mesh](/images/posts/game-design/0003/9.png)

路面資訊會另外根據道路用途標示出來，因此可以多準備幾種不同的材質分開貼上。這邊再根據 [Roman Papush 的道路 Shader 教學](https://youtu.be/vhrIEcVSI5M)製作可以輕易修改的程序產生材質。
![all road materials](/images/posts/game-design/0003/10.png)
![road showcase](/images/posts/game-design/0003/11.png)



# 成果
![result1](/images/posts/game-design/0003/12.png)
![result2](/images/posts/game-design/0003/13.png)
![result3](/images/posts/game-design/0003/14.png)
![result4](/images/posts/game-design/0003/15.png)
![result5](/images/posts/game-design/0003/16.png)

天空是根據 [@jannik_boysen 的教學](https://medium.com/@jannik_boysen/procedural-skybox-shader-137f6b0cb77c)製作的。

這個實驗結果並沒有辦法瞬間完成「某某城市」的 GTA，但作為一個基礎原型應該是相當充足的。而如果是作為背景，甚至應該已經是完全可用的程度。


# 限制

當然畢竟作為一個完全土炮的流程，限制當然也很多。以下會詳述各項待處理的限制：

## 路口交界

由於 OSM 拉下來的資料只有路，因此不會特別處理掉路與路之間交疊的區域。

## 人行道

以城市來說這個做法還缺少最重要的人行道。可以嘗試在 Blender 裡面藉由布林運算取得，但是可能會因為路面幾何的問題而無法有效取得。

## 地形

雖然像 Blender-GIS 可以拉衛星地形資料，但因為精度只有 30 公尺所以會造成奇怪的起伏。因此如果要做為遊戲空間，可能不適合選擇地形起伏大的地區。

## 資料標示不全

由於 OSM 是社群貢獻，因此完整度、正確性會根據地區有極大的差異。

## OSM 解析不全

由於 OSM 有一些複雜的 Relation 標記，標記物件之間的關係，如果沒有解析正確的話可能無法有效取得所有有用的資訊。

例如下圖是 Blender-GIS 取得的新宿都廳資料：

![bad resolve](/images/posts/game-design/0003/17.png)

但是實際上 OSM 標記的新宿都廳資料更加完整：

![good resolve](/images/posts/game-design/0003/18.png)

# 結語
隨著政府公開資料越來越多、以及各地社群的貢獻之下，顯然讓 OSM 的完整度對於遊戲、3D 創作等帶來不少幫助。

其中資料甚至也包含有行人穿越道等項目，如果隨時間更加完整，想必可以帶來更大的幫助。現階段要能夠進一步使用這些資料產生有效的遊戲關卡還需要更多的努力，不過至少作為一個乍看之下很精緻的場景似乎已經能做到了。

也期待是不是有人能藉由我分享的流程作出精彩的作品：）

# 參考資源

這裡列出一些我額外參考的資源。

## Interior mapping

我的客製建築內部空間對應是根據這個教學做的：

{{< youtube dUjNoIxQXAA >}}

## Houdini Game Dev Tool

Houdini 去年增加了一系列能夠使用 OSM 資料做城市建構的工具，其中個人認為最大的亮點是內建可以解析路口交界，產生更加自然的路面。

有興趣的可以嘗試看看[官方的相關 YouTube 影片](https://youtube.com/playlist?list=PLXNFA1EysfYkFzKS--S3_3393X2z1F_e0)。