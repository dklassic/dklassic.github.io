---
title: "Scalable"
date: 2022-12-18T10:00:23+08:00
draft: true
tags: ["Autopanic Zero","Game Design"]
---

Back in May 2022 I submitted Autopanic to a local contest, which I earned third place. The prize comes with a guaranteed coverage by biggest local gaming news site so not bad. But I digress.

After submission. I decided to take a break and play this "Vampire Survivor" everyone is crazy about, and oh boy, ain't it some of the best balancing I've ever seen.
The thing that surprised me most is probably how this kind of Shoot 'em Up ish design still holds up and people now crave for more. So, I decided to try my hand at revisiting the original idea of this project, but with some Vampire Survivor's design in mind. I then proceed to recreate my original idea for my game in seven days.

Though before that, I need to fit larger enemy count into my game.

Switch to manager pattern
Since enemy count is drastically increased, I need to squeeze out every single performance.
I've always use the Update() function in Unity to do everything, but according to Unity's own article, such method introduce overhead when used a lot.

I've already have an EnemyManager to do all the spawning and despawning, so it's just a matter of using it to update all the enemies. Which is easy enough.


Jobs for raycast
Since my AI relies on massive raycast count to decide its movement, large enemy count naturally results in some absurd amount of raycast. Here's a quick look at 100 enemies' raycast:

Actually, not bad! But we're talking hundreds of enemies here, gonna optimize it as much as I can or else players will shower negative review all over the internet.
So naturally I tried to use Jobs for multithreaded raycasting:

And...... the performance got worse. Which is expected since I implemented this jobified version the same as before. Each enemies still cast their own rays, just batched into a job. It would seem like when the ray count is low, batching it with job actually worsen its performance.

So let me try again. This time with the manager pattern, I use the EnemyManager to cast all the rays for all enemies at once, and then:

Now that's an improvement!

I also ported this design back to my original game, which don't actually need such efficiency but hopefully some players would be happy about it.
Also watching large amount of my enemies swarming though the map is quite satisfying.

