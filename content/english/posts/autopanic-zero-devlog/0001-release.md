---
title: "The Design of Autopanic Zero"
date: 2024-07-14T10:00:23+08:00
draft: false
tags: ["Autopanic Zero","Game Design"]
---

Probably the weirdest devlog in the world that started on game release, but here we are!

{{< youtube s6WSW1UOOhY >}}

<iframe src="https://store.steampowered.com/widget/1423670/" frameborder="0" width="500" height="190"></iframe>

I'm currently making another game *Autopanic* which is a twin-stick shooter with Rogue-like elements.

*Autopanic Zero* is a sister project that stemmed from *Autopanic*'s codebase, it is firstly made within 7 days just for fun, then took 3 days in a local convention back in 2022 to refine the basic pillars and it kind of just stuck there. The game was always meant to be randomly release out in the wilds at some point, but in December 2023 I decided to make it a full game worthy of a Steam release and use it to validate some theories of mine.

*Autopanic Zero* is used to validate the following assumptions:

- **I** can make and release a full game that lives up to **my** own standard of a releasable game
- I can follow Valve's instruction and properly perform the steps needed to release a game on Steam
- The visual make up is considered good and not cheap to players
- The basic game feel is considered fun to players

And also to answer some questions:

- Steam Next Fest is considered a no-brainer wishlist gathering opportunity, is it?
- How effective is a *good* game launched for free with zero marketing?

It's just day two of release so most of it are still ongoing, but there's at least one question answerable now: No, Steam Next Fest is currently not a no-brainer wishlist gathering opportunity.

Anyways, since *Autopanic Zero* is intentionally used to improve the design of *Autopanic*, I'll first talk about what design choices I made specifically for *Autopanic Zero*, then to how it improves *Autopanic*.

# *Autopanic Zero*'s Design

*Autopanic Zero* was made because I one day played *10 Minutes Till Dawn* and like it a lot, and since I'm already making a Rogue-like with random ability progression, it's rather easy to hack together a similar game by just setting a constant spawn of enemies in a large level.

But of course this doesn't really pose as a game good enough to stand on it's own, so I had to figure out something unique to this game alone.

## Figuring out what the game is

I think Unique Selling Point is overrated but I do believe I'm not here to make "[Another game] but worse". *10 Minutes Till Dawn* is basically *Vampire Survivor* but short and twin-stick shooter, if I just release the game as is this game is for no one.

I quickly fixated on two gripes I had with *Vampire Survivor* (which btw isn't their *fault*, it's not part of their design), first is the nearly meaningless character choice as it doesn't change the overall gameplay, second is bosses are just meatier punching bag. *Vampire Survivor* is pretty okay with those design due to the movement only player interaction, but since I'm making a game with a lot more player interactions, I need to improve on both of them to make it work.

So with bosses *Autopanic* already got some mini bosses ready, I just imported them here and make their attack pattern more suitable with large crowd of mobs around. As for meaningful starting choice, I feel like the weapon choice alone from *Autopanic* isn't good enough, so I firstly added an options to change the characteristics of player movement, then I added an ultimate gauge because I don't know what else to add.

And here it is, a 10 minute-ish loop horde survival game with three bosses to defeat.

## Iteration through playtesting

Early playtesters (gamedev friends of mine) are generally okay with the game but no one is amazed by it. Which is expected. But the final boss got easily vaporized by most playtesters, which is expected but seem way too anti-climatic than what I hoped for. So I later changed the final wave to just be a constant stream of enemies as a DPS check, which is more satisfying when the player survived.

The progression is originally designed to naturally unlock new ones when survived till a certain point with each equipment, but further playtests from non-gamedev friends who actually liked to play Survivor-like games pointed out the lack of clear progression is an issue, they have no idea when the game *ends* which to them are unlocking everything. *Autopanic* is originally designed to have zero permanent currency since it is an exploration based game, but Survivor-like players certainly is here for something more apparent.

I switched to a currency and shop system for equipment unlocks, but then realized my total equipment count is too low to be interesting enough when the progression is clear, and I also don't want to have an arbitrarily lengthy grind for each equipment.

![Original equipment of *Autopanic Zero*](/images/posts/autopanic-zero-devlog/0001/0001.png "Originally these are the only equipment planned for *Autopanic Zero*")

I know I'm supposed to release the game quick and move on, but again I'm also testing my assumption of "release a full game that lives up to **my** own standard of a releasable game", so I can't just let it be.

I decided to pull out an older design document featuring a more *Armored Core* adjacent design of *Autopanic Zero*, and quickly implemented all the equipment I had there. To my surprise, it only took like two days to make everything work (and a dozen to fix up follow-up issues) which speaks to how well written the original document back then is and it saved me.

So, *Armored Core* + *10 Minutes Till Dawn*, something like that.

![Current equipment of *Autopanic Zero*](/images/posts/autopanic-zero-devlog/0001/0002.png "Now *Autopanic Zero* features over 50 equipment to customize from")

## Steam Deck as baseline

Steam Deck is pretty cool and I personally loved playing games on it. While it certainly runs well for a machine of that size, it still struggles with 3D games in general and even *Vampire Survivor* can bring it down to its knees when the enemy count is overwhelming.

*Autopanic* is a game featuring small levels and a much smaller crowd, *Autopanic Zero* however is a game with large spaces and a way bigger crowd. Which means I need some serious optimization to make it run 60FPS on Steam Deck, and the bar is then raised to 90FPS because the release of Steam Deck OLED featuring a 90Hz screen.

Ultimately I managed to hit a high enough framerate by hunting down all the inefficiencies mostly due from unpooled object spawning and Unity issues large and small (like [light still breaks unlit shader's batching](https://forum.unity.com/threads/gpu-instancing-with-unlit-shader-broken-because-affected-by-different-forward-lights.583051/#post-3887902)), and then I drastically overhauled the enemy spawning algorithm to maintain a "just surrounded enough" enemy positioning while preventing enemies from idling outside of player view. The game will still push Steam Deck under 90FPS during the crowded moments, but that's probably as far as I can get without switching to a simplified version of enemy AI or changing the vector based rendering of the visuals (which is quite costly on the CPU rendering thread).

In the end even if players manually cap it to 60FPS, they'll still gain prolonged battery life out of it which is still a big thing when playing smaller games on Steam Deck.

## Axe irrelevant contents when needed

*Autopanic Zero* is originally planned to release on July 2nd, except I started from insomnia then quickly escalated to fever and headaches just few days before release. During those moments, I'm simply incapable of working so I knew I had to let go extra planned stuffs. *Autopanic Zero* is originally planned to feature more artwork and stories, I hope to make it an *Autopanic Expanded Universe* stuff or something. But I'm not really in a position to release that *perfect* version of *Autopanic Zero*, so I wrapped up everything I had until that point and made a clean cut so everything still makes sense, and I barely finished it before the pushed back release date of July 12th.

## Released to fail

Because of course it'll fail! I talked to almost no one about the release, sent zero preview code out there. But even with this predestined failure, I've surely gained a lot from it, even if it's just the fact that Steamworks Release function is so busted that I had to try three times to properly release my game haha. I also learnt that Valve doesn't really want donation style DLC which forced me to do a last minute decision to use my own tracks instead of free musics online so I can at least justify it as an OST.

This is also the cold hard truth of game release that I need to remember: even with a game of this caliber, even when release for free, it's still not enough to sell itself.



# How it improves *Autopanic*

So as far as *Autopanic Zero* goes, it literally pushes *Autopanic*'s codebase to the extreme. Forcing me to reexamine tons of inefficiencies I can get away with *Autopanic*'s smaller encounter, and therefore further drastically optimized *Autopanic*'s performance. The most significant part is for me to manage everything myself, basically no more Unity handled objects, my codebase is responsible for every single one of them.

From gameplay perspective, *Autopanic Zero* treaded some design choices that I definitely won't take if I just kept on trying to finish *Autopanic*. While I don't think they'll all be for the better in *Autopanic*, the change on perspective really gives me more to think about.

I also took the chance to implement basically every accessibility, Quality of Life options into the game, which of course then can be easily slotted into *Autopanic*'s codebase, so that even if *Autopanic* didn't end up being the best game in the world, all of my games will definitely be candidates of best accessibility.


So, so far so good? I've been making games for four years now, but I never felt worthy of calling myself a gamedev (even when I'm already hired by a game studio), now that I've released a game no one plays I think I can confidently say I AM a gamedev. And even with no one playing it, *Autopanic Zero* is still a cool game that I'll definitely enjoy anytime on Steam Deck. I managed to release a game I liked, neat!