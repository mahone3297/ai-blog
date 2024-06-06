+++
title = '[AI OpenAI] Securing Research Infrastructure for Advanced AI'
date = 2024-06-06T09:41:45+08:00
draft = false
categories = ['AI', 'OpenAI']
tags = ['AI', 'OpenAI']
description = 'Outlining the architecture supporting the secure training of frontier AI models at OpenAI.'
keywords = ['AI', 'OpenAI', 'secure AI training', 'research infrastructure', 'AI security']
+++

We outline our architecture that supports the secure training of frontier models.

![Media > Security](https://images.ctfassets.net/kftzwdyauwt9/3ND00DMJCGocsrnNtx1E15/4037d25fe74733aaf604061293faf647/Alignment_Blog_5_29.png?w=1920&q=90&fm=webp)

We’re sharing some high-level details on the security architecture of our research supercomputers.

OpenAI operates some of the largest AI training supercomputers, enabling us to deliver models that are industry-leading in both capabilities and safety while advancing the frontiers of AI. Our mission is to ensure that advanced AI benefits everyone, and the foundation of this work is the infrastructure that powers our research.

To achieve this mission safely, we prioritize the security of these systems. Here, we outline our current architecture and operations that support the secure training of frontier models at scale. This includes measures designed to protect sensitive model weights within a secure environment for AI innovation. While these security features will evolve over time, we think it’s valuable to provide a current snapshot of how we think about security of our research infrastructure. We hope this insight will assist other AI research labs and security professionals as they approach securing their own systems (and we're hiring).

## Threat Model
Research infrastructure presents a unique security challenge given the diverse and rapidly evolving nature of workloads required for experimentation.

Research infrastructure is home to several important types of assets that are essential to protect. Among these, unreleased model weights are paramount to protect because they represent core intellectual property and need to be safeguarded from unauthorized release or compromise.

With this purpose in mind, OpenAI created a series of research environments dedicated to the development and security of frontier models. The research infrastructure must support the protection of model weights, algorithmic secrets, and other sensitive assets used for developing frontier models by shielding them against unauthorized exfiltration and compromise. At the same time, researchers must have sufficient access to resources and the underlying compute infrastructure in order to be productive and efficient.

## Architecture
Our technical architecture for research is built on Azure, utilizing Kubernetes for orchestration. We leverage both to implement a security architecture that enables research while fitting our threat model.

### 1. Identity Foundation

Our identity foundation is built on Azure Entra ID (formerly Azure Active Directory). Azure Entra ID integrates with internal authentication and authorization frameworks and controls. Azure Entra ID enables risk-based verification on session creation, use of authentication tokens, and detection of anomalous logins. These features supplement our internal detection tools in identifying and blocking potential threats.

### 2. Kubernetes Architecture

We use Kubernetes to orchestrate and manage workloads in our infrastructure. Research workloads are protected by Kubernetes role-based access control (RBAC) policies to adhere to least-privilege principles. Admission Controller policies set a security baseline for workloads, controlling container privileges and network access to reduce risks.

We rely on modern VPN technology to provide secure networking to our research environments. Network policies define how workloads communicate with external services. We adopt a deny-by-default egress policy and explicitly allowlist authorized external communication paths. We extensively use private link network routing where offered to eliminate required routes to the Internet and keep this allowlist short.

For some higher-risk tasks we use gVisor(opens in a new window), a container runtime that provides additional isolation. This defense-in-depth approach ensures robust security and efficient management of workloads.

### 3. Storing Sensitive Data

Sensitive data like credentials, secrets, and service accounts require additional protection. We use key management services to store and manage sensitive information in our research infrastructure, and role-based access control to limit access to secrets so that only authorized workloads and users can retrieve or modify them.

### 4. Identity and Access Management (IAM) for Researchers and Developers

Access management is crucial to administering researcher and developer access to the systems outlined above. The security objectives with any IAM solution are to enable time-bound “least-privilege” access strategies across resources, efficient management, and auditability.

To that end, we built a service called AccessManager as a scalable mechanism to manage internal authorization and enable least-privilege authorization. This service federates access management decisions to approvers as defined by policies. This ensures that decisions to grant access to sensitive resources, including model weights, are made by authorized personnel with appropriate oversight.

AccessManager policies can be defined to be stringent or flexible, tailored to the resource in question. Requesting and being granted access to sensitive resources, such as storage in the research environment that contains model weights, requires multi-party approval. For sensitive resources, AccessManager authorization grants are set to expire after a specified period of time, meaning that privileges reduce to an unprivileged state if not renewed. By implementing these controls, we reduce the risk of unauthorized internal access and employee account compromise.

We integrated GPT-4 into AccessManager to facilitate least-privilege role assignment. Users can search for resources within AccessManager, and the service will use our models to suggest roles that can grant access to that resource. Connecting users to more specific roles combats dependence on otherwise broad, generic, and over-permissive roles. Humans in the loop mitigate the risk of the model proposing the wrong role, on both the initial role request and on a multi-party approval step if the policy for the specified role requires it.

### 5. CI/CD Security

Our infrastructure teams use Continuous Integration and Continuous Delivery (CI/CD) pipelines to build and test our research infrastructure. We’ve invested in securing our infrastructure CI/CD pipelines to make them more resilient against potential threats while maintaining the integrity of our development and deployment processes and velocity for our researchers and engineers.

We restrict the ability to create, access, and trigger infrastructure-related pipelines to prevent access to secrets available to the CI/CD service. Access to CI/CD workers is similarly restricted. Merging code to the deployment branch requires multi-party approval, adding an additional layer of oversight and security. We use infrastructure as code (IaC) paradigms for configuring infrastructure at scale in a consistent, repeatable, and secure manner. Expected configuration is enforced by CI on every change to our infrastructure, usually multiple times per day.

### 6. Flexibility

At the same time, research requires pushing the frontier. This can require rapid iteration on our infrastructure to support shifting functional requirements and constraints. This flexibility is essential to achieve both security and functional requirements, and in some cases it is vital to allow exceptions with appropriate compensating controls to achieve those goals.

## Protecting Model Weights
Protecting model weights from exfiltration from the research environment requires a defense-in-depth approach that encompasses multiple layers of security. These bespoke controls are tailored to safeguard our research assets against unauthorized access and theft, while ensuring they remain accessible for research and development purposes. These measures may include:

- Authorization: Access grants to research storage accounts containing sensitive model weights require multi-party approvals.
- Access: Storage resources for research model weights are private-linked into OpenAI’s environment to reduce exposure to the Internet and require authentication and authorization through Azure for access.
- Egress Controls: OpenAI’s research environment uses network controls that allow egress traffic only to specific predefined Internet targets. Network traffic to hosts not on the allowlist is denied.
- Detection: OpenAI maintains a mosaic of detective controls to backstop this architecture. Details of these controls are intentionally withheld.

## Auditing and Testing
OpenAI uses internal and external red teams to simulate adversaries and test our security controls for the research environment. We’ve had our research environment penetration tested by a leading third-party security consultancy, and our internal red team performs deep assessments against our priorities.

We’re exploring compliance regimes for our research environment. Since protecting model weights is a bespoke security problem, establishing a compliance framework to cover this challenge will require some customization. At this time we are evaluating existing security standards plus custom controls specific to protecting AI technology. This may grow to include AI-specific security and regulatory standards that address the unique challenges of securing AI systems, such as emerging efforts from the Cloud Security Alliance’s AI Safety Initiative(opens in a new window) or the NIST SP 800-218 AI updates.

## Research and Development on Future Controls
Securing increasingly advanced AI systems will require continuous innovation and adaptation. We are at the forefront of developing new security controls, as outlined in our “Reimagining Secure Infrastructure for Advanced AI” blog post. Our commitment to research and development ensures that we stay ahead of emerging threats and continue to enhance the security of our AI infrastructure.

## Join Us
At OpenAI, we are committed to the ongoing development and protection of advanced AI. We invite the AI and security communities to join us in this mission. By applying for our Cybersecurity Grant Program or joining our team, your contribution can help shape the future of AI security.

### Open Roles:

- Software Engineer, Security
- Security Engineer, Detection & Response (US, UK, JP)
- Enterprise Security Engineer
- Research Engineer, Privacy

---

<!-- - [原文](...) -->
- [original](https://openai.com/index/securing-research-infrastructure-for-advanced-ai/)
<!-- - [博客 - 从零开始学AI](...) -->
<!-- - [Blog | Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
