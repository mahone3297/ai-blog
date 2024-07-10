+++
title = '[AI 快手 LivePortrait] 引领高效肖像动画新时代'
date = 2024-07-09T11:22:31+08:00
draft = false
categories = ['AI', '快手', 'LivePortrait']
tags = ['AI', '快手', 'LivePortrait']
description = '快手推出了 LivePortrait，具备拼接与重定向控制的高效肖像动画，下载代码，准备环境，下载预训练权重并开始推理。'
keywords = ['AI', 'LivePortrait', '快手', '肖像动画', '拼接', '重定向']
+++

快手推出了 LivePortrait，具有拼接和重定向控制的高效肖像动画。

## 快速开始

### 下载代码，准备环境

```bash
git clone https://github.com/KwaiVGI/LivePortrait
cd LivePortrait

# create env using conda
conda create -n LivePortrait python==3.9.18
conda activate LivePortrait
# install dependencies with pip
pip install -r requirements.txt
```

### 下载预训练权重

- [Google Drive](https://drive.google.com/drive/folders/1UtKgzKjFAOmZkhNK-OYT0caJ_w2XAnib)
- [Baidu Yun](https://pan.baidu.com/s/1MGctWmNla_vZxDbEp2Dtzw?pwd=z5cn)

```bash
pretrained_weights
├── insightface
│   └── models
│       └── buffalo_l
│           ├── 2d106det.onnx
│           └── det_10g.onnx
└── liveportrait
    ├── base_models
    │   ├── appearance_feature_extractor.pth
    │   ├── motion_extractor.pth
    │   ├── spade_generator.pth
    │   └── warping_module.pth
    ├── landmark.onnx
    └── retargeting_models
        └── stitching_retargeting_module.pth
```

### 推理

```bash
python inference.py

# 指定图片和驱动视频
python inference.py -s assets/examples/source/s9.jpg -d assets/examples/driving/d0.mp4
```

### Gradio 接口

```bash
python app.py
```

### 推理速度评估

```bash
python speed.py
```

## 例子

试用了下，使用图片

![dutch-girl](dutch-girl.jpg)

生成视频如下

{{< video src="/ai-kuaishou-live-portrait-intro/dutch-girl--d3_concat.mp4" >}}

{{< video src="/ai-kuaishou-live-portrait-intro/dutch-girl--d3.mp4" >}}

感觉效果很不错！而且权重很小，600M左右。快手厉害了。

## FAQ

### ImportError: libGL.so.1: cannot open shared object file: No such file or directory
apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

---

- [homepage](https://liveportrait.github.io/)
- [github](https://github.com/KwaiVGI/LivePortrait)
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/ai-kuaishou-live-portrait-intro/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977569&idx=1&sn=fc7062cb3bc8fb45cde2daa9bfdfd9e4&chksm=86c7c824b1b04132e3ef44c5eb16626342b2d4f189160183573311b159a45495020faec6fc0a#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
