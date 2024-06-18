+++
title = '[AI Google] TimesFM：AI预测股市价格，能否助我财务自由？'
date = 2024-06-18T14:11:41+08:00
draft = false
categories = ['AI', 'Google', 'Timesfm']
tags = ['AI', 'Google', 'Timesfm']
description = '探索谷歌TimesFM模型，看看它能否通过预测股票价格帮助我们实现财务自由。'
keywords = ['AI', '谷歌', 'TimesFM', '时间序列预测', '股票价格预测']
+++

![](ai-google-timesfm-can-ai-predict-stock-prices-for-financial-freedom-sf-intricate-artwork-maste.jpeg)

今天我偶然发现了一个名为TimesFM的模型，它能够预测时间序列数据。于是我心中冒出了一个大胆的想法：如果这个模型可以预测股票价格，那么我是否能借此成为股神呢？

## 介绍
TimesFM（时间序列基础模型）是由谷歌研究院开发的一个预训练模型，专用于时间序列预测。它的强大功能和应用前景引起了我的浓厚兴趣。

## 安装
要开始使用TimesFM，你需要按照以下步骤安装环境：

```bash
conda env create --file=environment.yml
conda env create --file=environment_cpu.yml

conda activate tfm_env
pip install -e .
```

## 代码
以下是一个完整的代码示例，展示了如何使用TimesFM模型来预测股票价格：

```python
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from datetime import date
from timesfm import TimesFm
from huggingface_hub import login
import matplotlib.pyplot as plt

# 给定需要处理的股票代码，上海票以.ss结尾，深圳票以.sz结尾
start = date(2020, 1, 1)  # 使用date类创建日期对象
end = date(2024, 1, 1)  # 指定结束日期为2024年1月1日
codelist = ["000001.ss"]

# 增加错误重试机制的下载数据部分
for retry in range(3):  # 尝试下载最多3次
    try:
        data2 = yf.download(codelist, start=start, end=end)
        # 数据预处理
        data2 = data2['Adj Close'].dropna()  # 使用调整结算价格删除缺损值
        if not data2.empty:
            break  # 成功下载并处理数据，跳出循环
    except Exception as e:
        print(f"下载失败，第{retry+1}次尝试。错误：{e}")
        if retry < 2:  # 在最后一次尝试前等待
            time.sleep(5)  # 等待5秒后重试

if data2.empty:
    raise ValueError("数据为空，请更改时间区间再试一次或检查网络连接。")

context_len = 512  # 设置上下文长度
horizon_len = 256  # 设置预测期间的长度

if len(data2) < context_len:
    raise ValueError(f"数据长度小于上下文长度（{context_len}）")

context_data = data2[-context_len:]  # 使用最近512天的数据作为上下文

# 初始化和导入TimesFM模型
tfm = TimesFm(
    context_len=context_len,
    horizon_len=horizon_len,
    input_patch_len=32,
    output_patch_len=128,
    num_layers=20,
    model_dims=1280,
    backend='cpu',  # 修改这里，将'gpu'改为'cpu'
)

# 登录Hugging Face Hub，此处****需替换成自己的Hugging token
login("*****")

tfm.load_from_checkpoint(repo_id="google/timesfm-1.0-200m")

# 准备数据
forecast_input = [context_data.values]
frequency_input = [0]  #设置数据频率（0是高频率数据）

# 运行预测
point_forecast, experimental_quantile_forecast = tfm.forecast(
    forecast_input,
    freq=frequency_input,
)

# 设置图表尺寸为24*12英寸
plt.figure(figsize=(24, 12))

forecast_dates = pd.date_range(start=data2.index[-1] + pd.Timedelta(days=1), periods=horizon_len, freq='B')
forecast_series = pd.Series(point_forecast[0], index=forecast_dates)

# 添加部分：获取并绘制2024.1.1到当前时间的实际价格数据
current_date = datetime.datetime.now().date()
data_recent = yf.download(codelist, start=date(2024, 1, 1), end=current_date)

if not data_recent.empty:
    data_recent = data_recent['Adj Close'].dropna()
    plt.plot(data_recent.index, data_recent.values, label="Actual Prices (2024-Now)")

# 创建或更新图表（如果前面已有图表，这里是更新）
plt.plot(data2.index, data2.values, label="Actual Prices")
plt.plot(forecast_series.index, forecast_series.values, label="Forecasted Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"Price Compare & Forecast for {codelist[0]}")
plt.legend()

# 保存图表到文件，确保尺寸更改已生效
plt.savefig(f'{codelist[0]}_compare.png', bbox_inches='tight') 

# 显式关闭当前图表
plt.close(fig='all')
```

## 例图

最后，我运行了上涨指数和沪深300指数的预测，并生成了一些效果图：

![上证指数](000001.SS-compare.png)

![沪深300指数](000300.SS-compare.png)

## 结论

尽管TimesFM模型在一定程度上展示了其预测能力，但最终的效果仍未达到预期。看来，想通过预测股票价格实现财务自由还需更加努力，或许我还是得继续好好工作。

---

- [github](https://github.com/google-research/timesfm)
- [Google Research blog](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
- [Hugging Face checkpoint repo](https://huggingface.co/google/timesfm-1.0-200m)
- https://github.com/lhw828/timesfm
- [AI 博客 - 从零开始学AI](https://ai-blog.aihub2022.top/zh/post/ai-google-timesfm-intro/)
- [公众号 - 从零开始学AI](https://mp.weixin.qq.com/s?__biz=MzA3MDIyNTgzNA==&mid=2649977499&idx=1&sn=b797640ce9a8df227680d4567f6586bd&chksm=86c7c85eb1b041485c7bab75299bd4f6b422da0e854db440e8e246b937d17d058e1686a9a62e#rd)
<!-- - [CSDN - 从零开始学AI](...) -->
<!-- - [掘金 - 从零开始学AI](...) -->
<!-- - [知乎 - 从零开始学AI](...) -->
<!-- - [阿里云 - 从零开始学AI](...) -->
<!-- - [腾讯云 - 从零开始学AI](...) -->
