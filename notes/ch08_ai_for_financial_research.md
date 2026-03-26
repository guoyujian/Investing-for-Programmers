# Chapter 8 笔记: AI for financial research

## 笔记说明

- 本笔记用于承接 Chapter 8 的预习、问答和后续总结。
- 当前版本为预习版，目标是先把“AI 在金融研究里到底该做什么、不该做什么、ML 和 GenAI 各自适合什么范围”讲清楚，降低正文阅读阻力。
- 如果你想先不读原文，可以先看配套讲义版：[ch08_ai_for_financial_research_handout.md](/Users/gmet/Projects/learning/Investing-for-Programmers/notes/ch08_ai_for_financial_research_handout.md)

## 本章信息来源

- 直接解析 PDF：已解析原书 PDF 本体
- 章节目录提取：已提取 Chapter 8 及其小节目录
- 页码样本抽取：已抽取 PDF 第 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238 页
- 回退方案：本章暂未使用回退方案

## 快速导航

1. 本章导读：这一章在讲什么、最重要的概念是什么、读完后应能回答什么
2. 学习优先级与启动：先读哪里、重点抓什么、为什么这章不是“AI 选股捷径”
3. 分节预习笔记：按 `8.1` 到 `8.4` 整理主线
4. 第一轮讲义速览小结：这一轮最该留下什么、第二轮该重点补什么
5. 本章收束：这一章真正要留下来的 AI 研究边界

## 第一轮讲义速览小结

- 当前状态：第一轮 `简读 / 速览`（讲义）已完成，第二轮待回原文细读
- 这一轮最重要的收获：
  1. 不应该把 LLM 当成直接替你做投资决策的顾问
  2. 金融里的 ML 难点更多在市场、数据和维护成本，而不只是模型
  3. 窄 scope 的 use case 比“万能预测模型”现实得多
  4. GenAI 最适合做研究助理，而不是研究裁判
  5. prompt engineering 的核心是给出足够清楚的上下文、约束和目标
- 第二轮回原文最值得重点补的部分：
  1. `8.1.1 Unsupervised learning example` 的 cluster 示例
  2. `8.1.3 Market challenges` 与 `8.1.4 Technical challenges`
  3. `8.2.1 Comparing LLMs` 的对照实验和 Table 8.1
  4. `8.3.1 Using LLMs as research assistants`
  5. `8.4.2 Using prompts to find companies to invest in`
- 第二轮实践建议：
  - 用一个熟悉行业试写一组 investor profile prompt
  - 用 LLM 总结一份财报或 earnings call transcript
  - 对同一个问题比较两种不同 prompt 的输出差异

## 本章导读

### 本章主要内容

Chapter 8 表面上在讲：

1. 机器学习（ML）
2. 生成式 AI（GenAI）
3. LLM 的接入方式
4. prompt engineering

但它真正回答的是一个更现实的问题：

- AI 在金融研究里到底能帮到哪里，哪里又最容易把人带偏？

所以这章的主线不是“让 AI 替你选股”，而是：

1. 先理解 ML 为什么看起来有吸引力
2. 再理解市场为什么让 ML 很难稳定奏效
3. 然后看到 GenAI 的真正价值更多在研究辅助，而不是直接给买卖答案
4. 最后把 prompt 和研究流程连起来

### 本章结构

1. `From code to machine learning`
2. `From machine learning to generative AI`
3. `Practical use of GenAI`
4. `Prompt engineering`

更细的小节结构是：

1. `8.1 From code to machine learning`
2. `8.1.1 Unsupervised learning example`
3. `8.1.2 Supervised learning example`
4. `8.1.3 Market challenges`
5. `8.1.4 Technical challenges`
6. `8.1.5 Narrowing the scope`
7. `8.2 From machine learning to generative AI`
8. `8.2.1 Comparing LLMs`
9. `8.2.2 Complementing ML with GenAI`
10. `8.2.3 Challenges`
11. `8.2.4 Final judgement on ML and GenAI`
12. `8.3 Practical use of GenAI`
13. `8.3.1 Using LLMs as research assistants`
14. `8.3.2 Integrating LLMs into code`
15. `8.4 Prompt engineering`
16. `8.4.1 An investor’s profile`
17. `8.4.2 Using prompts to find companies to invest in`

### 本章最重要的概念

#### 1. AI 不是投资判断的替代品，而是研究流程的加速器

作者开头就故意抛出一个“危险问题”：

- 能不能直接问 LLM 给我三只股票，然后照着买？

这不是他真正推荐的做法，而是为了让你看到：

- 直接把投资判断外包给 AI，风险很高

这章最重要的底线是：

- AI 更适合加速研究、补充信息、帮助整理和启发
- 不适合被当成无条件可信的投资裁决器

#### 2. ML 的真正难点不在“会不会调包”，而在市场本身太难

这一章并不是在否定 ML，而是在提醒你：

- 市场是高噪声、动态变化、带有随机游走特征的系统

所以难点不只是算法，而是：

- 标签怎么定义
- 特征怎么选
- 信号和噪声怎么分
- 模型怎么避免过拟合
- 变了的市场环境怎么重新训练

#### 3. 缩小范围比盲目追求“万能预测模型”更重要

作者对 ML 的一个核心判断是：

- 能预测所有股票价格的万能模型，基本是幻想

更有希望的，是：

- 在更窄、更具体的任务上使用 ML
- 比如聚类、筛选、特定场景预测、局部模式识别

#### 4. GenAI 的长处更像“研究助理”

这一章后半段最重要的转向是：

- 不再问“LLM 能不能直接给我答案”
- 而是问“LLM 能不能帮我更快完成研究工作”

这包括：

- 总结长文档
- 快速了解管理层
- 梳理业务模式
- 高层分析非金融风险
- 帮你想 feature、想问题、想对照视角

#### 5. Prompt engineering 的本质不是技巧炫耀，而是把上下文说清楚

作者对 prompt engineering 的处理很实用。

他真正想说的是：

- 不是只想“问什么”
- 还要想“怎么问，提供多少上下文”

对投资研究来说，好的 prompt 不只是语句漂亮，而是会告诉模型：

- 你的风险偏好
- 你的资产经验
- 你的税务约束
- 你的 broker、钱包、持仓、偏好和排除项

### 读完本章后你应该能回答的问题

1. 作者为什么不建议直接拿 LLM 的投资建议下单
2. 无监督学习和监督学习在投资研究里分别能做什么
3. 为什么市场特性会让 ML 在金融里特别难
4. 为什么“缩小 scope”比追求万能模型更现实
5. GenAI 和传统 ML 在作者这里是替代关系还是互补关系
6. LLM 最适合承担哪些研究辅助工作
7. 什么叫一个对投资研究有用的 prompt

### 关键术语预告

- 机器学习（machine learning, ML）
- 监督学习（supervised learning）
- 无监督学习（unsupervised learning）
- 特征（features）
- 标签（labels）
- 聚类（clustering）
- K-means
- elbow curve
- 波动率（volatility）
- 随机森林（random forest）
- 随机游走（random walk）
- 有效市场理论（efficient market theory）
- 过拟合（overfitting）
- 欠拟合（underfitting）
- 生成式 AI（generative AI, GenAI）
- 大语言模型（large language model, LLM）
- 幻觉（hallucination）
- 非确定性（non-determinism）
- prompt engineering
- 系统提示词（system prompt）
- API key
- 开源模型（open-source model）
- 专有模型（proprietary model）
- 推理（inference）

### 少量关键原文

- 原文短摘录：`What if we stopped using code for financial research and relied on generative AI chatbots for investment advice?`
  - 位置：PDF 第 205 页，Chapter 8 开头
  - 中文解释：作者故意用一个激进问题开场，逼你先面对“能不能把判断外包给 AI”
  - 我的补充理解：整章都在回应这个问题，但答案并不是“可以放心交给 AI”

- 原文短摘录：`mindlessly following an LLM's investment advice is risky`
  - 位置：PDF 第 206 页
  - 中文解释：作者明确提醒，LLM 有 hallucinations 和信息过时风险
  - 我的补充理解：这是本章最该记住的红线之一

- 原文短摘录：`don’t just ponder what to ask, but also how`
  - 位置：PDF 第 232 页，`8.4 Prompt engineering`
  - 中文解释：prompt engineering 的本质不是玄学，而是把问题表达清楚
  - 我的补充理解：这句话几乎可以当本节总标题

### 本章与程序员能力的关系

- 这一章特别像“把程序员的实验能力、自动化能力和 AI 工具整合进研究流程”
- 你会自然用到几个熟悉动作：定义任务、选特征、划定范围、调用 API、评估输出、写 prompt
- 这章也在训练一种更成熟的 AI 使用心态：既会用，也会防
- 对程序员来说，这章的重要性不是“学会一个模型名”，而是学会“如何把 AI 嵌进研究流程而不失控”

### 建议阅读方式

这一章建议 `精读`，但第一轮最值得抓的是：

1. `8.1.1 Unsupervised learning example`
2. `8.1.2 Supervised learning example`
3. `8.1.3 Market challenges`
4. `8.1.4 Technical challenges`
5. `8.2.1 Comparing LLMs`
6. `8.2.3 Challenges`
7. `8.3.1 Using LLMs as research assistants`
8. `8.4.1 An investor’s profile`
9. `8.4.2 Using prompts to find companies to invest in`

这里真正重要的不是把每段代码都跑一遍，而是先看懂：

- ML 为什么在金融里诱人又危险
- GenAI 最适合的边界在哪里
- prompt 为什么是研究质量的一部分

## 学习优先级与启动

### 这一章到底最重要的是哪部分

如果只问“Chapter 8 最核心的是哪几节”，我会给这个判断：

- **真正的核心主线是 `8.1.3 + 8.1.4 + 8.2.1 + 8.3.1 + 8.4`**

可以把它们这样理解：

- `8.1.3 Market challenges`
  - 市场重点
  - 它决定你会不会对 ML 产生不切实际的预期

- `8.1.4 Technical challenges`
  - 工程重点
  - 它决定你能不能理解为什么金融 ML 往往卡在数据、特征和维护成本

- `8.2.1 Comparing LLMs`
  - 认知重点
  - 它决定你会不会把 LLM 输出误当成稳定可靠的投资建议

- `8.3.1 Using LLMs as research assistants`
  - 应用重点
  - 它决定你能不能把 LLM 放到合适的研究位置

- `8.4 Prompt engineering`
  - 操作重点
  - 它决定你能不能把 AI 输出质量真正提上来

### 第一遍先抓什么

如果你第一遍不想被模型名和代码包围，最推荐先抓 4 件事：

1. 无监督学习和监督学习在这里分别是在做什么
2. 作者为什么不断强调 market challenges 和 technical challenges
3. LLM 的局限到底体现在哪些例子里
4. 好的 prompt 为什么像“给研究助理写任务说明”

### 第一遍不必卡住的地方

第一遍可以先不要求自己彻底吃透：

- K-means 的数学细节
- 随机森林的训练细节
- 每个 provider SDK 的具体调用差异
- 各类模型版本的性能细节

先抓这些内容“在研究流程里干什么”，第二轮再补“怎么跑得更扎实”。

## 分节预习笔记

### `8.1 From code to machine learning`

- 这一节的目标是把“写 Python 抓数”推进到“用 ML 组织或预测数据”
- 开场先给了 NVIDIA 一年价格预测图（Figure 8.1，PDF 第 208 页），提醒你这种图看起来很有吸引力
- `8.1.1` 用 S&P 500 的聚类例子示范无监督学习：
  - 从 Wikipedia 取成分股
  - 拉一年的价格
  - 用 K-means 做 cluster
  - 先用 elbow curve 决定 cluster 数量（Figure 8.2，PDF 第 210 页）
  - 再用 scatter plot 看 returns / volatility 和 outliers（Figure 8.3，PDF 第 211 页）
- 这一节真正想让你看到的是：
  - ML 不一定先用来预测，也可以先用来整理和筛选

### `8.1.2 Supervised learning example`

- 这一节开始进入监督学习
- 作者先用前面的 cluster 结果构造 label，再讲如何做 analytical dataset
- 后面又给了一个更简单、可复现的股票价格预测示例：
  - 用 `AAPL`
  - 用 next day close 当 target
  - 用 random forest 做回归
- 这里最重要的不是“模型准不准”，而是：
  - label 怎么定义
  - feature 怎么选
  - 预测任务到底有没有现实意义

### `8.1.3 Market challenges`

- 这一节在讲：就算你懂 ML，也不代表市场会给你稳定模式
- 作者把困难拉回市场本身：
  - 市场可能接近有效
  - 股票常带有 random walk 特征
  - 少数大赢家拉高整体回报，绝大多数股票未必表现好
  - 宏观政策和政治变化会迅速改变过去的模式
- 一个典型例子是：
  - 新总统和 tariff 政策让原来的 cluster 表现发生变化（PDF 第 214 页）

### `8.1.4 Technical challenges`

- 这一节把困难从市场层拉回工程层
- 作者特别强调：
  - volatility（Figure 8.6，PDF 第 219 页）
  - overfitting / underfitting（Figure 8.7，PDF 第 220 页）
  - 数据量与数据管线
  - 模型维护成本
- 这一节的核心不是“技术很难”这么简单，而是：
  - 就算你找到信号，也未必能低成本、长期、稳定维护

### `8.1.5 Narrowing the scope`

- 这一节是全章最重要的收缩动作之一
- 作者明确说：
  - 万能 stock forecasting 模型像童话里的金鹅
  - 更现实的是做窄问题、局部 use case、特定模式识别

### `8.2 From machine learning to generative AI`

- 这一节开始把视角从 discriminative AI 切到 GenAI
- `8.2.1 Comparing LLMs` 用 GPT-4o、Gemini、Finance Chat 做比较
- 通过 Buffett / Lynch 类问题，作者展示：
  - 模型会给出听起来像样但并不可靠的答案
  - 输出具有非确定性
  - 数据源和时效性并不透明
- Table 8.1（PDF 第 223 页）是第二轮很值得回看的对照表

### `8.2.2` 到 `8.2.4`

- 作者没有把 ML 和 GenAI 设成非此即彼
- 更准确的判断是：
  - ML 适合更窄、更结构化的问题
  - GenAI 更适合更广义的研究辅助
  - 两者可以互补，比如用 GenAI 帮你想 feature、补研究脉络
- 同时也反复提醒：
  - dated information
  - hallucinations
  - broad prompts 带来的泛泛输出

### `8.3 Practical use of GenAI`

- 这是最落地的一节
- `8.3.1 Using LLMs as research assistants` 是整章我最建议你抓牢的一段：
  - 用 LLM 总结长文档
  - 快速了解管理层、lawsuits、insider trades、business model、customer segments
  - 高层分析非金融风险
- Table 8.2（PDF 第 226-227 页）对应 LLM 做高层非金融风险评估的例子
- `8.3.2 Integrating LLMs into code` 则开始讲接入：
  - OpenAI（Listings 8.8, 8.9，PDF 第 228 页）
  - Gemini（Listings 8.10, 8.11，PDF 第 229 页）
  - Mistral（Listing 8.12，PDF 第 230 页）
  - Hugging Face / 本地模型（Listing 8.13，PDF 第 231 页）
- 这节真正想讲的是：
  - 你可以把 LLM 作为研究基础设施的一部分，而不只是聊天网页

### `8.4 Prompt engineering`

- 这一节特别适合程序员视角
- 作者把 prompt engineering 讲得很朴素：
  - 不是玄学
  - 是把上下文、偏好、约束和目标说清楚
- `8.4.1 An investor's profile` 建议你把这些上下文告诉模型：
  - 风险偏好
  - 资金规模
  - 行业偏好
  - broker / wallet
  - 税务身份
  - 排除项和伦理偏好
- `8.4.2 Using prompts to find companies to invest in` 用 Netflix 做例子：
  - Figure 8.8（PDF 第 235-236 页）
  - 把 Netflix 早期成功的要素写进 prompt，看看能不能找出类似公司
  - 但作者仍然明确提醒：LLM 返回的公司只是研究入口，不是投资结论

## 本章收束

如果把 Chapter 8 压成一句话，它真正想留下的是：

- AI 在金融研究里最有价值的角色，不是替你做决定，而是帮助你更快、更广、更系统地做研究

所以这一章真正该带走的，是 4 层意识：

1. ML 很强，但市场和数据让它很难被神化
2. GenAI 很方便，但不能被当成权威投资顾问
3. AI 最适合嵌进研究流程，而不是替代尽调
4. prompt 和上下文质量，会直接决定输出质量
