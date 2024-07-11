+++
title = '[AI Fabric] 解锁AI的未来：深入探索Fabric开源框架'
date = 2024-07-10T21:30:31+08:00
draft = false
categories = ['AI', 'Fabric']
tags = ['AI', 'Fabric']
description = 'Fabric 是一个旨在通过人工智能增强人类能力的开源框架，解决了 AI 集成的难题。通过分解问题并应用 AI 解决方案，Fabric 帮助用户应对日常挑战，实现技术与人类的完美结合。'
keywords = ['AI', 'Fabric', '开源框架', '人工智能', '技术集成', 'Unix 哲学', '提示优化']
+++

今天看到一个项目，Fabric，我们一起来看下

## 介绍

fabric 是一个使用人工智能增强人类能力的开源框架。

## 为什么需要Fabric

因为作者认为，人工智能很强大，不存在能力问题，存在的是集成问题。

Fabric 的创建就是为了解决这个问题，让每个人都能精细地应用人工智能来应对日常挑战。

## 哲学

技术的目的是帮助人类繁荣。

### 将问题分解为组件

将问题分解为组件，然后一次一个地应用人工智能。

有点类似 Unix 哲学

### 提示太多

现在提示太多，也不知道是否有用，选择困难症。

### Fabric 的 prompt

- 使用 Markdown 来帮助确保最大程度的可读性和可编辑性
- 非常明确的指令
- 倾向于几乎只使用提示的系统部分

## 快速开始

```bash
git clone https://github.com/danielmiessler/fabric.git
cd fabric
sudo apt install pipx
pipx install .
fabric --setup

fabric --help

# update
pipx install . --force
fabric --update
```

## 使用 fabric 客户端

```bash
# 设置环境变量
export OPENAI_BASE_URL=...
export DEFAULT_MODEL=...
export OPENAI_API_KEY=...

pbpaste | fabric --pattern summarize
pbpaste | fabric --stream --pattern analyze_claims
yt --transcript https://youtube.com/watch?v=uXs-zPc63kM | fabric --stream --pattern extract_wisdom
pbpaste | analyze_claims --stream
```

## 分析
### 入口 fabric.py

看下 client 代码 `fabric/installer/client/cli/fabric.py`

argparse 解析命令行参数，然后执行相应的功能函数

```python
from .utils import Standalone, Update, Setup, Alias, run_electron_app
import argparse
import sys
import os

script_directory = os.path.dirname(os.path.realpath(__file__))

def main():
    parser = argparse.ArgumentParser(
        description="An open source framework for augmenting humans using AI."
    )
    parser.add_argument("--text", "-t", help="Text to extract summary from")
    parser.add_argument(
        "--copy", "-C", help="Copy the response to the clipboard", action="store_true"
    )
    parser.add_argument(
        '--agents', '-a',
        help="Use praisonAI to create an AI agent and then use it. ex: 'write me a movie script'", action="store_true"
    )

    parser.add_argument(
        "--output",
        "-o",
        help="Save the response to a file",
        nargs="?",
        const="analyzepaper.txt",
        default=None,
    )
    parser.add_argument('--session', '-S',
                        help="Continue your previous conversation. Default is your previous conversation", nargs="?", const="default")
    parser.add_argument(
        '--clearsession', help="deletes indicated session. Use 'all' to delete all sessions")
    parser.add_argument('--sessionlog', help="View the log of a session")
    parser.add_argument(
        '--listsessions', help="List all sessions", action="store_true")
    parser.add_argument(
        "--gui", help="Use the GUI (Node and npm need to be installed)", action="store_true")
    parser.add_argument(
        "--stream",
        "-s",
        help="Use this option if you want to see the results in realtime. NOTE: You will not be able to pipe the output into another command.",
        action="store_true",
    )
    parser.add_argument(
        "--list", "-l", help="List available patterns", action="store_true"
    )
    parser.add_argument(
        '--temp', help="set the temperature for the model. Default is 0", default=0, type=float)
    parser.add_argument(
        '--top_p', help="set the top_p for the model. Default is 1", default=1, type=float)
    parser.add_argument(
        '--frequency_penalty', help="set the frequency penalty for the model. Default is 0.1", default=0.1, type=float)
    parser.add_argument(
        '--presence_penalty', help="set the presence penalty for the model. Default is 0.1", default=0.1, type=float)
    parser.add_argument(
        "--update", "-u", help="Update patterns", action="store_true")
    parser.add_argument("--pattern", "-p", help="The pattern (prompt) to use")
    parser.add_argument(
        "--setup", help="Set up your fabric instance", action="store_true"
    )
    parser.add_argument('--changeDefaultModel',
                        help="Change the default model. For a list of available models, use the --listmodels flag.")

    parser.add_argument(
        "--model", "-m", help="Select the model to use"
    )
    parser.add_argument(
        "--listmodels", help="List all available models", action="store_true"
    )
    parser.add_argument('--remoteOllamaServer',
                        help='The URL of the remote ollamaserver to use. ONLY USE THIS if you are using a local ollama server in an non-default location or port')
    parser.add_argument('--context', '-c',
                        help="Use Context file (context.md) to add context to your pattern", action="store_true")

    args = parser.parse_args()
    home_holder = os.path.expanduser("~")
    config = os.path.join(home_holder, ".config", "fabric")
    config_patterns_directory = os.path.join(config, "patterns")
    config_context = os.path.join(config, "context.md")
    env_file = os.path.join(config, ".env")
    if not os.path.exists(config):
        os.makedirs(config)
    if args.setup:
        Setup().run()
        Alias().execute()
        sys.exit()
    if not os.path.exists(env_file) or not os.path.exists(config_patterns_directory):
        print("Please run --setup to set up your API key and download patterns.")
        sys.exit()
    if not os.path.exists(config_patterns_directory):
        Update()
        Alias()
        sys.exit()
    if args.changeDefaultModel:
        Setup().default_model(args.changeDefaultModel)
        sys.exit()
    if args.gui:
        run_electron_app()
        sys.exit()
    if args.update:
        Update()
        Alias()
        sys.exit()
    if args.context:
        if not os.path.exists(os.path.join(config, "context.md")):
            print("Please create a context.md file in ~/.config/fabric")
            sys.exit()
    if args.agents:
        standalone = Standalone(args)
        text = ""  # Initialize text variable
        # Check if an argument was provided to --agents
        if args.text:
            text = args.text
        else:
            text = standalone.get_cli_input()
        if text:
            standalone = Standalone(args)
            standalone.agents(text)
            sys.exit()
    if args.session:
        from .helper import Session
        session = Session()
        if args.session == "default":
            session_file = session.find_most_recent_file()
            if session_file is None:
                args.session = "default"
            else:
                args.session = session_file.split("/")[-1]
    if args.clearsession:
        from .helper import Session
        session = Session()
        session.clear_session(args.clearsession)
        if args.clearsession == "all":
            print(f"All sessions cleared")
        else:
            print(f"Session {args.clearsession} cleared")
        sys.exit()
    if args.sessionlog:
        from .helper import Session
        session = Session()
        print(session.session_log(args.sessionlog))
        sys.exit()
    if args.listsessions:
        from .helper import Session
        session = Session()
        session.list_sessions()
        sys.exit()
    standalone = Standalone(args, args.pattern)
    if args.list:
        try:
            direct = sorted(os.listdir(config_patterns_directory))
            for d in direct:
                print(d)
            sys.exit()
        except FileNotFoundError:
            print("No patterns found")
            sys.exit()
    if args.listmodels:
        gptmodels, localmodels, claudemodels, googlemodels = standalone.fetch_available_models()
        print("GPT Models:")
        for model in gptmodels:
            print(model)
        print("\nLocal Models:")
        for model in localmodels:
            print(model)
        print("\nClaude Models:")
        for model in claudemodels:
            print(model)
        print("\nGoogle Models:")
        for model in googlemodels:
            print(model)
        sys.exit()
    if args.text is not None:
        text = args.text
    else:
        text = standalone.get_cli_input()
    if args.stream and not args.context:
        if args.remoteOllamaServer:
            standalone.streamMessage(text, host=args.remoteOllamaServer)
        else:
            standalone.streamMessage(text)
        sys.exit()
    if args.stream and args.context:
        with open(config_context, "r") as f:
            context = f.read()
            if args.remoteOllamaServer:
                standalone.streamMessage(
                    text, context=context, host=args.remoteOllamaServer)
            else:
                standalone.streamMessage(text, context=context)
        sys.exit()
    elif args.context:
        with open(config_context, "r") as f:
            context = f.read()
            if args.remoteOllamaServer:
                standalone.sendMessage(
                    text, context=context, host=args.remoteOllamaServer)
            else:
                standalone.sendMessage(text, context=context)
        sys.exit()
    else:
        if args.remoteOllamaServer:
            standalone.sendMessage(text, host=args.remoteOllamaServer)
        else:
            standalone.sendMessage(text)
        sys.exit()

if __name__ == "__main__":
    main()
```

### prompt pattern

pattern 格式基本如下

```bash
├── summarize_debate
│   └── system.md
├── summarize_git_changes
│   └── system.md
├── summarize_git_diff
│   └── system.md
├── summarize_lecture
│   └── system.md
├── summarize_micro
│   ├── system.md
│   └── user.md
├── summarize_newsletter
│   ├── system.md
│   └── user.md
├── summarize_paper
│   ├── README.md
│   ├── system.md
│   └── user.md
├── summarize_prompt
│   └── system.md
├── summarize_pull-requests
│   ├── system.md
│   └── user.md
├── summarize_rpg_session
│   └── system.md
```

看下 `summarize_prompt/system.md` ，重点是结构化

```md
# IDENTITY and PURPOSE
You are an expert prompt summarizer. You take AI chat prompts in and output a concise summary of the purpose of the prompt using the format below.
Take a deep breath and think step by step about how to best accomplish this goal using the following steps.

# OUTPUT SECTIONS
- Combine all of your understanding of the content into a single, paragraph.
- The first sentence should summarize the main purpose. Begin with a verb and describe the primary function of the prompt. Use the present tense and active voice. Avoid using the prompt's name in the summary. Instead, focus on the prompt's primary function or goal.
- The second sentence clarifies the prompt's nuanced approach or unique features.
- The third sentence should provide a brief overview of the prompt's expected output.

# OUTPUT INSTRUCTIONS
- Output no more than 40 words.
- Create the output using the formatting above.
- You only output human readable Markdown.
- Do not output numbered lists or bullets.
- Do not output newlines.
- Do not output warnings or notes.

# INPUT:
INPUT:
```

---

- [github](https://github.com/danielmiessler/fabric)
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/ai-fabric-intro/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977587&idx=1&sn=06564d3c92a031bc7199e52af1bf4e6a&chksm=86c7c836b1b0412066f5a07b4077783a2c211e38bdb9bbf44440af39329a455eb41636664f9b#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
