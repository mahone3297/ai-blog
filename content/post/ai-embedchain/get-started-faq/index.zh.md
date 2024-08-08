+++
title = '[AI Embedchain] 开始使用 - 常见问题解答'
date = 2024-08-08T06:41:53+08:00
draft = false
categories = ['AI', 'Embedchain']
tags = ['AI', 'Embedchain']
description = ''
keywords = ['从零开始学AI']
+++

### Embedchain 支持 OpenAI 的 Assistant API 吗？
是的，支持。请参考 [OpenAI Assistant 文档页面](/examples/openai-assistant)。

### 如何使用 MistralAI 语言模型？
使用 Hugging Face 提供的模型：`mistralai/Mistral-7B-v0.1`

```python main.py
import os
from embedchain import App

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "hf_your_token"

app = App.from_config("huggingface.yaml")
```

```yaml huggingface.yaml
llm:
  provider: huggingface
  config:
    model: 'mistralai/Mistral-7B-v0.1'
    temperature: 0.5
    max_tokens: 1000
    top_p: 0.5
    stream: false

embedder:
  provider: huggingface
  config:
    model: 'sentence-transformers/all-mpnet-base-v2'
```

### 如何使用 OpenAI DevDay 发布的 ChatGPT 4 turbo 模型？
使用 OpenAI 提供的模型 `gpt-4-turbo`。

```python main.py
import os
from embedchain import App

os.environ['OPENAI_API_KEY'] = 'xxx'

# 从 gpt4_turbo.yaml 文件加载 llm 配置
app = App.from_config(config_path="gpt4_turbo.yaml")
```

```yaml gpt4_turbo.yaml
llm:
  provider: openai
  config:
    model: 'gpt-4-turbo'
    temperature: 0.5
    max_tokens: 1000
    top_p: 1
    stream: false
```

### 如何将 GPT-4 用作 LLM 模型？
```python main.py
import os
from embedchain import App

os.environ['OPENAI_API_KEY'] = 'xxx'

# 从 gpt4.yaml 文件加载 llm 配置
app = App.from_config(config_path="gpt4.yaml")
```

```yaml gpt4.yaml
llm:
  provider: openai
  config:
    model: 'gpt-4'
    temperature: 0.5
    max_tokens: 1000
    top_p: 1
    stream: false
```

### 我没有 OpenAI 积分，如何使用一些开源模型？
```python main.py
from embedchain import App

# 从 opensource.yaml 文件加载 llm 配置
app = App.from_config(config_path="opensource.yaml")
```

```yaml opensource.yaml
llm:
  provider: gpt4all
  config:
    model: 'orca-mini-3b-gguf2-q4_0.gguf'
    temperature: 0.5
    max_tokens: 1000
    top_p: 1
    stream: false

embedder:
  provider: gpt4all
  config:
    model: 'all-MiniLM-L6-v2'
```

### 在 Embedchain 中使用 OpenAI 模型时如何流式响应？
可以通过在配置文件中将 `stream` 设置为 `true` 来实现。

```yaml openai.yaml
llm:
  provider: openai
  config:
    model: 'gpt-3.5-turbo'
    temperature: 0.5
    max_tokens: 1000
    top_p: 1
    stream: true
```

```python main.py
import os
from embedchain import App

os.environ['OPENAI_API_KEY'] = 'sk-xxx'

app = App.from_config(config_path="openai.yaml")

app.add("https://www.forbes.com/profile/elon-musk")

response = app.query("Elon Musk 的净资产是多少？")
# 响应将随着生成在 stdout 中流式传输。
```

### 如何在多个应用程序会话中持久化数据？
通过在配置文件中添加一个 `id` 来设置应用程序，这样可以保留数据以供将来使用。您可以将这个 `id` 包含在 yaml 配置中，或者直接在 `config` 字典中输入。

```python app1.py
import os
from embedchain import App

os.environ['OPENAI_API_KEY'] = 'sk-xxx'

app1 = App.from_config(config={
    "app": {
      "config": {
        "id": "your-app-id",
      }
    }
})

app1.add("https://www.forbes.com/profile/elon-musk")

response = app1.query("Elon Musk 的净资产是多少？")
```

```python app2.py
import os
from embedchain import App

os.environ['OPENAI_API_KEY'] = 'sk-xxx'

app2 = App.from_config(config={
    "app": {
      "config": {
        # 这将持久化并从 app1 会话加载数据
        "id": "your-app-id",
      }
    }
})

response = app2.query("Elon Musk 的净资产是多少？")
```

## 引用

- [github](https://github.com/mem0ai/mem0/tree/main/embedchain)
- [doc](https://docs.embedchain.ai/)
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977720&idx=1&sn=ec729d1dfe571fcd928c0d0f1ef8d5a1&chksm=86c7c9bdb1b040abce8bc499539725bc04ae1ed1ce7bf2d20e7e9a2df11c828ac67c42ace601#rd)
