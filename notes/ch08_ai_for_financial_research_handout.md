# Chapter 8 讲义：AI for financial research

## 这份讲义怎么用

- 这是一份给“第一遍阅读”准备的讲义版，不要求你先读原文。
- 目标不是覆盖第八章每个模型和每段代码，而是先帮你抓住：作者怎么看 ML、怎么看 GenAI、又把它们放在金融研究里的什么位置。
- 第二遍回原文时，你只需要带着这份讲义去对照图、例子、listing 和作者的判断链。

## 本章在全书里的位置

如果说：

- Chapter 3 教你拿数据
- Chapter 4-6 教你做 thesis、管组合、搭监控
- Chapter 7 教你做风险控制

那么 Chapter 8 就是在问：

“AI 到底该放进这个研究系统的哪一层？”

所以这章不是单纯的 AI 介绍，也不是教你“用 AI 轻松选股”，而是在教你：

- 哪些事可以交给 AI 帮忙
- 哪些事不能外包给 AI
- 什么情况下 ML 和 GenAI 真有用

## 这一遍你最需要获得什么

读完这份讲义后，你至少应该拿到 5 个稳定结论：

1. 不应该把 LLM 当成直接给买卖结论的投资顾问
2. ML 在金融里最难的不是代码，而是市场本身和数据本身
3. 窄 scope 的 use case 比“万能预测模型”现实得多
4. GenAI 最适合做研究助理，而不是研究裁判
5. prompt engineering 的本质是提供正确上下文，而不是堆技巧

## 一页主线

如果把这一章压成最短的一条线，它其实是在讲：

1. 先看 ML 在金融里的两个入口：聚类和预测
2. 再看到市场和工程现实如何把“神奇模型”拉回地面
3. 然后转向 GenAI，比较几个 LLM 的表现
4. 接着把 LLM 放回合适的位置：研究助理、代码组件、信息整理器
5. 最后用 prompt engineering 提高研究质量

你可以把这一章理解成：

“AI 进入投资研究后的能力边界说明书”

## 核心概念讲解

### 1. 作者开场就在故意试探一个危险想法

Chapter 8 的开场很有意思。作者先问：

- 如果我们干脆不用代码做金融研究，而是直接问 GenAI chatbot 要投资建议，会怎样？

这个开场的作用不是推荐这么做，而是故意把风险摆到台面上。

原文位置：

- 开场问题：PDF 第 `205` 页
- 风险提醒：PDF 第 `206` 页

第一遍你要先记住作者的基本立场：

- `GenAI` 很有用
- 但 mindlessly follow 它的投资建议很危险

### 2. 一个很好的 ML 例子：先别预测，先聚类

作者没有一上来就说“我们来预测哪只股票会涨”，而是先给了一个更稳的无监督学习例子。

他做的事情是：

- 从 S&P 500 拿成分股
- 拉过去一年的价格数据
- 用 `K-means` 聚类
- 看哪些股票在 `returns / volatility` 上像一类

这个例子很重要，因为它在提醒你：

- ML 不一定只能拿来预测
- 也可以先拿来“整理混乱的数据”，帮你看出 outliers 和候选对象

回原文时建议这样看：

1. 先看问题设置：`8.1.1 Unsupervised learning example`，PDF 第 `208` 页
2. 再看 elbow curve：Figure `8.2`，PDF 第 `210` 页
3. 最后看 scatter plot：Figure `8.3`，PDF 第 `211` 页

### 3. 这个例子真正想让你学到什么

作者在 Figure 8.3 的 scatter plot 里，让你能 hover 每个点去看 ticker。

他其实是在训练你一个更实用的动作：

- 不要试图一次精读 500 家公司
- 先用方法把 universe 缩小

比如：

- 某些 outlier 可能是 turnaround 候选
- 某些高 return 点可能值得做成长研究
- 某些高 volatility 点可能值得做风险研究

所以无监督学习在这里的价值不是“自动赚钱”，而是：

- **帮你更高效地组织注意力**

### 4. 监督学习例子在讲什么

作者接着把无监督学习推进到监督学习。

这一段有两个层次：

1. 先说明 label 可以怎么构造
2. 再给一个更容易复现的价格预测例子

更具体地说：

- 他先把 cluster 结果转成 label，讲 analytical dataset 怎么来
- 后面又用 `AAPL` 的 next-day close 做 target，配上 random forest 做一个示范

这部分第一遍不要急着问：

- 这个模型准不准到可以下单吗？

作者更想你先看到：

- feature 和 label 的定义，本身就已经是研究判断的一部分

回原文时建议这样看：

- 监督学习示例起点：PDF 第 `212` 页
- 股票预测与 dataset 构造：PDF 第 `214-216` 页
- 相关 listing：`Listing 8.5` 到 `Listing 8.7`

### 5. 这一章最重要的转折：问题不只是模型，问题是市场

`8.1.3 Market challenges` 和 `8.1.4 Technical challenges` 是这章最重要的现实校正。

作者在这里想打断一个很常见的错觉：

- 只要模型够复杂，就能把市场吃透

他给出的现实是：

- 市场常常像 random walk
- 有效市场理论会让可预测性变弱
- 宏观政策和政治变化会快速改写旧模式
- 少数大赢家决定市场长期回报，导致样本极不均匀

再加上工程层面的问题：

- volatility 很高
- feature 太多容易 overfit，太少又会 underfit
- 数据管线和模型维护成本很重

回原文时建议这样看：

- market challenges：PDF 第 `216-219` 页
- Figure `8.6`（波动率例子）：PDF 第 `219` 页
- Figure `8.7`（overfitting / underfitting）：PDF 第 `220` 页

### 6. 一个很关键的收缩动作：缩小 scope

作者在 `8.1.5 Narrowing the scope` 里其实是在给前面所有“AI 能预测市场”的幻想降温。

他的核心意思是：

- 能预测所有股票价格的通用模型几乎像童话
- 更现实的路，是在窄任务、窄行业、窄问题上找胜率

这是整章特别值得记住的一条判断，因为它后面直接连到：

- ML 做局部任务
- GenAI 做研究辅助

### 7. 比较 LLM 的实验为什么重要

`8.2.1 Comparing LLMs` 用 GPT-4o、Gemini、Finance Chat 做了一个很有代表性的比较。

问的问题包括：

- 当前市场趋势是什么
- Buffett / Peter Lynch 风格会选什么股票

这个实验很重要，因为它不是为了证明哪个模型赢，而是为了暴露这些问题：

- 输出并不稳定
- 同样的“名嘴式建议”可能听起来很像
- 数据源和时效性并不透明
- 模型会给出已经不合适或甚至有错误的答案

回原文时建议这样看：

- 问题设置和结果解释：PDF 第 `223-224` 页
- 对照表：Table `8.1`，PDF 第 `223` 页

### 8. 作者对 GenAI 的真正判断：它更像研究助理

Chapter 8 后半段最该抓的一句话其实不是模型名，而是这个定位：

- `Using LLMs as research assistants`

作者给的高价值 use cases 很实在：

- 总结长文档
- 快速看管理层
- 查 pending lawsuits、insider trades、business model、customer segmentation
- 对非金融风险做高层梳理

这和“推荐我三只股票”是完全不同的用法。

前者更像：

- 把人本来就该做的研究，加速

后者更像：

- 把判断外包

回原文时建议这样看：

- `8.3.1 Using LLMs as research assistants`：PDF 第 `225-227` 页
- Table `8.2`：PDF 第 `226-227` 页

### 9. 代码接入这一节在干什么

`8.3.2 Integrating LLMs into code` 的重点不是 API 教程本身，而是：

- 把 LLM 变成研究基础设施的一部分

作者这里依次展示了：

- OpenAI：`Listings 8.8-8.9`，PDF 第 `228` 页
- Gemini：`Listings 8.10-8.11`，PDF 第 `229` 页
- Mistral：`Listing 8.12`，PDF 第 `230` 页
- Hugging Face / 本地模型：`Listing 8.13`，PDF 第 `231` 页

这一节最值得带走的不是 SDK 细节，而是：

- 商业模型通常要 API key
- 本地开源模型能省 API 成本，但要换成硬件、下载、部署和推理延迟成本

### 10. Prompt engineering 其实很朴素

作者在 `8.4 Prompt engineering` 里的态度很务实。

他不是在教“神奇咒语”，而是在说：

- 你给的上下文越清楚，答案越有机会靠谱

这在投资研究里尤其明显，因为模型需要知道：

- 你的风险偏好
- 你的行业经验
- 你的 broker 和 wallet
- 你的税务身份
- 你排斥哪些行业
- 你接受哪些资产

回原文时建议这样看：

- prompt engineering 总论：PDF 第 `232` 页
- investor profile：PDF 第 `232-235` 页
- Figure `8.8` 与 Netflix 提示例子：PDF 第 `235-237` 页

### 11. Netflix 这个例子为什么值得记住

这一节不是在推荐 Netflix，而是在示范：

- 怎样把一个你已经理解的商业模式，翻译成 prompt 的筛选条件

作者的思路是：

- 先想 Netflix 早期为什么成功
- 再把这些因素写进 prompt
- 然后让 LLM 给出“类似早期 Netflix”的候选公司

这个例子很好，因为它把 prompt engineering 从抽象技巧，变成了：

- 把 thesis / business model 翻译成可查询条件

同时作者也没放松警惕，他明确提醒：

- LLM 给的公司只是研究入口
- 不做 due diligence 直接投资仍然很危险

## 第一遍最该记住的 5 句话

1. `LLM` 很擅长给出“像答案的答案”，但这不等于它的投资建议可靠。
2. 金融里的 `ML` 难点更多在市场、数据和维护，而不是模型名气。
3. AI 真正有价值的地方，常常是缩小研究范围、加速研究流程。
4. 越是宽泛的问题，越容易得到泛泛而不可靠的回答。
5. 好的 prompt，本质上是把你的研究上下文、约束和目标说清楚。

## 第二遍回原文时重点看哪里

如果你第二遍回原文，我建议按这个顺序看：

1. `8.1.1 Unsupervised learning example`
  - 先看 ML 怎么帮你整理 universe
2. `8.1.3 Market challenges`
  - 再看为什么金融 ML 很难神化
3. `8.1.4 Technical challenges`
  - 把工程代价和模型边界补上
4. `8.2.1 Comparing LLMs`
  - 看看模型建议到底有多不稳定
5. `8.3.1 Using LLMs as research assistants`
  - 这是最值得拿来落地的一段
6. `8.4.1 An investor’s profile`
  - 看如何把上下文交给模型
7. `8.4.2 Using prompts to find companies to invest in`
  - 看如何把商业模式翻译成 prompt

## 哪些地方第一遍可以先放过

- 每个 ML 算法的数学细节
- 每段 SDK 代码的实现细节
- 各大模型之间的性能参数比较
- 每个 chart / listing 都立刻跑出来

第一遍先抓：

- 作者的立场
- AI 的能力边界
- 什么是“正确使用 AI 的姿势”

## 这章真正想让你获得什么

如果只用一句话总结 Chapter 8，我会这样说：

- 作者不是在教你“让 AI 替你投资”，而是在教你“怎样让 AI 成为一个有用但受约束的研究助手”。
