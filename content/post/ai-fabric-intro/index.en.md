+++
title = '[AI Fabric] Unlocking the Future of AI: An In-depth Exploration of the Fabric Open Source Framework'
date = 2024-07-10T21:30:31+08:00
draft = false
categories = ['AI', 'Fabric']
tags = ['AI', 'Fabric']
description = 'Fabric is an open-source framework designed to enhance human capabilities through artificial intelligence, addressing the challenges of AI integration. By breaking down problems and applying AI solutions, Fabric helps users tackle daily challenges, achieving a perfect blend of technology and humanity.'
keywords = ['AI', 'Fabric', 'open source framework', 'artificial intelligence', 'technology integration', 'Unix philosophy', 'prompt optimization']
+++

Today, I saw a project, Fabric, let's take a look together

## Introduction

Fabric is an open-source framework that uses artificial intelligence to augment human capabilities.

## Why Fabric

Because the author believes that AI is powerful, and there is no problem with its capabilities, but rather with integration.

The creation of Fabric aims to solve this problem, allowing everyone to finely apply AI to tackle daily challenges.

## Philosophy

The purpose of technology is to help humans thrive.

### Breaking problems into components

Break problems into components and then apply AI to each one, one at a time.

Somewhat similar to the Unix philosophy.

### Too many prompts

There are too many prompts now, and it's unclear whether they are useful, leading to decision paralysis.

### Fabric's prompts

- Use Markdown to help ensure maximum readability and editability.
- Very clear instructions.
- Tend to use almost exclusively the system part of the prompts.

## Quick Start

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

## Using the fabric client

```bash
# Set environment variables
export OPENAI_BASE_URL=...
export DEFAULT_MODEL=...
export OPENAI_API_KEY=...

pbpaste | fabric --pattern summarize
pbpaste | fabric --stream --pattern analyze_claims
yt --transcript https://youtube.com/watch?v=uXs-zPc63kM | fabric --stream --pattern extract_wisdom
pbpaste | analyze_claims --stream
```

## Analysis
### Entry fabric.py

Look at the client code `fabric/installer/client/cli/fabric.py`

`argparse` parses command-line arguments and then executes the corresponding function.

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

### Prompt patterns

The basic format of a pattern is as follows:

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

Let's take a look at `summarize_prompt/system.md`, the key is structuring.

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

- [GitHub](https://github.com/danielmiessler/fabric)
- [AI Blog - Learn AI from scratch](https://ai-blog.aihub2022.top/post/ai-fabric-intro/)
