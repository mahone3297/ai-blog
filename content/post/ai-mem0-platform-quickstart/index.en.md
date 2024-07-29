+++
title = '[AI Mem0 Platform] Quickstart: Empower Your AI Applications with Long-term Memory and Personalization!'
date = 2024-07-29T10:13:55+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = 'Explore the Mem0 Platform to quickly add long-term memory and personalization features to your AI applications. Through a smart memory layer, streamline development and enhance user experience, suitable for various scenarios such as learning assistants, customer support, health assistants, etc.'
keywords = ['AI', 'Mem0', 'Personalization', 'Long-term Memory', 'Smart Applications', 'API', 'Developer Tools', 'User Experience']
+++

## Introduction
Empower your AI applications with long-term memory and personalization capabilities.

## Welcome to Mem0 Platform
Mem0 Platform is a managed service that revolutionizes the way AI applications handle memory. By providing a smart, self-improving memory layer for Large Language Models (LLMs), we enable developers to create personalized AI experiences that evolve with each user interaction.

## Why Choose Mem0 Platform?
- Enhanced User Experience: Deliver tailored interactions that make your AI applications truly stand out.
- Simplified Development: Our API-first approach streamlines integration, allowing you to focus on building great features.
- Scalable Solution: Designed to grow with your application, from prototypes to production-ready systems.

## Key Features
- Comprehensive Memory Management: Easily manage long-term, short-term, semantic, and episodic memories for individual users, agents, and sessions through our robust APIs.
- Self-Improving Memory: Our adaptive system continuously learns from user interactions, refining its understanding over time.
- Cross-Platform Consistency: Ensure a unified user experience across various AI platforms and applications.
- Centralized Memory Control: Store, update, and delete memories effortlessly, taking away the hassle of memory management.

## Common Use Cases
- Personalized Learning Assistants
- Customer Support AI Agents
- Health Assistants
- Virtual Companions
- Productivity Tools
- Gaming AI

## Getting Started
Ready to supercharge your AI application with Mem0? Follow these steps:

- Sign Up: Create your Mem0 account on our platform.
- API Key: Generate your API key in the dashboard.
- Installation: Install our Python SDK using pip: `pip install mem0ai`
- Quick Implementation: Check out our Quickstart Guide to start using Mem0 quickly.

## Quickstart
Get started with Mem0 Platform in minutes

### Installation

```bash
pip install mem0ai
```

### API Key Setup
- Log in to Mem0 Platform
- Copy your API Key from the dashboard

### Instantiate Client

```python
from mem0 import MemoryClient
client = MemoryClient(api_key="your-api-key")
```

### Memory Operations
Mem0 provides a simple and customizable interface for performing CRUD operations on memory.

#### Create Memories
You can create long-term and short-term memories for your users, AI agents, etc. Here are some examples:

##### Long-term memory for a user

```python
messages = [
    {"role": "user", "content": "Hi, I'm Learn AI from Scratch. I'm very interested in AI."},
    {"role": "assistant", "content": "Hello Learn AI from Scratch! I've noted that you're very interested in AI. I'll keep this in mind for any learning-related recommendations or discussions."}
]
client.add(messages, user_id="learn-ai-from-scratch")
```

##### Short-term memory for a user session

```python
messages = [
    {"role": "user", "content": "I plan to read a book next month."},
    {"role": "assistant", "content": "That's exciting, Learn AI from Scratch! Reading a book next month sounds wonderful. Would you like some recommendations for AI-related books?"},
    {"role": "user", "content": "Yes, please!"},
    {"role": "assistant", "content": "Great! I'll remember that you're interested in AI-related books. I'll prepare a list for you in our next interaction."}
]
client.add(messages, user_id="learn-ai-from-scratch", session_id="read-a-book")
```

##### Long-term memory for an agent

```python
messages = [
    {"role": "system", "content": "You are a book recommendation assistant. Remember user preferences and provide tailored recommendations."},
    {"role": "assistant", "content": "Understood. I'll maintain personalized book recommendation preferences for each user based on their interests and past interactions."}
]
client.add(messages, agent_id="book-recommendation-assistant")
```

You can monitor memory operations on the platform:

#### Search Relevant Memories
You can also get related memories for a given natural language question using our search method.

```python
query = "What do you know about me?"
client.search(query, user_id="learn-ai-from-scratch")
```

#### Get All Memories
Fetch all memories for a user, agent, or session using the getAll() method.

Get all memories of an AI agent

```python
client.get_all(agent_id="book-recommendation-assistant")
```

Get all memories of a user

```python
user_memories = client.get_all(user_id="learn-ai-from-scratch")
```

Get short-term memories for a session

```python
short_term_memories = client.get_all(user_id="learn-ai-from-scratch", session_id="next-month-book-recommendation")
```

Get specific memory

```python
memory = client.get(memory_id="0e2bded6-4d55-11ef-b589-00163e064f1a")
```

#### Memory History
Get history of how a memory has changed over time

```python
# Add some message to create history
messages = [{"role": "user", "content": "I've recently been reading books related to AI"}]
client.add(messages, user_id="learn-ai-from-scratch")

# Add second message to update history
messages.append({'role': 'user', 'content': 'I have switched to reading novels now.'})
client.add(messages, user_id="learn-ai-from-scratch")

# Get history of how memory changed over time
memory_id = "<memory-id-here>"
history = client.history(memory_id)
```

#### Delete Memory
Delete specific memory:

```python
client.delete(memory_id)
```

Delete all memories of a user:

```python
client.delete_all(user_id="learn-ai-from-scratch")
```

Fun fact: You can also delete the memory using the add() method by passing a natural language command:

```python
client.add("Delete all of my book preferences", user_id="learn-ai-from-scratch")
```

---

- [github](https://github.com/mem0ai/mem0)
- [doc](https://docs.mem0.ai/overview)
