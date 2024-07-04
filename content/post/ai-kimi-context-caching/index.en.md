+++
title = '[AI Kimi] Context Caching Public Beta, Reducing Long Text Model Costs by 90%'
date = 2024-07-04T20:01:56+08:00
draft = false
categories = ['AI', 'Kimi']
tags = ['AI', 'Kimi', 'Context Caching']
description = "Kimi's Context Caching technology is now in public beta. This technology pre-stores data to significantly reduce computing costs and latency, suitable for long text models, helping to save up to 90% of costs and reduce first token latency by 83%."
keywords = ["AI", "Kimi", "Context Caching", "Data Management", "Cost Reduction"]
+++

Kimi's Context Caching technology is now in public beta. Let's take a look.

## Introduction

Context Caching is an efficient data management technique that allows the system to pre-store a large amount of data or information that may be frequently requested. This way, when you request the same information again, the system can quickly provide it from the cache without recalculating or retrieving it from the original data source, thus saving time and resources.

## Effects

- Costs reduced by up to 90%
- First token latency reduced by 83%

## Quick Start

### Create Cache

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
                "content": "You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in both Chinese and English conversations. You will provide users with safe, helpful, and accurate answers. At the same time, you will refuse to answer any questions related to terrorism, racial discrimination, explicit content, or violence. Moonshot AI is a proprietary term and cannot be translated into other languages."
            },
        ],
        "tools": [{
            "type": "function",
            "function": {
                "name": "CodeRunner",
                "description": "Code executor that supports running python and javascript code",
                "parameters": {
                    "properties": {
                        "language": {
                            "type": "string",
                            "enum": ["python", "javascript"]
                        },
                        "code": {
                            "type": "string",
                            "description": "Code goes here"
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

Response

```json
{
	'id': 'cache-essqmysd6h1111dauub1',
	'object': 'context_cache_object',
	'model': 'moonshot-v1',
	'messages': [{
		'role': 'system',
		'content': 'You are Kimi, an AI assistant provided by Moonshot AI. You are proficient in both Chinese and English conversations. You will provide users with safe, helpful, and accurate answers. At the same time, you will refuse to answer any questions related to terrorism, racial discrimination, explicit content, or violence. Moonshot AI is a proprietary term and cannot be translated into other languages.'
	}],
	'tools': [{
		'function': {
			'name': 'CodeRunner',
			'description': 'Code executor that supports running python and javascript code',
			'parameters': {
				'properties': {
					'code': {
						'description': 'Code goes here',
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

### Use Cache

Add `role="cache"`

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
            "content": "Write a program to determine if 3214567 is a prime number.",
        },
    ],
    temperature=0.3,
)

print(completion.choices[0].message)
```

Response

```plaintext
ChatCompletionMessage(content='To determine if a number is a prime number, we can use a simple algorithm: check all integers from 2 to the square root of the number to see if any of them can divide the number evenly. If one can, then the number is not a prime number. If none can, then it is a prime number.
For the given number 3214567, we can write a program to implement this algorithm. Here is an example code using Python:
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

This code defines a function `is_prime` that takes an integer as an argument and returns a boolean value indicating whether the number is a prime number. Then, we use this function to check if 3214567 is a prime number.', role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='CodeRunner:0', function=Function(arguments='{
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

## Pricing

- Cache resource fee = cache creation fee + cache storage fee
- One call fee = Cache call fee + Chat unmatched Cache input tokens fee + Output tokens fee

For detailed pricing, refer to the official documentation

[Caching - Moonshot AI Platform](https://platform.moonshot.cn/docs/price/caching)

---

- [「上下文缓存」正式公测，推动长文本模型降本 90%](https://mp.weixin.qq.com/s/72ubEn-6kHUVw34AzI4Pyg)
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
