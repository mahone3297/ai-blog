+++
title = '[AI Perplexica] AI驱动的开源搜索引擎'
date = 2024-07-02T10:33:39+08:00
draft = false
categories = ['AI', 'Perplexica']
tags = ['AI', 'Perplexica', '开源', '搜索引擎']
description = '探索Perplexica，一款由AI驱动的开源搜索引擎，了解其特点、使用方法以及如何安装。'
keywords = ['AI', 'Perplexica', '开源', '搜索引擎', '机器学习', 'SearxNG', 'LLMs']
+++

AI搜索引擎市场，有产品 https://www.perplexity.ai/ 。我们看下，它如何介绍自己

![How is Perplexity AI different?](how-perplexity-ai-different.png)

开源市场上，也有一款对标产品 Perplexica ，我们来看下

![perplexica](perplexica.png)

界面很像

## 介绍

Perplexica是一个开源的、由AI驱动的搜索工具或搜索引擎，它深入互联网寻找答案。受到Perplexity AI的启发，它是一个开源选项，不仅仅搜索网络，而且理解你的问题。它使用先进的机器学习算法，如相似性搜索和嵌入，来精炼结果，并提供带有引用来源的清晰答案。

使用SearxNG保持最新且完全开源，Perplexica确保你总是获得最新信息，同时不牺牲你的隐私。

## 特点

- **本地LLMs**：你可以使用Ollama来利用本地LLMs，如Llama3和Mixtral。
- **两种主要模式**：
  - **Copilot模式**：（开发中）通过生成不同的查询来增强搜索，找到更多相关互联网资源。与仅使用SearxNG的上下文进行普通搜索不同，它会访问最匹配的页面，并尝试直接从页面找到与用户查询相关的内容。
  - **普通模式**：处理你的查询并执行网络搜索。
- **焦点模式**：特定模式，更好地回答特定类型的问题。Perplexica目前有6种焦点模式：
  - **全模式**：搜索整个网络，找到最佳结果。
  - **写作助手模式**：有助于不需要网络搜索的写作任务。
  - **学术搜索模式**：寻找文章和论文，适合学术研究。
  - **YouTube搜索模式**：根据搜索查询找到YouTube视频。
  - **Wolfram Alpha搜索模式**：使用Wolfram Alpha回答需要计算或数据分析的查询。
  - **Reddit搜索模式**：搜索Reddit上的讨论和与查询相关的意见。
- **当前信息**：一些搜索工具可能会提供过时信息，因为它们使用爬虫数据并将其转换为嵌入，存储在索引中。与它们不同，Perplexica使用SearxNG，一个元搜索引擎来获取结果，重新排名并找到最相关来源，确保你总是获得最新信息，而无需日常数据更新的开销。

## 安装

### Docker(推荐)

1. 确保在您的系统上已安装并运行Docker。
2. 克隆Perplexica仓库：
   ```bash
   git clone https://github.com/ItzCrazyKns/Perplexica.git
   ```
3. 克隆后，导航到包含项目文件的目录。
4. 将`sample.config.toml`文件重命名为`config.toml`。对于Docker设置，您只需填写以下字段：
   - `OPENAI`：您的OpenAI API密钥。**如果您希望使用OpenAI的模型，则只需填写此字段**。
   - `OLLAMA`：您的Ollama API URL。您应将其输入为`http://host.docker.internal:PORT_NUMBER`。如果您在端口11434上安装了Ollama，请使用`http://host.docker.internal:11434`。对于其他端口，请相应调整。**如果您希望使用Ollama的模型而不是OpenAI的模型，则需要填写此字段**。
   - `GROQ`：您的Groq API密钥。**如果您希望使用Groq的托管模型，则只需填写此字段**。

     **注意**：启动Perplexica后，您可以从设置对话框中更改这些字段。
   - `SIMILARITY_MEASURE`：要使用的相似性测量（默认已填写；如果不确定，可以保留原样）。
5. 确保您位于包含`docker-compose.yaml`文件的目录中，并执行：
   ```bash
   docker compose up -d
   ```
6. 等待几分钟以完成设置。您可以在浏览器中访问http://localhost:3000来访问Perplexica。

**注意**：在容器构建完成后，您可以直接从Docker启动Perplexica，而无需打开终端。

### 非 Docker

1. 安装SearXNG并在SearXNG设置中允许`JSON`格式。
2. 克隆仓库并将根目录下的`sample.config.toml`文件重命名为`config.toml`。确保你完成了这个文件中所有必需的字段。
3. 将`ui`文件夹中的`.env.example`文件重命名为`.env`，并填写所有必要的字段。
4. 在填写了配置和环境文件后，在`ui`文件夹和根目录中运行`npm i`。
5. 安装依赖项，然后在`ui`文件夹和根目录中执行`npm run build`。
6. 最后，通过在`ui`文件夹和根目录中运行`npm run start`来启动前端和后端。

**注意**：推荐使用Docker，因为它简化了设置过程，尤其是对于管理环境变量和依赖项。

---

- [github](https://github.com/ItzCrazyKns/Perplexica)
<!-- - [AI 博客 - 从零开始学AI](...) -->
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
