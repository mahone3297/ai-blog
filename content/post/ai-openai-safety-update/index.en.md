+++
title = '[AI OpenAI] OpenAI Safety Update'
date = 2024-05-27T09:58:48+08:00
draft = false
categories = ['AI', 'OpenAI-blog']
tags = ['AI', 'OpenAI']
description = "Sharing our practices as part of the AI Seoul Summit. Learn about OpenAI's safety updates and commitments. Explore 10 key safety practices actively used and improved upon by OpenAI."
keywords = ["OpenAI", "AI Seoul Summit", "safety update", "AI safety", "safety practices", "model safety", "safety measures", "alignment research", "safety monitoring", "child protection", "election integrity", "impact assessment", "policy analysis", "security measures", "government partnership", "safety decision making", "Board oversight"]
+++

Sharing our practices as part of the AI Seoul Summit

![safety-blog-cover-02](https://images.ctfassets.net/kftzwdyauwt9/54pUOkZ0poSpo9udfZmN3g/e90a4235b3d8537bdddfcc7219b636d1/safety-blog-cover-02.jpg?w=1920&q=90&fm=webp)

We are proud to build and release models that are industry-leading on both capabilities and safety.

More than a hundred million users and millions of developers rely on the work of our safety teams. We view safety as something we have to invest in and succeed at across multiple time horizons, from aligning today’s models to the far more capable systems we expect in the future. This work has always happened across OpenAI and our investment will only increase over time.

We believe in a balanced, scientific approach where safety measures are integrated into the development process from the outset. This ensures that our AI systems are both innovative and reliable, and can deliver benefits to society.

At today’s AI Seoul Summit, we're joining industry leaders, government officials, and members of civil society to discuss AI safety. While there is still more work to do, we are encouraged by the additional Frontier AI Safety Commitments that OpenAI and other companies agreed upon today. The Commitments call on companies to safely develop and deploy their frontier AI models while sharing information about their risk mitigation measures, aligning with steps we have already taken. These include a pledge to publish safety frameworks like the Preparedness Framework(opens in a new window) we developed and adopted last year. 

We are sharing 10 practices we actively use and improve upon.

1. **Empirical model red-teaming and testing before release:** We empirically evaluate model safety before release, internally and externally, according to our Preparedness Framework and voluntary commitments. We won’t release a new model if it crosses a “Medium” risk threshold from our Preparedness Framework, until we implement sufficient safety interventions to bring the post-mitigation score back to “Medium”. More than 70 external experts helped to assess risks associated with GPT-4o through our external red teaming efforts, and we used these learnings to build evaluations based on weaknesses in earlier checkpoints in order to better understand later checkpoints.
2. **Alignment and safety research:** Our models have become significantly safer over time. This can be attributed to building smarter models which typically make fewer factual errors and are less likely to output harmful content even under adversarial conditions like jailbreaks. It is also due to our focused investment in practical alignment, safety systems, and post-training research. These efforts work to improve the quality of human-generated fine-tuning data, and in the future, the instructions our models are trained to follow. We are also conducting and publishing fundamental research aimed at dramatically improving our systems’ robustness to attacks like jailbreaks(opens in a new window).
3. **Monitoring for abuse:** As we have deployed increasingly capable language models via our API and ChatGPT, we have leveraged a broad spectrum of tools, including dedicated moderation(opens in a new window) models and the use of our own models for monitoring of safety risks and abuse. We have shared some critical findings along the way, including a joint disclosure (with Microsoft) of state actor abuse of our technology, so that others can better safeguard against similar risks. We also use GPT-4 for content policy development and content moderation decisions, enabling a faster feedback loop for policy refinement and less abusive material exposed to human moderators.
4. **Systematic approach for safety:** We implement a range of safety measures at every stage of the model's life cycle, from pre-training to deployment. As we advance in developing safer and more aligned model behavior, we also invest in pre-training data safety, system-level model behavior steering, data flywheel for continued safety improvement and robust monitoring infrastructure.
5. **Protecting children:** A critical focus of our safety work is protecting children. We’ve built strong default guardrails and safety measures into ChatGPT and DALL·-E that mitigate potential harms to children. In 2023, we partnered with Thorn’s Safer to detect, review and report Child Sexual Abuse Material to the National Center for Missing and Exploited Children if users attempt to upload it to our image tools. We continue to collaborate with Thorn, the Tech Coalition, All Tech is Human, Commonsense Media(opens in a new window) and the broader tech community to uphold the Safety by Design principles. 
6. **Election integrity:** We’re collaborating with governments and stakeholders to prevent abuse, ensure transparency on AI-generated content, and improve access to accurate voting information. To achieve this, we’ve introduced a tool for identifying images created by DALL·E 3, joined the steering committee of the Content Authenticity Initiative (C2PA), and incorporated C2PA metadata in DALL·E 3 to help people understand the source of media they find online. ChatGPT now directs users to official voting information sources in the U.S. and Europe. Additionally, we support the bipartisan “Protect Elections from Deceptive AI Act”(opens in a new window) proposed in the U.S. Senate, which would ban misleading AI-generated content in political advertising. 
7. **Investment in impact assessment and policy analysis:** Our impact assessment efforts have been widely influential in research, industry norms, and policy, including our early work(opens in a new window) on measuring the chemical, biological, radiological, and nuclear (CBRN) risks associated with AI systems, and our research estimating the extent to which different occupations and industries might be impacted by language models. We also publish pioneering work on how society can best manage associated risks – for example, by working with external experts to assess the implications of language models for influence operations(opens in a new window). 
8. **Security and access control measures:** We prioritize protecting our customers, intellectual property, and data. We deploy our AI models to the world as services, controlling access via API which enables policy enforcement. Our cybersecurity efforts include restricting access to training environments and high-value algorithmic secrets on a need-to-know basis, internal and external penetration testing, a bug bounty program, and more. We believe that protecting advanced AI systems will benefit from an evolution of infrastructure security and are exploring novel controls like confidential computing for GPUs and applications of AI to cyber defense to protect our technology. To empower cyber defense, we’re funding third-party security researchers with our Cybersecurity Grant Program.
9. **Partnering with governments:** We partner with governments around the world to inform the development of effective and adaptable AI safety policies. This includes showing our work and sharing our learnings, collaborating to pilot government and other third party assurance, and informing the public debate over new standards and laws.
10. **Safety decision making and Board oversight:** As part of our Preparedness Framework, we have an operational structure for safety decision-making. Our cross-functional Safety Advisory Group reviews model capability reports and makes recommendations ahead of deployment. Company leadership makes the final decisions, with the Board of Directors exercising oversight over those decisions. 

This approach has enabled us to build and deploy safe and capable models at the current level of capability.

As we move towards our next frontier model, we recognize we will need to evolve our practices, in particular to increase our security posture to ultimately be resilient to sophisticated state actor attacks and to ensure that we introduce additional time for safety testing before major launches. We and the field have a hard problem to solve in order to safely and beneficially deliver increasingly capable AI. We plan to share more on these evolving practices in the coming weeks.

---

- [original](https://openai.com/index/openai-safety-update/)
- 本文
    <!-- - [Blog | Learn AI from scratch](...) -->
    <!-- - [公众号 - 从零开始学AI](...) -->
    <!-- - [CSDN - 从零开始学AI](...) -->
    <!-- - [掘金 - 从零开始学AI](...) -->
    <!-- - [知乎 - 从零开始学AI](...) -->
    <!-- - [阿里云 - 从零开始学AI](...) -->
    <!-- - [腾讯云 - 从零开始学AI](...) -->
