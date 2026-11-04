---
title: "Mold Design Deep Dive"
date: 2026-11-04T09:00:01+08:00
draft: false
tags: ["Mold"]
---

So, it's probably a good time to talk about Mold in more detail.

<iframe frameborder="0" src="https://itch.io/embed/4955560" width="552" height="167"><a href="https://dkliao.itch.io/mold">Mold: vector graphics library by DK Liao</a></iframe>

It's a very surreal feeling seeing something I made getting thousands of download online and I'm really grateful for people who reached out to give feedback or even just simple gratitude. I feel like I need to make a more detailed post about the history behind it and maybe some causal deep dive.

# What and Why

Mold is a vector graphics library for both Godot and Unity, created for my game Autopanic. The visual design of Autopanic is in the vein of graphics realism, focusing on broad stroke graphics design like visual but used to represent actual objects to create some surreal scifi visual.

![Simple preview of Autopanic](/images/projects/mold/autopanic-preview.jpg)

One of the reasons why I went on this direction is becuase I thought keeping it simple would be great. The funny thing is that big modern game engines, or Godot and Unity more specifically, somehow lack the capability to draw simple shapes. Godot fares better with plenty of `draw_[shape]` functions and Polygon2D nodes, but those are limited to CanvasItem, which means you cannot draw 2D shapes in 3D world-space with them. Unity is a similar story, with UIToolkit having some of the capabilities while the legacy uGUI is fully sprite-based. Again, there's nothing for 3D world space.

And we haven't even talked about 3D primitives: Cuboids and Spheres? Sure. Cylinders? Kind of. But then there are Prisms, Cones, Pyramids, and Tori. These are still very common shapes, but if you need one, you'll need to pop open some modeling software.

Originally I was using a plugin for Unity called [Shapes](https://assetstore.unity.com/packages/tools/particles-effects/shapes-173167), but my need for code centric ergonomics and performance eventually pushed me to create my own renderer for these things. After some slippery slope, Mold turned out to be way more useful than I expected, so I started to think about the possibility of moving Mold into a plugin and maybe help others along the way.

# How does it work

The overall goal to create an easy to use simple shape renderer remains throughout, but to pull it off calls for different underlying implementation for 2D and 3D.

For 2D primitives, they are all rendered with a single Quad. Mold evaluates Signed Distance Field (SDF) to create crisp silhouette under any resolution. In combination with additional anti-aliasing steps keeping it smooth is what the "vector graphics library" is about.

For 3D primitives, Mold generates 3D meshes at runtime. While claiming it to be "vector" is certainly untrue, Mold implements automatic Level of Detail (LOD) system with dithering cross fade. Which means you'll always get a smooth look no matter what distance you look at, and Mold will automatically swap into low detail meshes when 3D primitives are far away. Thus achieves somewhat vector like visuals while keeping performance in check.

# Customizability

One big thing for Mold coming from Shapes is the need for more customizability. Mold aims to provide more ways to create visuals beyond a singular unlit color, including multiple ways to interpolate between two colors, and some nice to haves like Oklab support. Rounded 3D primitives are also really nice, very suitable for cutesy cosy projects.

Some final additions before launching 1.0 is the paint and pencil visual styles. I originally created them as custom shader examples, but I quickly realized they are a lot more useful than I initially thought. Not only this allows Mold to create shapes beyond simple clean geometry, it opened up a lot more possibilities for using it as a VFX tool, for example a dry brush stroke can certainly be used as a sword swipe even if it is not originally designed to do so.

# Performance

Autopanic is scoped to feature some form of voxel adjacent dynamic destruction system. Accompanied by the hope to get it running at 800p/90FPS on Steam Deck leads to the need for extreme performance optimization.

Outside of the previously mentioned LOD sytem, some highlights include the existence of compute based frustum culling, GameObject-less code centric API to avoid GameObject overhead, GPU based polyline/curve/polygon which has little cost to animate, and an Immediate Mode API that will automatically batch draw command so no manual sorting is needed. For what it's worth, Mold also had batch update API that is based on Burst/Jobs which can provide the best performance possible for the most extreme usage.

Mold also uses a mesh template system, which entails it will only dynamically generate the base template for each 3D primitives instead of generating anew for all primitives. Different dimensions including the roundness will share the same mesh template and then present the final geometry through deforming of vertex shader. This also means animating geometry is close to being free.

Lastly while Mold has Component based workflow and I would assume a lot of users will use it exclusively (and I do love prototyping with it). These components will generate preview mesh renderer to be used in Edit Mode, but when running in Play Mode, they will be automatically batched into the efficient renderer. Therefore all the performance benefit still applies when using the Components.

# Porting to Godot

I've been on the fence to dive into Godot for a while now, and one of the reasons that holds me off is exactly the fact that Shapes' creator showed little interest in porting Shapes to Godot. Now that I had my own plugin I feel like attempting the port is a good excuse to get me start using Godot, so I started the work. The good news is while Godot and Unity are structured a lot differently, they still rely on similar underlying graphics API and shared quite a lot of similarities. The bad news is Godot isn't quite in feature parity when it comes to rendering, and therefore I couldn't use the low level RenderingServer API for what Mold can do equivalently when using low level rendering API in Unity, like for example `RenderMeshPrimitives`. Ultimately I still used something similar to ensure the best performance I can get, but certainly that's something worth revisiting in the future.

I initially only wanted to do a singular C# port so that I can also keep the code structure in sync between Godot and Unity, but then I realized that C# currently does not support WebGL export. I know WebGL export is big for Godot (esp for browser play on itch) so after some evaluation I opted to do an additional GDscript port for those who might need it. Turns out the GDscript version had 50% more downloads than the C# version, so I'm glad I did it. Though the unfortunate truth is that running Mold with GDscript isn't the fastest thing in the world, and maintaining two ports for Godot alone is really painful. I'll try to move into GDextension in the future, starting from writing C++ code that I haven't done in years.

# Pricing

There has been some discussions about the pricing, $80, which isn't the cheapest thing in the world and I figure I should explain it in more detail here.

Firstly, I was originally planning to release Mold as an open source project. But I'm getting burnout from some big (10k+ stars) GitHub project. I'm afraid that Mold will be an addition to my already taxing unpaid open source work, so I decided to go for proprietary for now.

Picking the price is the next big question. Obviously Shapes is the biggest point of reference, at $100 (+10% VAT at $110). I don't think charging that much makes sense for Mold, and even Shapes itself frequently offer 50% discount. Ultimately I picked $80 for the following reasons:

- I dislike impulse purchase bait and I will not do discount.
- Pricing Mold too low feels like undermining Shapes in some sense, as Mold basically matches (with some features deemed out of scope) and outperforms Shapes in terms of functionalities.
- Unity Asset Store had some written rules about they actively discourage pricing assets too low from similar products. The review process of submitting an asset is almost a month so I wouldn't dare some complications throwing me back into the waiting queue.

On the other hand Mold had a very generous non-commercial version with no functional differences, which I would assume will benefit most of the users.

If I'm being honest I really can't tell if your project uses Mold or not. If you need it and you're running on shoestring budget, just grab the non-commercial version and get the headstart you need. As long as you're comfortable and knows what you're doing, I promise I won't hold it against you.

# Conclusion

All in all I'm really excited about Mold, and I'm glad I took the leap to port it to Godot! It's a somewhat magical feeling thinking I can make something that can theoretically benefit all developers. It's going to be a long journey maintaining Mold but that's what my games are running on anyways.

Mold is something I wanted when I started making games, hopefully it will help you to make yours, cheers!