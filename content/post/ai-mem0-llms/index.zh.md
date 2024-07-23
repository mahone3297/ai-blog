+++
title = '[AI Mem0] 大模型：一站式集成多种顶级AI模型，提升工作效率'
date = 2024-07-23T09:38:35+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = 'Mem0支持多种顶级大型语言模型，包括OpenAI、Groq、Together、AWS Bedrock等，让您轻松集成最适合需求的AI模型，提升工作效率和智能化水平。'
keywords = ['AI', 'Mem0', '大型语言模型', 'LLM', 'OpenAI', 'Groq', 'Together', 'AWS Bedrock', 'Litellm', 'Google AI', 'Anthropic', 'Mistral AI', 'OpenAI Azure']
+++

## 概览
Mem0 内置了对多种流行的大型语言模型的支持。它可以利用用户提供的大型语言模型，确保针对特定需求的高效使用。

- OpenAI
- Groq
- Together
- AWS Bedrock
- Litellm
- Google AI
- Anthropic
- Mistral AI
- OpenAI Azure

## OpenAI
```python
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o",
            "temperature": 0.2,
            "max_tokens": 1500,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## Groq
```python
import os
from mem0 import Memory

os.environ["GROQ_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "groq",
        "config": {
            "model": "mixtral-8x7b-32768",
            "temperature": 0.1,
            "max_tokens": 1000,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## Together
```python
import os
from mem0 import Memory

os.environ["TOGETHER_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "togetherai",
        "config": {
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "temperature": 0.2,
            "max_tokens": 1500,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## AWS Bedrock
```python
import os
from mem0 import Memory

os.environ['AWS_REGION'] = 'us-east-1'
os.environ["AWS_ACCESS_KEY"] = "xx"
os.environ["AWS_SECRET_ACCESS_KEY"] = "xx"

config = {
    "llm": {
        "provider": "aws_bedrock",
        "config": {
            "model": "arn:aws:bedrock:us-east-1:123456789012:model/your-model-name",
            "temperature": 0.2,
            "max_tokens": 1500,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## Litellm
```python
import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "litellm",
        "config": {
            "model": "gpt-3.5-turbo",
            "temperature": 0.2,
            "max_tokens": 1500,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## Google AI
```python
import os
from mem0 import Memory

os.environ["GEMINI_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "litellm",
        "config": {
            "model": "gemini/gemini-pro",
            "temperature": 0.2,
            "max_tokens": 1500,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## Anthropic
```python
import os
from mem0 import Memory

os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "litellm",
        "config": {
            "model": "claude-3-opus-20240229",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## Mistral AI
```python
import os
from mem0 import Memory

os.environ["MISTRAL_API_KEY"] = "your-api-key"

config = {
    "llm": {
        "provider": "litellm",
        "config": {
            "model": "open-mixtral-8x7b",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

## OpenAI Azure
```python
import os
from mem0 import Memory

os.environ["AZURE_API_KEY"] = "your-api-key"

# Needed to use custom models
os.environ["AZURE_API_BASE"] = "your-api-base-url"
os.environ["AZURE_API_VERSION"] = "version-to-use"

config = {
    "llm": {
        "provider": "litellm",
        "config": {
            "model": "azure_ai/command-r-plus",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)
m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
```

---

- [github](https://github.com/mem0ai/mem0)
- [doc](https://docs.mem0.ai/overview)
<!-- - [AI 博客 - 从零开始学AI](...) -->
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
