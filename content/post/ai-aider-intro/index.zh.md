+++
title = '[AI aider] 打造终端AI搭档：Aider让编程更智能更有趣！'
date = 2024-06-20T12:41:23+08:00
draft = false
categories = ['AI', 'aider']
tags = ['AI', 'aider']
description = '发现Aider，一个能在终端中与AI搭档编程的工具，让你的编程体验更智能、更有趣。'
keywords = ['AI', 'aider', '编程', 'AI搭档', '大型语言模型', '终端工具', 'git']
+++

今天给大家介绍一个超级酷炫的AI项目，叫做 [Aider](https://aider.chat/)。

## 介绍

Aider 是一个让你在终端里与AI搭档编程的工具。想象一下，你和一个超级智能的编程小伙伴在一起，Aider 让大型语言模型（LLMs）成为你的编程搭档，帮助你编辑本地 git 仓库中的代码。无论是从零开始的全新项目，还是现有的git仓库，Aider都能驾驭。最棒的是，它与 GPT-4o 和 Claude 3 Opus 配合简直天作之合，但几乎任何大型语言模型都能和它搭配使用。

![aider screencat](https://aider.chat/assets/screencast.svg)

## 开始

想要和你的AI搭档来一次愉快的编程之旅吗？那就来吧！

```bash
$ pip install aider-chat

# 进入一个 git 仓库
$ cd /to/your/git/repo

# 使用 GPT-4o 在你的仓库上工作
$ export OPENAI_API_KEY=your-key-goes-here
$ aider
```

然后你就可以和大模型开始畅聊代码了，Aider 会帮你改代码、git 提交，一气呵成。

## 特点，Repository map

强烈推荐阅读这篇精彩的文章 [Building a better repository map with tree sitter](https://aider.chat/2023/10/22/repomap.html)，文章详细阐述了如何构建更好的仓库地图。

在改代码的过程中，你需要解决三个问题：

1. 找到需要更改的代码。
2. 理解那段代码与整个代码库其他部分的关系。
3. 做出正确的代码更改以完成任务。

对于第3个问题，GPT-4 简直是神器。而第2个问题，我们用 repo map 来解决。

repo map 可以传递给 LLM，让它了解代码的上下文。当 repo map 太大时，我们会用一个图排名算法来找到最相关的部分。

那么，如何得到 repo map 呢？起初我们用的是 ctags，但因为文章中1，2，3，4的关系，最后切换成了 tree-sitter。

至于第1个问题，目前还需要手工解决。

## 试用结果

Aider 支持很多 LLM。我试用了 DeepSeek 这个模型，他们最近发布了 DeepSeek Coder V2 模型，号称代码能力超过 GPT4-Turbo。Aider 也说它在 aider 的代码编辑 benchmark 上获得了最高分。

然而，我用后感觉效果并不理想。。。也许是我用的不对姿势吧。

## 结论

总结一下：继续努力工作，继续AI吧。生活需要一点点坚持，也许下一个代码大神就是你。

---

- [官网](https://aider.chat/)
- [github](https://github.com/paul-gauthier/aider)
- [Building a better repository map with tree sitter](https://aider.chat/2023/10/22/repomap.html)
- https://deepseek.com/
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/ai-aider-intro/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977505&idx=1&sn=21a91feef83c38edc7ad0727751a184b&chksm=86c7c864b1b0417296dda0f3f20cee58f8e5fd66ac514b53f2722efb7524e80472c0fe2a69c8#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
