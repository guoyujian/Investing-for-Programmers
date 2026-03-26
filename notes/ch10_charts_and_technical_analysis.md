# Chapter 10 笔记: Charts and technical analysis

## 笔记说明

- 本笔记用于承接 Chapter 10 的预习、问答和后续总结。
- 当前版本为预习版，目标是先把“图表到底在投资研究里解决什么问题、技术分析能提供什么帮助、又容易在哪些地方过度解读”讲清楚，降低正文阅读阻力。
- 如果你想先不读原文，可以先看配套讲义版：[ch10_charts_and_technical_analysis_handout.md](/Users/gmet/Projects/learning/Investing-for-Programmers/notes/ch10_charts_and_technical_analysis_handout.md)

## 本章信息来源

- 直接解析 PDF：已解析原书 PDF 本体
- 章节目录提取：已提取 Chapter 10 及其小节目录
- 页码样本抽取：已抽取 PDF 第 263, 264, 265, 266, 267, 268, 269, 270, 271, 273, 274, 278, 281, 288, 291, 292, 293, 295 页
- 回退方案：本章暂未使用回退方案

## 快速导航

1. 本章导读：这一章在讲什么、最重要的概念是什么、读完后应能回答什么
2. 学习优先级与启动：先读哪里、重点抓什么、为什么这章不是“指标大全”
3. 分节预习笔记：按 `10.1` 到 `10.3` 整理主线
4. 第一轮讲义速览小结：这一轮真正带走什么、第二轮回原文时先补哪里
5. 本章收束：这一章真正要留下来的图表与技术分析边界

## 本章导读

### 本章主要内容

Chapter 10 表面上在讲：

1. 图表（charts）
2. 图表模式（patterns）
3. candlesticks
4. moving averages
5. Ichimoku Cloud
6. Streamlit 可视化

但它真正回答的是一个更基础的问题：

- 当价格只是数字时，你怎么把它们变成可读、可比较、可解释的“故事”？

所以这章的主线不是“背指标”，而是：

1. 先理解图表为什么能给价格加上下文
2. 再理解 pattern 和技术分析想从价格里读什么
3. 然后看到 candlestick、均线、MACD、Ichimoku 这些工具分别在补什么维度
4. 最后把这些图表放回一个更可操作的可视化界面里

### 本章结构

1. `Charts`
2. `Using charts to interpret price changes`
3. `Visualization with Streamlit`

更细的小节结构是：

1. `10.1 Charts`
2. `10.1.1 Reading charts`
3. `10.1.2 Patterns`
4. `10.1.3 Interpreting a chart`
5. `10.1.4 Alternative chart types`
6. `10.2 Using charts to interpret price changes`
7. `10.2.1 Candlesticks`
8. `10.2.2 Charts based on averages`
9. `10.2.3 Ichimoku Cloud`
10. `10.3 Visualization with Streamlit`

### 本章最重要的概念

#### 1. 图表不是装饰，而是价格语境压缩器

作者开头拿“没有参考价格就很难报价”的直觉做引子，想说明：

- 价格数字本身不够
- 你需要历史、范围、波动和对比

图表的第一层价值，不是预测未来，而是让你先知道：

- 这个价格现在处在什么位置
- 过去发生过什么
- 这次波动到底算不算夸张

#### 2. 技术分析的核心是从价格行为中找结构

这一章并不是直接把技术分析当真理，而是把它放回一种更谨慎的位置：

- 它在尝试从历史价格行为中找模式、趋势、支撑、阻力和动量

作者也明确承认：

- 图表模式只是模板
- 很多时候判断会错
- 有人甚至会把技术分析看成近似赌博

也就是说，这章更像是在训练你“看懂技术分析在看什么”，而不是要求你完全信它。

#### 3. 时间尺度会改变你对同一张图的理解

这一章很重要的一点是：

- 同样一次下跌，放在 5 天和放在 30 年图上，心理感受完全不同

所以 chart reading 的关键不是只看局部形状，而是：

- 先选对时间尺度
- 再解释价格变化

#### 4. 单个指标不够，最好把多个维度拼起来

Chapter 10 后半段开始进入：

- candlesticks
- moving averages
- MACD
- Bollinger Bands
- Ichimoku Cloud

这些工具不是同一件事换名字，而是在补不同视角：

- OHLC 结构
- 平滑趋势
- 动量
- 波动边界
- 趋势 + 支撑/阻力的综合图层

#### 5. 技术分析最终还是要落到可视化工具

最后的 Streamlit 一节很关键，因为它把本章从“看书里的图”推进到：

- 你自己能不能把这些图画出来、交互查看、在浏览器里切换

### 读完本章后你应该能回答的问题

1. 为什么图表能让价格数据更容易被理解
2. 为什么同一段价格变化放到不同时间尺度里会得到不同解释
3. double top、support、resistance、breakout 这些词在看什么
4. candlestick 和简单折线图相比，多提供了什么信息
5. moving averages、MACD、Ichimoku 分别适合读什么
6. 为什么作者最后要引入 Streamlit 做可视化

### 关键术语预告

- 图表（chart）
- 时间序列（time series）
- 回撤（drawdown）
- 波动率（volatility）
- 模式（pattern）
- reversal
- continuation
- support line
- resistance line
- breakout
- candlestick
- 开盘价 / 最高价 / 最低价 / 收盘价（OHLC）
- simple moving average（SMA）
- exponential moving average（EMA）
- Bollinger Bands
- MACD
- Ichimoku Cloud
- Streamlit

### 少量关键原文

- 原文短摘录：`Every chart tells a story.`
  - 位置：PDF 第 295 页，Summary
  - 中文解释：作者把图表定位成叙事载体，而不是纯装饰图
  - 我的补充理解：这几乎可以当整章总标题

- 原文短摘录：`Technical analysis ... is a study of historical price developments.`
  - 位置：PDF 第 264 页附近
  - 中文解释：技术分析首先是研究历史价格，不是神秘预测学
  - 我的补充理解：把它放回“历史价格结构”会更不容易神化它

- 原文短摘录：`Chart patterns are just templates.`
  - 位置：PDF 第 273 页
  - 中文解释：图形模式只是过去的模板，不是保证书
  - 我的补充理解：这是阅读本章时很重要的自我校正

### 本章与程序员能力的关系

- 这一章很像“把数值序列做成可读界面”
- 你会自然用到程序员熟悉的几个视角：抽象、可视化、时间窗口、平滑、信号和噪声
- 最后一节 Streamlit 更是把分析推进到一个最小可交互产品
- 对程序员来说，这章的重要性不是“信不信技术分析”，而是学会如何把价格数据转成可读系统

### 建议阅读方式

这一章建议 `精读`，但第一轮最值得抓的是：

1. `10.1 Charts`
2. `10.1.1 Reading charts`
3. `10.1.2 Patterns`
4. `10.2.1 Candlesticks`
5. `10.2.2 Charts based on averages`
6. `10.2.3 Ichimoku Cloud`
7. `10.3 Visualization with Streamlit`

这里真正重要的不是记住每个指标公式，而是先看懂：

- 图表在补什么上下文
- 技术分析想从价格里读什么
- 多种图表和指标各自在补哪个维度

## 学习优先级与启动

### 这一章到底最重要的是哪部分

如果只问“Chapter 10 最核心的是哪几节”，我会给这个判断：

- **真正的核心主线是 `10.1 + 10.2.1 + 10.2.2 + 10.2.3 + 10.3`**

可以把它们这样理解：

- `10.1 Charts`
  - 认知重点
  - 它决定你会不会先把价格变化放回语境

- `10.2.1 Candlesticks`
  - 结构重点
  - 它决定你能不能看懂 OHLC 在一根图形里怎么表达

- `10.2.2 Charts based on averages`
  - 趋势重点
  - 它决定你会不会把“平均价格”当成动态参照系

- `10.2.3 Ichimoku Cloud`
  - 综合重点
  - 它决定你能不能接受一种把趋势、动量、支撑阻力揉在一起的图层

- `10.3 Visualization with Streamlit`
  - 落地重点
  - 它决定你会不会把图表理解推进到可交互工具

### 第一遍先抓什么

如果你第一遍不想被指标名压住，最推荐先抓 4 件事：

1. 作者为什么先讲“价格需要上下文”
2. pattern 到底是在看什么，而不只是形状
3. candlestick 和 moving average 各自补了什么信息
4. 为什么最后会用 Streamlit 收尾

### 第一遍不必卡住的地方

第一遍可以先不要求自己彻底吃透：

- 每个 technical indicator 的全部计算细节
- 各类 pattern 的全部名字
- Streamlit 示例的实现细节
- mplfinance 的具体 API

先抓这些内容“在图表阅读里干什么”，第二轮再补“怎么算和怎么画”。

## 分节预习笔记

### `10.1 Charts`

- 开头用“买东西不知道合理价”的例子说明价格参考的重要性
- 作者先让你看无上下文图，再逐渐补上：
  - 这是 S&P 500
  - 时间区间只有几天
  - 11% 的下跌放在指数上和放在单股上意义不同
- Table 10.1（PDF 第 266 页）和 Figure 10.4（PDF 第 267 页）帮助你把大幅回撤放回更长时间尺度
- NVIDIA 的例子（PDF 第 268-269 页）则把单股、增长和 earnings 连接起来

### `10.1.1 Reading charts`

- 这一节的重点是：
  - 图表识别常常先从故事感开始
  - 你看到形状，会自然给它编解释
- 作者用 Bitcoin 图举例，说明投资者会先从图像上认模式，再慢慢赋予它含义

### `10.1.2 Patterns`

- 这里开始进入典型 pattern
- 作者用 double top 举例（Figure 10.10，PDF 第 271 页）
- 同时也提醒：
  - mean reversion 和 momentum 都是不同的解释框架
  - pattern 只是模板，不是保证
- support / resistance / breakout 在 PDF 第 273-274 页是一组很值得第二轮回看的概念

### `10.2 Using charts to interpret price changes`

- 这一节开始从“讲图”进入“讲指标”
- 如果只想先有一个够用的直觉，可以先这样记：
  - `candlestick`：把一段时间的 OHLC 压进一根图形
  - `moving averages`：把最近一段时间价格做平均，帮助看平滑趋势
  - `MACD`：帮助观察趋势动量是在增强还是减弱
  - `Ichimoku Cloud`：把趋势、动量、支撑阻力叠成一张综合图

#### `10.2.1 Candlesticks`

- candlestick 的重点是把 OHLC 压进一根图形
- Figure 10.18（PDF 第 278 页）是这一节最关键的图
- 它比单纯折线图多了：
  - 开盘和收盘关系
  - 当日波动区间
  - bullish / bearish 的直观信息

#### `10.2.2 Charts based on averages`

- 这一节先从“平均价格”直觉讲起，再引出：
  - SMA
  - EMA
  - 其他加权平均
- 后面还会连到：
  - moving average ribbons
  - Bollinger Bands
  - MACD
- Figure 10.21（PDF 第 284 页）、Figure 10.22（PDF 第 285-286 页）、Figure 10.23（PDF 第 288 页）都是第二轮值得重点看的图

#### `10.2.3 Ichimoku Cloud`

- Ichimoku 的重点不是某一条线，而是把：
  - 趋势
  - 动量
  - 支撑阻力
  一起叠到一张图里
- Figure 10.24（PDF 第 290 页）是第二轮建议重点回看的图

### `10.3 Visualization with Streamlit`

- 这一节特别适合程序员
- 作者不是停在“会看图”，而是继续推进到“能自己画图和切换图”
- Listings 10.7 和 10.8（PDF 第 291-293 页）展示：
  - 如何在本地快速起一个 web UI
  - 如何切换 ticker、时间、plot type
  - 如何把 returns、candles、MACD、cloud 等图接到一个界面里
- Figure 10.25（PDF 第 292 页）和 Figure 10.26（PDF 第 294 页）是第二轮建议重点回看的展示图

## 第一轮讲义速览小结

### 当前状态

- Chapter 10 第一轮 `简读 / 速览`（讲义）已完成。
- 当前目标已经从“先建立图表语言直觉”推进到“第二轮回原文补图、补指标、补可视化实践”。

### 这一轮最该留下的 5 个结论

1. 图表的第一作用不是预测，而是给价格加上下文。
2. pattern 和 technical analysis 更像是解释价格结构的语言，不是保证未来的公式。
3. candlestick、moving averages、MACD、Ichimoku 不是重复工具，而是在补不同维度。
4. 同一段价格变化放到不同时间尺度里，意义会完全改变。
5. 作者最后讲 Streamlit，是在把“会看图”推进到“能把图做成自己的研究工具”。

### 第二轮回原文建议优先补的部分

1. `10.1.2 Patterns`
   - 重点补：double top、support、resistance、breakout
   - 建议位置：PDF 第 `271-274` 页
2. `10.2.1 Candlesticks`
   - 重点补：OHLC 和 Figure `10.18`
   - 建议位置：PDF 第 `278-280` 页
3. `10.2.2 Charts based on averages`
   - 重点补：SMA、EMA、MACD、Bollinger Bands
   - 建议位置：PDF 第 `281-288` 页
4. `10.2.3 Ichimoku Cloud`
   - 重点补：Figure `10.24`
   - 建议位置：PDF 第 `290` 页
5. `10.3 Visualization with Streamlit`
   - 重点补：Listings `10.7-10.8` 和 Figure `10.25-10.26`
   - 建议位置：PDF 第 `291-294` 页

### 第二轮最小实践建议

- 选一个你熟悉的资产，同时看短周期和长周期图，比较同一次回撤在不同时间尺度里的意义。
- 手动画出一组 support / resistance，或者自己用工具画出一条 SMA / EMA，看你是否真的能把“趋势”读成结构。

## 本章收束

如果把 Chapter 10 压成一句话，它真正想留下的是：

- 图表不是预测水晶球，但它们能把价格行为、波动、趋势和动量变成你能真正看懂的结构

所以这一章真正该带走的，是 4 层意识：

1. 价格需要上下文
2. pattern 可以提供参考，但不能神化
3. 指标各自在补不同维度
4. 图表最终可以被做成自己的分析界面
