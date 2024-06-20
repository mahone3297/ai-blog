+++
title = '[AI aider] Create Your AI Partner in Terminal: Aider Makes Coding Smarter and More Fun!'
date = 2024-06-20T12:41:23+08:00
draft = false
categories = ['AI', 'aider']
tags = ['AI', 'aider']
description = 'Discover Aider, a tool that lets you pair program with AI in the terminal, making your coding experience smarter and more enjoyable.'
keywords = ['AI', 'aider', 'programming', 'AI partner', 'large language model', 'terminal tool', 'git']
+++

Today, I’m excited to introduce a super cool AI project called [Aider](https://aider.chat/).

## Introduction

Aider is a tool that lets you pair program with AI in the terminal. Imagine having a super-smart coding buddy by your side. Aider makes large language models (LLMs) your coding partner, helping you edit code in your local git repositories. Whether you’re starting a new project from scratch or working with an existing git repository, Aider has you covered. It works best with GPT-4o and Claude 3 Opus, but it can pair with almost any large language model.

![aider screencat](https://aider.chat/assets/screencast.svg)

## Getting Started

Ready to embark on a delightful coding journey with your AI buddy? Here we go!

```bash
$ pip install aider-chat

# Change directory into a git repo
$ cd /to/your/git/repo

# Work with GPT-4o on your repo
$ export OPENAI_API_KEY=your-key-goes-here
$ aider
```

Then you can start chatting with the large model, and Aider will help you modify the code and commit to git, all in one go.

## Features: Repository Map

I highly recommend reading this great article [Building a better repository map with tree sitter](https://aider.chat/2023/10/22/repomap.html) for a detailed explanation on building better repository maps.

When modifying code, you need to solve three problems:

1. Find the code that needs to be changed.
2. Understand how that piece of code relates to the rest of the codebase.
3. Make the correct code changes to complete the task.

For problem 3, GPT-4 is simply a magic wand. For problem 2, we use a repo map.

The repo map can be passed to the LLM to give it context. When the repo map is too large, we use a graph ranking algorithm to find the most relevant parts.

How do we get the repo map? Initially, we used ctags, but because of the relationships in the article, we finally switched to tree-sitter.

As for problem 1, it currently requires manual intervention.

## Trial Results

Aider supports many LLMs. I tried the DeepSeek model, and they recently released the DeepSeek Coder V2 model, claiming its coding ability surpasses GPT-4 Turbo. Aider also stated that it scored the highest on Aider's code editing benchmark.

However, my results were not very impressive... Maybe I was using it wrong.

## Conclusion

In conclusion: Keep working hard, and keep using AI. Persistence is key, and perhaps the next coding genius could be you.

---

- [Official Website](https://aider.chat/)
- [GitHub](https://github.com/paul-gauthier/aider)
- [Building a better repository map with tree sitter](https://aider.chat/2023/10/22/repomap.html)
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [CSDN - Learn AI from scratch](...) -->
<!-- - [Juejin - Learn AI from scratch](...) -->
<!-- - [Zhihu - Learn AI from scratch](...) -->
<!-- - [Alibaba Cloud - Learn AI from scratch](...) -->
<!-- - [Tencent Cloud - Learn AI from scratch](...) -->
