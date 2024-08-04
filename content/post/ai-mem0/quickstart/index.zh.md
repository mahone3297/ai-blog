+++
title = '[AI Mem0] 快速开始：智能记忆管理，让你的数据活起来！'
date = 2024-07-22T07:58:30+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = "了解如何安装、初始化和使用 AI Mem0 进行增删查改的全面指南，从基础到高级配置，全面覆盖。"
keywords = ["AI", "Mem0", "快速入门", "智能记忆", "安装", "初始化", "使用指南"]
+++

- [[AI Mem0] 概览，智能自我改进记忆层](https://ai-blog.aihub2022.top/zh/post/ai-mem0-intro/)

之前介绍了一下概览，今天来看下快速开始

很简单，基本上就是CRUD

---

## 安装
```bash
pip install mem0ai
```

## 基本使用
### 初始化
#### 基础
```python
from mem0 import Memory
m = Memory()
```

#### 高级
如果是在生产环境使用，如下

运行 qdrant 服务
```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

初始化
```python
from mem0 import Memory

config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    },
}

m = Memory.from_config(config)
```

### 添加
```python
# For a user
result = m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
print(result)
```

输出
```json
[
  {
    'id': 'm1',
    'event': 'add',
    'data': 'Likes to play cricket on weekends'
  }
]
```

### 获取
```python
# Get all memories
all_memories = m.get_all()
print(all_memories)
```

输出
```json
[
  {
    'id': 'm1',
    'text': 'Likes to play cricket on weekends',
    'metadata': {
      'data': 'Likes to play cricket on weekends',
      'category': 'hobbies'
    }
  },
  # ... other memories ...
]
```

```python
# Get a single memory by ID
specific_memory = m.get("m1")
print(specific_memory)
```

输出
```json
{
  'id': 'm1',
  'text': 'Likes to play cricket on weekends',
  'metadata': {
    'data': 'Likes to play cricket on weekends',
    'category': 'hobbies'
  }
}
```

### 搜索
```python
related_memories = m.search(query="What are Alice's hobbies?", user_id="alice")
print(related_memories)
```

输出
```json
[
  {
    'id': 'm1',
    'text': 'Likes to play cricket on weekends',
    'metadata': {
      'data': 'Likes to play cricket on weekends',
      'category': 'hobbies'
    },
    'score': 0.85  # Similarity score
  },
  # ... other related memories ...
]
```

### 更新
```python
result = m.update(memory_id="m1", data="Likes to play tennis on weekends")
print(result)
```

输出
```json
{
  'id': 'm1',
  'event': 'update',
  'data': 'Likes to play tennis on weekends'
}
```

### 历史
```python
history = m.history(memory_id="m1")
print(history)
```

输出
```json
[
  {
    'id': 'h1',
    'memory_id': 'm1',
    'prev_value': None,
    'new_value': 'Likes to play cricket on weekends',
    'event': 'add',
    'timestamp': '2024-07-14 10:00:54.466687',
    'is_deleted': 0
  },
  {
    'id': 'h2',
    'memory_id': 'm1',
    'prev_value': 'Likes to play cricket on weekends',
    'new_value': 'Likes to play tennis on weekends',
    'event': 'update',
    'timestamp': '2024-07-14 10:15:17.230943',
    'is_deleted': 0
  }
]
```

### 删除
```python
m.delete(memory_id="m1") # Delete a memory

m.delete_all(user_id="alice") # Delete all memories
```

### 重置
```python
m.reset() # Reset all memories
```

---

- [github](https://github.com/mem0ai/mem0)
- [doc](https://docs.mem0.ai/overview)
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/ai-mem0-quickstart/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977645&idx=1&sn=2de802cc56cae6f79481f5ceb74944d3&chksm=86c7c9e8b1b040fe565554375bb32407e4da1cd5d63994650904486f0f469de43f6b0e5a7260#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
