+++
title = '[AI words] 突破瓶颈：如何将AI words网站构建时间缩短一半'
date = 2024-06-15T17:16:35+08:00
draft = false
categories = ['AI', 'AI words']
tags = ['AI', 'AI words']
description = '了解我如何优化AI words网站的构建过程，将构建时间从14分钟缩短到仅仅7分钟。本文详细介绍了优化步骤和遇到的挑战。'
keywords = ['AI', 'AI words', '优化', '网站性能', '构建过程', '网站开发']
+++

在一个阳光明媚的早晨，我坐在电脑前，满怀期待地按下了“构建”按钮，准备生成我的新网站 [AI words](https://ai-words.aihub2022.top/)。这个网站的目标是为每个单词生成一个单独的页面，总共有5000个单词。可是，构建过程竟然需要整整14分钟！我心想，难道没有办法让这个过程更快一些吗？

## 初探性能瓶颈

于是，我决定与我的AI助手进行一次深入的对话。我们讨论了各种可能的优化方案，并最终决定先进行详细的性能分析。我们加入了 metrics 来检测每个模板的耗时情况，特别是希望找到优化 AI words 网站构建的突破口。结果很快出来了：

```plaintext
      cumulative       average       maximum      cache  percent  cached  total  
        duration      duration      duration  potential   cached   count  count  template
      ----------      --------      --------  ---------  -------  ------  -----  --------
   11m14.127830535s  1.484863062s  8.275081851s          0        0       0    454  index.html
   6m18.63167821s   34.730478ms  6.838507807s         39        0       0  10902  partials/head/head.html
   6m9.997678009s   18.474942ms  3.123818975s          0        0       0  20027  partials/data/title.html
   1m5.89808511s    7.257498ms   62.181409ms          0        0       0   9080  _default/single.html
```

从数据中可以看出，index.html 是必要的，但是 head.html 却是耗时大户。优化 AI words 网站的构建时间，首先要解决这个问题。于是，我决定从这里入手。

## 初战告捷

我与AI助手再次讨论，决定尝试为这些 partials 加入缓存。于是，我动手调整了代码，并满怀期待地再次按下了“构建”按钮。几分钟后，我惊讶地发现，性能有了显著提升，构建时间从14分钟缩减到了7分钟！我简直不敢相信自己的眼睛：

```plaintext
      cumulative       average       maximum      cache  percent  cached  total  
        duration      duration      duration  potential   cached   count  count  template
      ----------      --------      --------  ---------  -------  ------  -----  --------
   5m52.246181489s  775.872646ms  2.862713569s          0        0       0    454  index.html
   1m3.632475614s    7.007981ms   66.654399ms          0        0       0   9080  _default/single.html
   40.250901904s    4.432918ms    52.10609ms          2        0       0   9080  partials/article/article.html
```

## 意外挫折

正当我为这一突破欣喜若狂时，下午的一次例行检查让我冷静下来。我发现，所有页面的标题都变成了“404 not found”。怎么会这样？我赶紧检查代码，发现问题出在缓存上。这个发现让我心情沉重，只好无奈地回滚代码，构建时间又回到了14分钟。看着 AI words 网站构建时间又回到起点，我有些失望。

## 绝地反击

尽管遭遇挫折，我并没有放弃。冷静下来后，我重新分析性能瓶颈，发现 title.html 中的计算量过大，严重拖慢了速度。其实，我的需求并不复杂，于是我决定简化 title.html 的代码。

经过一番调整，我再一次按下了“构建”按钮。随着时间的推移，我紧张地盯着屏幕上的进度条，终于，结果出来了——构建时间再次缩短到了7分钟！这一次，我不仅感受到了成功的喜悦，更体会到了坚持和改进的力量。

```plaintext
      cumulative       average       maximum      cache  percent  cached  total  
        duration      duration      duration  potential   cached   count  count  template
      ----------      --------      --------  ---------  -------  ------  -----  --------
   5m53.388687234s  778.389178ms  1.685881574s          0        0       0    454  index.html
   1m7.814885681s    7.468599ms   67.456653ms          0        0       0   9080  _default/single.html
    35.24786248s    3.881923ms    63.40133ms          2        0       0   9080  partials/article/article.html
```

## 最终胜利

通过这次优化过程，我不仅成功将构建时间减半，更重要的是，我学到了如何通过分析和调整代码来提升性能。每一次的失败和成功都让我变得更强大、更有经验。未来，我会继续优化，让我的网站 AI words 运行得更快、更稳定。这次的经历让我明白，坚持和改进是通向成功的必经之路。

---

- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/ai-words-optimize-build-process/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977485&idx=1&sn=8c0f44e59ab78efe26224b2446ac2ad5&chksm=86c7c848b1b0415e3b11d727a69f8e5626860ee8b28989d363cf7a59b9c98e99ccc59c454c94#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
