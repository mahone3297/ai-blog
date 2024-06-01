+++
title = '[AI OpenAI] Disrupting deceptive uses of AI by covert influence operations'
date = 2024-06-01T16:53:51+08:00
draft = false
categories = ['AI', 'OpenAI']
tags = ['AI', 'OpenAI']
description = 'OpenAI disrupts covert influence operations leveraging AI models, ensuring transparency and safety in AI-generated content.'
keywords = ['AI', 'OpenAI', 'covert influence operations', 'AI safety', 'disrupting deceptive uses']
+++

We’ve terminated accounts linked to covert influence operations; no significant audience increase due to our services.

![The image is an abstract background with soft, blended hues of purple, pink, and blue. The pastel colors mix seamlessly, creating a dreamy and serene atmosphere, reminiscent of a twilight sky or an ethereal mist.](https://images.ctfassets.net/kftzwdyauwt9/4oeOcYU7pdkkcl4y3sjZOr/4122e73e2f9fc8d6522fbc4025dbf7af/IO_Blog_Image.png?w=1920&q=90&fm=webp)

OpenAI is committed to enforcing policies that prevent abuse and to improving transparency around AI-generated content. That is especially true with respect to detecting and disrupting covert influence operations (IO), which attempt to manipulate public opinion or influence political outcomes without revealing the true identity or intentions of the actors behind them. 

In the last three months, we have disrupted five covert IO that sought to use our models in support of deceptive activity across the internet. As of May 2024, these campaigns do not appear to have meaningfully increased their audience engagement or reach as a result of our services. 

This blog describes the threat actors we disrupted, attacker trends we identified, and important defensive trends - including how designing AI models with safety in mind in many cases prevented the threat actors from generating the content they desired, and how AI tools have made our own investigations more efficient. Alongside this blog, we are publishing a trend analysis that describes the behavior of these malicious actors in detail.

[Read the full report](https://downloads.ctfassets.net/kftzwdyauwt9/5IMxzTmUclSOAcWUXbkVrK/3cfab518e6b10789ab8843bcca18b633/Threat_Intel_Report.pdf)

Threat actors work across the internet. So do we. By collaborating with industry, civil society, and government we tackle the creation, distribution, and impact of IO content.  Our investigations and disruptions were made possible in part because there’s been so much detailed threat reporting over the years by distribution platforms and the open-source community. OpenAI is publishing these findings, as other tech companies do, to promote information sharing and best practices amongst the broader community of stakeholders.

## Disruption of covert influence operations
Over the last three months, our work against IO actors has disrupted covert influence operations that sought to use AI models for a range of tasks, such as generating short comments and longer articles in a range of languages, making up names and bios for social media accounts, conducting open-source research, debugging simple code, and translating and proofreading texts. 

Specifically, we disrupted: 

- A previously unreported operation from Russia, which we dubbed Bad Grammar, operating mainly on Telegram and targeting Ukraine, Moldova, the Baltic States and the United States. The people behind Bad Grammar used our models to debug code for running a Telegram bot and to create short, political comments in Russian and English that were then posted on Telegram.  
- An operation originating in Russia known as Doppelganger. People acting on behalf of Doppelganger used our models to generate comments in English, French, German, Italian and Polish that were posted on X and 9GAG; translate and edit articles in English and French that were posted on websites linked to this operation; generate headlines; and convert news articles into Facebook posts. 
- A Chinese network known as Spamouflage, which used our models to research public social media activity, generate texts in languages including Chinese, English, Japanese and Korean that were then posted across platforms including X, Medium and Blogspot, and debug code for managing databases and websites, including a previously unreported domain, revealscum[.]com. 
- An Iranian operation known as the International Union of Virtual Media (IUVM), which used our models to generate and translate long-form articles, headlines and website tags that were then published on a website linked to this Iranian threat actor, iuvmpress[.]co; 
- Activity by a commercial company in Israel called STOIC, because technically we disrupted the activity, not the company. We nicknamed this operation Zero Zeno, for the founder of the stoic school of philosophy. The people behind Zero Zeno used our models to generate articles and comments that were then posted across multiple platforms, notably Instagram, Facebook, X, and websites associated with this operation.   

The content posted by these various operations focused on a wide range of issues, including Russia’s invasion of Ukraine, the conflict in Gaza, the Indian elections, politics in Europe and the United States, and criticisms of the Chinese government by Chinese dissidents and foreign governments.  

So far, these operations do not appear to have benefited from meaningfully increased audience engagement or reach as a result of our services. Using Brookings’ Breakout Scale, which assesses the impact of covert IO on a scale from 1 (lowest) to 6 (highest), none of the five operations included in our case studies scored higher than a 2 (activity on multiple platforms, but no breakout into authentic communities). 

## Attacker trends
Based on the investigations into influence operations detailed in our report, and the work of the open-source community, we have identified the following trends in how covert influence operations have recently used artificial intelligence models like ours. 

- Content generation: All these threat actors used our services to generate text (and occasionally images) in greater volumes, and with fewer language errors than would have been possible for the human operators alone. 
- Mixing old and new: All of these operations used AI to some degree, but none used it exclusively. Instead, AI-generated material was just one of many types of content they posted, alongside more traditional formats, such as manually written texts or memes copied from across the internet.  
- Faking engagement: Some of the networks we disrupted used our services to help create the appearance of engagement across social media - for example, by generating replies to their own posts. This is distinct from attracting authentic engagement, which none of the networks we describe here managed to do to a meaningful degree.  
- Productivity gains: Many of the threat actors that we identified and disrupted used our services in an attempt to enhance productivity, such as summarizing social media posts or debugging code.

## Defensive trends
While much of the public debate so far has focused on the potential or actual use of AI by attackers, it is important to remember the advantages that AI offers to defenders. Our investigations also benefit from industry sharing and open-source research.

- Defensive design: We impose friction on threat actors through our safety systems, which reflect our approach to responsibly deploying AI. For example, we repeatedly observed cases where our models refused to generate the text or images that the actors asked for. 
- AI-enhanced investigation: Similar to our approach to using GPT-4 for content moderation and cyber defense, we have built our own AI-powered tools to make our detection and analysis more effective. The investigations described in the accompanying report took days, rather than weeks or months, thanks to our tooling. As our models improve, we’ll continue leveraging their capabilities to improve our investigations too.   
- Distribution matters: Like traditional forms of content, AI-generated material must be distributed if it is to reach an audience. The IO posted across a wide range of different platforms, including X, Telegram, Facebook, Medium, Blogspot, and smaller forums, but none managed to engage a substantial audience. 
- Importance of industry sharing: To increase the impact of our disruptions on these actors, we have shared detailed threat indicators with industry peers. Our own investigations benefited from years of open-source analysis conducted by the wider research community. 
- The human element: AI can change the toolkit that human operators use, but it does not change the operators themselves. Our investigations showed that these actors were as prone to human error as previous generations have been - for example, publishing refusal messages from our models on social media and their websites. While it is important to be aware of the changing tools that threat actors use, we should not lose sight of the human limitations that can affect their operations and decision making.  

We are committed to developing safe and responsible AI, which involves designing our models with safety in mind and proactively intervening against malicious use. Detecting and disrupting multi-platform abuses such as covert influence operations can be challenging because we do not always know how content generated by our products is distributed. But we are dedicated to finding and mitigating this abuse at scale by harnessing the power of generative AI.

---

- [original](https://openai.com/index/disrupting-deceptive-uses-of-AI-by-covert-influence-operations/)
- [Blog | Learn AI from scratch](https://blog.aihub2022.top/en/post/ai-openai-disrupting-deceptive-uses-of-ai-by-covert-influence-operations/)
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
