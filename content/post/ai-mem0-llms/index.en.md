+++
title = '[AI Mem0] Large Language Models: One-stop Integration of Multiple Top AI Models to Boost Efficiency'
date = 2024-07-23T09:38:35+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = 'Mem0 supports multiple top large language models, including OpenAI, Groq, Together, AWS Bedrock, and more, allowing you to easily integrate the AI models that best suit your needs, enhancing work efficiency and intelligent capabilities.'
keywords = ['AI', 'Mem0', 'Large Language Models', 'LLM', 'OpenAI', 'Groq', 'Together', 'AWS Bedrock', 'Litellm', 'Google AI', 'Anthropic', 'Mistral AI', 'OpenAI Azure']
+++

## Overview
Mem0 comes with built-in support for various popular large language models. It can leverage the large language models provided by the user, ensuring efficient use for specific needs.

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
- [AI Blog - Learn AI from scratch](https://ai-blog.aihub2022.top/post/ai-mem0-llms/)
<!-- - [WeChat - Learn AI from scratch](...) -->
<!-- - [CSDN - Learn AI from scratch](...) -->
<!-- - [Juejin - Learn AI from scratch](...) -->
<!-- - [Zhihu - Learn AI from scratch](...) -->
<!-- - [Aliyun - Learn AI from scratch](...) -->
