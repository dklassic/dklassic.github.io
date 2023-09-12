---
title: "Delayed Result Gathering"
date: 2023-09-11T21:09:11+08:00
draft: false
tags: ["Autopanic"]
---

So there's this technique called Delayed Result Gathering where you can delay the gathering of Jobs' result, to prevent stalling the main thread in waiting.

In normal method, a Job related loop would look like this:

```C#
Loop()
{
    DispatchJob();
    GatherResult();
    DoOtherStuffs();
}
```

Right? But then this whole sequence is executed within a frame, which means `GatherResult` had to stall everything else and wait for the Job to finish first. Which means the whole process essentially looked more akin to this:

```C#
Loop()
{
    DispatchJob();
    // Wait until Job done
    GatherResult();
    DoOtherStuffs();
}
```

With Delayed Result Gathering, we essentially collect the result at the start of next frame, as in:

```C#
Loop()
{
    // Hopefully the Job is done
    GatherResult();
    DispatchJob();
    // No need to wait for Job done
    DoOtherStuffs();
}
```

With a single frame of delay, the Job can be done asynchronously, ideally. One can even push it further, to collect the result only when the Job is fully complete, resulting in zero waiting:

```C#
Loop()
{
    if(jobDone) // Wait for the Job completely asynchronously
        GatherResult();
    if(!jobDispatched)
        DispatchJob();
    // No need to wait for Job done
    DoOtherStuffs()
}
```

Though for some reason, back when I tried to implement it [when I'm researching how to write a scalable AI]({{< ref "/0000-scalable-ai" >}}), Unity gave me some error preventing me to do so. I figure the performance improvement is already good enough, so I just leave it as is.

Recently I read [an example](https://github.com/simplestargame/SimpleMeshChunkSample) on how to generate combined mesh asynchronously using Jobs. And I realized that there's a much intuitive way of implementing Delayed Result Gathering, which allows me to write it in the much intuitive DispatchJob -> GatherResult order.

So I've done it using Coroutine:

```C#
Coroutine()
{
    JobHandle handle = DispatchJob();
    while(!handle.IsComplete)
        yield return null;
    handle.Complete();
    GatherResult();
}
```

And so now the EnemyManager can update 100 enemies easily without getting stalled by the Job.

![no delayed result gathering profile](/images/posts/autopanic-devlog/0023/1.png "Before, the EnemyManager stalls to wait for the Job done.")

![delayed result gathering profile 1](/images/posts/autopanic-devlog/0023/2.png "After, the EnemyManager simply continue whatever it needs to do and wait for the result asynchronously.")

![delayed result gathering profile 2](/images/posts/autopanic-devlog/0023/3.png "After, when the result is ready to be gathered, proceed with the processing.")