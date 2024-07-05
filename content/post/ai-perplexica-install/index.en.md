+++
title = '[AI Perplexica] Installation Guide: Easily Deploy AI-Powered Open Source Search Engine'
date = 2024-07-05T23:56:45+08:00
draft = false
categories = ['AI', 'Perplexica']
tags = ['AI', 'Perplexica']
description = 'A detailed guide on how to deploy the AI-powered open-source search engine Perplexica using Docker in your local environment, allowing you to quickly get started and experience its powerful features.'
keywords = ['AI', 'Perplexica', 'installation', 'Docker', 'tutorial']
+++

- [[AI Perplexica] AI-Powered Open Source Search Engine](https://ai-blog.aihub2022.top/zh/post/ai-perplexica-intro/)
- [[AI Perplexica] In-Depth Analysis: Unveiling the AI Architecture](https://ai-blog.aihub2022.top/zh/post/ai-perplexica-architecture/)

Previously, we covered the introduction, features, and architecture of Perplexica, and learned about its working principles.

Today, let's deploy it together.

## Installation

### Docker

- Install Docker
    - https://docs.docker.com/engine/install/ubuntu/
- Install Docker Compose
    - https://docs.docker.com/compose/install/
- Clone the code
    ```bash
    git clone https://github.com/ItzCrazyKns/Perplexica.git
    ```
- Configure config.toml
    ```bash
    cp sample.config.toml config.toml
    ```
- Start Docker
    ```bash
    docker compose up -d
    ```

## Usage

After the installation is complete, you can access it at http://127.0.0.1:3000/

![perplexica-installed](perplexica-installed.png)

The default theme is dark.

Click the settings button in the lower left corner, make some configurations, fill in the fields (model name, url, api key), and click save.

![perplexica-settings](perplexica-settings.png)

Now, you can chat. Let's try it.

![perplexica-chat-1](perplexica-chat-1.png)

As mentioned in previous articles, if it knows the answer, it will respond directly without searching.

![perplexica-chat-2](perplexica-chat-2.png)

![perplexica-chat-3](perplexica-chat-3.png)

![perplexica-chat-4](perplexica-chat-4.png)

Some of the subsequent questions trigger searches.

The speed is a bit slow, possibly due to slow search or LLM, not sure for now.

---

- [github](https://github.com/ItzCrazyKns/Perplexica)
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [AI 博客 - 从零开始学AI](...) -->
<!-- - [WeChat Official Account - Learn AI from scratch](...) -->
<!-- - [CSDN - Learn AI from scratch](...) -->
<!-- - [Juejin - Learn AI from scratch](...) -->
<!-- - [Zhihu - Learn AI from scratch](...) -->
<!-- - [Alibaba Cloud - Learn AI from scratch](...) -->
<!-- - [Tencent Cloud - Learn AI from scratch](...) -->
