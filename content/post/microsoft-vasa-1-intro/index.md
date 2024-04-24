+++
title = 'VASA-1：以音频驱动的逼真实时生成的对话脸部'
date = 2024-04-24T09:53:04+08:00
draft = false
categories = []
tags = []
description = ''
keywords = []
+++

肖像 + 声音 = 视频，该领域，最早阿里EMO，之后腾讯MuseV，AniPortrait。

今天，微软出了 VASA-1，这个效果是真好。排第一。可惜没放出源码。我们来看下。

---

简而言之：单张肖像照片+语音音频=在实时生成的超逼真对话脸部视频中，具有精确的唇音同步、栩栩如生的面部行为和自然的头部运动。

![teaser](https://vasavatar.github.io/VASA-1/image/teaser.jpg)

## 摘要
我们介绍了VASA，一个框架，用于在给定单张静态图像和语音音频片段的情况下，生成具有吸引力的视觉情感技能（VAS）的虚拟角色的栩栩如生的对话脸部。我们的首款模型，VASA-1，不仅能够产生与音频精确同步的唇部运动，还能捕捉到广泛的面部细微差别和自然的头部运动，从而增强了真实感和生动感的感知。核心创新包括一个在面部潜在空间中工作的整体面部动态和头部运动生成模型，以及使用视频开发出这样一种富有表现力和解耦的面部潜在空间。通过包括对一组新指标进行评估在内的大量实验，我们展示了我们的方法在各个方面显著优于以往的方法。我们的方法不仅提供了高质量的视频，具有逼真的面部和头部动态，还支持在可忽略的起始延迟下以高达40帧每秒的速度在线生成512x512的视频。这为模拟人类对话行为的逼真化头像的实时交互铺平了道路。

（注意：本页面上的所有肖像图像均为由StyleGAN2或DALL·E-3生成的虚拟、不存在的身份，除了蒙娜丽莎。我们正在探索为虚拟的、互动的角色生成视觉情感技能，而不是模仿现实世界中的任何人。这只是一个研究演示，没有产品或API发布计划。另请参阅本页面底部的更多我们的负责任AI考虑。）

### 逼真度和生动性
我们的方法不仅能够产生精确的唇音同步，还能生成丰富表达的面部细微差别和自然的头部运动。它可以处理任意长度的音频并稳定输出无缝的对话脸部视频。

{{< video src="https://vasavatar.github.io/VASA-1/video/l5.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/l8.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/l3.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/l4.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/l7.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/l2.mp4" >}}

一个分钟长的音频输入的示例。

{{< video src="https://vasavatar.github.io/VASA-1/video/9.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/3.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/10.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/15.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/11.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/7.mp4" >}}

更多简短的示例与多样化的音频输入

### 生成的可控性
我们的扩散模型接受可选信号作为条件，例如主要眼睛注视方向和头部距离，以及情绪偏移量。

{{< video src="https://vasavatar.github.io/VASA-1/video/female_gaze.mp4" >}}

在不同主要凝视方向下的生成结果（分别为正前方、向左、向右和向上）

{{< video src="https://vasavatar.github.io/VASA-1/video/female_scale.mp4" >}}

在不同头部距离尺度下的生成结果

{{< video src="https://vasavatar.github.io/VASA-1/video/male_emotion.mp4" >}}

在不同情感偏移下的生成结果（分别为中性、快乐、愤怒和惊讶）

### 分布外泛化
我们的方法表现出处理训练分布之外的照片和音频输入的能力。例如，它可以处理艺术照片、歌唱音频和非英语语音。这些类型的数据在训练集中并未出现。

{{< video src="https://vasavatar.github.io/VASA-1/video/o1.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/o2.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/o6.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/o5.mp4" >}}

### 解耦能力
我们的潜在表示将外观、3D头部姿态和面部动态解耦，这使得生成内容的单独属性控制和编辑成为可能。

{{< video src="https://vasavatar.github.io/VASA-1/video/sameid_female_0.mp4" >}}
{{< video src="https://vasavatar.github.io/VASA-1/video/same_latent.mp4" >}}

相同输入照片搭配不同运动序列（左两个案例），以及相同运动序列搭配不同照片（右三个案例）。

{{< video src="https://vasavatar.github.io/VASA-1/video/male_disen.mp4" >}}

姿态和表情编辑（原始生成结果，仅姿态结果，仅表情结果，以及带有旋转姿态的表情）

### 实时效率
我们的方法在离线批量处理模式下，能够以45帧每秒（fps）的速度生成512x512大小的视频帧，并且在在线流式传输模式下，支持最高40fps的帧率，仅有170毫秒的前置延迟，这一性能是在配备单个NVIDIA RTX 4090 GPU的桌面PC上评估得出的。

{{< video src="https://vasavatar.github.io/VASA-1/video/realtime_demo.mp4" >}}

### 风险和负责任的人工智能考虑
我们的研究重点是为虚拟人工智能化身生成视觉情感技能，旨在积极应用。它不旨在创建用于误导或欺骗的内容。然而，像其他相关的内容生成技术一样，它仍然可能被潜在地滥用于冒充人类。我们反对任何创建误导性或对真实人物有害内容的行为，并有兴趣应用我们的技术来推进伪造检测。目前，通过这种方法生成的视频仍然包含可识别的人工痕迹，并且数值分析表明，要达到真实视频的真实性还有一段差距。

在承认滥用可能性的同时，重要的是要认识到我们技术的实质性积极潜力。好处——例如增强教育公平性、改善沟通挑战者的可访问性、为有需要的人提供陪伴或治疗支持等——强调了我们研究和其他相关探索的重要性。我们致力于负责任地开发人工智能，目标是推进人类福祉。

鉴于这样的背景，我们没有计划发布在线演示、API、产品、额外的实施细节或任何相关产品，直到我们确定这项技术将被负责任地使用，并符合适当的法规。

- [官网](https://www.microsoft.com/en-us/research/project/vasa-1/)
- 本文
    <!-- - [博客 - 从零开始学AI](...) -->
    <!-- - [微信 - 从零开始学AI](...) -->
    <!-- - [CSDN - 从零开始学AI](...) -->
    <!-- - [掘金 - 从零开始学AI](...) -->
    <!-- - [知乎 - 从零开始学AI](...) -->
    <!-- - [阿里云 - 从零开始学AI](...) -->
    <!-- - [腾讯云 - 从零开始学AI](...) -->
