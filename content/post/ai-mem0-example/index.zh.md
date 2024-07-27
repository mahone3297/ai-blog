+++
title = '[AI Mem0] 结合Mem0编写有状态AI应用，让应用更智能、更个性化'
date = 2024-07-27T12:03:01+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = 'Mem0为您的应用程序带来革命性的AI体验，通过大型语言模型提供个性化、可靠且成本效益高的智能交互。无论是聊天机器人、虚拟助手还是AI代理，Mem0都能帮助您实现长期记忆和吸引人的用户体验。'
keywords = ['AI', 'Mem0', '大型语言模型', '个性化体验', '智能应用', '虚拟助手', '聊天机器人', '客户支持', '旅行助手', '个性化学习']
+++

## 要点

看下，如何结合 Mem0 编写 app

- memory 先 search
- 将 search 得到的 memory 附在 prompt 中发给 LLM
- 最后 memory add

---

## 概述
如何在现有应用程序中使用Mem0？

使用Mem0，你可以创建基于大型语言模型的有状态应用程序，如聊天机器人、虚拟助手或AI代理。Mem0通过提供一个记忆层来增强你的应用程序，使响应：

- 更加个性化
- 更加可靠
- 通过减少大型语言模型交互次数来降低成本
- 更加吸引人
- 支持长期记忆

## 示例
以下是一些关于如何将Mem0集成到各种应用程序中的示例：

### 个性化AI导师
您可以使用Mem0创建一个个性化的AI导师。本指南将引导您完成必要的步骤，并提供完整的代码以帮助您入门。

#### 概述
个性化AI导师利用Mem0在交互过程中保留信息，从而实现定制的学习体验。通过与OpenAI的GPT-4模型集成，导师可以为用户查询提供详细且具有上下文感知的响应。

#### 设置
在开始之前，请确保您已安装所需的依赖项。您可以使用pip安装必要的软件包：

```bash
pip install openai mem0ai
```

#### 完整代码示例
以下是使用Mem0创建和与个性化AI导师互动的完整代码：

```python
from openai import OpenAI
from mem0 import Memory
import os

# 设置OpenAI API密钥
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

# 初始化OpenAI客户端
client = OpenAI()

class PersonalAITutor:
    def __init__(self):
        """
        初始化PersonalAITutor，配置内存和OpenAI客户端。
        """
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333,
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.client = client
        self.app_id = "app-1"

    def ask(self, question, user_id=None):
        """
        向AI提问并将相关信息存储在内存中

        :param question: 提问的问题。
        :param user_id: 可选的用户ID，用于关联内存。
        """
        # 向AI发送一个流式聊天完成请求
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "你是一个个人AI导师。"},
                {"role": "user", "content": question}
            ]
        )
        # 将问题存储在内存中
        self.memory.add(question, user_id=user_id, metadata={"app_id": self.app_id})

        # 实时打印AI的响应
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        获取与给定用户ID关联的所有记忆。

        :param user_id: 可选的用户ID，用于过滤记忆。
        :return: 记忆列表。
        """
        return self.memory.get_all(user_id=user_id)

# 实例化PersonalAITutor
ai_tutor = PersonalAITutor()

# 定义一个用户ID
user_id = "从零开始学AI"

# 提问
ai_tutor.ask("我在学习计算机科学入门。什么是队列？简要说明。", user_id=user_id)
```

#### 获取记忆
您可以随时使用以下代码获取所有记忆：

```python
memories = ai_tutor.get_memories(user_id=user_id)
for m in memories:
    print(m['text'])
```

#### 关键点
- 初始化：PersonalAITutor类通过必要的内存配置和OpenAI客户端设置进行初始化。
- 提问：ask方法向AI发送问题，并将相关信息存储在内存中。
- 获取记忆：get_memories方法获取与用户关联的所有存储记忆。

#### 结论
随着对话的进行，Mem0的记忆会根据交互自动更新，提供持续改进的个性化学习体验。此设置确保AI导师能够提供上下文相关且准确的响应，增强整体教育过程。

### 客户支持AI代理
您可以使用Mem0创建一个个性化的客户支持AI代理。本指南将引导您完成必要的步骤，并提供完整的代码以帮助您入门。

#### 概述
客户支持AI代理利用Mem0在交互过程中保留信息，从而实现个性化和高效的支持体验。

#### 设置
使用pip安装必要的软件包：

```bash
pip install openai mem0ai
```

#### 完整代码示例
以下是使用Mem0创建和与客户支持AI代理互动的简化代码：

```python
from openai import OpenAI
from mem0 import Memory
import os

# 设置OpenAI API密钥
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

class CustomerSupportAIAgent:
    def __init__(self):
        """
        初始化CustomerSupportAIAgent，配置内存和OpenAI客户端。
        """
        config = {
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333,
                }
            },
        }
        self.memory = Memory.from_config(config)
        self.client = OpenAI()
        self.app_id = "customer-support"

    def handle_query(self, query, user_id=None):
        """
        处理客户查询并将相关信息存储在内存中。

        :param query: 处理的客户查询。
        :param user_id: 可选的用户ID，用于关联内存。
        """
        # 向AI发送一个流式聊天完成请求
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "你是一个客户支持AI代理。"},
                {"role": "user", "content": query}
            ]
        )
        # 将查询存储在内存中
        self.memory.add(query, user_id=user_id, metadata={"app_id": self.app_id})

        # 实时打印AI的响应
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        获取与给定客户ID关联的所有记忆。

        :param user_id: 可选的用户ID，用于过滤记忆。
        :return: 记忆列表。
        """
        return self.memory.get_all(user_id=user_id)

# 实例化CustomerSupportAIAgent
support_agent = CustomerSupportAIAgent()

# 定义一个客户ID
customer_id = "从零开始学AI"

# 处理客户查询
support_agent.handle_query("我需要帮助处理我的最近订单。它还没有到达。", user_id=customer_id)
```

#### 获取记忆
您可以随时使用以下代码获取所有记忆：

```python
memories = support_agent.get_memories(user_id=customer_id)
for m in memories:
    print(m['text'])
```

#### 关键点
- 初始化：CustomerSupportAIAgent类通过必要的内存配置和OpenAI客户端设置进行初始化。
- 处理查询：handle_query方法向AI发送查询，并将相关信息存储在内存中。
- 获取记忆：get_memories方法获取与客户关联的所有存储记忆。

#### 结论
随着对话的进行，Mem0的记忆会根据交互自动更新，提供持续改进的个性化支持体验。

### 个性化AI旅行助手
使用Mem0创建一个个性化AI旅行助手。本指南提供分步指导和完整的代码以帮助您开始。

#### 概述
个性化AI旅行助手使用Mem0在交互之间存储和检索信息，提供量身定制的旅行规划体验。它与OpenAI的GPT-4模型集成，以提供详细且具有上下文意识的用户查询响应。

#### 设置
使用pip安装所需的依赖项：

```bash
pip install openai mem0ai
```

#### 完整代码示例
以下是使用Mem0创建和与个性化AI旅行助手交互的完整代码：

```python
import os
from openai import OpenAI
from mem0 import Memory

# 设置OpenAI API密钥
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

class PersonalTravelAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.memory = Memory()
        self.messages = [{"role": "system", "content": "You are a personal AI Assistant."}]

    def ask_question(self, question, user_id):
        # 检索之前相关的记忆
        previous_memories = self.search_memories(question, user_id=user_id)
        prompt = question
        if previous_memories:
            prompt = f"用户输入：{question}\n 之前的记忆：{previous_memories}"
        self.messages.append({"role": "user", "content": prompt})

        # 使用GPT-4o生成响应
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})

        # 将问题存储在记忆中
        self.memory.add(question, user_id=user_id)
        return answer

    def get_memories(self, user_id):
        memories = self.memory.get_all(user_id=user_id)
        return [m['text'] for m in memories]

    def search_memories(self, query, user_id):
        memories = self.memory.search(query, user_id=user_id)
        return [m['text'] for m in memories]

# 使用示例
user_id = "从零开始学AI"
ai_assistant = PersonalTravelAssistant()

def main():
    while True:
        question = input("问题：")
        if question.lower() in ['q', 'exit']:
            print("退出...")
            break

        answer = ai_assistant.ask_question(question, user_id=user_id)
        print(f"答案：{answer}")
        memories = ai_assistant.get_memories(user_id=user_id)
        print("记忆：")
        for memory in memories:
            print(f"- {memory}")
        print("-----")

if __name__ == "__main__":
    main()
```

#### 关键组件
- 初始化：PersonalTravelAssistant类使用OpenAI客户端和Mem0记忆设置进行初始化。
- 提问：ask_question方法向AI发送问题，结合之前记忆，并存储新信息。
- 记忆管理：get_memories和search_memories方法处理存储记忆的检索和搜索。

#### 使用
- 在环境变量中设置您的OpenAI API密钥。
- 实例化PersonalTravelAssistant。
- 使用main()函数在循环中与助手交互。

#### 结论
这个个性化AI旅行助手利用Mem0的记忆能力提供具有上下文意识的响应。随着您与它的互动，助手学习和改进，提供越来越个性化的旅行建议和信息。

---

- [github](https://github.com/mem0ai/mem0)
- [doc](https://docs.mem0.ai/overview)
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/ai-mem0-example/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977681&idx=1&sn=dd5bff5a0827d0943f94b555e8c9a81d&chksm=86c7c994b1b04082b6987f42e50e0793f6222e0c72dda304455d862bff8908fa4d0a098bd5b6#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
