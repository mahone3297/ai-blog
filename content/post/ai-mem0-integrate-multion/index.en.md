+++
title = '[AI Mem0 MultiOn] Integrating Mem0 with MultiOn for Efficient Automated Web Tasks'
date = 2024-07-25T10:14:42+08:00
draft = false
categories = ['AI', 'Mem0', 'MultiOn']
tags = ['AI', 'Mem0', 'MultiOn']
description = 'Learn how to create a personalized browser agent that remembers user preferences and automates web tasks using Mem0 and MultiOn. This article provides detailed setup, configuration, and operational steps.'
keywords = ['AI', 'Mem0', 'MultiOn', 'Automation', 'Browser Agent', 'Personalization']
+++

Let's look at an example of integrating Mem0 with MultiOn.

---

Build a personal browser agent that remembers user preferences and automates web tasks. It integrates Mem0 for memory management and MultiOn for executing browser actions, enabling personalized and efficient web interactions.

## Overview
In this example, we will create a browser-based AI agent to search arxiv.org for research papers relevant to the user's research interests.

## Setup and Configuration
Install necessary libraries:

```bash
pip install mem0ai multion
```

First, we'll import the necessary libraries and set up our configurations.

```python
import os
from mem0 import Memory
from multion.client import MultiOn

# Configuration
OPENAI_API_KEY = 'sk-xxx'  # Replace with your actual OpenAI API key
MULTION_API_KEY = 'your-multion-key'  # Replace with your actual MultiOn API key
USER_ID = "Learn AI from Scratch"

# Set up OpenAI API key
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Initialize Mem0 and MultiOn
memory = Memory()
multion = MultiOn(api_key=MULTION_API_KEY)
```

## Adding Memories to Mem0
Next, we'll define our user data and add it to Mem0.

```python
# Define user data
USER_DATA = """
About me
- I am the host of the WeChat official account 'Learn AI from Scratch'
- I am interested in AI and ML infrastructure
"""

# Add user data to memory
memory.add(USER_DATA, user_id=USER_ID)
print("User data added to memory.")
```

## Retrieving Relevant Memories
Now, we'll define our search command and retrieve relevant memories from Mem0.

```python
# Define search command and retrieve relevant memories
command = "Find arxiv papers I should read based on my interests."

relevant_memories = memory.search(command, user_id=USER_ID, limit=3)
relevant_memories_text = '\n'.join(mem['text'] for mem in relevant_memories)
print(f"Relevant memories:")
print(relevant_memories_text)
```

## Browsing arXiv
Finally, we'll use MultiOn to browse arXiv based on our command and relevant memories.

```python
# Create prompt and browse arXiv
prompt = f"{command}\n My past memories: {relevant_memories_text}"
browse_result = multion.browse(cmd=prompt, url="https://arxiv.org/")
print(browse_result)
```

## Conclusion
By integrating Mem0 with MultiOn, you have created a personalized browser agent that remembers user preferences and automates web tasks. For more details and advanced usage, refer to the full manual.

---

## Summary
From the above example, we can see how to use Mem0. Basically, it's about CRUD operations and searching in Mem0. When requesting the LLM, include the memory retrieved from the search and send it along with the request.

Later, we will look at the implementation of Mem0 together and see how to achieve CRUD and search.

---

- [github](https://github.com/mem0ai/mem0)
- [doc](https://docs.mem0.ai/overview)
<!-- - [AI Blog - Learn AI from Scratch](...) -->
<!-- - [WeChat Official Account - Learn AI from Scratch](...) -->
<!-- - [CSDN - Learn AI from Scratch](...) -->
<!-- - [Juejin - Learn AI from Scratch](...) -->
<!-- - [Zhihu - Learn AI from Scratch](...) -->
<!-- - [Alibaba Cloud - Learn AI from Scratch](...) -->
<!-- - [Tencent Cloud - Learn AI from Scratch](...) -->
