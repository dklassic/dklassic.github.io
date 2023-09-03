---
title: "Unity Built-in RP DRS and FSR2 Implementation"
date: 2023-09-01T09:00:01+08:00
draft: false
tags: ["Unity"]
---

I accidentally figured out a problem I have with DRS implementation in Unity, so I decided it's best to write it down so someone else might find it useful. On the other hand having it figured out also means I can finally implement FSR2 in my game.

Here we go!

# The problem

[Autopanic](https://store.steampowered.com/app/1274830) is a weird game to say the least. In order to ensure the best experience for players, I've decided to do my best polishing overall experience to prevent frustration within this already bizarre game.

I focus on three parts:

- Performance: to be able to run at older computers as much as possible.
- User Experience: if I didn't have intent for something, always go for a version that favor's player.
- Accessibility: Besides disability assistance, I'd like to ensure players can play in whatever way they want.

Anyways, Autopanic is already pretty light on the performance side of things, as a final stretch I'd like to add in Dynamic Resolution for good measure. The one that I've implemented last November is a bit meh due to limitations posed by Unity, but I finally figure it out just yesterday.

# Dynamic Resolution Scaling

Dynamic Resolution Scaling, as in the resolution can change dynamically depending on the load of GPU. Which is like the last ditch effort to somewhat fix GPU performance if all else fails.

Anyways, Unity has implemented its own DRS solution for quite a while. Besides requiring DX12 or Vulkan, how it functions is quite a mystery on its own. In my game, I have my UIs rendered using Screen Space - Camera setup. You'd think by keeping Allow Dynamic Resolution unchecked on the camera will keep the UI rendered at crisp native resolution, that's not the case.

As long as the camera with lowest depth has DRS active, it'll force all cameras to be affected by DRS. On the flipside, if the lowest depth camera has Allow Dynamic Resolution unchecked, no other camera can be scaled with DRS.

I have zero idea why it works this way, but I've found some workarounds to do DRS with crisp UI.

First off, there are three methods (that I know of) to scale a Camera render:

- **ScalableBufferManager**, basically how Unity implements DRS, affecting cameras with Allow Dynamic Resolution checked (or not).
- **Camera Rect**, a hack to scale down Rect size in OnPreRender then scale it back up in OnRenderImage.

Both of which will suffer from the above mentioned issue, where the lowest depth camera will affect everything above.

- **Render Texture**, manually scaling Render Texture. This will also be affected by ScalableBufferManager if Dynamically Scalable is checked in Render Texture's setting.

Anyways, here are two ways to prevent UI being affected:

- **Screen Space - Overlay UI**, which won't be affect. But this way requires some workaround to do post processing on the UI which isn't exactly idea in my case.
- **Use Render Texture to display gameplay footage**, which of course can be scaled separately from the UI. But my current rendering workflow requires HDR value to work, so isn't particularly great.

I opted for overlay UI as of last year, but now that I finally figured out how to do a workaround. So here's a story about Unity's Built-in RP black box.

## Unity Automatic Camera Linking in Built-in RP

I accidentally learnt that in Built-in RP, Unity will automagically link cameras into a stack of sorts, which will allow the lowest camera of the stack to control the whole viewport of the stack. Which is why problem mentioned above happens. And to break this automatic behavior, one can simply set viewport of each camera to a slightly different value.

So... I just set my three cameras as W=1, 1.000001, and 0.999999 respectively and all is fixed. I can scale each camera independently.

Thanks no thanks, Unity.

## Scaling Determination

So since with a way of choice to scale, comes a problem of how to decide.

I simply copy pasta [Official Sample](https://github.com/Unity-Technologies/DynamicResolutionSample) which is a tad aggressive but good enough.

The sample uses [`UnityEngine.Rendering.FrameTimingManager`](https://docs.unity3d.com/ScriptReference/FrameTimingManager.html) to retrieve GPU timing, which only works on DX12, Vulkan, and Metal. To improve the usability, I implement one using `Time.unscaledDeltaTime` in case someone is stuck on DX11, which is obviously not the best choice but better than nothing.

# FSR2 Implementation

With the camera scaling issue fixed, I grabbed the code from [this open source project FSR2Unity](https://github.com/ndepoel/FSR2Unity) and implemented FSR2 support in my game as well. I intentionally only enable FSR2 on the lowest camera which is the one that renders all the background, and keep the gameplay related camera at native resolution, which in turn make the scaling even less noticeable.

So here are the results.

## Ultra Performance (3x per axis)

720p Native:

![720p native](/images/posts/game-design/0016/720.png)

720p -> 2160p FSR2:

![720p FSR](/images/posts/game-design/0016/720FSR2.png)

Pretty effective huh. The result seems both anti-aliased and super sampled, just as FSR2 is intended for. Of course it is far from looking like a native 4K image, but way better than actual native 720p image.

## Quality (1.5x per axis)

1440p Native:

![1440p native](/images/posts/game-design/0016/1440.png)

1440p -> 2160p FSR2:

![1440p FSR](/images/posts/game-design/0016/1440FSR2.png)

As resolution increases, it's more down to one's taste. FSR2's *improvement* seems much minimal here:

- Anti-aliased, sure, but also blurry due to temporal nature.
- Not really super sampled ish.
- Not much performance gain.
- But at least temporally stable.

## Ultra Quality (1.3x per axis)

At this point, FSR2 is now more of a better TAA than Unity TAA:

- The performance requirement now exceeds native.
- Better visual quality than native.
- Temporally stable.
- Less blurry than typical TAA.

Both Quality and Ultra Quality can be treat as a better TAA than Unity TAA itself. One can even go in and change the scaling to 1x for a DLAA-like high quality anti-aliasing.

## Conclusion, I Guess

Anyways, it is more than usable at this point.

With DRS, keeping UI rendered in native resolution can easily fool players as a much higher resolution while keeping performance in check. With my dual camera setup and only the bottom using FSR2, makes it extremely hard to notice the artefacts at normal viewing distance without knowing what to look for.

Though the results may vary between projects, so feel free to leave comments if you have interesting conflicting findings in your own project!

## Extra Note

This FSR2 implementation can support DRS with `ScalableBufferManager`, which due to FSR2's robustness hides the resolution adjustment very well.

Though for some reason ScalableBufferManager seems to scale some unwanted RTs which will cause glitching artefacts as I had to give up on this one. Thanks no thanks, Unity.