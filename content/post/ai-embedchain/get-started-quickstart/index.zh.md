+++
title = '[AI Embedchain] 开始使用 - 快速开始'
date = 2024-08-04T20:22:17+08:00
draft = false
categories = ['AI', 'Embedchain']
tags = ['AI', 'Embedchain']
description = ''
keywords = ['从零开始学AI']
+++

## 安装

首先安装 Python 包：

```bash
pip install embedchain
```

安装包后，根据您的偏好，您可以选择使用以下内容：

## 开源模型

本节提供了一个快速入门示例，展示了如何使用 Mistral 作为开源 LLM（大型语言模型）和 Sentence transformers 作为开源嵌入模型。这些模型是免费的，并且主要在您的本地机器上运行。

我们使用的是在 Hugging Face 上托管的 Mistral，因此您需要一个 Hugging Face 令牌来运行此示例。它是 *免费* 的，您可以在此处创建一个 [here](https://huggingface.co/docs/hub/security-tokens)。

```python
import os
# 将此行替换为您的 HF 令牌
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "hf_xxxx"

from embedchain import App

config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.2',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  }
}
app = App.from_config(config=config)
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
app.query("What is the net worth of Elon Musk today?")
# 回答：Elon Musk 今天的净资产是 2587 亿美元。
```

## 付费模型

在本节中，我们将使用来自 OpenAI 的 LLM 和嵌入模型。

```python
import os
from embedchain import App

# 将此行替换为您的 OpenAI 密钥
os.environ["OPENAI_API_KEY"] = "sk-xxxx"

app = App()
app.add("https://www.forbes.com/profile/elon-musk")
app.add("https://en.wikipedia.org/wiki/Elon_Musk")
app.query("What is the net worth of Elon Musk today?")
# 回答：Elon Musk 今天的净资产是 2587 亿美元。
```

## 引用

- [github](https://github.com/mem0ai/mem0/tree/main/embedchain)
- [doc](https://docs.embedchain.ai/)
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/)
