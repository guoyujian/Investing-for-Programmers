# Chapter 9 笔记: AI agents

## 笔记说明

- 本笔记用于承接 Chapter 9 的预习、问答和后续总结。
- 当前版本为预习版，目标是先把“AI agent 和普通 chatbot 到底差在哪、怎样把 agent 放进投资研究流程、为什么需要工作流 / 记忆 / 工具 / RAG”讲清楚，降低正文阅读阻力。
- 如果你想先不读原文，可以先看配套讲义版：[ch09_ai_agents_handout.md](/Users/gmet/Projects/learning/Investing-for-Programmers/notes/ch09_ai_agents_handout.md)

## 本章信息来源

- 直接解析 PDF：已解析原书 PDF 本体
- 章节目录提取：已提取 Chapter 9 及其小节目录
- 页码样本抽取：已抽取 PDF 第 240, 241, 242, 243, 244, 245, 246, 248, 249, 251, 252, 253, 255, 257, 258, 259, 260, 261 页
- 回退方案：本章暂未使用回退方案

## 快速导航

1. 本章导读：这一章在讲什么、最重要的概念是什么、读完后应能回答什么
2. 学习优先级与启动：先读哪里、重点抓什么、为什么这章不是“agent 框架导览”
3. 分节预习笔记：按 `9.1` 到 `9.3` 整理主线
4. 第一轮讲义速览小结：这一轮最该留下什么、第二轮该重点补什么
5. 本章收束：这一章真正要留下来的 agent 工作流意识

## 第一轮讲义速览小结

- 当前状态：第一轮 `简读 / 速览`（讲义）已完成，第二轮待回原文细读
- 这一轮最重要的收获：
  1. agent 的本质不是更会聊天，而是更有流程、记忆和工具
  2. one-shot prompting 适合简单任务，但复杂研究需要多步工作流
  3. prompt repository 和结果导出是很实用的 agent 起点
  4. RAG 的重点是把额外资料带进回答，而不是让模型凭空更懂
  5. agent 的价值主要在结构化研究，不在神化自动判断
- 第二轮回原文最值得重点补的部分：
  1. `9.1.2 Agentic design patterns`
  2. `9.2.1 Prompt repository`
  3. `9.2.2 Export results`
  4. `9.3.1 From one-shot prompting to agents`
  5. `9.3.2 Retrieval-augmented generation`
- 第二轮实践建议：
  - 给自己整理一个最小 prompt repository
  - 试做一次“one-shot prompt vs 带工具 agent”的对比
  - 用一组本地文本材料模拟最小 RAG

## 本章导读

### 本章主要内容

Chapter 9 表面上在讲：

1. AI agents
2. prompt repository
3. Notion 导出
4. LangChain
5. RAG
6. n8n

但它真正回答的是一个更核心的问题：

- 如果 LLM 已经能回答问题，为什么我们还需要 agent 和工作流？

所以这一章的主线不是“再学几个框架名”，而是：

1. 先理解 one-shot prompting 的边界
2. 再理解 agent 为什么需要 memory、strategy、reflection、tool use、planning、multi-agent
3. 然后看到不用框架时如何把 prompt、结果和导出组织起来
4. 最后再进入框架、RAG 和多数据源集成

### 本章结构

1. `Requirements`
2. `Agentic workflows without frameworks`
3. `Framework for AI agents`

更细的小节结构是：

1. `9.1 Requirements`
2. `9.1.1 Successful communication`
3. `9.1.2 Agentic design patterns`
4. `9.2 Agentic workflows without frameworks`
5. `9.2.1 Prompt repository`
6. `9.2.2 Export results`
7. `9.3 Framework for AI agents`
8. `9.3.1 From one-shot prompting to agents`
9. `9.3.2 Retrieval-augmented generation`

### 本章最重要的概念

#### 1. agent 不是“更会聊天的 LLM”，而是“有流程、有记忆、有工具的任务单元”

作者开头先把 Chapter 8 里的一次性提问推进到更复杂的协作流程。

这一章真正要你看到的是：

- chatbot 更像一次性问答
- agent 更像能持续执行步骤、调用工具、保留上下文并输出结果的工作流节点

#### 2. 成功的 agent 通信，关键不只是 prompt，而是 memory + strategy

Chapter 9 一上来就把“成功沟通”拆成几个条件：

- memory
- strategy
- reflection
- tool use
- planning
- multi-agent

也就是说，agent 的价值不只来自模型本身，而来自：

- 能否拿到外部信息
- 能否保留上下文
- 能否按目标组织动作

#### 3. 没有框架也能做 agentic workflow，但你要自己补结构

作者中段先讲“without frameworks”，这点很重要。

他不是一上来就让你学 LangChain，而是先做两件很朴素但很关键的事：

- 建 prompt repository
- 把研究结果导出到一个可复用的知识库（如 Notion）

这部分的核心意思是：

- 先把工作流结构化，再谈框架

#### 4. RAG 的核心不是酷炫，而是把补充数据带进回答过程

本章后半段进入 RAG 时，作者想讲的不是定义本身，而是：

- LLM 训练时没见过、或记不住、或没权限拿到的信息，必须通过额外检索带进来

这就是为什么：

- earnings call transcript
- 本地文档
- 自己的 prompt catalog
- 外部数据库

会变得重要。

#### 5. agent 的真正价值在结构化研究，不在“自动神谕”

整章看下来，作者并不是在说：

- agent 会替你做投资决策

而是在说：

- agent 可以把研究任务拆开、组织、复用、导出、再检索

### 读完本章后你应该能回答的问题

1. one-shot prompting 和 AI agent 的差别到底是什么
2. 为什么 memory、strategy、reflection、tool use 会被单独提出来
3. 为什么 prompt repository 是一个很实用的起点
4. 为什么研究结果要导出到像 Notion 这样的结构化地方
5. LangChain / n8n / RAG 在本章里各自扮演什么角色
6. 为什么 agent 适合结构化研究，而不该被神化成万能分析师

### 关键术语预告

- AI agent
- one-shot prompting
- memory
- reflection pattern
- tool use pattern
- planning pattern
- multi-agent pattern
- prompt repository
- workflow
- export results
- Notion
- LangChain
- no-code
- retrieval-augmented generation（RAG）
- vector database
- context
- orchestrator
- MCP

### 少量关键原文

- 原文短摘录：`Building AI agents for structured research`
  - 位置：PDF 第 240 页，Chapter 9 开头
  - 中文解释：作者直接把 agent 和“structured research”绑在一起
  - 我的补充理解：这说明本章重点不是聊天，而是研究流程设计

- 原文短摘录：`one-shot prompting`
  - 位置：PDF 第 241 页
  - 中文解释：作者拿一次性问答当对照组，来说明 agent 为什么值得引入
  - 我的补充理解：这一章很多内容都可以理解成“怎么超越 one-shot”

- 原文短摘录：`The multi-agent pattern coordinates multiple specialized agents`
  - 位置：PDF 第 244 页
  - 中文解释：多 agent 的重点是 specialization + coordination
  - 我的补充理解：它更像团队协作，而不是一个超大 agent 什么都做

### 本章与程序员能力的关系

- 这一章特别像“把 AI 嵌进研究系统的工程化下一步”
- 你会自然用到程序员熟悉的视角：状态、记忆、工具调用、数据源、工作流、结果导出、组件编排
- 本章也在训练你从“会用模型”走到“会设计 agentic system”
- 对程序员来说，这章的重要性不是框架 API，而是 workflow thinking

### 建议阅读方式

这一章建议 `精读`，但第一轮最值得抓的是：

1. `9.1.1 Successful communication`
2. `9.1.2 Agentic design patterns`
3. `9.2.1 Prompt repository`
4. `9.2.2 Export results`
5. `9.3.1 From one-shot prompting to agents`
6. `9.3.2 Retrieval-augmented generation`

这里真正重要的不是把每段 LangChain 代码都背下来，而是先看懂：

- agent 为什么需要结构化组件
- 没框架时最小 workflow 长什么样
- RAG 和多源数据为什么会成为下一步

## 学习优先级与启动

### 这一章到底最重要的是哪部分

如果只问“Chapter 9 最核心的是哪几节”，我会给这个判断：

- **真正的核心主线是 `9.1 + 9.2 + 9.3.2`**

可以把它们这样理解：

- `9.1 Requirements`
  - 概念重点
  - 它决定你能不能把 agent 理解成工作流，而不是更高级聊天框

- `9.2 Agentic workflows without frameworks`
  - 实务重点
  - 它决定你是否能在不用大框架时先搭起最小流程

- `9.3.2 Retrieval-augmented generation`
  - 数据重点
  - 它决定你是否理解 agent 为什么要接外部信息源

### 第一遍先抓什么

如果你第一遍不想被框架名和代码量压住，最推荐先抓 4 件事：

1. one-shot prompting 为什么不够
2. agentic design patterns 各自在补什么能力
3. prompt repository 为什么值得单独成节
4. RAG 到底是在解决“模型不知道什么”的问题

### 第一遍不必卡住的地方

第一遍可以先不要求自己彻底吃透：

- LangChain 的具体类和方法
- vector database 的实现细节
- n8n 的 UI 操作步骤
- 每个 listing 的代码细节

先抓这些内容“在研究系统里干什么”，第二轮再补“怎么实现得更稳”。

## 分节预习笔记

### `9.1 Requirements`

- 这一节从 one-shot prompting 的局限讲起
- 作者用“只能问一个问题”和“能持续追问专家”的对比，说明 why agent
- `9.1.1 Successful communication` 的重点不是 prompt 话术，而是条件：
  - memory
  - strategy
  - reflection
  - tool use
  - planning
  - multi-agent
- Figure 9.1（PDF 第 245 页）是第二轮很值得回看的总览图

### `9.1.2 Agentic design patterns`

- 这里特别适合程序员读，因为它像在讲可复用设计模式
- `reflection pattern` 的例子是 trading bot：
  - 收盘后回看盈利、风险暴露、执行准确度
  - 再决定第二天怎么调整
  - 更完整地说，是把“执行 -> 评估 -> 调整”做成循环
  - 作者给的调整方向包括：收紧风险阈值、降低低收益策略优先级、微调执行时机
  - 这节回原文时可直接对照 PDF 第 243 页
- `tool use pattern` 强调 agent 不该只靠内部推理，而应调用外部工具
- `planning pattern` 强调动态任务分解与优先级调整
- `multi-agent pattern` 用“乐观派 / 怀疑派 / 中立裁决者”做买股判断的类法庭例子（PDF 第 244 页）

### `9.2 Agentic workflows without frameworks`

- 这一节很重要，因为作者先讲“先别急着上框架”
- `9.2.1 Prompt repository` 用 SQLite 之类的简单数据库存 prompts 和 tags
- 这一段真正想教的是：
  - 好 prompts 值得复用
  - 研究工作流需要可检索、可复用、可分类的 prompt 资产
- Listing 9.1（PDF 第 248 页）和后续取 prompt 的例子（PDF 第 252 页）是第二轮值得回看的代码

### `9.2.2 Export results`

- 这一节的重点不是 Notion 本身，而是：
  - 研究结果需要落地
  - 不能只停在聊天窗口里
- 作者把 Notion 当成一个结构化出口，帮助把研究组织到统一地方
- Figure 9.2（PDF 第 248-249 页）和 Figure 9.3（PDF 第 251-252 页）适合第二轮看整体工作流

### `9.3 Framework for AI agents`

- 这一节开始引入 no-code 与 code 两条路
- 作者把 n8n 和 LangChain 放在一起，强调的是：
  - UI 编排 vs 代码编排
  - abstraction 的便利 vs 灵活性和定制化
- `9.3.1 From one-shot prompting to agents` 给了一个会查 `MSFT` 新闻的 agent transcript（PDF 第 255 页）
- 这一段真正想讲的是：
  - agent 会自己决定下一步 action，而不是只吐一段文本
 - 更细一点看，这段是三步走：
   - 先用 `Listing 9.4` 展示普通 one-shot prompt
   - 再用 `Listing 9.5` 接入 `YahooFinanceNewsTool`
   - 最后在 transcript 里展示 `Thought -> Action -> Observation -> Final Answer`
 - transcript 里最关键的细节是：
   - agent 先判断“应该去查 Microsoft 的最新新闻”
   - 然后调用 `yahoo_finance_news`
   - 再把 `MSFT` 作为工具输入
   - 读取返回的新闻摘要后，才给出高层结论
 - 这节真正想说明的是：
   - agent 比 one-shot prompt 多出来的是 `reason -> act -> observe -> answer` 的工作流
 - 回原文时建议对照：
   - `Listing 9.4`：PDF 第 253-254 页
   - `Listing 9.5`：PDF 第 254 页
   - transcript：PDF 第 255 页

### `9.3.2 Retrieval-augmented generation`

- 这一节是全章最关键的数据层内容
- 作者用自动驾驶 / LiDAR 公司的文本材料做例子：
  - `pony.txt`
  - `oust.txt`
  - `lazr.txt`
  - `invz.txt`
  - `aeva.txt`
- 再给两种不同 context：
  - 偏好 LiDAR
  - 不偏好 LiDAR
- 然后看 agent 在同一材料库上如何给出不同推荐
- Figure 9.4（PDF 第 259-260 页）是这部分最值得第二轮回看的图
- 这节真正想说明的是：
  - agent 输出不是凭空生成
  - 它会受到检索到的文档和你提供的 context 共同影响

## 本章收束

如果把 Chapter 9 压成一句话，它真正想留下的是：

- AI agent 的核心价值，不是替你神奇回答一切，而是把研究任务组织成“可检索、可复用、可输出、可迭代”的工作流

所以这一章真正该带走的，是 4 层意识：

1. 先从 one-shot prompt 走向 workflow
2. 再从单次回答走向 memory 和 tool use
3. 再把 prompts 和结果变成可复用资产
4. 最后用 RAG 把外部资料真正接进 agent
