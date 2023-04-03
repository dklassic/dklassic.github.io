---
title: "Auto Tester"
date: 2022-12-24T22:36:11+08:00
draft: false
tags: ["Autopanic","Game Design"]
---

So, as a solo developer, it's extremely hard to juggle with all the numbers for balancing.

To help me with that, an automated tester was deployed to help me quickly validate my design changes.

Here's a snippet of it in action:

{{< youtube lH0svQIR79A>}}

# Auto Tester

I first have the idea of automated testing since my revamp of player and enemy code base. Although still separated, a lot of the designs for player and enemy were structured to be similar. I quite fascinated by some automation test talks from GDC, and figure it should be extremely useful for my game to have one. Though I never went the extra mile to setup an automated test, my later systems are often written with automated tests in mind.

Fast forward to me making a spinoff project, I only want to hack together something somewhat enjoyable as fast a possible. But Survivor-like gameplay takes quite some effort both physically and mentally to play through, and it is also extremely time consuming to do playtest myself. I'm not quite ready to lose my friends to an unbalanced gameplay so I decided it's time to deploy an automated tester.

# Auto Tester for Autopanic Zero

![Auto Tester for Autopanic Zero](/images/posts/autopanic-devlog/0017/3.gif)

Automated tester for Autopanic Zero is pretty rudimentary. All it does is:

- Always target nearest enemy
- Having a preferred distance from target
- Shoot constantly
- Initially dash whenever available, I later make it assess how surrounded it is to trigger the dash

But it is already useful enough to validate the general balance before I had to dive in and check the experience in depth. This helped me focusing on broad strokes when tweaking my game instead of burying myself in details.

So I'm quite happy with the results. Still, there's only combat in Zero which makes it trivial to implement, but Autopanic has much more interactions to consider.

# A detour at Sigono

For some reason I have the privilege to work in Sigono, the studio behind the excellent OPUS: Echo of Starsong.

I've been helping to port the game to iOS and to save performance in a finished product without full picture of the code base is a trial and error effort. Thankfully they have a automated testing system with automated screen recording which helped me check the result of my tweak without me having to play through the whole game.

Their automated system more than once saved my ass, and solidifies my desire to finally implement automated tester in Autopanic.

# Auto Tester for Autopanic

So automated tester in Autopanic is deployed to do the following:

- Clear an encounter
- Reach reward and claim it
- Move towards a randomly selected exit and use it
- Interact with shops
- Die
- Repeat infinitely

The tester tries to mimic an actual gameplay and only teleports when needed (since I haven't implemented a proper path finding algorithm).

It's not smart enough to win the game on its own, but it is robust enough to consistently making to the first boss and occasionally winning. When I really need it to make it to the end, I'll just lock its health so it can power through.

Autopanic is an absurd project for a solo developer if I'm being honest. Some design choices intentionally adds burden to the  system, zero load screen and no cut policy isn't something I'd recommend trying without proper experience, but that's where I am right now. So the deployment of automated tester really helped a lot, and has since helped me with:

- Continuously sanity checking the healthiness of the code base and the overall performance
- Infinite retrying to help identify rare bugs
- A quick validation of the overall game balance
- A quick method to generate believable gameplay and screenshots without me having to play

Automated testing is basically free quality assurance workforce. I think small developers will benefit a lot from deploying one.
