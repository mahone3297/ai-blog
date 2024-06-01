+++
title = '[AI Google] I/O 2024大会上我们宣布的100件事情'
date = 2024-05-28T10:03:51+08:00
draft = false
categories = ['AI', 'Google']
tags = ['AI', 'Google']
description = 'I/O 2024 发生了很多事情！无论你对最新的 Gemini 应用更新感兴趣，对开发者即将推出的内容感到特别兴奋，还是迫不及待想尝试最新的生成式 AI 工具，这里几乎为每个人都提供了一些内容。不信？以下是我们在过去两天宣布的 100 件事情。'
keywords = ['AI', 'Google', 'Gemini', '生成式 AI', '开发者', '搜索服务', 'Android', '负责任的 AI']
+++

![A black background with various 3D, rainbow-hued “I”s and “O”s falling down on the right-hand third of the screen.](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IO24_100Things_Hero.width-1200.format-webp.webp)

I/O 2024 发生了很多事情！无论你对最新的 Gemini 应用更新感兴趣，对开发者即将推出的内容感到特别兴奋，还是迫不及待想尝试最新的生成式 AI 工具，这里几乎为每个人都提供了一些内容。不信？以下是我们在过去两天宣布的 100 件事情。

## AI 时刻和模型动能

1. 我们推出了 Gemini 1.5 Flash：一款设计成轻量级的模型，旨在快速高效地提供规模化服务。1.5 Flash 是在 API 中提供的最快的 Gemini 模型。
2. 我们显著改进了 1.5 Pro，我们在各种任务上性能最佳的通用模型。
3. 1.5 Pro 和 1.5 Flash 均可在 Google AI Studio 和 Vertex AI 上以公共预览方式提供，具有 100 万令牌上下文窗口。
4. 1.5 Pro 也可通过 Google AI Studio 和 Vertex AI 的等待列表向开发者提供具有 200 万令牌上下文窗口的版本。

{{< video "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/gemini_2M_tokens_aao_TF9UOn5.mp4" >}}

Gemini 1.5 的 200 万令牌功能与主要基础模型的上下文长度进行比较。

5. 我们分享了 Project Astra：我们对 AI 助手未来的愿景。

6. 我们宣布了 Trillium，我们定制 AI 加速器 Tensor Processing Unit (TPU) 的第六代。这是迄今为止性能最好的 TPU。

7. 与 TPU v5e 相比，Trillium TPU 的每个芯片的峰值计算性能提高了 4.7 倍。

8. 它们也是我们最具可持续性的一代：与 TPU v5e 相比，Trillium TPU 的能效提高了超过 67%。

9. 我们还演示了 NotebookLM 的早期音频概览的原型，该概览使用一系列上传的材料为用户创建个性化的口头讨论。

10. 我们宣布了使用 Google Search 进行基础性搜索的工具 —— 连接 Gemini 模型与世界知识、广泛可能的主题或互联网上最新信息的工具 —— 现在已经在 Vertex AI 上普遍可用。

11. 我们在 Gemini API 和 AI Studio 中添加了音频理解功能，因此 Gemini 1.5 Pro 现在可以跨图片和音频进行推理，用于 AI Studio 中上传的视频。

12. 从 Pixel 开始，使用 Gemini Nano 和 Multimodality 的应用程序将能够像人类一样理解世界 —— 不仅通过文本输入，还通过视觉、听觉和口语。

## 生成式媒体模型和实验室实验
13. 我们宣布了 Imagen 3，我们迄今为止质量最高的图像生成模型。

14. Imagen 3 理解你提示背后的自然语言和意图，并结合更长提示中的细节。这有助于它生成令人难以置信的细节，产生比我们先前的模型更少分散注意力的视觉工艺品的逼真、栩栩如生的图像。

15. Imagen 3 也是我们迄今为止渲染文本最好的模型 —— 这对于图像生成模型来说是一个挑战。

16. 我们向 ImageFX 的可信测试者推出了 Imagen 3，你可以注册加入等待列表。

17. Imagen 3 也将于今年夏天推出到 Vertex AI。

18. 然后我们宣布了 Veo，我们迄今为止最能干的视频生成模型。它可以生成高质量的 1080p 分辨率视频，超过一分钟，采用各种电影和视觉风格。

19. 我们还将在未来将 Veo 的一些功能带到 YouTube Shorts 和其他产品中。

20. 我们展示了 Veo 能帮助艺术家做什么，通过与电影制作人合作 —— 包括 Donald Glover，他用 Veo 进行了一部电影项目的实验。

21. 我们突出了 Music AI Sandbox，一套音乐 AI 工具，允许人们从头开始创建新的乐器部分，在跟踪器之间转移风格等。你现在可以在 YouTube 上找到一些全新的合作歌曲 —— 包括 Wyclef Jean 和 Marc Rebillet 的歌曲。

22. 还要确保查看 Infinite Wonderland，这是一个体验，艺术家和谷歌创意人员一起实验，不断调整一个 AI 模型，无尽地重新想象小说《爱丽丝漫游奇境记》的视觉世界。Infinite Wonderland 的读者可以根据每个艺术家各自的风格为书中的每一句话生成似乎无限的图像。

23. 我们宣布了 VideoFX，我们最新的实验性工具，使用 Google DeepMind 的生成式视频模型 Veo，让你将一个想法变成一个视频片段。

24. 它还配备了一个故事板模式，让你逐个场景迭代，并向你的最终视频添加音乐。

{{< video "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/F168_fxtools_VideoFX_StoryBoard_16x9_v32.mp4" >}}

25. 我们在 ImageFX 中增加了更多编辑控制功能 —— 这是社区的一个最受欢迎的功能请求 —— 这样你就可以通过简单地刷过图像来添加、删除或更改元素。

26. ImageFX 还将使用 Imagen 3 来解锁更多逼真的效果，拥有更丰富的细节，更少的视觉工艺品和更准确的文本渲染。

27. MusicFX 有一个名为 “DJ 模式”的新功能，可以帮助你通过结合流派和乐器来混合节奏，利用生成式 AI 的力量使音乐故事栩栩如生。

28. 从本周起，ImageFX 和 MusicFX 现在通过实验室在 100 多个国家和地区提供服务。

## 通过 Gemini 应用完成更多任务的新方式
29. 我们将 Gemini 1.5 Pro，我们的尖端模型，引入到 Gemini 高级订阅者中 —— 这意味着 Gemini 高级现在拥有 100 万令牌的上下文窗口，并且可以做一些像理解 1500 页 PDF 文件这样的事情。

30. 这也意味着 Gemini 高级现在拥有世界上任何商业可用聊天机器人中最大的上下文窗口。

31. 我们添加了通过 Google Drive 或直接从您的设备上传文件到 Gemini 高级的功能。

32. 不久，Gemini 高级将帮助您分析数据，快速发现见解，并从上传的数据文件（如电子表格）构建图表。

33. 对旅行者来说，有个好消息：Gemini 高级有一个新的规划功能，超越了一系列建议活动的列表，实际上会为您创建一个定制的行程。

{{< video "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/smaller-Gemini_Miami_Planner_v10_Combo_LandscapeMP4_1.mp4" >}}

34. 然后是 Gemini Live，适用于 Gemini 高级订阅者，这是一种新的、以移动为主的对话体验，使用最先进的语音技术，帮助您与 Gemini 进行更自然、更直观的口头对话。

35. Gemini Live 让您可以从 10 种自然语音中选择它可以回答您的声音；此外，您可以按自己的节奏说话，或者在回答中间提出澄清问题。

36. Google Messages 中的 Gemini 现在可以让您在与朋友交流的同一应用程序中与 Gemini 聊天。

37. Gemini 高级订阅者很快就可以创建 Gems，即为您梦想的任何情景量身定制的 Gemini 版本。只需描述您想要 Gem 做什么以及您希望它如何回应，Gemini 将接受这些指示并为您特定的需求创建一个 Gem。

38. 还要留意与 Gemini 连接的更多谷歌工具，包括 Google 日历、任务、Keep 和时钟。

## 让搜索为您服务的更新
39. 我们正在使用定制的新 Gemini 模型为 Google 搜索带来 Gemini 的高级功能 —— 包括多步推理、规划和多模态 —— 与我们一流的搜索系统相结合。

40. 搜索中的 AI 概述将从本周开始向美国所有人推出，更多国家将很快加入。

{{< video "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AI_Overviews_-_Sofa_qGYHf9J_f4Fy1lb.mp4" >}}

41. 多步推理功能即将在美国英语查询的搜索实验室中推出 AI 概述。因此，您可以询问像 “在波士顿找到最好的瑜伽或普拉提工作室，并显示有关其入门优惠和从比肯山到达的步行时间的详细信息” 这样复杂的问题，而不是将您的问题分成多个搜索。

42. 很快，当您对某个主题不熟悉或试图深入了解某个主题时，您将能够通过选项调整您的 AI 概述，以简化语言或更详细地介绍。

43. 搜索还将获得新的规划功能。例如，定制的餐饮和旅行规划将于今年晚些时候在搜索实验室中推出，很快将推出更多类别，如派对和健身。

44. 由于视频理解技术的进步，您现在可以通过视频提出问题。搜索可以为您解答复杂的视觉问题，然后通过 AI 概述解释下一步操作，并提供资源。

45. 不久，当您寻找新的创意时，搜索中的生成式 AI 也将创建一个 AI 组织的结果页面。这些 AI 组织的搜索结果页面将在您搜索餐饮、菜谱、电影、音乐、书籍、酒店、购物等类别时提供。

## Workspace 和照片中 Gemini 模型的帮助
46. Gemini 1.5 Pro 现在通过 Workspace 实验室在 Gmail、文档、Drive、幻灯片和表格的侧边栏中可用 —— 下个月将向我们的 Gemini for Workspace 客户和 Google One AI 高级订阅者推出。

47. 您将能够使用 Gmail 的侧边栏对电子邮件进行摘要，以获取最重要的详细信息和行动项目。

48. 除了摘要之外，Gmail 的移动应用程序很快将使用 Gemini 提供另外两个新功能：上下文智能回复和 Gmail 问答。

49. 在未来几周内，Gmail 和文档中的“帮助我写”将支持西班牙语和葡萄牙语。

50. 今年晚些时候在实验室中，您甚至可以要求 Gemini 自动在 Drive 中组织电子邮件附件，生成包含数据的表格，然后使用数据问答分析数据。

51. Google 照片中的一个名为 “问照片” 的新实验性功能使查找特定回忆或回忆图库中包含的信息变得更加容易。该功能使用 Gemini 模型，并将在未来几个月内推出。

{{< video "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/IO24_AskPhotos_InLine_BdayParty_1_sFo2Epv.mp4" >}}

52. 您还可以使用 Ask Photos 从最近的旅行中创建一个精彩的画廊，它甚至会为您撰写个性化的标题，供您在社交媒体上分享。

## Android 的进步
53. 从今年晚些时候开始，Pixel 将使用 Gemini Nano —— Android 内置的设备上的基础模型 —— 具有多模态功能。除了处理文本输入外，您的 Pixel 手机还将能够更好地理解上下文中的更多信息，如景观、声音和口语。

54. Talkback 是 Android 设备的辅助功能，它帮助盲人和低视力人士使用触摸和语音反馈更好地与他们的设备进行交互，由于 Gemini Nano 具有多模态功能，这一功能正在得到改进。

55. 一项新的选择性骗局保护功能将使用 Gemini Nano 的设备 AI 以隐私保护的方式帮助检测电话诈骗。请在今年晚些时候查看更多详细信息。

56. 我们宣布 Circle to Search 目前已在超过 1 亿部 Android 设备上可用，并且我们计划在今年年底前将其数量翻倍。

57. 不久之后，您将能够在 Android 上使用 Gemini 创建、拖放生成的图像到 Gmail、Google Messages 等应用程序中，或询问您正在观看的 YouTube 视频相关信息。

58. 如果您拥有 Gemini 高级订阅，您还可以选择 “询问此 PDF” 以快速获取答案，而无需滚动多页。

59. 学生现在可以直接从选择的 Android 手机和平板电获得学习帮助，使用 Circle to Search 功能。这一功能由 LearnLM 提供支持 —— 我们基于 Gemini 的新模型系列，专门为学习而调整。

60. 今年晚些时候，Circle to Search 将能够解决更多涉及符号公式、图表、图形等复杂问题。

{{< video "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Circle_to_Search_Homework_Help_Samsung_1.mp4" >}}

61. 哦，我们推出了 Android 15 的第二个测试版。

62. Theft Detection Lock 使用强大的谷歌 AI 来感知您的设备是否被抢夺，并迅速锁定您手机上的信息。

63. Android 15 将引入私人空间功能，允许您选择应用程序保持在一个单独的空间内，并需要额外的身份验证才能打开。

64. 如果单独的锁屏对于您的私人空间不够，您甚至可以完全隐藏它的存在。

65. 今年晚些时候，Google Play Protect 将使用设备上的 AI 帮助发现试图隐藏其操作以进行欺诈或网络钓鱼的应用程序。

66. 我们将在 Google Messages 中为日本用户带来更新的消息体验，支持 RCS。

67. 不久之后，在美国，您将能够创建仅包含文本的数字通行证。只需拍摄通行证的照片（如保险卡或活动门票），然后将其轻松添加到您的 Google 钱包中以便快速访问。

68. 我们展示了增强现实内容将直接在 Google 地图中提供，为我们与三星和高通合作为 Android 生态系统打造的扩展现实（XR）平台奠定了基础。

69. 您现在可以在 Max 和 Peacock 上观看您最喜爱的节目的剧集，或者在部分车辆上开始愤怒的小鸟游戏，这些车辆具有内置的 Google 功能。

70. 我们还将 Google Cast 带到了搭载 Android Automotive OS 的汽车上，从今年晚些时候开始，首先是 Rivian，这样您就可以轻松地从手机向车载投放视频内容。

71. 今年晚些时候，Wear OS 5 将对手表的电池寿命进行优化。例如，参加户外马拉松活动将比使用 Wear OS 4 的手表节省多达 20% 的电力。

72. Wear OS 5 还将为健身应用程序提供支持更多数据类型的选项，如地面接触时间、步幅长度和垂直摆动。

73. 现在，使用个性化 AI 生成的描述，在 Google TV 和其他 Android TV OS 设备上选择要观看的内容更加容易，这得益于我们的 Gemini 模型。

74. 这些 AI 生成的描述还将填补电影和节目中缺失或未翻译的描述。

75. 一个有趣的统计数据：自推出以来，人们已经建立了超过 10 亿个快速配对连接。

76. 本月晚些时候，您将能够使用快速配对在 Find My Device 应用程序中连接和查找物品，如您的钥匙、钱包或行李箱，配合 Chipolo 和 PebbleBee 的蓝牙跟踪器标签（更多合作伙伴即将加入）。

## 开发者的进展
77. 您可以参加 Gemini API 开发者竞赛，成为发现最有帮助和开创性的 AI 应用程序的一部分。奖品是一辆 1981 年定制的电动改装德洛瑞安。

78. 我们推出了 PaliGemma，我们第一个为视觉问答和图像字幕优化的视觉语言开放模型。

79. 我们预览了 Gemma 的下一个版本，Gemma 2。它建立在全新的架构上，并将包括一个更大的 27B 参数实例，该实例的性能优于其两倍大小的模型，并在单个 TPU 主机上运行。

![一个黑色屏幕，标题为“Gemma 2”。下面写着：“27B 参数。优化适用于 TPUs 和 GPUs。性能优于两倍大小的模型。”](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Dev_27B_1KVcc5s.width-1000.format-webp.webp)

80. 现在可以使用 Gemini 模型帮助开发者在 Android Studio、IDX、Firebase、Colab、VSCode、Cloud 和 Intellj 中提高生产力。

81. Gemini 1.5 Pro 将于今年晚些时候进入 Android Studio。配备了较大的上下文窗口，该模型能够提供更高质量的响应，并解锁了多模态输入等用例。

82. Google AI Studio 现在在包括英国和欧盟在内的 200 多个国家/地区提供服务。

83. Gemini API 现在支持并行函数调用和视频帧提取。

84. 而且，Gemini API 中的新上下文缓存功能将于下个月推出，您将能够通过以较低成本缓存经常使用的上下文文件来简化大型提示的工作流程。

85. Android 现在提供一流的支持 Kotlin 多平台，以帮助开发者在各个平台上共享应用程序的业务逻辑。

86. 可调整大小的模拟器、Compose UI 检查模式和由 Firebase 提供支持的 Android 设备流式传输是所有可以帮助开发者构建各种形式因素的新产品。

87. 从 Chrome 126 开始，Gemini Nano 将内置到 Chrome 桌面客户端中。

88. 多页面应用程序的 View Transitions API，这是一个广受欢迎的功能，现在可用，开发者可以轻松构建流畅、流畅的应用程序导航，而不受网站架构的限制。

89. 我们推出了 Project IDX，我们的新一体化开发者体验，用于全栈、多平台应用程序，现在已经向所有人开放尝试。

90. Firebase 推出了 Firebase Genkit 的测试版，这将使开发者更轻松地将生成式 AI 体验集成到他们的应用程序中。

91. Firebase 还发布了 Firebase Data Connect，这是开发者使用 SQL 与 Firebase（通过 Google Cloud SQL）的新方法。这不仅将 SQL 工作流程引入 Firebase，还将减少开发者需要编写的应用程序代码量。

92. 我们与 James Manyika、Jeff Dean 和 Koray Kavukcuoglu 一起深入探讨了驱动我们 AI 的技术和研究。

## 负责任的 AI 进展
93. 我们正在通过一种我们称之为“AI 辅助红队”的新技术增强红队活动 —— 这是一种已被证明的实践，我们主动测试自己系统的弱点并试图破解它们。

94. 我们还将 SynthID 扩展到两种新的模态：文本和视频。

95. SynthID 文本水印功能将在未来几个月内通过我们更新的负责任生成式 AI 工具包开源。

96. 我们宣布了 LearnLM，这是一个基于 Gemini 并针对学习进行优化的新模型系列。LearnLM 已经为我们的产品提供了一系列功能，包括 Gemini、搜索、YouTube 和 Google Classroom。

{{< video "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/RAI_LearnLM_Gemini_Chat_v26_InlineAnimation_Shorter_9a5XA1g.mp4" >}}

97. 我们将与哥伦比亚教师学院、亚利桑那州立大学、纽约大学 Tisch 学院和可汗学院等机构的专家合作，进一步完善和扩展 LearnLM，使其超越我们的产品范围。

98. 我们还与 MIT RAISE 合作开发了一门在线课程，该课程旨在使教育工作者有效地在课堂上使用生成式 AI。

99. 我们开发了一个名为 Illuminate 的新实验性工具，使知识更易于获取和消化。

100. Illuminate 可以生成一个由两个 AI 生成的声音组成的对话，概述研究论文的关键见解。您可以立即注册尝试。

---

- [原文](https://blog.google/technology/ai/google-io-2024-100-announcements/)
- [博客 - 从零开始学AI](https://blog.aihub2022.top/post/ai-google-io-2024-100-announcements/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977258&idx=1&sn=e078a722ebaba041f6a8149b09a0f963&chksm=86c7cb6fb1b042796c9f186711680815259e895ead723a37304aeebf15c11038d43dd2e45b72#rd)
