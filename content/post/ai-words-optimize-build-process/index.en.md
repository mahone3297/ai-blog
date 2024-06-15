+++
title = '[AI words] Breakthrough: How to Halve the Build Time of AI words Website'
date = 2024-06-15T17:16:35+08:00
draft = false
categories = ['AI', 'AI words']
tags = ['AI', 'AI words']
description = 'Learn how I optimized the build process of the AI words website, reducing the build time from 14 minutes to just 7 minutes. This article details the optimization steps and challenges encountered.'
keywords = ['AI', 'AI words', 'optimization', 'website performance', 'build process', 'website development']
+++

On a sunny morning, I sat at my computer, eagerly pressing the "build" button to generate my new website, [AI words](https://ai-words.aihub2022.top/). This website aimed to create a separate page for each word, with a total of 5,000 words. But to my surprise, the build process took a whopping 14 minutes! I thought, isn't there a way to make this process faster?

## Exploring Performance Bottlenecks

Determined to find a solution, I decided to have an in-depth conversation with my AI assistant. We discussed various optimization plans and finally decided to conduct a detailed performance analysis. We added metrics to detect the time consumption of each template, especially hoping to find a breakthrough in optimizing the AI words website build time. The results came in quickly:

```plaintext
      cumulative       average       maximum      cache  percent  cached  total  
        duration      duration      duration  potential   cached   count  count  template
      ----------      --------      --------  ---------  -------  ------  -----  --------
   11m14.127830535s  1.484863062s  8.275081851s          0        0       0    454  index.html
   6m18.63167821s   34.730478ms  6.838507807s         39        0       0  10902  partials/head/head.html
   6m9.997678009s   18.474942ms  3.123818975s          0        0       0  20027  partials/data/title.html
   1m5.89808511s    7.257498ms   62.181409ms          0        0       0   9080  _default/single.html
```

From the data, it was clear that index.html was necessary, but head.html was a major time consumer. To optimize the AI words website build time, we needed to address this issue. So, I decided to start here.

## Initial Victory

Discussing with my AI assistant again, we decided to try adding caching for these partials. I adjusted the code and eagerly pressed the "build" button once more. A few minutes later, I was amazed to see a significant improvement in performance—the build time was reduced from 14 minutes to 7 minutes! I could hardly believe my eyes:

```plaintext
      cumulative       average       maximum      cache  percent  cached  total  
        duration      duration      duration  potential   cached   count  count  template
      ----------      --------      --------  ---------  -------  ------  -----  --------
   5m52.246181489s  775.872646ms  2.862713569s          0        0       0    454  index.html
   1m3.632475614s    7.007981ms   66.654399ms          0        0       0   9080  _default/single.html
   40.250901904s    4.432918ms    52.10609ms          2        0       0   9080  partials/article/article.html
```

## Unexpected Setback

Just as I was elated with this breakthrough, an afternoon routine check brought me back to reality. I found that all the page titles had turned into "404 not found." How could this happen? I hurriedly checked the code and discovered the problem was with the cache. This discovery left me downhearted, and I had no choice but to roll back the code, bringing the build time back to 14 minutes. Watching the AI words website build time return to its original state, I felt a bit disappointed.

## Fighting Back

Despite the setback, I did not give up. After calming down, I reanalyzed the performance bottleneck and found that the calculations in title.html were too heavy, severely slowing down the process. My needs were actually not that complex, so I decided to simplify the title.html code.

After some adjustments, I pressed the "build" button once more. As time passed, I nervously watched the progress bar on the screen. Finally, the result came in—the build time was reduced to 7 minutes again! This time, I not only felt the joy of success but also experienced the power of persistence and improvement.

```plaintext
      cumulative       average       maximum      cache  percent  cached  total  
        duration      duration      duration  potential   cached   count  count  template
      ----------      --------      --------  ---------  -------  ------  -----  --------
   5m53.388687234s  778.389178ms  1.685881574s          0        0       0    454  index.html
   1m7.814885681s    7.468599ms   67.456653ms          0        0       0   9080  _default/single.html
    35.24786248s    3.881923ms    63.40133ms          2        0       0   9080  partials/article/article.html
```

## Final Victory

Through this optimization process, I not only successfully halved the build time but also learned how to improve performance by analyzing and adjusting the code. Each failure and success made me stronger and more experienced. In the future, I will continue to optimize, making my AI words website run faster and more stable. This experience taught me that persistence and improvement are the keys to success.

---

<!-- - [原文](...) -->
<!-- - [original](...) -->
<!-- - [AI 博客 - 从零开始学AI](...) -->
<!-- - [AI Blog - Learn AI from scratch](...) -->
<!-- - [公众号 - 从零开始学AI](...) -->
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
