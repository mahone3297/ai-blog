+++
title = '[AI Mem0] 源码解读，带你了解 Mem0 的实现'
date = 2024-07-30T13:48:31+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = "本文将深入解析 Mem0 的源码，带你全面了解其实现原理和具体使用方法，助你更好地应用这款强大的 AI 工具。"
keywords = ["AI", "Mem0", "源码解析", "教程", "机器学习", "深度学习", "人工智能"]
+++

## 使用

先来看下，如何 Mem0 的使用

```python
import os
os.environ["OPENAI_API_KEY"] = "sk-xxx"

from mem0 import Memory

m = Memory()

# 1. Add: Store a memory from any unstructured text
result = m.add("I am working on improving my tennis skills. Suggest some online courses.", user_id="alice", metadata={"category": "hobbies"})

# Created memory --> 'Improving her tennis skills.' and 'Looking for online suggestions.'

# 2. Update: update the memory
result = m.update(memory_id=<memory_id_1>, data="Likes to play tennis on weekends")

# Updated memory --> 'Likes to play tennis on weekends.' and 'Looking for online suggestions.'

# 3. Search: search related memories
related_memories = m.search(query="What are Alice's hobbies?", user_id="alice")

# Retrieved memory --> 'Likes to play tennis on weekends'

# 4. Get all memories
all_memories = m.get_all()
memory_id = all_memories[0]["id"] # get a memory_id

# All memory items --> 'Likes to play tennis on weekends.' and 'Looking for online suggestions.'

# 5. Get memory history for a particular memory_id
history = m.history(memory_id=<memory_id_1>)

# Logs corresponding to memory_id_1 --> {'prev_value': 'Working on improving tennis skills and interested in online courses for tennis.', 'new_value': 'Likes to play tennis on weekends' }
```

## MemoryBase

Mem0 的 CRUD 到底是如何实现的？我们来看下源码。

MemoryBase 是一个抽象类，定义了一些接口方法

- get
- get_all
- update
- delete
- history

```python
class MemoryBase(ABC):
    @abstractmethod
    def get(self, memory_id):
        """
        Retrieve a memory by ID.

        Args:
            memory_id (str): ID of the memory to retrieve.

        Returns:
            dict: Retrieved memory.
        """
        pass

    @abstractmethod
    def get_all(self):
        """
        List all memories.

        Returns:
            list: List of all memories.
        """
        pass

    @abstractmethod
    def update(self, memory_id, data):
        """
        Update a memory by ID.

        Args:
            memory_id (str): ID of the memory to update.
            data (dict): Data to update the memory with.

        Returns:
            dict: Updated memory.
        """
        pass

    @abstractmethod
    def delete(self, memory_id):
        """
        Delete a memory by ID.

        Args:
            memory_id (str): ID of the memory to delete.
        """
        pass

    @abstractmethod
    def history(self, memory_id):
        """
        Get the history of changes for a memory by ID.

        Args:
            memory_id (str): ID of the memory to get history for.

        Returns:
            list: List of changes for the memory.
        """
        pass
```

## Memory

Memory 实现 MemoryBase 接口

```python
class Memory(MemoryBase):
```

### init

```python
    def __init__(self, config: MemoryConfig = MemoryConfig()):
        self.config = config
        self.embedding_model = EmbedderFactory.create(self.config.embedder.provider)
        # Initialize the appropriate vector store based on the configuration
        vector_store_config = self.config.vector_store.config
        if self.config.vector_store.provider == "qdrant":
            self.vector_store = Qdrant(
                host=vector_store_config.host,
                port=vector_store_config.port,
                path=vector_store_config.path,
                url=vector_store_config.url,
                api_key=vector_store_config.api_key,
            )
        else:
            raise ValueError(
                f"Unsupported vector store type: {self.config.vector_store_type}"
            )

        self.llm = LlmFactory.create(self.config.llm.provider, self.config.llm.config)
        self.db = SQLiteManager(self.config.history_db_path)
        self.collection_name = self.config.collection_name
        self.vector_store.create_col(
            name=self.collection_name, vector_size=self.embedding_model.dims
        )
        self.vector_store.create_col(
            name=self.collection_name, vector_size=self.embedding_model.dims
        )
        capture_event("mem0.init", self)
```

初始化 embedding_model, vector_store(这里只能是 Qdrant), llm, db, collection_name

### add

```python
    def add(
        self,
        data,
        user_id=None,
        agent_id=None,
        run_id=None,
        metadata=None,
        filters=None,
        prompt=None,
    ):
        """
        Create a new memory.

        Args:
            data (str): Data to store in the memory.
            user_id (str, optional): ID of the user creating the memory. Defaults to None.
            agent_id (str, optional): ID of the agent creating the memory. Defaults to None.
            run_id (str, optional): ID of the run creating the memory. Defaults to None.
            metadata (dict, optional): Metadata to store with the memory. Defaults to None.
            filters (dict, optional): Filters to apply to the search. Defaults to None.

        Returns:
            str: ID of the created memory.
        """
```

- 将用户 data 发给 llm ，得到 extracted_memories
- 将用户 data 转成 embeddings
- vector_store 根据 embeddings search 得到 existing_memories
- 将新，老 memory 发给 llm 来 merge
- 调用函数 _create_memory_tool 进行实际操作
    - vector_store insert
    - db add_history

### get

```python
    def get(self, memory_id):
        """
        Retrieve a memory by ID.

        Args:
            memory_id (str): ID of the memory to retrieve.

        Returns:
            dict: Retrieved memory.
        """
```

- vector_store 根据 memory_id 去 get

### get_all

```python
    def get_all(self, user_id=None, agent_id=None, run_id=None, limit=100):
        """
        List all memories.

        Returns:
            list: List of all memories.
        """
```

- vector_store 根据 collection_name, filters, limit 调用 list 接口

### search

```python
    def search(
        self, query, user_id=None, agent_id=None, run_id=None, limit=100, filters=None
    ):
        """
        Search for memories.

        Args:
            query (str): Query to search for.
            user_id (str, optional): ID of the user to search for. Defaults to None.
            agent_id (str, optional): ID of the agent to search for. Defaults to None.
            run_id (str, optional): ID of the run to search for. Defaults to None.
            limit (int, optional): Limit the number of results. Defaults to 100.
            filters (dict, optional): Filters to apply to the search. Defaults to None.

        Returns:
            list: List of search results.
        """
```

- embedding_model 将 query 转 embeddings
- vector_store 根据 embeddings search

### update

```python
    def update(self, memory_id, data):
        """
        Update a memory by ID.

        Args:
            memory_id (str): ID of the memory to update.
            data (dict): Data to update the memory with.

        Returns:
            dict: Updated memory.
        """
```

- 调用 _update_memory_tool
    - existing_memory = self.vector_store.get
    - embeddings = self.embedding_model.embed(data)
    - self.vector_store.update
    - self.db.add_history

### delete

```python
    def delete(self, memory_id):
        """
        Delete a memory by ID.

        Args:
            memory_id (str): ID of the memory to delete.
        """
```

- 调用 _delete_memory_tool
    - existing_memory = self.vector_store.get
    - self.vector_store.delete
    - self.db.add_history

### delete_all

```python
    def delete_all(self, user_id=None, agent_id=None, run_id=None):
        """
        Delete all memories.

        Args:
            user_id (str, optional): ID of the user to delete memories for. Defaults to None.
            agent_id (str, optional): ID of the agent to delete memories for. Defaults to None.
            run_id (str, optional): ID of the run to delete memories for. Defaults to None.
        """
```

- memories = self.vector_store.list
- foreach memories
    - _delete_memory_tool

### history

```python
    def history(self, memory_id):
        """
        Get the history of changes for a memory by ID.

        Args:
            memory_id (str): ID of the memory to get history for.

        Returns:
            list: List of changes for the memory.
        """
```

- self.db.get_history

### reset

```python
    def reset(self):
        """
        Reset the memory store.
        """
```

- self.vector_store.delete_col
- self.db.reset()

## AnonymousTelemetry

- capture_event 收集信息
- telemetry 用的是 Posthog(https://us.i.posthog.com)

## SQLiteManager

- db 用的是 sqlite3
- 一个记录历史的表

```sql
CREATE TABLE IF NOT EXISTS history (
    id TEXT PRIMARY KEY,
    memory_id TEXT,
    prev_value TEXT,
    new_value TEXT,
    event TEXT,
    timestamp DATETIME,
    is_deleted INTEGER
)
```

## MemoryClient

```python
class MemoryClient:
    """Client for interacting with the Mem0 API.

    This class provides methods to create, retrieve, search, and delete memories
    using the Mem0 API.

    Attributes:
        api_key (str): The API key for authenticating with the Mem0 API.
        host (str): The base URL for the Mem0 API.
        client (httpx.Client): The HTTP client used for making API requests.
    """
```

- 主要用于跟平台(https://api.mem0.ai/v1)交互
- 接口
    - add
    - get
    - get_all
    - search
    - delete
    - delete_all
    - history
    - reset

## Embedding

```python
class EmbeddingBase(ABC):
    @abstractmethod
    def embed(self, text):
        """
        Get the embedding for the given text.

        Args:
            text (str): The text to embed.

        Returns:
            list: The embedding vector.
        """
        pass
```

- HuggingFaceEmbedding(model_name="multi-qa-MiniLM-L6-cos-v1")
- Ollama(model="nomic-embed-text")
- OpenAI(model="text-embedding-3-small")

## LLM

```python
class LLMBase(ABC):
    def __init__(self, config: Optional[BaseLlmConfig] = None):
        """Initialize a base LLM class

        :param config: LLM configuration option class, defaults to None
        :type config: Optional[BaseLlmConfig], optional
        """
        if config is None:
            self.config = BaseLlmConfig()
        else:
            self.config = config

    @abstractmethod
    def generate_response(self, messages):
        """
        Generate a response based on the given messages.

        Args:
            messages (list): List of message dicts containing 'role' and 'content'.

        Returns:
            str: The generated response.
        """
        pass
```

- AWSBedrockLLM(anthropic.claude-3-5-sonnet-20240620-v1:0)
- GroqLLM(llama3-70b-8192)
- LiteLLM(gpt-4o)
- OllamaLLM(llama3)
- OpenAILLM(gpt-4o)
- TogetherLLM(mistralai/Mixtral-8x7B-Instruct-v0.1)

## VectorStore

```python
class VectorStoreBase(ABC):
    @abstractmethod
    def create_col(self, name, vector_size, distance):
        """Create a new collection."""
        pass

    @abstractmethod
    def insert(self, name, vectors, payloads=None, ids=None):
        """Insert vectors into a collection."""
        pass

    @abstractmethod
    def search(self, name, query, limit=5, filters=None):
        """Search for similar vectors."""
        pass

    @abstractmethod
    def delete(self, name, vector_id):
        """Delete a vector by ID."""
        pass

    @abstractmethod
    def update(self, name, vector_id, vector=None, payload=None):
        """Update a vector and its payload."""
        pass

    @abstractmethod
    def get(self, name, vector_id):
        """Retrieve a vector by ID."""
        pass

    @abstractmethod
    def list_cols(self):
        """List all collections."""
        pass

    @abstractmethod
    def delete_col(self, name):
        """Delete a collection."""
        pass

    @abstractmethod
    def col_info(self, name):
        """Get information about a collection."""
        pass
```

- 只有 Qdrant 一个实现

## 总结

- 核心就是 Memory 类，实现了 MemoryBase 接口
- 通过 embedding_model 来处理文本
- 通过 vector_store 存储 embedding
- 通过 llm 处理数据
- 通过 db 记录 Memory 的历史

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
