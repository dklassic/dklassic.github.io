---
title: "11. Open World Tokyo"
date: 2022-10-23T15:54:48+08:00
draft: false
tags: ["Autopanic"]
---

In short, huge mess. But I learned so much from it.

![land roam](/images/posts/autopanic-devlog/0011/1.gif)
![sky roam](/images/posts/autopanic-devlog/0011/2.gif)

Though OSM marking of Tokyo is pretty robust, the data is pretty difficult to use outside of plain 2D map.

The most difficult part is to solve intersections and generate road mesh, which is extremely hard so have universally good result with a single ruleset.

For example, here's a good one:

![good lining](/images/posts/autopanic-devlog/0011/9.png)

Here's one less so:

![bad lining](/images/posts/autopanic-devlog/0011/10.png)

Real world roads are complex and hard to generate road mesh with one single ruleset. And this is probably the hardest part of cloning real world Tokyo.

This attempt also made me look more closely to Microsoft Flight Simulator's result, then found out that their result is no better than mine:

![cluster lamp](/images/posts/autopanic-devlog/0011/12.jpg)
![bad intersection](/images/posts/autopanic-devlog/0011/13.jpg)


What a relief!

Anyways I still managed to produce some serviceable background level stuff, and hopefully I'll one day actually deliver on this idea.

![all in one](/images/posts/autopanic-devlog/0011/8.gif)

**What matters is the shaders we learned along the way**

Before this, I was afraid to write shaders, but with this three month vacation, I tried my hands at Unity's Shader Graph to make shaders.

I have no knowledge of 3D modeling and I figure I should try to decorate everything with shader. I learned to make procedural building exterior shader. I learned to make road wet with simplex noise:

![noise water](/images/posts/autopanic-devlog/0011/15.png)

Even tried my hand at mimicking Falconeer's approach overriding the whole lighting system and made a submerged version of Tokyo using shader alone:

![underwater](/images/posts/autopanic-devlog/0011/16.png)

I have so much fun making shaders during this three month period, and I'm now convinced that shaders can do ANYTHING!

Which helped me a lot later on when I wanted to make better scenery for Autopanic.
