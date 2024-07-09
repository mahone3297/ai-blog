+++
title = '[AI Kuaishou LivePortrait] Leading the New Era of Efficient Portrait Animation'
date = 2024-07-09T11:22:31+08:00
draft = false
categories = ['AI', 'Kuaishou', 'LivePortrait']
tags = ['AI', 'Kuaishou', 'LivePortrait']
description = 'Kuaishou has launched LivePortrait, featuring efficient portrait animation with stitching and redirection control. Download the code, prepare the environment, download pre-trained weights, and start inference.'
keywords = ['AI', 'LivePortrait', 'Kuaishou', 'portrait animation', 'stitching', 'redirection']
+++

Kuaishou has launched LivePortrait, featuring efficient portrait animation with stitching and redirection control.

## Quick Start

### Download the code and prepare the environment

```bash
git clone https://github.com/KwaiVGI/LivePortrait
cd LivePortrait

# create env using conda
conda create -n LivePortrait python==3.9.18
conda activate LivePortrait
# install dependencies with pip
pip install -r requirements.txt
```

### Download pre-trained weights

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

### Inference

```bash
python inference.py

# specify source image and driving video
python inference.py -s assets/examples/source/s9.jpg -d assets/examples/driving/d0.mp4
```

### Gradio Interface

```bash
python app.py
```

### Inference Speed Evaluation

```bash
python speed.py
```

## Examples

Tried it with an image

![dutch-girl](dutch-girl.jpg)

The generated videos are as follows

{{< video src="/ai-kuaishou-live-portrait-intro/dutch-girl--d3_concat.mp4" >}}

{{< video src="/ai-kuaishou-live-portrait-intro/dutch-girl--d3.mp4" >}}

The results look great! And the weights are quite small, around 600MB. Kuaishou is impressive.

## FAQ

### ImportError: libGL.so.1: cannot open shared object file: No such file or directory
apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

---

- [homepage](https://liveportrait.github.io/)
- [github](https://github.com/KwaiVGI/LivePortrait)
<!-- - [original](...) -->
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - Learn AI from scratch](...) -->
<!-- - [CSDN - Learn AI from scratch](...) -->
<!-- - [Juejin - Learn AI from scratch](...) -->
<!-- - [Zhihu - Learn AI from scratch](...) -->
<!-- - [Alibaba Cloud - Learn AI from scratch](...) -->
<!-- - [Tencent Cloud - Learn AI from scratch](...) -->
