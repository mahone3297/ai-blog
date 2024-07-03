+++
title = '[AI Perplexica] In-Depth Analysis: Unveiling AI Architecture'
date = 2024-07-03T10:18:59+08:00
draft = false
categories = ['AI', 'Perplexica']
tags = ['AI', 'Perplexica']
description = 'Learn about the core architecture of Perplexica, explore its user interface, agent chains, large language models, embedding models, and how they work together to efficiently handle complex queries.'
keywords = ['AI', 'Perplexica', 'architecture', 'large language models', 'embedding models', 'web search']
+++

- [[AI Perplexica] AI-Driven Open Source Search Engine](https://ai-blog.aihub2022.top/post/ai-perplexica-intro/)

In the previous article, we gave a basic introduction to Perplexica, including its features and how to install it.

Today, let's dive into Perplexica's architecture.

## Perplexica's Architecture

Perplexica's architecture consists of the following key components:

1. **User Interface**: A web-based interface that allows users to interact with Perplexica for searching images, videos, and much more.
2. **Agent/Chains**: These components predict Perplexica's next actions, understand user queries, and decide whether a web search is necessary.
3. **SearXNG**: A metadata search engine used by Perplexica to search the web for sources.
4. **LLMs (Large Language Models)**: Utilized by agents and chains for tasks like understanding content, writing responses, and citing sources. Examples include Claude, GPTs, etc.
5. **Embedding Models**: To improve the accuracy of search results, embedding models re-rank the results using similarity search algorithms such as cosine similarity and dot product distance.

## How does Perplexica work?

We will understand how Perplexica works by taking an example of a scenario where a user asks: "How does an A.C. work?". We'll break down the process into steps to make it easier to understand. The steps are as follows:

1. The message is sent via WS to the backend server where it invokes the chain. The chain will depend on your focus mode. For this example, let's assume we use the "webSearch" focus mode.
    - The message is sent via web socket.
2. The chain is now invoked; first, the message is passed to another chain where it first predicts (using the chat history and the question) whether there is a need for sources and searching the web. If there is, it will generate a query (in accordance with the chat history) for searching the web that we'll take up later. If not, the chain will end there, and then the answer generator chain, also known as the response generator, will be started.
    - This part can also be referred to as query rewrite or pre-LLM.
3. The query returned by the first chain is passed to SearXNG to search the web for information.
    - Traditional search, using SearXNG here.
4. After the information is retrieved, it is based on keyword-based search. We then convert the information into embeddings and the query as well, then we perform a similarity search to find the most relevant sources to answer the query.
    - Traditional search engines return a lot of information, using an embedding model for similarity search.
5. After all this is done, the sources are passed to the response generator. This chain takes all the chat history, the query, and the sources. It generates a response that is streamed to the UI.
    - Here, the LLM is called, passing the chat history, query, and sources together to the LLM, which then generates the answer and streams it to the UI.

### How are the answers cited?

The LLMs are prompted to do so. We've prompted them so well that they cite the answers themselves, and using some UI magic, we display it to the user.

### Image and Video Search

Image and video searches are conducted in a similar manner. A query is always generated first, then we search the web for images and videos that match the query. These results are then returned to the user.

---

- [gitlab](https://github.com/ItzCrazyKns/Perplexica)
- [AI Blog - Learn AI from scratch](https://ai-blog.aihub2022.top/post/ai-perplexica-architecture/)
