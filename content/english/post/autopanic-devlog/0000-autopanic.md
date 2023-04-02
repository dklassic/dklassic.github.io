---
title: "00. The Target"
date: 2022-10-14T04:02:38+08:00
draft: false
tags: ["Autopanic"]
---

![old thumbnail](/images/posts/autopanic-devlog/0000/1.png)
![combat action](/images/posts/autopanic-devlog/0000/2.gif)

I'm currently making a fully diegetic minimalist twin-stick shooter with Rogue-like elements.

# Setup

An AI assistant wake you up from a long slumber. All you can do is to follow its guidance and ascend to the top floor.

# Goals

I find 13 Sentinels: Aegis Rim combat visual to be simple and effective, but the combat design itself leaves a lot to be desired. So I wanted to make a twin-stick shooter with 13 Sentinels: Aegis Rim's visual. That's it!

The game eventually evolves into a game with Rogue-like elements because I wanted to make the game about overcoming impossible odds.

# Devlog

I'm doing the devlog retrospectively because I started with zero game development knowledge and stumbled a lot during my development. Only now when the game is nearly finished, I can finally sort my development out and write a cohesive story documenting it.

# Visual Design

Since I started this project with zero knowledge about 3D and art in general, I limited myself early on to use only vector graphics and 3D primitives throughout the game.

This decision also has impact on my design. Sometimes I give up on a design only because of my visual design toolset couldn't do it justice. In the end this design choice helped my game to be focused.

# Fully Diegetic

For no apparent reason, I've decided to make every single element in my game to be diegetic, as in, existing in the game world. To simply put, for whatever stuff player is looking at, that thing actually has a meaning in-game.

Some quick examples:

- Instead of just a button prompt, the prompt is your buddy AI speaking to you.
- Instead of characters speaking to each other without voice acting, they are communicating through text.

This design choice caused quite some issue later on, but overall I think it should result in an interesting experience.

# Unity 3D

I'm using Unity3D for the development. I try to avoid 3rd party plugins with the exception of DOTween for easy tweening operation and Shapes for vector graphics rendering.
