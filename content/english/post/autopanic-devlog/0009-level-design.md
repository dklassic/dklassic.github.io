---
title: "09. The Lack of Level Design"
date: 2022-10-21T10:00:32+08:00
draft: true
tags: ["Autopanic"]
---

The Lack of Level Design

I'm quite inspired by Oskar Stalberg's work on Bad North, and I remember seeing him mentioning the level design.
Can’t remember the exact quote and I forgot which tweet does it come from, but I think it is something like this:
Quote
Every randomly generated level is a valid test of player's combat skill

It was a tweet about how WFC can be easily utilized in a combat-focused game but not so much in a puzzle game.

Anyhow, I decided to follow this philosophy so that I can quickly went over level design and focus on other pressing matters.
So I first started by making a level editor:


Tried and true 2D checkbox, easy. My idea is to make some generally serviceable shapes then use random decoration to fill up the space. I'm not going to impress players with fully unique level visuals so I just simply do none.

By randomly spawning decorations in level, essentially an unique combat puzzle has spawned.
I prepared several types of decoration:
Pillar - Blocks everything, can be destroyed
Railing - Blocks non-flying units, serves as a dynamically spawned gap
Trap - Just some explosives

To prevent random decoration killing the experience, I've added some additional rules:
Max amount of decorations allowed is root squared tile count
Decoration can only spawn if that tile has at least six neighbor tile
Decoration cannot spawn if any neighbor tile has decoration
Decoration cannot spawn if adjacent to Exit tile or Entrance tile
Worked out pretty well.

Not that this will generate any memorable encounter on its own, but it indeed change the flow of the level drastically enough to produce unique combat puzzle on every random generation.


This approach also allows me to preview all layouts easily in my UI system:



Level Visuals
I'm definitely not going it impress anyone, but I hope to provide some interesting floor patterns to be discovered during gameplay. These patterns will be revealed dynamically whenever a light source shows up. I find this approach easy to make yet still feels interesting to see them through the crack of light.


