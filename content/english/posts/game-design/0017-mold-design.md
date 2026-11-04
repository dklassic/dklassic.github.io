---
title: "Mold Design Dive"
date: 2026-11-04T09:00:01+08:00
draft: false
tags: ["Mold"]
---

So, it's probably a good time to talk about Mold.

<iframe frameborder="0" src="https://itch.io/embed/4955560" width="552" height="167"><a href="https://dkliao.itch.io/mold">Mold: vector graphics library by DK Liao</a></iframe>

Mold is a vector graphics library created for my game Autopanic. The visual design of Autopanic is in the vein of graphics realism, focusing on broad stroke graphics design like visual but used to represent actual objects to create some surreal scifi visual.

![Simple preview of Autopanic](/images/projects/mold/autopanic-preview.jpg)

One of the reasons why I went on this direction is becuase I thought keeping it simple would be great. The funny thing is that big modern game engines, or Godot and Unity more specifically, somehow lack the capability to draw simple shapes. Godot fares better with plenty of `draw_[shape]` functions and Polygon2D nodes, but those are limited to CanvasItem, which means you cannot draw 2D shapes in 3D world-space with them. Unity is a similar story, with UIToolkit having some of the capabilities while the legacy uGUI is fully sprite-based. Again, there's nothing for 3D world space.

And we haven't even talked about 3D primitives: Cuboids and Spheres? Sure. Cylinders? Kind of. But then there are Prisms, Cones, Pyramids, and Tori. These are still very common shapes, but if you need one, you'll need to pop open some modeling software.

