+++
title = '[AI MoneyPrinterTurbo] 一键成片，超级印钞机'
date = 2024-06-26T16:24:00+08:00
draft = false
categories = ['AI', '文生视频']
tags = ['AI', '文生视频', 'MoneyPrinterTurbo']
description = '探索MoneyPrinterTurbo的奇妙旅程，一个文生视频工具，让您只需一键，就能体验从安装到配置，再到创建高清短视频的全过程。'
keywords = ['AI', '文生视频', 'MoneyPrinterTurbo', '高清短视频', '一键生成']
+++

今天，我们将踏上一段关于**MoneyPrinterTurbo**的探索之旅，这是一个文生视频工具，旨在让视频创作变得轻松而有趣。

## 故事的开始

想象一下，你只需要提供一个视频主题或关键词，剩下的——视频文案、素材、字幕、背景音乐，全部自动生成，最终合成一个高清的短视频。这听起来像是魔法，但**MoneyPrinterTurbo**让它成为了现实。

## 安装与配置

我们的旅程从安装开始。首先，我们需要安装**ImageMagick**，一个强大的图像处理工具：

```bash
sudo apt-get install imagemagick
```

接着，我们克隆**MoneyPrinterTurbo**的仓库，并设置Python环境：

```bash
git clone   
cd MoneyPrinterTurbo
conda create -n MoneyPrinterTurbo python=3.10
conda activate MoneyPrinterTurbo
pip install -r requirements.txt
```

在**config.toml**文件中，你需要配置以下内容，以启动你的视频创作之旅：

- pexels_api_keys
- llm_provider
- llm api keys

## 启动应用

现在，你可以通过UI界面或API启动你的视频创作引擎：

- UI界面：
  ```bash
  sh webui.sh
  ```
- API接口：
  ```bash
  python main.py
  ```

界面很清楚，操作也很简单。真的就是输入主题，其他一键生成。

![MoneyPrinterTurbo webui](webui.png)

## 见证奇迹

最后，我们一起看下生成的视频。效果一般。

{{< video src="/ai-MoneyPrinterTurbo-intro/pet-dog-vs-cat.mp4" >}}

## 原理

原理看起来比较简单

- 你提供主题，LLM生成描述和关键词
- 从 pexels pixabay 下载视频，图片
- tts 生成语音
- 配上字幕
- 背景音乐默认就几个

最后，将上面所有东西合在一起，视频完成。

## 结语

目前阶段的AI，只能到这个程度。看来，还需要努力工作。

---

- [github](https://github.com/harry0703/MoneyPrinterTurbo)
<!-- - [AI 博客 - 从零开始学AI](...) -->
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
