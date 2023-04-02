---
title: "07. Custom UI Framework"
date: 2022-10-19T10:10:01+08:00
draft: true
tags: ["Autopanic"]
---

Back then I'm all sold on the new Unity Input System, which has some really promising features and I don't want to walk back to use the old input system. However the new Input System for whatever reason doesn't gel well with their UI Events.

So I need a custom UI framework.

Inspired by Phi Dinh's Recompile, I figure a fully text-based UI would be great for my project.
Although I'm incapable to do fancy ASCII animation and having to support Chinese characters by default ('cause, I speak Mandarin) removes quite a lot of  presentation choices, limiting myself can help me focus more on actual useful stuffs.

Building a robust UI framework is imminent anyways because before that I was debugging by clicking on Unity's editor window. The back and forth between game screen and editor takes me out of the flow, traversing the scene hierarchy doesn't help either.

I started by building an enemy spawner:

An elegant weapon for a more civilized age.

This makes the enemy testing process much easier. No more drag & drop and clicking through scene hierarchy.

The UI framework gradually grows into a behemoth supporting all sorts of stuffs easily. For example, my system menu UI can be initiated with a class that inherits the GeneralUISystemWithNavigation class. Then I can simply do:
```
protected override void InitializeUI()
{
    systemWindow ??= NewWindow("ui_system", DefaultSetup);
    AddButton("ui_system_Resume", systemWindow, () => CloseMenu(true, false));
    AddButton("ui_system_Visual", systemWindow, () => OpenSubMenu(0));
    AddButton("ui_system_Audio", systemWindow, () => OpenSubMenu(1));
    AddButton("ui_system_Control", systemWindow, () => OpenSubMenu(2));
    AddButton("ui_system_Language", systemWindow, () => OpenSubMenu(3));
    AddButton("ui_system_Accessibility", systemWindow, () => OpenSubMenu(4));
    exitUI = AddButton("ui_system_Exit", systemWindow, () => OpenSubMenu(7));
}
```


And then vuala:


Though all the game's UI are done with this framework, my debug menus made the most out of this framework:
