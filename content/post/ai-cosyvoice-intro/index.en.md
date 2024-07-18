+++
title = '[AI CosyVoice] Alibaba Open-Source Speech Generation Model'
date = 2024-07-18T09:27:25+08:00
draft = false
categories = ['AI', 'CosyVoice']
tags = ['AI', 'CosyVoice']
description = 'Explore Alibaba open-source multilingual speech generation model CosyVoice, and learn about its full-stack inference, training, and deployment capabilities.'
keywords = ['AI', 'CosyVoice', 'speech generation', 'open source', 'multilingual', 'model']
+++

## Introduction

CosyVoice is a large-scale multilingual speech generation model that provides full-stack capabilities for inference, training, and deployment.

## Installation
### Clone and Install

- Clone the repository
```bash
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
# If submodule cloning fails due to network issues, run the following command until successful
cd CosyVoice
git submodule update --init --recursive
```
- Install Conda: Refer to https://docs.conda.io/en/latest/miniconda.html
- Create a Conda environment:
```bash
conda create -n cosyvoice python=3.8
conda activate cosyvoice
# WeTextProcessing requires pynini, install it using conda as it works across all platforms.
conda install -y -c conda-forge pynini==2.1.5
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com

# If encountering sox compatibility issues
# ubuntu
sudo apt-get install sox libsox-dev
# centos
sudo yum install sox sox-devel
```
### Model Download
We strongly recommend downloading our pre-trained CosyVoice-300M, CosyVoice-300M-SFT, CosyVoice-300M-Instruct models, and CosyVoice-ttsfrd resources.

If you are an expert in the field and only interested in training your own CosyVoice model from scratch, you can skip this step.

```python
# SDK model download
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice-300M', local_dir='pretrained_models/CosyVoice-300M')
snapshot_download('iic/CosyVoice-300M-SFT', local_dir='pretrained_models/CosyVoice-300M-SFT')
snapshot_download('iic/CosyVoice-300M-Instruct', local_dir='pretrained_models/CosyVoice-300M-Instruct')
snapshot_download('iic/CosyVoice-ttsfrd', local_dir='pretrained_models/CosyVoice-ttsfrd')
```

```python
# git model download, make sure git lfs is installed
mkdir -p pretrained_models
git clone https://www.modelscope.cn/iic/CosyVoice-300M.git pretrained_models/CosyVoice-300M
git clone https://www.modelscope.cn/iic/CosyVoice-300M-SFT.git pretrained_models/CosyVoice-300M-SFT
git clone https://www.modelscope.cn/iic/CosyVoice-300M-Instruct.git pretrained_models/CosyVoice-300M-Instruct
git clone https://www.modelscope.cn/iic/CosyVoice-ttsfrd.git pretrained_models/CosyVoice-ttsfrd
```

Optionally, you can unzip the ttsfrd resources and install the ttsfrd package for better text normalization performance.

Note that this step is not mandatory. If you do not install the ttsfrd package, WeTextProcessing will be used by default.

```bash
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd-0.3.6-cp38-cp38-linux_x86_64.whl
```

## Usage
### Basic Usage

For zero-shot/cross-lingual inference, use the CosyVoice-300M model. For sft inference, use the CosyVoice-300M-SFT model. For instruct inference, use the CosyVoice-300M-Instruct model. First, add third_party/Matcha-TTS to your PYTHONPATH.

```bash
export PYTHONPATH=third_party/Matcha-TTS
```

```python
from cosyvoice.cli.cosyvoice import CosyVoice
from cosyvoice.utils.file_utils import load_wav
import torchaudio

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-SFT')
# sft usage
print(cosyvoice.list_avaliable_spks())
output = cosyvoice.inference_sft('Hello, I am the Tongyi generative speech model, how can I assist you?', 'Chinese Female')
torchaudio.save('sft.wav', output['tts_speech'], 22050)

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M')
# zero-shot usage for Chinese/English/Japanese/Cantonese/Korean
prompt_speech_16k = load_wav('zero_shot_prompt.wav', 16000)
output = cosyvoice.inference_zero_shot('Receiving a birthday gift from a friend far away, the unexpected surprise and heartfelt wishes filled my heart with sweet joy, and a smile bloomed like a flower.', 'I hope you can do even better than me.', prompt_speech_16k)
torchaudio.save('zero_shot.wav', output['tts_speech'], 22050)
# cross-lingual usage
prompt_speech_16k = load_wav('cross_lingual_prompt.wav', 16000)
output = cosyvoice.inference_cross_lingual('And then later on, fully acquiring that company. So keeping management in line, interest in line with the asset that\'s coming into the family is a reason why sometimes we don\'t buy the whole thing.', prompt_speech_16k)
torchaudio.save('cross_lingual.wav', output['tts_speech'], 22050)

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-Instruct')
# instruct usage, supports <laughter></laughter><strong></strong>[laughter][breath]
output = cosyvoice.inference_instruct('Facing challenges, he showed extraordinary <strong>courage</strong> and <strong>wisdom</strong>.', 'Chinese Male', 'Theo \'Crimson\', is a fiery, passionate rebel leader. Fights with fervor for justice, but struggles with impulsiveness.')
torchaudio.save('instruct.wav', output['tts_speech'], 22050)
```

### Launch Web Demo

You can quickly familiarize yourself with CosyVoice using our web demo page. We support sft/zero-shot/cross-lingual/instruct inference in the web demo.

See the demo website for details.

```python
# For sft inference, change to iic/CosyVoice-300M-SFT, or for instruct inference, change to iic/CosyVoice-300M-Instruct
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M
```

### Advanced Usage

For advanced users, we provide training and inference scripts in examples/libritts/cosyvoice/run.sh. You can follow this recipe to familiarize yourself with CosyVoice.

## Build for Deployment

Optionally, if you want to use grpc for service deployment, you can run the following steps. Otherwise, you can ignore this step.

```python
cd runtime/python
docker build -t cosyvoice:v1.0 .
# If you want to use instruct inference, change to iic/CosyVoice-300M-Instruct
# for grpc usage
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/grpc && python3 server.py --port 50000 --max_conc 4 --model_dir iic/CosyVoice-300M && sleep infinity"
python3 grpc/client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
# for fastapi usage
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/fastapi && MODEL_DIR=iic/CosyVoice-300M fastapi dev --port 50000 server.py && sleep infinity"
python3 fastapi/client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
```

---

- [github](https://github.com/FunAudioLLM/CosyVoice)
- [online demo](https://www.modelscope.cn/studios/iic/CosyVoice-300M)
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [WeChat Public Account - Learn AI from scratch](...) -->
<!-- - [CSDN - Learn AI from scratch](...) -->
<!-- - [Juejin - Learn AI from scratch](...) -->
<!-- - [Zhihu - Learn AI from scratch](...) -->
<!-- - [Alibaba Cloud - Learn AI from scratch](...) -->
<!-- - [Tencent Cloud - Learn AI from scratch](...) -->
