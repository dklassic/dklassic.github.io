---
title: "延遲結果蒐集"
date: 2023-09-11T21:09:11+08:00
draft: false
tags: ["自動混亂"]
---

有一個技巧叫做「<abbr title=Delayed Result Gathering>延遲結果蒐集</abbr>」，可以避免主執行緒被迫要等待 Job 完成。

正常的 Job 寫法，通常循環會長這樣：

```C#
Loop()
{
    DispatchJob() // 發派 Job
    GatherResult() // 蒐集結果
    DoOtherStuffs()
}
```

合理吧？但這整個流程要在一幀內執行完成，也代表說 `GatherResult` 必須要阻止後續所有操作，等到這個 Job 先完成才行。也就代表說，真正的流程會更像這樣：

```C#
Loop()
{
    DispatchJob() // 發派 Job
    // 等待 Job 完成
    GatherResult() // 蒐集結果
    DoOtherStuffs()
}
```

藉由延遲結果蒐集的概念，我們可以在下一幀的開頭再蒐集結果，也就是：

```C#
Loop()
{
    // 希望 Job 已經完成了
    GatherResult() // 蒐集結果
    DispatchJob() // 發派 Job
    // 不需要等 Job 完成
    DoOtherStuffs()
}
```

在這個一幀的延遲下，就可以讓 Job 的執行能非同步化，理想上啦。也可以再進一步調整成，只有在計算保證完成時才蒐集結果，這樣就可以完全彌平等待時間：

```C#
Loop()
{
    if(jobDone) // 用非同步的方式等待工作完成
        GatherResult() // 蒐集結果
    if(!jobDispatched)
        DispatchJob() // 發派 Job
    // 不需要等 Job 完成
    DoOtherStuffs()
}
```

不過基於某些理由，當時我在[研究怎樣撰寫可規模化的 AI 時]({{< ref "/0000-scalable-ai" >}})，試著實作卻會收到 Unity 的一些錯誤訊息阻止我。當時實作多執行緒操作後，效能也大幅強化了，我就暫時不管這件事了。

不過最近閱讀一篇[關於怎樣用 Job 來非同步地合併模型的範例](https://github.com/simplestargame/SimpleMeshChunkSample)，並且意識到有一種更直覺的方式可以實作延遲結果蒐集，讓我可以用「發派 Job→蒐集結果」的順序形式處理。

於是我使用 Coroutine 來實作：

```C#
Coroutine()
{
    JobHandle handle = DispatchJob()
    while(!handle.IsComplete)
        yield return null;
    handle.Complete();
    GatherResult();
}
```

在這樣的修改後，我的敵人管理流程可以在不需要被 Job 卡住的情況下輕鬆在 0.1ms 內更新 100 個敵人。

![no delayed result gathering profile](/images/posts/autopanic-devlog/0023/1.png "修改前，EnemyManager 要等待 Job 完成才能繼續。")

![delayed result gathering profile](/images/posts/autopanic-devlog/0023/2.png "修改後，EnemyManager 可以繼續往下跑，並且用非同步的方式等待結果。")