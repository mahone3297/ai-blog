+++
title = '[AI CrewAI] Be the Boss, Form an AI Team, and Collaborate with AI Agents to Complete Tasks'
date = 2024-07-13T12:43:34+08:00
draft = false
categories = ['AI', 'CrewAI']
tags = ['AI', 'CrewAI']
description = "Learn how to achieve AI agent collaboration with CrewAI to boost productivity and efficiency. CrewAI provides a solid foundation for building intelligent assistant platforms, automated customer service suites, and multi-agent research teams."
keywords = ["AI", "CrewAI", "AI agents", "automation", "intelligent assistant"]
+++

## Why Use CrewAI?
The power of AI collaboration is not to be underestimated. CrewAI is designed to enable AI agents to assume roles, share goals, and operate as a coordinated unit—much like a well-trained team. Whether you are building an intelligent assistant platform, an automated customer service suite, or a multi-agent research team, CrewAI provides the foundation for complex multi-agent interactions.

## Getting Started

### Installation

```bash
pip install crewai
pip install crewai[tools]
```

### Code

```python
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

# You can choose to use a local model through Ollama for example. See https://docs.crewai.com/how-to/LLM-Connections/ for more information.

# os.environ["OPENAI_API_BASE"] = 'http://localhost:11434/v1'
# os.environ["OPENAI_MODEL_NAME"] ='openhermes'  # Adjust based on available model
# os.environ["OPENAI_API_KEY"] ='sk-111111111111111111111111111111111111111111111111'

# You can pass an optional llm attribute specifying what model you wanna use.
# It can be a local model through Ollama / LM Studio or a remote
# model like OpenAI, Mistral, Antrophic or others (https://docs.crewai.com/how-to/LLM-Connections/)
#
# import os
# os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'
#
# OR
#
# from langchain_openai import ChatOpenAI

search_tool = SerperDevTool()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  # You can pass an optional llm attribute specifying what model you wanna use.
  # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
  tools=[search_tool]
)
writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.""",
  expected_output="Full analysis report in bullet points",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant AI advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
  process = Process.sequential
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)
```

## Key Features
- Role-based Agent Design: Customize agents based on specific roles, goals, and tools.
- Autonomous Agent Delegation: Agents can autonomously delegate tasks and inquire among themselves, enhancing problem-solving efficiency.
- Flexible Task Management: Define tasks with customizable tools and dynamically assign them to agents.
- Process-Driven: Currently supports sequential task execution and hierarchical processes, with more complex processes (like consensus and autonomous processes) under development.
- Save Output as File: Save the output of individual tasks as files for later use.
- Parse Output to Pydantic or JSON: Parse the output of individual tasks to Pydantic models or JSON, if desired.
- Compatible with Open-Source Models: Use Open AI or open-source models to run your teams. Refer to the page on connecting CrewAI to LLMs for detailed information on configuring agents to connect to models, including those running locally.

![crewAI-mindmap](crewAI-mindmap.png)

## CrewAI vs. Other Products
- Autogen: While Autogen excels at creating conversational agents that can work together, it lacks an inherent process concept. Coordinating interactions between agents in Autogen requires additional programming, which can become complex and cumbersome as task scale grows.
- ChatDev: ChatDev introduces the concept of processes to AI agents, but its implementation is quite rigid. ChatDev's customization is limited and not suited for production environments, which can hinder scalability and flexibility in real-world applications.

CrewAI's Advantage: CrewAI is designed for production environments. It offers the flexibility of Autogen's conversational agents and the structured process approach of ChatDev but without the rigidity. CrewAI's processes are designed to be dynamic and adaptive, seamlessly integrating into development and production workflows.

## Highlights

We only need to write some code like above, define some role agents and tasks, and then let CrewAI coordinate them to complete tasks and achieve goals.

This allows us to focus on the tasks themselves, rather than the interactions between agents. This is a very interesting concept, and I look forward to seeing how CrewAI can play a greater role in the future.

---

- [github](https://github.com/crewAIInc/crewAI)
- [crewai-examples](https://github.com/joaomdmoura/crewai-examples)
- [pipx install](https://pipx.pypa.io/stable/installation/)
- [poetry install](https://python-poetry.org/docs/#installation)
- [AI Blog - Learn AI from scratch](https://ai-blog.aihub2022.top/post/ai-crewai-intro/)
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
