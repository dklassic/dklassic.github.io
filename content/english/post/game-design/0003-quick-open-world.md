---
title: "A quick and dirty large scale city production workflow"
date: 2021-03-29T19:16:23+08:00
draft: false
tags: ["Game Design"]
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

With Blender plugin [Blender-GIS](https://github.com/domlysz/BlenderGIS), one can retrieve models such like this:

![buildings](/images/posts/game-design/0003/1.png)

They are mostly blocks extruded from outlines, but pretty serviceable for cities.

But with some other plugin like [Blender-OSM](https://gumroad.com/l/blender-osm), you can actually generate different kinds of roof:

![roof](/images/posts/game-design/0003/2.png)

If you further purchase the [premium version of Blender-OSM](https://gumroad.com/l/blosm), textures will be included:

![texture](/images/posts/game-design/0003/3.png)

I on the other hand wanted to challenge myself making shaders, also I think a less realistic but customable material is much useful, so I [wired a Unity HDRP/URP shader out of Shader Graph](https://github.com/dklassic/Unity-Simple-Building-Triplanar-Shader)

![custom shader](/images/posts/game-design/0003/4.jpg)
![building result](/images/posts/game-design/0003/5.png)

Here are some footage in motion:

![moving across](/images/posts/game-design/0003/6.gif)
![flying across](/images/posts/game-design/0003/7.gif)
![day night cycle](/images/posts/game-design/0003/8.gif)


## Roads

Blender-GIS and Blender-OSM both provides road retrieval tool, but Blender-OSM provides a full mesh out of the box. Here's an example:

![road mesh](/images/posts/game-design/0003/9.png)

Roads are also separated by type, so I follow [Roman Papush's Road Shader Tutorial](https://youtu.be/vhrIEcVSI5M) and made several variations.

![all road materials](/images/posts/game-design/0003/10.png)
![road showcase](/images/posts/game-design/0003/11.png)

## Result

![result1](/images/posts/game-design/0003/12.png)
![result2](/images/posts/game-design/0003/13.png)
![result3](/images/posts/game-design/0003/14.png)
![result4](/images/posts/game-design/0003/15.png)
![result5](/images/posts/game-design/0003/16.png)

Skybox is based on [Jannik Boysen's tutorial]((https://medium.com/@jannik_boysen/procedural-skybox-shader-137f6b0cb77c)).

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

OSM consists of some complicated relation, and the tools mentioned above can't solve all of them properly. Here's Shinjiku government building solved by Blender-GIS:

![bad resolve](/images/posts/game-design/0003/17.png)

While the actual data contains a much detailed model:

![good resolve](/images/posts/game-design/0003/18.png)

# Conclusion

I initially though I can effortlessly made a driving game based in Tokyo open world, but it turns out much more work is required. But I've learnt quite a lot from this attempt and still believes this is possible. Thank you for reading this piece and hopefully it is any bit useful to you.

# Extra Resources

My custom building exterior Shader Graph's interior mapping part is based on the GameDevGuide tutorial:

{{< youtube dUjNoIxQXAA >}}

# Bonus

Houdini released a set of game dev tools last year focusing on utilizing OSM data. Might worth a try, and here's an [official tutorial playlist on the tool](https://youtube.com/playlist?list=PLXNFA1EysfYkFzKS--S3_3393X2z1F_e0).

I think the highlight is the intersection solving tool.

