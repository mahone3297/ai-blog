+++
title = "[AI Mem0] Quick Start: Intelligent Memory Management to Bring Your Data to Life!"
date = 2024-07-22T07:58:30+08:00
draft = false
categories = ["AI", "Mem0"]
tags = ["AI", "Mem0"]
description = "A comprehensive guide on how to install, initialize, and use AI Mem0 for CRUD operations, covering everything from basic to advanced configurations."
keywords = ["AI", "Mem0", "quick start", "intelligent memory", "installation", "initialization", "usage guide"]
+++

- [[AI Mem0] Overview: Intelligent Self-Improving Memory Layer](https://ai-blog.aihub2022.top/zh/post/ai-mem0-intro/)

Previously, we introduced an overview. Today, let's take a look at the quick start.

It's straightforward, basically just CRUD.

---

## Installation
```bash
pip install mem0ai
```

## Basic Usage
### Initialization
#### Basic
```python
from mem0 import Memory
m = Memory()
```

#### Advanced
If used in a production environment, as follows

Run qdrant service
```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```

Initialization
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

### Add
```python
# For a user
result = m.add("Likes to play cricket on weekends", user_id="alice", metadata={"category": "hobbies"})
print(result)
```

Output
```json
[
  {
    'id': 'm1',
    'event': 'add',
    'data': 'Likes to play cricket on weekends'
  }
]
```

### Get
```python
# Get all memories
all_memories = m.get_all()
print(all_memories)
```

Output
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

Output
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

### Search
```python
related_memories = m.search(query="What are Alice's hobbies?", user_id="alice")
print(related_memories)
```

Output
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

### Update
```python
result = m.update(memory_id="m1", data="Likes to play tennis on weekends")
print(result)
```

Output
```json
{
  'id': 'm1',
  'event': 'update',
  'data': 'Likes to play tennis on weekends'
}
```

### History
```python
history = m.history(memory_id="m1")
print(history)
```

Output
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

### Delete
```python
m.delete(memory_id="m1") # Delete a memory

m.delete_all(user_id="alice") # Delete all memories
```

### Reset
```python
m.reset() # Reset all memories
```

---

- [GitHub](https://github.com/mem0ai/mem0)
- [Documentation](https://docs.mem0.ai/overview)
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [Official WeChat Account - Learn AI from scratch](...) -->
<!-- - [CSDN - Learn AI from scratch](...) -->
<!-- - [Juejin - Learn AI from scratch](...) -->
<!-- - [Zhihu - Learn AI from scratch](...) -->
<!-- - [Alibaba Cloud - Learn AI from scratch](...) -->
<!-- - [Tencent Cloud - Learn AI from scratch](...) -->
