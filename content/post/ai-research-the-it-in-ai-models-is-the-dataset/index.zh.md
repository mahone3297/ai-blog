+++
title = '[AI Research] AI 模型中的“it”是数据集'
date = 2024-05-10T10:17:34+08:00
draft = false
categories = ['AI', 'Research']
tags = ['AI', 'Research']
description = "模型效果的好坏，最重要的是数据集，而不是架构，超参数，优化器。"
keywords = ["AI", "Research", "模型", "数据集", "架构", "超参数", "优化器"]
+++

**模型效果的好坏，最重要的是数据集，而不是架构，超参数，优化器。**

---

我现在已经在 OpenAI 工作了将近一年。在这段时间里，我训练了很多生成模型。比起任何人都有权利训练的要多。当我花费这些时间观察调整各种模型配置和超参数的效果时，有一件事让我印象深刻，那就是所有训练运行之间的相似之处。

我越来越清楚地认识到，这些模型确实以令人难以置信的程度逼近它们的数据集。这意味着它们不仅学会了什么是狗或猫，还学会了不重要的分布之间的插值频率，比如人类可能拍摄的照片或人类常写下的单词。

这表现为 - 长时间训练在相同数据集上，几乎每个具有足够权重和训练时间的模型都会收敛到相同的点。足够大的扩散卷积-联合产生与 ViT 生成器相同的图像。AR 抽样产生与扩散相同的图像。

这是一个令人惊讶的观察！它意味着模型行为不是由架构、超参数或优化器选择确定的。它是由您的数据集确定的，没有别的。其他一切都是为了高效地将计算逼近该数据集而采取的手段。

那么，当您提到“Lambda”、“ChatGPT”、“Bard”或“Claude”时，您所指的不是模型权重。而是数据集。

---

- [原文](https://nonint.com/2023/06/10/the-it-in-ai-models-is-the-dataset/)
- 本文
    - [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/post/ai-research-the-it-in-ai-models-is-the-dataset/)
    - [微信 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977011&idx=1&sn=33e2a53e3e08fcd82fc878b495cefa51&chksm=86c7ca76b1b04360fb5f31c688c2a143fe0ec6e6b0a7185a379bc203f2c80119d5b2bf632618#rd)
    - [CSDN - 从零开始学AI](https://blog.csdn.net/mahone3297/article/details/138657435)
    - [掘金 - 从零开始学AI](https://juejin.cn/post/7366948087128817700)
    - [知乎 - 从零开始学AI](https://zhuanlan.zhihu.com/p/696934253)
    - [阿里云 - 从零开始学AI](https://developer.aliyun.com/article/1504718)
    - [腾讯云 - 从零开始学AI](https://cloud.tencent.com/developer/article/2416239)
