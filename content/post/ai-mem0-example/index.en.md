+++
title = '[AI Mem0] Build Stateful AI Applications with Mem0 for Smarter, More Personalized Experiences'
date = 2024-07-27T12:03:01+08:00
draft = false
categories = ['AI', 'Mem0']
tags = ['AI', 'Mem0']
description = 'Mem0 brings a revolutionary AI experience to your applications by providing personalized, reliable, and cost-effective intelligent interactions through large language models. Whether its chatbots, virtual assistants, or AI agents, Mem0 helps you achieve long-term memory and engaging user experiences.'
keywords = ['AI', 'Mem0', 'large language models', 'personalized experiences', 'intelligent applications', 'virtual assistants', 'chatbots', 'customer support', 'travel assistants', 'personalized learning']
+++

## Key Points

Let's see how to build an app with Mem0

- memory search first
- attach the searched memory to the prompt and send it to the LLM
- finally add memory

---

## Overview
How to use Mem0 in existing applications?

Using Mem0, you can create stateful applications based on large language models, such as chatbots, virtual assistants, or AI agents. Mem0 enhances your application by providing a memory layer, making responses:

- More personalized
- More reliable
- Cost-effective by reducing interactions with large language models
- More engaging
- Supporting long-term memory

## Examples
Here are some examples of how to integrate Mem0 into various applications:

### Personalized AI Tutor
You can use Mem0 to create a personalized AI tutor. This guide will walk you through the necessary steps and provide the full code to get you started.

#### Overview
The personalized AI tutor leverages Mem0 to retain information during interactions, enabling a customized learning experience. Integrated with OpenAI's GPT-4 model, the tutor can provide detailed and context-aware responses to user queries.

#### Setup
Before starting, ensure you have installed the required dependencies. You can install the necessary packages using pip:

```bash
pip install openai mem0ai
```

#### Complete Code Example
Here is the complete code to create and interact with a personalized AI tutor using Mem0:

```python
from openai import OpenAI
from mem0 import Memory
import os

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

# Initialize OpenAI client
client = OpenAI()

class PersonalAITutor:
    def __init__(self):
        """
        Initialize the PersonalAITutor, configuring memory and OpenAI client.
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
        Ask a question to the AI and store related information in memory.

        :param question: The question to ask.
        :param user_id: Optional user ID for associating memory.
        """
        # Send a streaming chat completion request to the AI
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "You are a personal AI tutor."},
                {"role": "user", "content": question}
            ]
        )
        # Store the question in memory
        self.memory.add(question, user_id=user_id, metadata={"app_id": self.app_id})

        # Print the AI's response in real-time
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve all memories associated with a given user ID.

        :param user_id: Optional user ID for filtering memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)

# Instantiate the PersonalAITutor
ai_tutor = PersonalAITutor()

# Define a user ID
user_id = "Learn AI from scratch"

# Ask a question
ai_tutor.ask("I am learning the basics of computer science. What is a queue? Please explain briefly.", user_id=user_id)
```

#### Retrieving Memories
You can retrieve all memories at any time using the following code:

```python
memories = ai_tutor.get_memories(user_id=user_id)
for m in memories:
    print(m['text'])
```

#### Key Points
- Initialization: The PersonalAITutor class initializes with necessary memory configuration and OpenAI client setup.
- Asking Questions: The ask method sends questions to the AI and stores related information in memory.
- Retrieving Memories: The get_memories method retrieves all stored memories associated with a user.

#### Conclusion
As interactions continue, Mem0's memory will automatically update based on interactions, providing a continuously improving personalized learning experience. This setup ensures that the AI tutor can deliver context-aware and accurate responses, enhancing the overall educational process.

### Customer Support AI Agent
You can use Mem0 to create a personalized customer support AI agent. This guide will walk you through the necessary steps and provide the full code to get you started.

#### Overview
The customer support AI agent leverages Mem0 to retain information during interactions, enabling a personalized and efficient support experience.

#### Setup
Install the required packages using pip:

```bash
pip install openai mem0ai
```

#### Complete Code Example
Here is the complete code to create and interact with a customer support AI agent using Mem0:

```python
from openai import OpenAI
from mem0 import Memory
import os

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

class CustomerSupportAIAgent:
    def __init__(self):
        """
        Initialize the CustomerSupportAIAgent, configuring memory and OpenAI client.
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
        Handle customer query and store related information in memory.

        :param query: The customer query to handle.
        :param user_id: Optional user ID for associating memory.
        """
        # Send a streaming chat completion request to the AI
        stream = self.client.chat.completions.create(
            model="gpt-4",
            stream=True,
            messages=[
                {"role": "system", "content": "You are a customer support AI agent."},
                {"role": "user", "content": query}
            ]
        )
        # Store the query in memory
        self.memory.add(query, user_id=user_id, metadata={"app_id": self.app_id})

        # Print the AI's response in real-time
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

    def get_memories(self, user_id=None):
        """
        Retrieve all memories associated with a given customer ID.

        :param user_id: Optional user ID for filtering memories.
        :return: List of memories.
        """
        return self.memory.get_all(user_id=user_id)

# Instantiate the CustomerSupportAIAgent
support_agent = CustomerSupportAIAgent()

# Define a customer ID
customer_id = "Learn AI from scratch"

# Handle customer query
support_agent.handle_query("I need help with my recent order. It hasn't arrived yet.", user_id=customer_id)
```

#### Retrieving Memories
You can retrieve all memories at any time using the following code:

```python
memories = support_agent.get_memories(user_id=customer_id)
for m in memories:
    print(m['text'])
```

#### Key Points
- Initialization: The CustomerSupportAIAgent class initializes with necessary memory configuration and OpenAI client setup.
- Handling Queries: The handle_query method sends queries to the AI and stores related information in memory.
- Retrieving Memories: The get_memories method retrieves all stored memories associated with a customer.

#### Conclusion
As interactions continue, Mem0's memory will automatically update based on interactions, providing a continuously improving personalized support experience.

### Personalized AI Travel Assistant
Use Mem0 to create a personalized AI travel assistant. This guide provides step-by-step instructions and complete code to get you started.

#### Overview
The personalized AI travel assistant uses Mem0 to store and retrieve information between interactions, providing a tailored travel planning experience. It integrates with OpenAI's GPT-4 model to provide detailed and context-aware responses to user queries.

#### Setup
Install the required dependencies using pip:

```bash
pip install openai mem0ai
```

#### Complete Code Example
Here is the complete code to create and interact with a personalized AI travel assistant using Mem0:

```python
import os
from openai import OpenAI
from mem0 import Memory

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-xxx'

class PersonalTravelAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.memory = Memory()
        self.messages = [{"role": "system", "content": "You are a personal AI Assistant."}]

    def ask_question(self, question, user_id):
        # Retrieve previously relevant memories
        previous_memories = self.search_memories(question, user_id=user_id)
        prompt = question
        if previous_memories:
            prompt = f"User input: {question}\n Previous memories: {previous_memories}"
        self.messages.append({"role": "user", "content": prompt})

        # Generate response using GPT-4o
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=self.messages
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})

        # Store the question in memory
        self.memory.add(question, user_id=user_id)
        return answer

    def get_memories(self, user_id):
        memories = self.memory.get_all(user_id=user_id)
        return [m['text'] for m in memories]

    def search_memories(self, query, user_id):
        memories = self.memory.search(query, user_id=user_id)
        return [m['text'] for m in memories]

# Usage example
user_id = "Learn AI from scratch"
ai_assistant = PersonalTravelAssistant()

def main():
    while True:
        question = input("Question: ")
        if question.lower() in ['q', 'exit']:
            print("Exiting...")
            break

        answer = ai_assistant.ask_question(question, user_id=user_id)
        print(f"Answer: {answer}")
        memories = ai_assistant.get_memories(user_id=user_id)
        print("Memories:")
        for memory in memories:
            print(f"- {memory}")
        print("-----")

if __name__ == "__main__":
    main()
```

#### Key Components
- Initialization: The PersonalTravelAssistant class initializes with OpenAI client and Mem0 memory setup.
- Asking Questions: The ask_question method sends questions to the AI, combines previous memories, and stores new information.
- Memory Management: The get_memories and search_memories methods handle retrieval and search of stored memories.

#### Usage
- Set your OpenAI API key in the environment variable.
- Instantiate the PersonalTravelAssistant.
- Use the main() function to interact with the assistant in a loop.

#### Conclusion
This personalized AI travel assistant uses Mem0's memory capabilities to provide context-aware responses. As you interact with it, the assistant learns and improves, offering increasingly personalized travel advice and information.

---

- [github](https://github.com/mem0ai/mem0)
- [doc](https://docs.mem0.ai/overview)
- [AI Blog - Learn AI from scratch](https://ai-blog.aihub2022.top/post/ai-mem0-example/)
