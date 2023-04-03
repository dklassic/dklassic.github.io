---
title: "08. AI Behavior Revamp and Procedural Animation"
date: 2022-10-20T10:00:25+08:00
draft: false
tags: ["Autopanic"]
---

# AI Behavior Revamp

My old solution relies on Unity's NavMesh and NavMeshAgent. This becomes a chore to me later on because:

- As my levels becomes more dynamic, managing NavMesh becomes a tedious work
NavMeshAgent can reliably move towards the destination, but also costs too much to request frequently
- My gameplay is very fast-paced, so I'd like my enemies to react to player action as fast as possible

So I decided to move to a custom solution that is basically about picking a preferred direction and move forward.

## Movement Determination

Generally a level may look something like this:

![obstacles](/images/posts/game-design/0004/1.jpg)

For each calculation, the agent will check the following things:

- Obstacle around the agent (e.g. other agents, traps, and decors)
- Distance and direction towards a preferred location (e.g. movement destination and target agent)

So it's all about avoid bumping into obstacles and wanting to have a certain distance between certain target. Which looked like this:

![scoring](/images/posts/game-design/0004/3.jpg)

Then I added some physical constraints to make the agent move more naturally, such as:

- Having acceleration/deceleration speed
- Having max speed
- Will decelerate if the preferred direction is too different from current direction
- Have a max rotation speed

I could've gone further and have rotation acceleration/deceleration, but I find it somewhat hard to balance around the numbers, so I've decided to omit it for now.

So far so good:

![movement](/images/posts/game-design/0004/4.gif)
![enemy roaming](/images/posts/autopanic-devlog/0008/1.gif)

This approach also helps me make some actions more dynamic, such as "Strategic Dash" and "Emergency Evade", for these action can now be used with understandings of the environment instead of a fixed direction and stuffs.

I've then spend some time optimizing raycast with multithread but nothing fancy.


## Attack Pattern

I decided to move towards the idea of an attack pattern. To ensure the combat won't become raw skill-based chaos, but a more manageable situation to be learned and resolved by the players.

So I constructed a hefty list of actions available, just to name a few:

![commands](/images/posts/autopanic-devlog/0008/3.png)
![enemy pattern](/images/posts/autopanic-devlog/0008/2.png)


And now instead of making multitude of enemy prefabs, I now have one enemy prefab that will instantiate with a EnemySetting scriptable object, which makes modification a lot easier.

![enemy setting](/images/posts/autopanic-devlog/0008/4.png)

Now with enemy behavior revamped, time to add in procedural animation.

# Procedural Animation

Procedural Animation in my game is a big topic, because basically every single changing element was procedural, i.e. code driven.

I know early on that I'm not going to be doing keyframes at all. Not only because I'm just but one guy, also that I've watched the famous talk from David Rosen about procedural animation in Overgrowth and was convinced that procedural animation can be used to achieve suitably high quality animation with way less effort.

## UI Animation

Not much to talk about here due to my simple UI setup, but I do have several glitch effect setup for the windows, which is driven by something like this:

```
switch (CurrentTransition)
{
    case WindowTransition.Noise:
        maskIndex[i, j] = UnityEngine.Random.Range(0, TextUtility.FadeIn.Length - 1);
        break;
    case WindowTransition.Glitch:
        if (UnityEngine.Random.value > 0.5f)
            maskIndex[i, j] += Mathf.FloorToInt(Time.unscaledDeltaTime / maskAnimationStep);
        break;
    case WindowTransition.DamageGlitch:
        if (UnityEngine.Random.value > 0.5f)
            maskIndex[i, j] += Mathf.FloorToInt(Time.unscaledDeltaTime / maskAnimationStep);
        break;
    case WindowTransition.Random:
        if (UnityEngine.Random.value > 0.25f)
            maskIndex[i, j] += Mathf.FloorToInt(UnityEngine.Random.Range(1, TextUtility.FadeIn.Length - 1) * Time.unscaledDeltaTime / maskAnimationStep);
        break;
    default:
        maskIndex[i, j] += Mathf.FloorToInt(Time.unscaledDeltaTime / maskAnimationStep);
        break;
}
```

Some demonstration:

![ui animation](/images/posts/autopanic-devlog/0008/5.gif)

## Generic Procedural Animation

This part is a bit more fun. Mostly done with DOTween because DOTween is just great. Some examples:

### Hit Reaction
```csharp
icon.DOPunchRotation(damageForce / unitSize, 0.5f, 10, 0)
```

![hit reaction](/images/posts/autopanic-devlog/0008/6.gif)

### Weapon Recoil
```csharp
recoilTarget.DOPunchPosition(recoilForce / unitSize, recoilDuration, 1)
```

![rifle recoil](/images/posts/autopanic-devlog/0008/7.gif)
![shotgun recoil](/images/posts/autopanic-devlog/0008/8.gif)

Simple, quick to make, and can include the consideration of physicality quite easily.

## Procedural Movement Animation

Now comes the fun part, though maybe not much to be explained.

I find that making procedural movement animation is basically programming the process of how the real world counterpart would move:

- If leg is too far away, move
- If moving, lean
- Move faster if displacement is large

Which is as rudimentary as it can be, but this also makes it hard to find resources to follow. I ended up learning more about procedural animation by looking at [Jakob Wahlberg](https://twitter.com/Jakob_Wahlberg)'s tweets.

Since I revamped enemy behavior, my AI now have some proper physicality in its movement. So as long as my procedural movement animation can automatically accommodate the displacement of the unit, the result will always be great:

![All movements](/images/posts/game-design/0005/8.gif)

And by extension, it also works on player controlled character:

![procedural animation](/images/posts/autopanic-devlog/0008/9.gif)

So with procedural animation in place, my game finally looks a lot more complete.
