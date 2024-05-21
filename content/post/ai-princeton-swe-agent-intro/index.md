+++
title = '[AI SWE-agent] 帮你解决Github中的bug和issue'
date = 2024-04-16T16:52:36+08:00
draft = false
categories = ['AI', 'AI程序员']
tags = ['AI', 'AI程序员', 'SWE-agent', 'princeton']
description = 'SWE-agent将语言模型（例如GPT-4）转化为软件工程代理，可以在真实的GitHub存储库中修复错误和问题。'
keywords = ['Princeton Swe Agent', 'SWE-agent', 'GPT-4', '软件工程代理', 'GitHub存储库', 'bug修复', 'issue解决']
+++

AI程序员竞争激烈。Devin出来后，开源的OpenDevin随后推出。

现在，Princeton的SWE-agent也来了。它能帮你修复GitHub中的bug和issue。好的地方在于，他提出了一个“代理-计算机接口（ACI）”。

我试了下，报错了，请求频率太高，没办法。谁有token能支持下吗？我可以再试下。

---

## 👋 概述
SWE-agent将语言模型（例如GPT-4）转化为软件工程代理，可以在真实的GitHub存储库中修复错误和问题。

在[SWE-bench](https://github.com/princeton-nlp/SWE-bench)上，SWE-agent解决了**12.29%**的问题，在整个测试集上取得了最先进的性能。

SWE-agent由普林斯顿大学的研究人员构建和维护。

![results+preview](https://github.com/princeton-nlp/SWE-agent/raw/main/assets/results+preview.png)

### ✨ 代理-计算机接口（ACI）
我们通过设计简单的以语言模型为中心的命令和反馈格式来实现这些结果，以便让语言模型更容易浏览存储库、查看、编辑和执行代码文件。我们将此称为**代理-计算机接口**（ACI），并构建了SWE-agent存储库，以便轻松迭代用于存储库级别编码代理的ACI设计。

就像典型的语言模型需要良好的提示工程一样，良好的ACI设计在使用代理时会产生更好的结果。正如我们在论文中所展示的，没有经过良好调整的ACI的基准代理要比SWE-agent表现得差得多。

SWE-agent包含我们在代理-计算机接口设计过程中发现非常有用的功能：
1. 我们添加了一个在发出编辑命令时运行的linter，并且如果代码在语法上不正确，则不让编辑命令通过。
2. 我们为代理提供了一个特殊构建的文件查看器，而不是让它只是简单地```cat```文件。我们发现，当每次显示100行时，此文件查看器的效果最佳。我们构建的文件编辑器具有向上和向下滚动以及在文件内执行搜索的命令。
3. 我们为代理提供了一个特殊构建的完整目录字符串搜索命令。我们发现，重要的是使此工具简洁地列出匹配项-我们只简单地列出每个至少有一个匹配项的文件。向模型显示有关每个匹配项的更多上下文信息被证明对模型而言过于混乱。
4. 当命令的输出为空时，我们返回一条消息，指示“您的命令已成功运行且未生成任何输出。”

阅读我们的论文以获取更多详细信息[即将推出！]。

```
@misc{yang2024sweagent,
      title={SWE-agent: Agent Computer Interfaces Enable Software Engineering Language Models}, 
      author={John Yang and Carlos E. Jimenez and Alexander Wettig and Shunyu Yao and Karthik Narasimhan and Ofir Press},
      year={2024},
}
```

## 🚀 设置

### 🏎️ 快速设置和运行

您可以直接使用Docker运行软件。

1. [安装 Docker](https://docs.docker.com/engine/install/)，然后在本地启动 Docker。
2. 运行 `docker pull sweagent/swe-agent:latest`
3. 将您的API令牌添加到一个名为 `keys.cfg` 的文件中，如下所述 [下方](#-add-your-api-keystokens)

然后运行

```bash
# 注意：
# 这假定 keys.cfg 在您当前的目录中（否则请修复下面的路径）
# 此命令相当于快速启动中显示的脚本
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(pwd)/keys.cfg:/app/keys.cfg \
  sweagent/swe-agent-run:latest \
  python run.py --image_name=sweagent/swe-agent:latest \
  --model_name gpt4 \
  --data_path https://github.com/pvlib/pvlib-python/issues/1603 \
  --config_file config/default_from_url.yaml  --skip_existing=False
```

> [!TIP]
> * 有关不同API密钥/令牌的更多信息，请参阅 [下方](#-add-your-api-keystokens)。
> * 如果您在Windows上使用docker，请使用 `-v //var/run/docker.sock:/var/run/docker.sock`
>   （双斜杠）进行转义（[更多信息](https://stackoverflow.com/a/47229180/)）。
> * 如果遇到问题，请参阅[安装问题部分](#-installation-issues)以获取更多帮助。

### 🐍 使用conda进行设置（开发版本）

要安装开发版本：

1. [安装 Docker](https://docs.docker.com/engine/install/)，然后在本地启动 Docker。
2. 克隆此存储库
3. [安装 Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)，然后使用 `conda env create -f environment.yml` 创建 `swe-agent` 环境
4. 使用 `conda activate swe-agent` 激活环境。
5. 运行 `./setup.sh` 创建 `swe-agent` docker 镜像。
6. 在此存储库的根目录创建一个 `keys.cfg` 文件（[见下方](#-add-your-api-keystokens)）

> [!WARNING]
> 在Windows上可能会遇到一些问题（我们正在解决）。
> 同时，您可以简单地使用Docker（见上文）。
> 如果您想要最新版本，您还可以通过运行此存储库根目录中的 `Dockerfile` 来构建自己的 `swe-agent-run` 容器，命令如下：
> `docker build -t sweagent/swe-agent-run:latest .`

> [!TIP]
> 如果遇到docker问题，请参阅[安装问题部分](#-installation-issues)以获取更多帮助。

### 🔑 添加您的API密钥/令牌

对于conda设置，请在此存储库的根目录创建一个 `keys.cfg` 文件，并使用您的API密钥填充它。

```
GITHUB_TOKEN: '在此处填写GitHub令牌（必填）'
OPENAI_API_KEY: '如果使用OpenAI模型，请在此处填写OpenAI API密钥（可选）'
```

如果您使用docker，请使用 [`-e` 选项](https://stackoverflow.com/a/30494145/) 将密钥传递给docker容器。

🔎 不同密钥的更多选项

所有密钥都是可选的。

```
GITHUB_TOKEN: '在此处填写GitHub令牌'
OPENAI_API_KEY: '如果使用OpenAI模型，请在此处填写OpenAI API密钥'
ANTHROPIC_API_KEY: '如果使用Anthropic模型，请在此处填写Anthropic API密钥'
TOGETHER_API_KEY: '如果使用Together模型，请在此处填写Together API密钥'
AZURE_OPENAI_API_KEY: '如果使用Azure OpenAI模型，请在此处填写Azure OpenAI API密钥'
AZURE_OPENAI_ENDPOINT: '如果使用Azure OpenAI模型，请在此处填写Azure OpenAI终结点'
AZURE_OPENAI_DEPLOYMENT: '如果使用Azure OpenAI模型，请在此处填写Azure OpenAI部署'
AZURE_OPENAI_API_VERSION: '如果使用Azure OpenAI模型，请在此处填写Azure OpenAI API版本'
OPENAI_API_BASE_URL: '如果使用本地或备用api终结点，请在此处填写LM基本URL'
```

有关获取[Anthropic](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)、[OpenAI](https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key)和[GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)令牌的教程，请参阅以下链接。

### 更多安装提示

如果您在运行docker时遇到问题

* 确保允许使用Docker套接字。在Docker桌面中，点击 *设置* > *高级* > *允许使用默认Docker套接字（需要密码）*
* 如果您的docker安装使用不同的套接字，您可能需要创建符号链接，请参阅[此命令示例](https://github.com/princeton-nlp/SWE-agent/issues/20#issuecomment-2047506005)

仍然有问题？请[打开GitHub问题](https://github.com/princeton-nlp/SWE-agent/issues/new/choose)！

## 🔥 快速开始：解决真实的GitHub问题！

使用此脚本，您可以在任何GitHub问题上运行SWE-agent！
```bash
python run.py --model_name gpt4 \
  --data_path https://github.com/pvlib/pvlib-python/issues/1603 \
  --config_file config/default_from_url.yaml
```

您也可以将其应用于本地存储库：
```bash
python run.py --model_name gpt4 \
  --data_path /path/to/my_issue.md \
  --repo_path /path/to/my/local/repo \
  --config_file config/default_from_url.yaml \
  --apply_patch_locally
```

> [!TIP]
> * 运行 `python run.py --help` 来查看所有可用选项。
> * 您可以通过提供 `--open_pr` 标志，让代理在问题已解决时自动打开PR。请负责任地使用此功能（在您自己的存储库中或经过仔细考虑后）。

* 查看 [`scripts/`](scripts/) 文件夹中的其他有用脚本和详细信息。
* 查看 [`config/`](config/) 文件夹以了解如何定义您自己的配置的详细信息！
* 查看 [`sweagent/agent/`](sweagent/agent/) 文件夹以了解基于配置的工作流背后的逻辑详情。
* 查看 [`sweagent/environment/`](sweagent/environment/) 文件夹以了解 `SWEEnv` 环境（接口 + 实现）的详情。
* 查看 [`trajectories/`](trajectories) 文件夹以了解 `run.py` 输出的详情。

Ollama 支持

通过指定 `--model` 为 `ollama:model_name` 并使用 `--host_url` 指向用于提供 ollama 的 URL（默认为 `http://localhost:11434`），可以使用 ollama 服务器提供的模型。有关使用 ollama 的更多详细信息，请参阅[此处](https://github.com/ollama/ollama/tree/main/docs)。

```bash
python run.py --model_name ollama:deepseek-coder:6.7b-instruct \
  --host_url http://localhost:11434 \
  --data_path https://github.com/pvlib/pvlib-python/issues/1603 \
  --config_file config/default_from_url.yaml
```

## 💽 基准测试

SWE-agent流水线包括两个步骤。首先，SWE-agent接收一个输入的GitHub问题，并返回一个试图修复它的拉取请求。我们称这一步骤为*推理*。第二步（目前仅适用于SWE-bench基准测试中的问题）是*评估*拉取请求，以验证它确实修复了问题。

> [!WARNING]
> 目前，对于一小部分存储库，在 `arm64` / `aarch64` 架构计算机上安装存在已知问题。我们正在努力解决，但如果您想在整个SWE-bench上运行和评估，最简单的方法是使用 `x86` 机器。

### 👩‍💻 推理
**在 *任何* GitHub 问题上进行推理**：请参阅[上文](#-quickstart-solve-real-life-github-issues-)。

**在SWE-bench上进行推理**：在[SWE-bench Lite](https://www.swebench.com/lite.html)上运行SWE-agent并生成补丁。
```bash
python run.py --model_name gpt4 \
  --per_instance_cost_limit 2.00 \
  --config_file ./config/default.yaml
```

如果您想在来自SWE-bench的*单个*问题上运行，请使用 `--instance_filter` 选项，如下所示：
```bash
python run.py --model_name gpt4 \
  --instance_filter marshmallow-code__marshmallow-1359
```

### 🧪 评估
此步骤仅适用于来自SWE-bench集合的问题。要评估生成的拉取请求：
```bash
cd evaluation/
./run_eval.sh <predictions_path>
```
将 `<predictions_path>` 替换为模型预测的路径，该路径应该是从*推理*步骤生成的。`<predictions_path>` 参数应类似于 `../trajectories/<username>/<model>-<dataset>-<hyperparams>/all_preds.jsonl`
* 有关评估工作原理的详细信息，请参阅 [`evaluation/`](evaluation/) 文件夹。

## 💫 贡献
- 如果您想提问、了解即将推出的功能，并参与未来的开发，请加入我们的[Discord社区](https://discord.gg/AVEFbBn2rH)!
- 如果您想为代码库做出贡献，我们欢迎[问题](https://github.com/princeton-nlp/SWE-agent/issues)和[拉取请求](https://github.com/princeton-nlp/SWE-agent/pulls)!
- 如果您想看到关于某个主题的文章或教程，请通过[问题](https://github.com/princeton-nlp/SWE-agent/issues)告诉我们。

联系人: [John Yang](https://john-b-yang.github.io/) 和 [Carlos E. Jimenez](http://www.carlosejimenez.com/) (邮箱: {jy1682, carlosej}@princeton.edu)。

## 🪪 许可证
MIT。请查看 `LICENSE` 文件。

---

- [官网](https://github.com/princeton-nlp/SWE-agent)
- 本文
    - [博客 - 从零开始学AI](https://blog.aihub2022.top/post/ai-princeton-swe-agent-intro/)
    - [微信 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649976847&idx=1&sn=29eabef2321bd02ed2eb331d452efe39&chksm=86c7cacab1b043dc0b435f1e3eed951cd29ce65500003010a3f8b9194760798a43fdf0eef42a#rd)
    - [CSDN - 从零开始学AI](https://blog.csdn.net/mahone3297/article/details/137859929)
    - [知乎 - 从零开始学AI](https://zhuanlan.zhihu.com/p/692920824)
