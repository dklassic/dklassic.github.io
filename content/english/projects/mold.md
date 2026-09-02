---
title: "Mold"
draft: false
enableComments: false
showToc: true
showTip: false
---

Mold is my answer to a very specific problem: **“I just want to draw a shape here.”**

It is a procedural 2D/3D geometric primitive renderer for Unity and Godot. Instead of opening image-editing or modeling software every time I need a box, a rounded cylinder, a dashed line, or some other simple shape, I can describe it in code and keep working in the engine.

![Mold Thumbnail](/images/projects/mold/mold.png)

# Why I made it

I have always liked making games out of simple geometry. While working on *Autopanic*, I needed to draw a lot primitives, and I wanted my game to run really fast, so I made my own solution. That small utility kept growing until it became something generic enough to use across projects—and, hopefully, useful to other people who enjoy working the same way.

![A selection of animated shapes rendered with Mold](/images/projects/mold/mold-shapes.gif)

# What it does

Mold includes a broad collection of 2D and 3D primitives, with a few features I especially like.

## Rounded 3D geometry

Pretty much every shape looks friendlier with softened edges, so Mold can generate rounded boxes, cylinders, prisms, and other primitives without sending them through a modeling tool first.

![Editing a rounded 3D mesh in Mold](/images/projects/mold/rounded-mesh.gif)

## Oklab color blending

In addition to the usual blend modes, Mold can blend colors in the perceptually uniform Oklab color space. Gradients stay vivid and travel between colors more naturally, which is particularly handy for making a whole scene feel coherent.

![Mold color blending modes, including linear RGB and Oklab](/images/projects/mold/color-blending.gif)

## Automatic level of detail

Mold can automatically select a lower-detail version of each 3D primitive as it moves farther from the camera. The levels cross-fade with a dithered transition, reducing the cost of dense scenes without a distracting hard pop when the geometry changes.

![Mold automatically changing primitive detail levels across a dense scene](/images/projects/mold/automatic-lod.gif)

![Mold's primitive and blend-mode catalog](/images/projects/mold/basic-molds.png)

The API is code-centric, but it does not force everything to live in code. Unity has optional `MoldComponent` authoring, while Godot has `MoldNode`, so shapes can also be adjusted directly in the editor.

| Unity component authoring | Godot node authoring |
| --- | --- |
| ![Editing a Mold component in Unity](/images/projects/mold/component-authoring.png) | ![Editing a Mold node in Godot](/images/projects/mold/node-authoring.png) |

Under the hood, Mold uses Unity's low-level instanced mesh drawing and Godot's `MultiMesh` rendering. It supports retained-mode rendering as the main workflow, with an immediate-mode API when that is more convenient.

# What can you make with it?

Simple shapes can go surprisingly far. This little solar system was rendered in Godot using only Mold:

![A miniature solar system rendered with Mold in Godot](/images/projects/mold/mold-godot-demo.gif)

The full [Mini Outer Wilds](https://dkliao.itch.io/mini-outer-wilds) experiment was built with roughly 3,000 lines of GDScript and no art assets. Mold has also been used to assemble colorful miniature towns and small strategy-game scenes:

![A miniature town made from Mold primitives](/images/projects/mold/mold-town.png)

![A small hex-grid world made from Mold primitives](/images/projects/mold/hex-kingdom.png)

# A small reality check

Mold is mainly designed for world-space rendering. Unity UI rendering is possible, but it is not the most straightforward use case. Its anti-aliased 2D primitives can look crisp and vector-like at any resolution, but Mold is not an SVG renderer. Oklab blending also costs more than ordinary linear RGB blending, so it is best used where the visual difference matters.

Mold is currently in beta while I work out the final distribution and licensing plan. If this sounds useful for something you are making, [join the Discord](https://discord.gg/w57PEN42KV).
