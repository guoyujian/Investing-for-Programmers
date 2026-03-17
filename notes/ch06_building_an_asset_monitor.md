# Chapter 6 笔记: Building an asset monitor

## 笔记说明

- 本笔记用于承接 Chapter 6 的预习、问答和后续总结。
- 当前版本为预习版，目标是先把“资产监控系统到底在解决什么问题、数据从哪里来、怎样整合成一个可持续使用的个人系统”讲清楚，降低正文阅读阻力。
- 如果你想先不读原文，可以先看配套讲义版：[ch06_building_an_asset_monitor_handout.md](/Users/gmet/Projects/learning/Investing-for-Programmers/notes/ch06_building_an_asset_monitor_handout.md)

## 本章信息来源

- 直接解析 PDF：已解析原书 PDF 本体
- 章节目录提取：已提取 Chapter 6 及其小节目录
- 页码样本抽取：已抽取 PDF 第 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166 页
- 回退方案：本章暂未使用回退方案

## 快速导航

1. 本章导读：这一章在讲什么、最重要的概念是什么、读完后应能回答什么
2. 学习优先级与启动：先读哪里、重点抓什么、为什么这章是“个人研究系统”的关键拼图
3. 分节预习笔记：按 `6.1` 到 `6.6` 整理主线
4. 第一轮讲义速览小结：这一轮最该留下什么、第二轮该重点补什么
5. 本章收束：这一章真正要留下来的系统意识

## 第一轮讲义速览小结

- 当前状态：第一轮 `简读 / 速览`（讲义）已完成，第二轮待回原文细读
- 这一轮最重要的收获：
  1. `asset monitor` 不是记账表，而是持仓控制面板
  2. 真正困难的地方不在收益计算，而在多源数据整合
  3. 统一 schema、ticker 映射和货币转换是落地系统的硬问题
  4. stocks、ETFs、bonds、crypto 能放进一个系统，但不能按同一逻辑硬套
  5. 这一章是在把前面几章的能力收束成一个长期可维护的个人工具
- 第二轮回原文最值得重点补的部分：
  1. `6.1 Architecture` 的整体数据流
  2. `6.2 The spreadsheet` 中各 worksheet 的设计
  3. `6.4 Enriching data` 中 lookup、mapping、货币转换
  4. `6.5 Processing assets` 中 stocks / ETFs / bonds / crypto 的差异化处理
- 第二轮实践建议：
  - 用自己的 3-5 个资产先画一版最小 monitor schema
  - 手动列一次 ticker mapping 和货币转换需要的字段
  - 尝试搭一个最小 spreadsheet overview 页，只先放总市值、yield、资产分类和来源

## 本章导读

### 本章主要内容

前面几章更多是在讲：

- 该看什么资产
- 怎么理解财务和数据
- 如何形成 thesis

Chapter 6 则开始回答一个非常程序员的问题：

- 如果我已经持有了一些资产，怎么把它们持续监控起来？

这一章表面上在讲：

1. 架构（architecture）
2. 表格（spreadsheet）
3. 数据提取（extracting data）
4. 数据增强（enriching data）
5. 按资产类型处理（processing assets）
6. 展望（outlook）

但真正主线不是“做个表格”，而是：

1. 怎样把多个来源的持仓汇总到一个统一系统里
2. 怎样把不同资产的价值、收益和未来预期统一表示
3. 怎样让资产监控从“手工记账”升级成“可持续运行的数据管线”

### 本章结构

1. `Architecture`
2. `The spreadsheet`
3. `Extracting data`
4. `Enriching data`
5. `Processing assets`
6. `Outlook`

更细的小节结构是：

1. `6.1 Architecture`
2. `6.2 The spreadsheet`
3. `6.3 Extracting data`
4. `6.3.1 Alpaca: A developer-first broker`
5. `6.3.2 Interactive Brokers: A legacy powerhouse with a modern twist`
6. `6.4 Enriching data`
7. `6.5 Processing assets`
8. `6.5.1 Stocks`
9. `6.5.2 Exchange-traded funds`
10. `6.5.3 Bonds`
11. `6.5.4 Cryptocurrencies`
12. `6.6 Outlook`

### 本章最重要的概念

#### 1. 资产监控不是“记账表”，而是持仓的统一控制面板

作者开头就把目标讲得很清楚：

- staying in control
- staying informed

也就是说，这一章的监控系统不是只拿来记买了什么，而是要帮助你：

- 看总市值
- 看被动收入
- 看表现最好和最差的资产
- 看距离财务目标还有多远

#### 2. 真正的难点不在分析，而在数据整合

这一章最像工程问题的地方是：

- 资产来自不同 broker、exchange、wallet、offline sources
- 它们的数据格式不统一
- 有的能自动抓，有的只能手动补

所以 Chapter 6 的核心不是单一 API，而是：

- 统一数据结构
- 统一标识符
- 统一货币口径

#### 3. 一个个人 monitor 也需要明确架构

作者这里并不是随手写几个脚本，而是在搭一个最小架构：

- 数据源
- 中间数据结构
- 增强逻辑
- 导出层

这和程序员做 ETL / data pipeline 很像。只不过这里处理的是你自己的资产。

#### 4. 不同资产不能硬套同一处理逻辑

这一章很重要的一点是：

- stocks、ETFs、bonds、crypto 都可以统一放进一个系统
- 但不能假装它们完全一样

比如：

- 股票适合拿 `currentPrice`、`targetMeanPrice`、`dividendRate`
- ETF 有 `navPrice`，但很难谈单一公司的 target price
- bond 更像按票面收益和到期结构处理
- crypto 还涉及 exchange / wallet / staking yield 和外部价格源

所以统一的是监控框架，不是分析细节。

#### 5. 这章已经非常接近“个人研究系统成品”

如果说前几章在建立研究能力，那这章已经在开始产出：

- 一个你以后真能长期维护的工具雏形

它会直接把：

- Chapter 3 的数据抓取
- Chapter 4 的 thesis 跟踪
- Chapter 5 的 yield 视角

全都收进一个更系统的容器里。

### 读完本章后你应该能回答的问题

1. 为什么资产监控系统需要统一数据结构，而不是临时拼脚本
2. 为什么 offline assets 也应该进入同一个 monitor
3. 为什么 ticker 映射、货币转换和 lookup table 在实务里很重要
4. stocks、ETFs、bonds、crypto 为什么不能完全按同一逻辑处理
5. 为什么 Google Sheets / spreadsheet 在个人投资系统里依然有价值
6. 这一章怎样把前面几章的研究能力真正串成个人系统

### 关键术语预告

- 资产监控（asset monitor）
- 架构（architecture）
- central repository
- spreadsheet
- worksheet
- 数据提取（extracting data）
- 数据增强（enriching data）
- 数据处理（processing assets）
- 离线资产（offline assets）
- SQLite
- broker API
- Alpaca
- Interactive Brokers
- KYC
- lookup table / asset lookup
- ticker mapping
- Google Finance
- gspread
- ISIN
- Binance

### 少量关键原文

- 原文短摘录：`This chapter is about staying in control, staying informed`
  - 位置：PDF 第 147 页，Chapter 6 开头
  - 中文解释：这一章的主目标不是炫技，而是建立对持仓的控制感和可见性
  - 我的补充理解：这是个人研究系统第一次真正变成“持续运行中的系统”

- 原文短摘录：`we’ll build a data science notebook to consolidate information about your holdings from various sources into a central repository`
  - 位置：PDF 第 148 页，`6.1 Architecture`
  - 中文解释：作者明确把 notebook + central repository 作为本章架构核心
  - 我的补充理解：这句话几乎就是整章的系统设计原则

- 原文短摘录：`Although they differ in detail, we can sum up dividend payments from stocks, coupon rates from bonds, and staking rewards from crypto as "yield"`
  - 位置：PDF 第 166 页，Summary
  - 中文解释：作者试图给不同资产建立一个共同收益语言
  - 我的补充理解：这正是 monitor 里“统一看板”的关键前提

### 本章与程序员能力的关系

- 这一章几乎就是把投资研究变成一个小型数据工程项目
- 你会自然用到程序员熟悉的几个动作：定义 schema、统一标识符、处理异构数据、做 ETL、导出展示层
- 本章也是全书里最像“个人系统搭建”的章节之一
- 对程序员来说，这章的重要性不只是学一个 notebook，而是学“怎样把投资信息系统化”

### 建议阅读方式

这一章建议 `精读`，而且是本书里很值得慢一点的一章。

当前最值得抓的是：

1. `6.1 Architecture`
2. `6.2 The spreadsheet`
3. `6.3 Extracting data`
4. `6.4 Enriching data`
5. `6.5 Processing assets`

这里真正重要的不是背每段代码，而是看懂：

- 为什么系统要先有统一输入结构
- 为什么 enrich / process / export 要分层
- 为什么不同资产虽然能进一个系统，但处理方式不能完全一样

## 学习优先级与启动

### 这一章到底最重要的是哪部分

如果只问“Chapter 6 最核心的是哪几节”，我会给这个判断：

- **真正的核心主线是 `6.1 + 6.3 + 6.4 + 6.5`**

可以把它们这样理解：

- `6.1 Architecture`
  - 系统重点
  - 它决定你有没有一个正确的 monitor 心智模型

- `6.3 Extracting data`
  - 接入重点
  - 它决定你怎么把分散持仓接进系统

- `6.4 Enriching data`
  - 数据重点
  - 它决定你怎么把原始持仓变成可分析对象

- `6.5 Processing assets`
  - 业务重点
  - 它决定你会不会按资产特性做正确处理

### 这一章先怎么读

- 第一段先读 PDF 第 147-151 页
- 目标不是先看具体 broker，而是先理解：
  1. asset monitor 在解决什么问题
  2. 为什么需要 architecture 和 central repository
  3. 为什么 spreadsheet 仍然是个合理的展示层

- 第二段再读 PDF 第 151-157 页
- 目标是补上：
  1. 如何从不同 broker 提取数据
  2. 为什么要统一 schema
  3. 为什么要处理 ticker mismatch 和 currency conversion

- 第三段再读 PDF 第 158-166 页
- 目标是看懂：
  1. 不同资产类别怎样进入同一系统
  2. 为什么 stocks / ETFs / bonds / crypto 既能统一又必须区分
  3. Chapter 6 最后想让你留下什么模板意识

### 第一段最该抓住的内容

- 资产监控系统的目标是控制感，不只是好看
- 先统一持仓数据，再谈图表和导出
- offline assets 也必须纳入系统
- 架构设计比单个 API 更重要

### 第一段阅读提醒

- 不要把这章误读成“Google Sheets 教程”
- 不要一上来就纠结某家 broker 的接入细节
- 先看清楚作者为什么要把不同资产统一到同一套 schema
- 记住：这章的核心不是工具名字，而是系统分层

## 分节预习笔记

### 6.1 Architecture

#### 这一节最该抓住的主线

- 监控系统的第一步是定义数据流，不是先写公式
- 数据从多源进入 central repository，再导出到可视化层
- 架构先行，后面才不容易越写越乱

#### 对当前阶段最重要的结论

- monitor 不是单一表格，而是一条 data flow

### 6.2 The spreadsheet

- spreadsheet 是展示层，也是过滤、汇总和对比的交互层
- 它让你快速看价值、yield 和 live data
- 这里的重点是“结果怎么被使用”，不是表格本身有多炫

### 6.3 Extracting data

#### 这一节最该抓住的主线

- broker 不同，接口和数据结构就不同
- 你需要先定义统一 target schema，再去接入不同来源
- security / keys / KYC 这些现实约束也必须进入系统设计

#### 对当前阶段最重要的结论

- 不是 API 越多越好，而是输入结构越统一越好

### 6.4 Enriching data

- 原始持仓不够用，还需要价格、yield、target、currency 等补充信息
- ticker 映射和 lookup table 很关键
- enrichment 是“从持仓记录走向分析对象”的桥梁

### 6.5 Processing assets

#### 这一节最该抓住的主线

- 可以统一 monitor
- 但不能用同一分析逻辑硬套所有资产

#### 6.5.1 Stocks

- 股票适合补 current price、target price、dividend rate 等信息
- 适合直接算 value、past gain、projected gain、yield

#### 6.5.2 Exchange-traded funds

- ETF 可以沿用部分股票处理思路
- 但不能期待像单个公司那样有完整 target / thesis 逻辑

#### 6.5.3 Bonds

- bond 的关键标识更像 ISIN，不是普通 ticker
- 债券更适合按 yield 和 par value 逻辑处理

#### 6.5.4 Cryptocurrencies

- crypto 需要对接不同 price provider
- 还要同时考虑 exchange 持仓和 ledger 持仓
- staking yield 也要进入系统

### 6.6 Outlook

- 这一章不是最终成品，而是模板
- 真正重要的是你以后可以继续往这个 monitor 里加更多分析和自动化能力

## 本章收束

学完这一章后，你最应该留下的不是某个 API 的调用方式，而是下面这些稳定结论：

1. asset monitor 本质上是一个个人投资数据系统
2. 多源持仓必须先统一结构，才能稳定分析
3. enrichment 和 processing 是 monitor 的关键中间层
4. 不同资产可以共用同一框架，但不能混用同一业务逻辑
5. Chapter 6 是把“研究能力”开始沉淀成“长期工具”的关键章节
