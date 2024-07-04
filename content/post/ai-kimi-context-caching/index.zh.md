+++
title = '[AI Kimi] Context Caching 正式公测，推动长文本模型降本 90%'
date = 2024-07-04T20:01:56+08:00
draft = false
categories = ['AI', 'Kimi']
tags = ['AI', 'Kimi', 'Context Caching']
description = "Kimi 的上下文缓存（Context Caching）技术正式公测。该技术通过预先存储数据，显著降低了计算成本和延迟，适用于长文本模型，帮助节省高达 90% 的费用，并将首 Token 延迟降低 83%。"
keywords = ["AI", "Kimi", "Context Caching", "数据管理", "降低成本"]
+++

Kimi 的上下文缓存（Context Caching）技术，开启了公测。我们一起来看下。

## 介绍

上下文缓存（Context Caching）是一种高效的数据管理技术，它允许系统预先存储那些可能会被频繁请求的大量数据或信息。这样，当您再次请求相同信息时，系统可以直接从缓存中快速提供，而无需重新计算或从原始数据源中检索，从而节省时间和资源。

## 效果

- 费用最高降低 90 %
- 首 Token 延迟降低 83%

## 快速开始

### 创建 cache

```python
from openai import OpenAI
import requests
import json

client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.cn/v1",
)

res = requests.post(
    url = "https://api.moonshot.cn/v1/caching",
    headers = {
        "Authorization": "Bearer $MOONSHOT_API_KEY"            
    },
    json = {
        "model": "moonshot-v1",
        "messages": [
            {
                "role": "system",
                "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"
            },
        ],
        "tools": [{
            "type": "function",
            "function": {
                "name": "CodeRunner",
                "description": "代码执行器，支持运行 python 和 javascript 代码",
                "parameters": {
                    "properties": {
                        "language": {
                            "type": "string",
                            "enum": ["python", "javascript"]
                        },
                        "code": {
                            "type": "string",
                            "description": "代码写在这里"
                        }
                    },
                    "type": "object"
                }
            }
        }],
        "name": "CodeRunner",
        "ttl": 3600
    }
)

print(json.loads(res.text))
```

返回

```json
{
	'id': 'cache-essqmysd6h1111dauub1',
	'object': 'context_cache_object',
	'model': 'moonshot-v1',
	'messages': [{
		'role': 'system',
		'content': '你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。'
	}],
	'tools': [{
		'function': {
			'name': 'CodeRunner',
			'description': '代码执行器，支持运行 python 和 javascript 代码',
			'parameters': {
				'properties': {
					'code': {
						'description': '代码写在这里',
						'type': 'string'
					},
					'language': {
						'enum': ['python', 'javascript'],
						'type': 'string'
					}
				},
				'type': 'object'
			}
		},
		'type': 'function'
	}],
	'name': 'CodeRunner',
	'description': '',
	'metadata': None,
	'expired_at': 1718847499,
	'status': 'pending',
	'tokens': 72
}
```

### 使用 cache

加 `role="cache"`

```python
from openai import OpenAI

client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url = "https://api.moonshot.cn/v1",
)

completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[  
        {
            "role": "cache",
            "content": "cache_id=cache-essqmysd6h1111dauub1;reset_ttl=3600",
        },
        {
            "role": "user",
            "content": "编程判断 3214567 是否是素数。",
        },
    ],
    temperature=0.3,
)

print(completion.choices[0].message)
```

返回

```plaintext
ChatCompletionMessage(content='判断一个数是否是素数，我们可以使用一个简单的算法：检查从2到该数的平方根之间的所有整数是否能整除该数。如果有一个能整除，那么这个数就不是素数。如果没有任何数能整除它，那么它就是素数。
对于给定的数3214567，我们可以编写一个程序来实现这个算法。下面是一个使用Python语言的示例代码：
import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

number_to_check = 3214567
print(is_prime(number_to_check))

这段代码定义了一个函数`is_prime`，它接受一个整数作为参数，并返回一个布尔值，表示这个数是否是素数。然后，我们使用这个函数来检查3214567是否是素数。', role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='CodeRunner:0', function=Function(arguments='{
    "code": "import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

number_to_check = 3214567
is_prime(number_to_check)
"
}', name='CodeRunner'), type='function', index=0)])
```

## 计费

- cache 资源费 = cache 创建费 + cache 存储费
- 一次调用收费 = Cache 调用收费+ Chat 未匹配 Cache 的 Input Tokens 收费 + Output Tokens 收费

具体详细价格看官方文档

[Caching - Moonshot AI 开放平台](https://platform.moonshot.cn/docs/price/caching)

---

- [「上下文缓存」正式公测，推动长文本模型降本 90%](https://mp.weixin.qq.com/s/72ubEn-6kHUVw34AzI4Pyg)
<!-- - [AI 博客 - 从零开始学AI](...) -->
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
