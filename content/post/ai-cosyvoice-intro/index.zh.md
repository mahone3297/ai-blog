+++
title = '[AI CosyVoice] 阿里开源语音生成模型'
date = 2024-07-18T09:27:25+08:00
draft = false
categories = ['AI', 'CosyVoice']
tags = ['AI', 'CosyVoice']
description = '探索阿里开源的多语言语音生成模型 CosyVoice，了解其全栈推理、训练和部署能力。'
keywords = ['AI', 'CosyVoice', '语音生成', '开源', '多语言', '模型']
+++

## 介绍

CosyVoice 是多语言大规模语音生成模型，提供推理、训练和部署的全栈能力。

## 安装
### 克隆并安装

- 克隆仓库
```bash
git clone --recursive https://github.com/FunAudioLLM/CosyVoice.git
# 如果由于网络问题导致子模块克隆失败，请运行以下命令直到成功
cd CosyVoice
git submodule update --init --recursive
```
- 安装 Conda: 请参阅 https://docs.conda.io/en/latest/miniconda.html
- 创建 Conda 环境:
```bash
conda create -n cosyvoice python=3.8
conda activate cosyvoice
# WeTextProcessing 需要 pynini，使用 conda 安装它，因为它可以在所有平台上执行。
conda install -y -c conda-forge pynini==2.1.5
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host=mirrors.aliyun.com

# 如果遇到 sox 兼容性问题
# ubuntu
sudo apt-get install sox libsox-dev
# centos
sudo yum install sox sox-devel
```
### 模型下载
我们强烈推荐您下载我们预训练的 CosyVoice-300M、CosyVoice-300M-SFT、CosyVoice-300M-Instruct 模型和 CosyVoice-ttsfrd 资源。

如果您是该领域的专家，并且只对从头训练自己的 CosyVoice 模型感兴趣，可以跳过此步骤。

```python
# SDK 模型下载
from modelscope import snapshot_download
snapshot_download('iic/CosyVoice-300M', local_dir='pretrained_models/CosyVoice-300M')
snapshot_download('iic/CosyVoice-300M-SFT', local_dir='pretrained_models/CosyVoice-300M-SFT')
snapshot_download('iic/CosyVoice-300M-Instruct', local_dir='pretrained_models/CosyVoice-300M-Instruct')
snapshot_download('iic/CosyVoice-ttsfrd', local_dir='pretrained_models/CosyVoice-ttsfrd')
```

```python
# git 模型下载，请确保已安装 git lfs
mkdir -p pretrained_models
git clone https://www.modelscope.cn/iic/CosyVoice-300M.git pretrained_models/CosyVoice-300M
git clone https://www.modelscope.cn/iic/CosyVoice-300M-SFT.git pretrained_models/CosyVoice-300M-SFT
git clone https://www.modelscope.cn/iic/CosyVoice-300M-Instruct.git pretrained_models/CosyVoice-300M-Instruct
git clone https://www.modelscope.cn/iic/CosyVoice-ttsfrd.git pretrained_models/CosyVoice-ttsfrd
```

可选地，您可以解压 ttsfrd 资源并安装 ttsfrd 包以获得更好的文本规范化性能。

请注意，这一步不是必需的。如果您没有安装 ttsfrd 包，我们将默认使用 WeTextProcessing。

```bash
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd-0.3.6-cp38-cp38-linux_x86_64.whl
```

## 使用
### 基本使用

对于零样本/跨语言推理，请使用 CosyVoice-300M 模型。对于 sft 推理，请使用 CosyVoice-300M-SFT 模型。对于 instruct 推理，请使用 CosyVoice-300M-Instruct 模型。首先，将 third_party/Matcha-TTS 添加到您的 PYTHONPATH。

```bash
export PYTHONPATH=third_party/Matcha-TTS
```

```python
from cosyvoice.cli.cosyvoice import CosyVoice
from cosyvoice.utils.file_utils import load_wav
import torchaudio

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-SFT')
# sft 使用
print(cosyvoice.list_avaliable_spks())
output = cosyvoice.inference_sft('你好，我是通义生成式语音大模型，请问有什么可以帮您的吗？', '中文女')
torchaudio.save('sft.wav', output['tts_speech'], 22050)

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M')
# 零样本使用，用于中文/英文/日文/粤语/韩语
prompt_speech_16k = load_wav('zero_shot_prompt.wav', 16000)
output = cosyvoice.inference_zero_shot('收到好友从远方寄来的生日礼物，那份意外的惊喜与深深的祝福让我心中充满了甜蜜的快乐，笑容如花儿般绽放。', '希望你以后能够做的比我还好呦。', prompt_speech_16k)
torchaudio.save('zero_shot.wav', output['tts_speech'], 22050)
# 跨语言使用
prompt_speech_16k = load_wav('cross_lingual_prompt.wav', 16000)
output = cosyvoice.inference_cross_lingual('And then later on, fully acquiring that company. So keeping management in line, interest in line with the asset that\'s coming into the family is a reason why sometimes we don\'t buy the whole thing.', prompt_speech_16k)
torchaudio.save('cross_lingual.wav', output['tts_speech'], 22050)

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-Instruct')
# instruct 使用，支持 <laughter></laughter><strong></strong>[laughter][breath]
output = cosyvoice.inference_instruct('在面对挑战时，他展现了非凡的<strong>勇气</strong>与<strong>智慧</strong>。', '中文男', 'Theo \'Crimson\', is a fiery, passionate rebel leader. Fights with fervor for justice, but struggles with impulsiveness.')
torchaudio.save('instruct.wav', output['tts_speech'], 22050)
```

### 启动 Web 演示

您可以使用我们的 Web 演示页面快速熟悉 CosyVoice。我们支持在 Web 演示中进行 sft/零样本/跨语言/instruct 推理。

详情请参见演示网站。

```python
# 对于 sft 推理，请更改为 iic/CosyVoice-300M-SFT，或对于 instruct 推理，请更改为 iic/CosyVoice-300M-Instruct
python3 webui.py --port 50000 --model_dir pretrained_models/CosyVoice-300M
```

### 高级使用

对于高级用户，我们在 examples/libritts/cosyvoice/run.sh 中提供了训练和推理脚本。您可以按照此配方熟悉 CosyVoice。

## 构建用于部署

可选地，如果您想使用 grpc 进行服务部署，可以运行以下步骤。否则，您可以忽略此步骤。

```python
cd runtime/python
docker build -t cosyvoice:v1.0 .
# 如果您想使用 instruct 推理，请更改为 iic/CosyVoice-300M-Instruct
# 对于 grpc 使用
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/grpc && python3 server.py --port 50000 --max_conc 4 --model_dir iic/CosyVoice-300M && sleep infinity"
python3 grpc/client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
# 对于 fastapi 使用
docker run -d --runtime=nvidia -p 50000:50000 cosyvoice:v1.0 /bin/bash -c "cd /opt/CosyVoice/CosyVoice/runtime/python/fastapi && MODEL_DIR=iic/CosyVoice-300M fastapi dev --port 50000 server.py && sleep infinity"
python3 fastapi/client.py --port 50000 --mode <sft|zero_shot|cross_lingual|instruct>
```

---

- [github](https://github.com/FunAudioLLM/CosyVoice)
- [online demo](https://www.modelscope.cn/studios/iic/CosyVoice-300M)
<!-- - [AI 博客 - 从零开始学AI](...) -->
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
