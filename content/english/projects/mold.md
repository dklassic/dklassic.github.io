---
title: "Mold"
draft: false
enableComments: false
showToc: true
showTip: false
---

https://dkliao.itch.io/mold

Mold is a real-time vector graphics library for Unity and Godot.

![Mold Thumbnail](/images/projects/mold/mold.png)

![A selection of animated shapes rendered with Mold](/images/projects/mold/mold-shapes.gif)

# What it does

Mold includes a broad collection of 2D and 3D primitives, and capable of rendering 2D primitives with infinite resolution while capable of efficiently presenting 3D primitives silky smooth. A few additional features really helped my work:

## Monilithic MoldComponent/MoldNode

![Mold's primitive and blend-mode catalog](/images/projects/mold/basic-molds.png)

A monilithic MoldComponent/MoldNode to create any shape you want, while still batch them efficiently with underlying low level rendering.

| Unity component authoring | Godot node authoring |
| --- | --- |
| ![Editing a Mold component in Unity](/images/projects/mold/component-authoring.gif) | ![Editing a Mold node in Godot](/images/projects/mold/node-authoring.gif) |

Under the hood, Mold uses Unity's `RenderMeshPrimitives` API and Godot's `MultiMesh` for rendering. It supports retained-mode rendering as the main workflow, with an immediate-mode API when that is more convenient.

## Rounded 3D geometry

Mold can generate rounded boxes, cylinders, prisms, and other primitives without sending them through a modeling tool.
Additionally, Mold uses vertex shader to deform the mesh, which means most of the resizing does not trigger the
regeneration of meshes and you can cheaply do so.

![Editing a rounded 3D mesh in Mold](/images/projects/mold/rounded-mesh.gif)

## Oklab color blending

In addition to the usual blend modes, Mold can blend colors in the perceptually uniform Oklab color space. Gradients stay vivid and travel between colors more naturally, which is particularly handy for making a whole scene feel coherent.

![Mold color blending modes, including linear RGB and Oklab](/images/projects/mold/color-blending.gif)

## Automatic level of detail

Mold can automatically select a lower-detail version of each 3D primitive as it moves farther from the camera. The levels cross-fade with a dithered transition, reducing the cost of dense scenes without a distracting hard pop when the geometry changes.

![Mold automatically changing primitive detail levels across a dense scene](/images/projects/mold/automatic-lod.gif)

## GPU based polyine

Mold implements a GPU based polyline solution which can handle potentially millions of lines and points without a hitch.
Optional CPU based polyline is still available for precise mesh construction.

![Mold GPU based polyline running on Unity](/images/projects/mold/gpu-polyline.gif)

Additionally, full fledge Curbe is also supported. The curve also exposes an Evaluate function so that you can
sample the path should you need it.

![Mold Curve running on Unity](/images/projects/mold/curve.gif)

## Built-in paint and pencil visual available

Mold supports custom materials, but creating one by adapting the built-in shaders can be very difficult.
So Mold also has two premade custom materials: paint and pencil, which mimics the look of paint and pencil
strokes. Use them directly and maybe reference them to create your own custom materials!

![Mold pencil stroke](/images/projects/mold/stroke-pencil.png)
![Mold paint stroke](/images/projects/mold/stroke-paint.png)

## Optional order-independent transparency support

Mold supports both Weighted OIT and AdaptiveVoxel OIT, which while requires additional setup to be used on typical engine transparent objects, works about perfect if your project only has Mold transparent objects.

![Mold with AVOIT](/images/projects/mold/avoit.gif)

# What can you make with it?

Simple shapes can go surprisingly far. This little solar system was rendered in Godot using only Mold:

![A miniature solar system rendered with Mold in Godot](/images/projects/mold/mold-godot-demo.gif)

The full [Mini Outer Wilds](https://dkliao.itch.io/mini-outer-wilds) experiment was built with roughly 3,000 lines of GDScript and no art assets. Mold has also been used to assemble colorful miniature towns and small strategy-game scenes:

![A miniature town made from Mold primitives](/images/projects/mold/mold-town.png)

![A small hex-grid world made from Mold primitives](/images/projects/mold/hex-kingdom.png)

# A small reality check

Mold is mainly designed for world-space rendering. Unity UI rendering is possible, but it is not the most straightforward use case. Its anti-aliased 2D primitives can look crisp and vector-like at any resolution, but Mold is not an SVG renderer. Oklab blending also costs more than ordinary linear RGB blending, so it is best used where the visual difference matters.

Mold is currently in beta while I work out the final distribution and licensing plan. If this sounds useful for something you are making, [join the Discord](https://discord.gg/w57PEN42KV).
