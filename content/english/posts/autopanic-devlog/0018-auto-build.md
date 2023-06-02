---
title: "Auto builder and auto versioning"
date: 2023-06-01T12:20:11+08:00
draft: false
tags: ["Autopanic", "misc"]
---

Autopanic is now in the phase of mass external playtest, so that I can get a better grasp if my designs are working or not. Accompanying extensive playtest sessions, I'm now required to switch between different features constantly and starting to make a lot of mistakes building and uploading the wrong version.

Time to make an auto builder.

# The Features

![feature toggle](/images/posts/autopanic-devlog/0018/2.png)

Currently there are several features for Autopanic:

- Debug Start Up, instead of the usual loading the game normally, give me several options to quickly setup my test environment.

![debug start up](/images/posts/autopanic-devlog/0018/3.png)

- Allow Debug Tool, should be self-explanatory.
- Allow In Game Logger, display additional info on screen for testing purpose.
- Allow Incompatible Save, save conversion between versions doesn't exist yet, by default I simply purge incompatible save.
- Skip Tutorial Setting, my tutorial starts with a sequence of settings, to save me some pain here's a skip.
- Allow Steamwork, since Steamwork messes with the editor, it's forced off by default but sometimes I need to test it in editor.

These correspond to some of the following scenario:

- Personal playtest session uses every combination.
- External playtester will play out normally, but I want them to be able to access debug tool just in case.
- To test on Release version, the internal debug log will have to be shown on screen.
- Sometimes I'll have to remove Steamwork and pack the game in a zip.

So with great features, comes great responsibility to remember which is for which, and remember to setup correctly before exporting the game. But with the extensive playtest, I now make enough mistakes for me to decide to offload it to an Auto Builder.

# Auto Builder

![auto builder](/images/posts/autopanic-devlog/0018/1.png)

Simply put, to setup a one click building tool that exports the project with the right setting.

Unity's editor tool allows for the access of `UnityEditor.BuildPipeline.BuildPlayer` to trigger the build, and `UnityEditor.PlayerSettings.SetScriptingDefineSymbols` to setup the define symbols. So that's it:

1. Change the define symbol
2. Build the game
3. Revert the define symbol

Done.

Well, not quite.

# Auto Versioning

Autopanic is an extremely small game, both in terms of content and assets included. The game built is around 200MB which can be compressed into 70-80MB, the build process takes 20 seconds with Mono and 1 minute with IL2CPP, which is absurdly fast .

So I can quickly iterate on my design and playtesters can receive patches as soon as reported. But with fast iteration comes the problem of actually knowing which version playtesters are on. Steam doesn't notify each client instantly for patches unless the user verifies game file manually, so I need to mark versions properly to know if the problem has already been fixed or not.

But well, let's just say I'm not going to bump that Application.version every time I build, so I need some automatic way of versioning. And here's where the version control comes in.

See, Git tracks each commit with a SHA value, which is almost guaranteed to be unique even with just the first few digits. So I just need to read the .git folder and get the SHA every time I build, and say, maybe also every time I enter play mode.

Of course this comes at the cost of increasing the time required to enter play mode (RIP my super fast enter play mode time), but it should more then make up for actually knowing where I am, in terms of my code, all the time.

![Commit](/images/posts/autopanic-devlog/0018/5.png)

And so I can just show the relevant information on screen all the time:

```C#
$"v{Version} {Git branch} ({Current commit SHA})\n" +
$"{Build Profile} [{Target Platform}]\n" +
$"@ {Time of the build or just the time entering play mode}";
```

![SHA](/images/posts/autopanic-devlog/0018/4.png)

Anyways, back to playtest and iterating!
