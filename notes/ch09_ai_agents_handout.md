# Chapter 9 讲义：AI agents

## 这份讲义怎么用

- 这是一份给“第一遍阅读”准备的讲义版，不要求你先读原文。
- 目标不是覆盖第九章每个框架和每段代码，而是先帮你抓住：什么叫 agent、为什么 one-shot prompting 不够、怎样把 agent 放进结构化研究流程。
- 第二遍回原文时，你只需要带着这份讲义去对照图、例子、listing 和工作流设计。

## 本章在全书里的位置

如果说：

- Chapter 8 教你正确使用 LLM 和 GenAI

那么 Chapter 9 就是在问：

- 当你不满足于“一问一答”时，怎样把 LLM 变成一个能持续参与研究流程的 agent？

所以这章不是“再学几个 AI 概念”，而是在把 AI 从工具，推进到系统组件。

## 这一遍你最需要获得什么

读完这份讲义后，你至少应该拿到 5 个稳定结论：

1. agent 不等于更聪明的 chatbot，而是带有流程、记忆和工具的工作单元
2. one-shot prompting 适合简单任务，但复杂研究需要多步交互和结构
3. prompt repository 和结果导出是很实际的 agent 起点
4. RAG 的重点是把额外资料带进回答，而不是让模型“凭空更懂”
5. agent 的价值主要在结构化研究，不在神化自动判断

## 一页主线

如果把这一章压成最短的一条线，它其实是在讲：

1. 先说明 one-shot prompting 为什么不够
2. 再拆出一个 agent 真正需要哪些能力
3. 然后给你一个不用框架也能跑的最小工作流
4. 再引入 n8n、LangChain 和 RAG 这类更强的实现方式
5. 最后把 agent 放回研究流程，而不是放到神话里

你可以把这一章理解成：

“把 LLM 组织成研究工作流的入门章”

## 核心概念讲解

### 1. 作者先从 one-shot prompting 的边界讲起

Chapter 9 一开始不是讲框架，而是讲一个更基本的限制：

- 你只问一次、模型只答一次，这种交互在复杂研究里不够

作者拿“只能向专家问一个问题”和“能持续追问专家”做对比，这个类比非常好。

因为研究现实里常常是：

- 第一个回答会引出第二个问题
- 第二个问题又会依赖前面的上下文

这就是 one-shot prompting 的天然边界。

回原文时建议这样看：

- Chapter 9 开场：PDF 第 `240-241` 页
- `9.1 Requirements`：PDF 第 `241` 页

### 2. agent 真正需要什么

作者在 `9.1` 里其实是在给 agent 下“能力清单”。

至少包括：

- `memory`
- `strategy`
- `reflection`
- `tool use`
- `planning`
- `multi-agent`

这套清单非常重要，因为它说明：

- agent 的强，不是因为模型突然变聪明
- 而是因为它被放进了一个有组织的结构里

回原文时建议这样看：

- 设计模式与需求展开：PDF 第 `242-244` 页
- 总览图：Figure `9.1`，PDF 第 `245` 页

### 3. 一个很直观的例子：reflection pattern

作者给 reflection pattern 的例子是 trading bot。

这个 bot 不是全天机械执行后就结束，而是：

- 收盘后回看盈利
- 看风险暴露
- 看执行准确度
- 再决定第二天怎么调整策略

这个例子很像程序员做事后复盘。

它在告诉你：

- agent 不只是执行动作
- 还应该回看结果并修正下一轮动作

如果按作者的原始链路把这个例子写完整，大概是这样：

1. 交易日中
- trading bot 按预设策略执行交易
- 它先专注“把动作做出来”

2. 收盘后
- 它开始聚合关键指标
- 作者点到的至少包括：
  - `profitability`
  - `risk exposure`
  - `execution accuracy`

3. 复盘时
- bot 会检查：
  - 哪些策略表现不好
  - 哪些策略错过了关键市场信号
  - 哪些动作让风险暴露过高

4. 下一轮调整
- 根据这些反馈，它会修改第二天的做法
- 作者给的典型动作包括：
  - 收紧风险阈值
  - 降低低收益策略的优先级
  - 微调执行时机

所以这个例子真正想说明的不是：

- agent 会自动变聪明

而是：

- agent 如果能把“执行 -> 评估 -> 调整”做成循环，就会比只会重复执行的系统更像一个真正可进化的工作流

你也可以把它翻成我们更熟悉的话：

- 白天跑任务
- 晚上看监控和复盘
- 第二天调参数和策略

回原文时建议这样看：

- `reflection pattern`：PDF 第 `243` 页
- 先看定义，再看 trading bot 这个例子

### 4. 一个很好的多 agent 例子：法庭式投资辩论

作者讲 `multi-agent pattern` 时，用了一个非常好懂的例子：

- 一个 agent 是乐观派
- 一个 agent 是怀疑派
- 第三个 agent 是中立裁决者

它们像法庭一样围绕“要不要买一只股票”来辩论。

这个例子很重要，因为它把多 agent 的价值讲得很清楚：

- 不是为了堆模型
- 而是为了让不同视角分工协作

回原文时建议这样看：

- multi-agent 例子：PDF 第 `244` 页

### 5. 作者为什么先讲“without frameworks”

这是第九章很好的地方。

很多人一说 agent，就直接跳到框架、SDK、图形编排工具。但作者没有。

他先讲：

- 不用框架，你也能开始做 agentic workflow

而且起点非常朴素：

- 把 prompts 存进数据库
- 给 prompts 打 tag
- 以后按场景取出来复用

这在投资研究里非常合理，因为很多研究问题会反复出现：

- earnings call 前要检查什么
- 某种 thesis 需要问哪些问题
- 某类资产风险分析有哪些固定维度

回原文时建议这样看：

- `9.2.1 Prompt repository`：PDF 第 `246-248` 页
- schema / SQL 例子：PDF 第 `248` 页
- 读取 prompts 的代码：PDF 第 `252` 页

### 6. prompt repository 这个例子到底在解决什么

这部分特别值得你记住。

因为它真正解决的是：

- 好 prompt 很容易在聊天里散掉
- 但研究工作流需要可复用的 prompt 资产

也就是说，作者在把 prompt 从：

- 一次性的聊天输入

变成：

- 可存储、可检索、可复用、可版本化的研究组件

这一步其实非常程序员。

### 7. 为什么要导出到 Notion

`Export results` 这一节重点不在 Notion 产品本身，而在一个更大的原则：

- 研究结果不能只留在 agent 当次输出里

如果不导出，你会碰到这些问题：

- 结果不可复查
- 结果不可累积
- 结果不可和后续研究串起来

所以 Notion 在作者这里更像：

- 研究结果的统一落点

回原文时建议这样看：

- 工作流图与导出结果：Figure `9.2`（PDF 第 `248-249` 页）、Figure `9.3`（PDF 第 `251-252` 页）

### 8. 框架这一节真正想讲什么

作者后面引入 `n8n` 和 `LangChain`，但重点不是比较哪个更潮。

他想讲的是：

- no-code 和 code 是两种不同抽象层

你可以用 UI 画流程，也可以用 Python 写逻辑。

这里最值得带走的不是框架名，而是：

- 任何 agent framework 都是在帮你管理节点、状态、工具调用和流程编排

### 9. 一个很具体的 agent 例子：会查新闻的 MSFT agent

在 `9.3.1` 里，作者给了一个会查 `MSFT` 新闻的 agent transcript。

这个例子重要的地方不在于“Microsoft 应不应该买”，而在于：

- agent 会先决定下一步 action
- 再去调用 `yahoo_finance_news`
- 再根据 observation 继续 reasoning

也就是说，它不是只吐一个静态答案，而是：

- 先行动，再回答

如果把这段例子拆细，链路大概是这样：

1. 先有一个普通 LLM 调用
- 作者先用 `Listing 9.4` 展示 LangChain 的 one-shot prompt
- 比如直接让模型做 `Google` 的 `SWOT analysis`
- 这一步本质上还是“给提示词 -> 拿回答”

2. 再切到 agent 版本
- 到 `Listing 9.5`，作者把 `YahooFinanceNewsTool()` 加进 `tools`
- 然后用 `initialize_agent(...)` 建一个 `ZERO_SHOT_REACT_DESCRIPTION` 类型的 agent
- 再问它：
  - `What happened today with Microsoft stocks?`

这一步和普通 LLM 调用的关键差别是：

- 现在模型不只是直接回答
- 而是先判断“我需要用哪个工具”

3. transcript 里发生了什么

作者把 `verbose=True` 打开后，你能看到 agent 的中间过程：

- `Entering new AgentExecutor chain`
  - 说明 agent 开始进入执行链
- `I should check the latest financial news for Microsoft to see what happened today.`
  - 这是 agent 的内部想法：先去查新闻，而不是直接硬答
- `Action: yahoo_finance_news`
  - 它选中了 Yahoo Finance 新闻工具
- `Action Input: MSFT`
  - 它把自然语言问题转换成了 ticker 级输入
- `Observation: ...`
  - 工具返回了新闻内容摘要
  - 原文里举到的标题大致包括：
    - `Is Microsoft (MSFT) the Best Machine Learning Stock to Buy Now?`
    - `Microsoft Corporation (MSFT): Still Among "Cleanest" AI Plays`
- `Thought: Based on the news articles...`
  - agent 读完 observation 后，再做归纳
- `Final Answer: Microsoft stocks are still performing well in the machine learning and AI sectors.`
  - 最后才给用户可读回答

4. 这段例子真正想说明什么

这段 transcript 最值钱的，不是最终那句结论，而是你能看见：

- agent 会先决定要不要用工具
- 会把用户问题转成适合工具的输入
- 会把工具结果重新并入 reasoning
- 然后才输出最后答案

也就是说，agent 相比 one-shot prompting，多出来的是：

- `reason -> act -> observe -> reason -> answer`

这也是为什么作者会把这一节命名为：

- `From one-shot prompting to agents`

5. 这段的边界也要看清楚

作者并不是在说：

- 这样就等于完成了高质量投资研究

更准确地说，这只是一个最小演示，说明：

- agent 已经可以不靠“纯记忆”回答问题
- 而是开始接外部数据源

但它仍然有明显边界：

- 它依赖接入的数据源质量
- 它做的是高层总结，不是完整尽调
- 最终结论仍然可能过粗、过乐观或过时

回原文时建议这样看：

- 先看 one-shot 示例：`Listing 9.4`，PDF 第 `253-254` 页
- 再看 agent 代码：`Listing 9.5`，PDF 第 `254` 页
- 最后看 transcript：PDF 第 `255` 页

回原文时建议这样看：

- `9.3.1 From one-shot prompting to agents`：PDF 第 `253-255` 页

### 10. 本章最关键的数据层：RAG

`9.3.2 Retrieval-augmented generation` 是整章最重要的一段之一。

它要解决的问题很直接：

- 模型自己并不知道你手头这批文档里的细节
- 那你就得先把文档检索出来，再带进回答过程

作者这里用了自动驾驶 / LiDAR 公司做例子，文件包括：

- `pony.txt`
- `oust.txt`
- `lazr.txt`
- `invz.txt`
- `aeva.txt`

然后又加了两个不同 context：

- 一种偏好 LiDAR
- 一种不偏好 LiDAR

这时同一套材料，agent 会给出不同推荐。

这个例子最想说明的是：

- agent 的回答不是纯靠模型记忆
- 而是会受到检索到的资料和你提供的上下文一起影响

回原文时建议这样看：

- 文档载入与 context：PDF 第 `257-258` 页
- 图：Figure `9.4`，PDF 第 `259-260` 页
- 结果示例：PDF 第 `260` 页

### 11. LiDAR 这个 RAG 例子为什么特别好

因为它把 Chapter 4 的赛道研究又连回来了。

你会看到：

- 同样是自动驾驶公司
- 只是上下文偏好变了
- 输出就会变

这非常贴近真实研究：

- 你的偏好
- 你的 thesis
- 你检索到的材料

都会影响 agent 最后的推荐。

这也正是为什么 agent 不能被神化成“客观真理机”。

## 第一遍最该记住的 5 句话

1. agent 的本质不是“更能聊”，而是“更有流程”。
2. prompt 只是入口，memory、tool use、planning 才让 agent 真正像 agent。
3. 没有框架也可以先做出最小 agentic workflow。
4. RAG 不是锦上添花，而是把额外资料带进回答的关键机制。
5. agent 真正有价值的地方，是结构化研究、复用研究和输出研究结果。

## 第二遍回原文时重点看哪里

如果你第二遍回原文，我建议按这个顺序看：

1. `9.1 Requirements`
  - 先把 agent 的能力清单抓牢
2. `9.1.2 Agentic design patterns`
  - 看各模式各自在补什么
3. `9.2.1 Prompt repository`
  - 这是最务实的起点之一
4. `9.2.2 Export results`
  - 看研究结果如何真正落地
5. `9.3.1 From one-shot prompting to agents`
  - 看 agent 如何从回答走向行动
6. `9.3.2 Retrieval-augmented generation`
  - 看外部资料如何真正进入 agent

## 哪些地方第一遍可以先放过

- LangChain 每个类的 API 细节
- vector database 的具体实现
- n8n 的操作 UI 细节
- 每个 listing 的全部代码

第一遍先抓：

- 为什么要 agent
- agent 在补 one-shot 的什么短板
- 工作流、prompt 资产、RAG 分别解决什么问题

## 这章真正想让你获得什么

如果只用一句话总结 Chapter 9，我会这样说：

- 作者不是在教你“堆一个很酷的 agent”，而是在教你“怎样把 LLM 组织成一个真正能服务研究流程的系统组件”。
