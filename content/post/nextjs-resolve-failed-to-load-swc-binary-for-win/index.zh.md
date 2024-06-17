+++
title = '[NextJs] 解决 Failed to load SWC binary for win32/64'
date = 2024-06-17T16:42:28+08:00
draft = false
categories = ['NextJS']
tags = ['NextJS']
description = '快速解决 Next.js 在 Windows 下运行时 SWC Binary 报错的方法，包括安装 Microsoft Visual C++ Redistributable 和确认处理器架构。'
keywords = ['Next.js', 'SWC binary error', 'Windows', 'Microsoft Visual C++ Redistributable', '处理器架构', 'node 进程架构']
+++

在运行 Next.js `npm run dev` 程序时，你可能会遇到这样一个让人抓狂的报错：

```bash
Failed to load SWC binary for win32/64 (Next.js)
next-swc.win32-x64-msvc.node is not a valid Win32 application.
```

不用担心，这并不是世界末日！其实，官方已经给出了详细的解决方案，今天我们就来一起解决这个棘手的问题。

## 首先，问题的根源

这个错误主要是由于缺少必要的 Microsoft Visual C++ Redistributable 组件。你可以在 [微软官网](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170) 下载并安装它。

## 解决方案一步到位

### 1. 确认你的处理器架构

在 Windows 系统中，确认处理器架构非常简单，只需以下几步：
- 打开“设置”应用程序（可以通过按 Win + I 快速打开）。
- 进入“系统” > “关于”。
- 在“设备规格”部分，查找“系统类型”。你会看到类似“基于 x64 的处理器”或“基于 ARM64 的处理器”的描述。

这样，你就知道了你的处理器是 x64 还是 ARM64。

### 2. 检查 Node 进程架构

进一步确保你的 Node 进程架构也一致。打开命令提示符（cmd），输入以下命令：

```bash
node -p "process.arch"
```

这样你就能看到类似 `x64` 或 `arm64` 的结果。

### 3. 安装正确的 SWC 包

根据你的处理器架构，运行以下命令重新安装适合的 SWC 包：

```bash
npm i @next/swc-win32-x64-msvc
```

## 大功告成

现在，你可以再次运行 `npm run dev`，看看报错是否已经解决。如果一切顺利，你的 Next.js 项目应该能够正常启动了！

---

- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/nextjs-resolve-failed-to-load-swc-binary-for-win/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977490&idx=1&sn=af76ac46cc26628f6b7b1c7e2fe122be&chksm=86c7c857b1b04141915c5c98beeb808ab3824910a62d12305c8147d3fedfca993b18463942ee#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
