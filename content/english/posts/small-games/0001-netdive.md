---
title: "NetDive"
date: 2025-08-04T22:26:23+09:00
draft: false
tags: ["Game Design","NetDive"]
---

NetDive is such a random project, I got the idea out of nowhere but it felt compelling enough that I feel like I can make it in an instant. Not quite, ended up taking three months. But most of it is just because my day job is taxing, otherwise the total clocked hours would be closer to 3 weeks of fulltime work.

PS: the 3 weeks of fulltime work here might seem very little (which still is very fast), but it only refers to actual in-engine work, which totally ignores all the background design/music/sound work, and ignored the fact that I had a multiyear UI framework project and a newly built game framework just before making this game. So it's not really that easy.

Anyways, here’s a small post about how it was made.

{{< youtube R-WedWzdoM0 >}}

<iframe src="https://store.steampowered.com/widget/3718870/" frameborder="0" width="500" height="190"></iframe>

# Where It Started

Back in April 2025, I was busying with a lot of stuffs. Then out of nowhere my friend [PeDev](https://x.com/PeDev_) decided to throw me into oblivion by sending me a link to a game called NodeBuster.

[NodeBuster](https://store.steampowered.com/app/3107330/Nodebuster/), if you haven’t heard of it, is apparently an “experimental incremental game” that’s currently sitting on 12,108 reviews with 97% being positive as of the time of writing. What is an “experimental incremental game”? How did it sold some hundred thousands of copies? Also the fact that it had some interest clean shape representation which is totally something I dig so I felt compelled to give it a go.

I came away quite satisfied, not exactly the kind of game I would normally play but there’s nothing wrong about killing time alongside good sound effects and tunes if you got some to spare. I’m however very confused as to the “taking damage” part of the experience. You see in NodeBuster you are but a reticle aiming for nodes to bust, but you somehow take damage both over time and when hitting an enemy. So I did some searching and apparently it mostly all started from a game called To the Core.

In [To The Core](https://store.steampowered.com/app/1988550/To_The_Core/) you played as a drilling machine. When you dig you use oil, when you’re just sitting around you still waste oil, that made a lot more sense!

So I did some imagining on how I would approach the same idea, and quickly realized I have just the story to be told with this gameplay, and I do need to make some more action oriented game to validate the design of my ongoing game framework (as oppose to the almost VN like game I was working on at the time), incremental game is also very well structured alongside a 2-3 hr play time I wager it wouldn’t take much time to finish. So I took the plunge and dived in.

# The Story

I’ve only recently realized that I’m more interested in telling interesting stories in interesting ways. I have a story about an apocalyptic world caused by AI rampage lying around, but I haven’t really figured out the 4W1Hs yet. I want the reason to be interesting, human hating AI/war effort AI gone rogue is too much of a cliche at this point.

While figuring out a better fantasy to fit the taking damage/damage over time concept, it naturally occurred to me that some program diving in a stream of packets makes sense. Then why does the program intercepts packets? Hummm… how about just pure curiosity of kindness even? That’s when the idea of an AI learning to be a human kicks in, and the rest is history.

Usually I'd advocate for putting player into action as fast as possible, but there isn’t a lot of space between incremental gameplay so I had to do the beginning/ending/tons of readable lores in between approach for this one.

# The Gameplay

Incremental games are mostly about good numerical designs and less so about say... tight timed input gameplay, but apparently so called experimental incremental games seeks to *fix* that. Though I kind of just naturally settled on a SHMUP flavored gameplay, because of several reasons:

- I don't want to just copy NodeBuster or make anything that just feel like a cheap knockoff. Being just simple shapes and NodeBuster also is somewhat loosely cyber themed, so I had to mix up the gameplay enough to separate both.
- I had some gripes with the performance of NodeBuster, SHMUP kind of provides a quick way out solving this, more on this later.

It definitely has its cons. Technically I do limited the player freedom to only one dimension which is a *downgrade* from NodeBuster. I might be able to make it into a full on SHUMP style scroller, but I wanted to keep it simple because the schedule I had in mind with this game and I think players are just here to enjoy simple gameplay to keep their minds occupied instead of actually wanted to play a challenging game.

![Gameplay](/images/netdive/Gameplay.gif)

I later dug deeper and realized that these sort of game usually had some prestige system where you restart the game but become faster this time around, which results in an interesting constant decision making moments balancing when to restart. I tried out another game called [Digseum](https://store.steampowered.com/app/3361470/Digseum/) which besides making my hand ache for clicking too much, showed me what a satisfying moment it is when you restarted with a powerful ability and return back to where you came from with ease feels like.


# The Visual

Not much to say either. I kind of only ever made games with simple shapes and it still fits the cyber themed story so that’s that. I tried to add in more varieties in terms of visuals, with colors and backgrounds and stuffs.

One thing to say though, I quite fixated to make the feeling of diving and emerging from data stream to be satisfying right from the get go. That being said, the diving and emerging visuals and sound effects are actually basically the last thing I did during the development.

![Dive](/images/netdive/Dive.gif)

I do have a small story to share about the skill tree layout though. It is predetermined but generated with a random scatter points then constrain and relax considering where its prerequisites are. It came out pretty great, but I at some point wrote a wrong algorithm resulting in my skill tree swimming away haha.

![Swimming Skill Tree](/images/netdive/SwimmingSkillTree.gif)

# The Performance

I’m quite fixated on two things on front:

- Running 800p/90FPS on Steam Deck
- Delivering satisfying visuals through sheer amount of entities

The first part is due to me owning a Steam Deck OLED, so I intrinsically wanted to hit the 90FPS cap and have HDR support. The second however is inherently my lack of skills in creating detailed work, so I had to make up with visual design and maybe just bruteforce it by sheer amount to provide interesting visuals. 

This leads to adopting the idea of separating data and renderer of faster memory access, and the intentionally flattened hierarchy to prevent overhead. This wasn’t quite enough but still pretty close to locked 90 in typical gameplay. I might move into team Big Fat Struct at some point, but turns out handling 3000+ entities actually isnt that bad with my current halfbaked approach, makes me think that the scope of my game probably never would need an ECS.

Speaking of performance, Nodebuster due to its design requiring the player to pick up all loots by mouse, can never despawn any drop of loot. But later part of the games requires quite some grind so you and up needing to let it idle around and come back to collect things manually, and Steam Deck can't really handle the entities performant enough. With my SHMUP style gameplay it ensured entities on screen is fully managed. I can despawn them as soon as they're out of the screen, which also means players using with ultra wide monitors will suffer from not being able to despawn enemy early on, but that a natural sacrifice one had to make for more screen real estate anyways.

All the Physics responses in NetDive was faked for a very controlled result. But of course the physics itself is just Unity built in physics. I initially used Continuous Dynamic on Rigidbodies, but it took up too much in the frame time graph so I switched to Continuous Speculative instead. The collision doesn't need to be that accurate anyways.

# Sound Design

It’s been a long time since I last did proper sound design work. The original sound effects for Autopanic was done in an intensive weeks of work back when I have zero experience, and I kind of never touched it since. Autopanic Zero only reused the same effects, and I’m kind of ashamed not being able to properly go through it another pass because players do complain about it in Zero.

I’ve been using Resonic Player for sound management, but due to circumstances I’m now developing mostly on macOS, which isn’t supported by Resonic. I remembered another friend of mine who did sound design on the Nine Sols once recommended me Soundly, which turned out to support macOS so I gave it a try.

[Soundly](https://getsoundly.com/) had pretty good integration with Fmod and Wwise, and as far as I can tell seems to be the only sound library app out there to do so. It’s a bit unfortunate that they arbitrarily limited local storage up to 10000 audio files only if you’re on Free tier, and they intentionally sabotage your search result with their Pro cloud library, which really sucks, but I guess they’re not here for charity anyways. Apart from that Soundly features similar sound searching (analyzation needed beforehand) and placeholder voiceline which should be a nice to have, and also is available for free tier so that’s nice of them.

The workflow using Soundly is very smooth: find sound, select sound, pop them into fmod in a one click ish fashion. NetDive’s sound design was done within half a day, and I was quite happy with the result. That speaks something about Soundly and ofc my personal growth as a sound designer since 2022.

Designing for a incremental game has its unique challenge of needing to carefully navigate the line between annoying, satisfying, and underwhelming. I would imagine a better approach is probably to set up a system to dynamically balance between volume and different sfx for the same event, I don’t really have good grasp right now and I kind of wanted to wrap up the project for now, so I just did it the old fashion way of manually adjusting everything until it is sometimes satisfying and at least not annoying.

One interesting note is that one of the playtesters said the soundscape sounds like hearing tablewares clashing in a restaurant alongside lofi music, so I later doubled down on that particular image doing final polishing.

# Conclusion

NetDive is a project that I have many fun working with. The scope is clear, the iteration is fast, a near fully C# based project almost using Unity only as a renderer makes everything so much reliable, or at least it is some selfowned reliable issue. Having the timespan to be way longer than I expected is a bit unfortunate, but the actual development time isn't bad at all, I would hope to keep up this pace and release much more games than I used to.