+++
title = '[AI Mem0] Source Code Analysis: Understanding the Implementation of Mem0'
date = 2024-07-30T13:48:31+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = "This article will delve into the source code of Mem0, giving you a comprehensive understanding of its implementation principles and specific usage methods to help you better utilize this powerful AI tool."
keywords = ["AI", "Mem0", "Source Code Analysis", "Tutorial", "Machine Learning", "Deep Learning", "Artificial Intelligence"]
+++

## Usage

First, let's look at how to use Mem0

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

How is Mem0's CRUD implemented? Let's look at the source code.

MemoryBase is an abstract class that defines some interface methods:

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

Memory implements the MemoryBase interface

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

Initializes embedding_model, vector_store (here it can only be Qdrant), llm, db, collection_name

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

- Sends user data to llm to get extracted_memories
- Converts user data to embeddings
- vector_store searches for existing_memories based on embeddings
- Sends new and old memories to llm to merge
- Calls the _create_memory_tool function to perform the actual operation
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

- vector_store gets memory by memory_id

### get_all

```python
    def get_all(self, user_id=None, agent_id=None, run_id=None, limit=100):
        """
        List all memories.

        Returns:
            list: List of all memories.
        """
```

- vector_store calls the list interface based on collection_name, filters, limit

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

- embedding_model converts query to embeddings
- vector_store searches based on embeddings

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

- Calls _update_memory_tool
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

- Calls _delete_memory_tool
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

- capture_event collects information
- telemetry uses Posthog (https://us.i.posthog.com)

## SQLiteManager

- db uses sqlite3
- A table to record history

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

- Mainly used to interact with the platform (https://api.mem0.ai/v1)
- Interfaces
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

- Only one implementation: Qdrant

## Summary

- The core is the Memory class, which implements the MemoryBase interface
- Processes text through the embedding_model
- Stores embeddings through vector_store
- Processes data through llm
- Records Memory's history through db

---

- [github](https://github.com/mem0ai/mem0)
- [doc](https://docs.mem0.ai/overview)
