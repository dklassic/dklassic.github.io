---
title: "Mold Frequently Asked Questions (FAQ)"
draft: false
enableComments: false
showToc: true
showTip: false
---

# Is there functional difference between the free non-commercial version and the paid version?

None. They're the exact same with license difference.

# The C# addon cannot be loaded?

Be sure to create the C# solution and build the project before attempting to activate the addon.

# Does the performance holds up under XXX?

Performance problem is always a very complicated question to answer. A more detailed answer will be down below but the truly short answer is "It depends" and "Benchmark is king".

And here's the long answer:

- If you're strictly using the GDScript version of Mold, it'll definitely have way lower performance than the C# counterpart, so if you're doing something crazy it's best to use the C# version or wait for the upcoming GDextension port of Mold.
- Mold is designed to be performant by default, but graphics is complicated and the "sensible default" might not get you what you wanted.
- However, Mold had a lot of knobs to turn and ways to render the image so it's highly possible to tune it to suit your project's need, but it also requires you to understand what they mean and for you to decide what your project is about.
- This is called performance budgeting which is for the developer to choose the trade-off between what they absolutely wanted to achieve and how many frame time budget can be used for that specific feature.
- Mold had a dedicated section in the documentation about everything performance, my suggestion is to simply try it out and see if it works (especially since there's free version available), and if the things mentioned in the performance section can help. I cannot in good faith guarantee you it "holds up" without knowing anything about the exact budgeting of your project and your lowest targeted device, the only thing trustworthy is benchmark in build, rinse and repeat.
- None of my personal project does mobile export, but my own game Autoapnic runs at 800p/90FPS on Steam Deck with tens of thousands of objects animated at any given time.


# What's the difference between Mold and the Unity Asset Shapes?

Mold is definitely inspired by Shapes, and I'm a long time Shapes user. In fact I paid for Shapes twice because Unity banned one of my account and asked for nonsensical materials to unban me, so I had to start anew and buy Shapes again.

Mold, however, was designed with fundementally different goal in mind and had completely different implementation. Shapes is a good asset, if you're happy with it (and it's workflow) there's probably no obvious reason to use Mold.

Mold was created because I need more performance and customizability which Shapes does not provide. I think the big win is if you run into performance issue with Shapes then maybe see if the additional features interests you, if not I think Shapes is good as is.

As for what I can said about the feature advantages of Mold, here's a list:

- Implements a lot more 3D primitives, alongside the capability to create Rounded shapes.
- Implements arbitrary polygon with per vertex color interpolation.
- Implements more color mode, particularly for 3D primitives.
- Has Oklab blending support.
- Has official custom shader support with example shader.
- Implements procedural paint/pencil strokes.
- Implements full spline support.
- Implements native uGUI support for 2D primitives.
- Implements optional order-independent transparency workflow.
- Does not require additional URP RendererFeature for immediate mode drawing.

The rest is all about performance:

- Has a retained mode workflow without GameObject overhead, so you can spawn primitives from code alone while not having performance implications of immediate mode.
- Even with component based workflow, it will automatically switch to use the more efficient backend internally in Play Mode. And this does not sacrifice Play Mode scene view selection.
- Has GPU culling option.
- Has automatic LOD system with dithering cross fade support, so the 3D primitives will always look smooth while keeping performance in check.
- Has GPU based polyline/curve, which can make animating it extremely cheap.
- Has fully vertex shader based deformation, so animating any 3D primitive is very cheap.
- Has Burst based batched update API, while having optional Job based variant so you can do it efficiently over multithread.

