---
title: "A quick and dirty large scale city production workflow"
date: 2021-03-29T19:16:23+08:00
draft: true
tags: ["Gamedev"]
---

# Introduction
Open world games always fascinates me. But actually making one is pretty intimidating as a solo dev, while a procedural toolset might work, making a robust one might be tedious and thereby time consuming. After being burnt out from an older project, I decided to take a break and have some fun. So I decided to test how fast can I hack an open world with the least tools and costs.

The final result here is shown using Unity, but I believe the tools prior and general workflow is perfectly doable in any engine.

# The Goal
The goal is to hack an open world with the least tools and costs. So let's make it clear what it means:

Almost zero barrier to replicate the attempt for anyone

Making a large scale city is the actual attempt, it can serve as actual level but most probably usable as a background

Also I will be focusing on the workflow rather than the actual steps above, but all tools used here has a lot of YouTube tutorials out there, I'm just trying to hack them together.

# The Workflow
Open Street Map is a community contributed map data, and this workflow relies heavily on it. OSM surprisingly has a lot of 3D building markers in it, so we can retrieve both the buildings and road information out of it.

## Buildings

With Blender plugin Blender-GIS[1], one can retrieve models such like this: https://imgur.com/qAebT6J. They are mostly blocks extruded from outlines, but pretty serviceable for cities.

But with some other plugin like Blender-OSM[2], you can actually generate different kinds of roof: https://imgur.com/f6dt7az. If you further purchase the premium version of Blender-OSM[3], textures will be included: https://imgur.com/sKHFBvn.

I on the other hand wanted to challenge myself making shaders, also I think a less realistic but customable material is much useful, so I wired a Unity HDRP/URP shader out of Shader Graph[4](https://imgur.com/VjeNatZ, https://imgur.com/bYxBsOp).

Here's day night cycle in motion (auto exposure setting is a bit off I think it is actually pretty good) https://imgur.com/kPLgbdY.

## Roads

Blender-GIS and Blender-OSM both provides road retrieval tool, but Blender-OSM provides a full mesh out of the box. Here's an example: https://imgur.com/Nic7wW1.

Roads are also separated by type, so I follow Roman Papush's Road Shader Tutorial[5] and made several variations(https://imgur.com/7akfI8X, https://imgur.com/ZJbUyka).

## Result
https://imgur.com/sd7OSYb

https://imgur.com/t2eAWgN

https://imgur.com/iUyqNi5

https://imgur.com/k8qh7dX

https://imgur.com/uLmufX6 (skybox based on Jannik Boysen's tutorial[6])

You definitely cannot make a GTA of the city you live in out of the box with this workflow, but I think the result is perfectly serviceable as a basis, more importantly already usable as a complicated background.

# Limitation
It is free! So of course there are caveats. Here are some for you to consider:

## Road intersection unsolved

OSM provides only nodes for roads, so intersection between roads remain unsolved and you'll see disgusting Z-fighting. A custom mesh manipulating solution is needed to fix this. Potential solution here but it seems to be Blender version dependent so I can't get it to work.

## No sidewalks yet

This is probably the most important part to make the whole thing work on the ground, but unfortunately my attempts at using boolean operation in Blender to cut out road only doesn't work properly.

## No actually usable terrain

Though Blender-GIS can pull elevation data and elevates buildings along it, the resolution of 30 meters will result in weird fluctuation. A place where you can get away with flat plane is much preferable.

## Inconsistent data quality

Since OSM is community contributed, the quality and density of data varies quite a lot depending on the location.

## Improperly solved relation

OSM consists of some complicated relation, and the tools mentioned above can't solve all of them properly. Here's Shinjiku government building solved by Blender-GIS https://imgur.com/3mteLBS, while the actual data contains a much detailed model https://imgur.com/V4zdDdY.

# Conclusion
I initially though I can effortlessly made a driving game based in Tokyo open world, but it turns out much more work is required. But I've learnt quite a lot from this attempt and still believes this is possible. Thank you for reading this piece and hopefully it is any bit useful to you.

# Resources
[1] Blender-GIS: https://github.com/domlysz/BlenderGIS

[2] Blender-OSM (free version): https://gumroad.com/l/blender-osm

[3] Blender-OSM (premium version): https://gumroad.com/l/blosm

[4] My custom building exterior Shader Graph: https://github.com/dklassic/Unity-Simple-Building-Triplanar-Shader

interior mapping part is based on the GameDevGuide tutorial: https://youtu.be/dUjNoIxQXAA

[5] Roman Papush's Procedural Road Shader Graph Tutorial: https://youtu.be/vhrIEcVSI5M

[6] Jannik Boysen's Skybox Shader Graph Tutorial: https://medium.com/@jannik_boysen/procedural-skybox-shader-137f6b0cb77c

# Bonus
Houdini released a set of game dev tools last year focusing on utilizing OSM data. Might worth a try: https://youtube.com/playlist?list=PLXNFA1EysfYkFzKS--S3_3393X2z1F_e0. I think the highlight is the intersection solving tool.

