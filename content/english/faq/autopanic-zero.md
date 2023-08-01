---
title: "Autopanic Zero FAQ"
draft: false
enableComments: false
showTip: false
---

Created: May 10, 2022

*Last Updated April 3, 2023:* Here are answers to frequently asked questions about my second game, ***Autopanic Zero***!

# Where does *Autopanic Zero* come from?

***Autopanic*** is originally designed to be a shoot ‘em up when it started. Here’s an [old Reddit post](https://www.reddit.com/r/Unity3D/comments/fwgt8o/day_7_in_my_twin_stick_shooter_attempt/) of its early days.

Anyways after wrapping up most core pillars of ***Autopanic*** in May 2022, I decided to take a look at this phenomenal game called ***Vampire Survivor*** that stormed the internet. And oh boy, isn’t it fun!

So now that my game is a much overkill version of that original vision, I thought to myself that it’ll be interesting to revisit the original idea with the tools I have. Following the popularity of games like ***20 Minutes Till Dawn***, I figure some people might appreciate something like this as it is.

Hence ***Autopanic Zero*** was born.

I later decided that the world don't really need yet another plain survivor style game, so I decided to borrow some hints from ***Armored Core***.

# So is *Autopanic Zero* connected to *Autopanic* in any way?

Yes, indeed.

***Autopanic Zero*** canonically takes place after the events of ***Autopanic***… Wait a second, ***Zero*** is actually a sequel. Did I mess it up? Crap.

# Where can I get *Autopanic*?

***Autopanic Zero*** will soon be available on:

- [Steam](https://store.steampowered.com/app/1423670/)

<!-- # Now that *Autopanic Zero* is out, what's next?

Still polishing up ***Autopanic***, should be releasing very soon. -->

<!-- # Will *Autopanic Zero* be receiving extra content updates?

I’d like to do so as long as I’m financially available! I find making Autopanic Zero to be a fun side project to test out designs and even contributes retroactively towards ***Autopanic***'s development. But I’m super broke now so I need to polish up and release ***Autopanic*** as soon as possible first.

If you’d like to support development of extra content, please consider buying the DLC. But please only purchase it if you find yourself comfortable supporting the content as it is now.

I’ll also make the project open source whenever I can no longer update it. -->

# What are the minimum system requirements?

This one is tricky.

I can only say that CPU is the key to run this game smoothly and the game will gladly use up all the cores you have. I’ve done multitude of optimization to allow the overkill AI inherited from ***Autopanic*** to run at a much larger scale.

I’m personally satisfied about the result. Further optimization would require a complete overhaul of AI structure, which I’m convinced to do some time in the future, just not now.

For now please make sure you have a powerful multicore CPU. If you’re running into trouble, turn off the destruction simulation entirely, enable dynamic resolution, and limiting framerate might help for a smoother gameplay.

# Does *Autopanic Zero* have PC controller support?

Yes! The game automatically work with any controller thrown at it. If not? That’s probably Unity’s fault. You can also toggle on/off Steam Input, both of which might lead to a proper detection of controller input.

# Is *Autopanic Zero* a multiplayer game, or are there any plans for multiplayer?

On one hand the idea does sound interesting, but on the other hand I’m not particularly sure how to make such design. Plus I haven’t written any netcode for games yet, would took some serious research to ensure it being bug-free.

Will probably investigate but don’t keep your hopes up.

# Does *Autopanic Zero* support PC cloud saves?

Yes! You may also find local copies of your saves under `Documents/Saved Games/Autopanic Zero`.

<!-- # I ran into a technical issue with the game. What should I do?

If you need technical support, please have a look in [Autopanic Zero Tech Fixes]({{< ref "/tech-fixes/autopanic-zero" >}}). If the problem still hasn't been resolved, you can find help in [Autopanic Steam Technical Support forum](https://steamcommunity.com/app/1423670/discussions/1/) or in the official Discord server `#autopanic-tech-support` channel, which should help get you sorted. -->


# How do I use auto aim in *Autopanic Zero* with Mouse and Keyboard?

Go to Accessibility and turn off Use Mouse Aim. Auto aim will kick in.

Hol'up Mouse aiming should be quite easy, why don't you just aim?

# So that’s it for the *Autopanic Zero* FAQ?

That’s all of it! Thanks for reading ;)