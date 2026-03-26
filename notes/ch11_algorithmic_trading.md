# Chapter 11 笔记: Algorithmic trading

## 笔记说明

- 本笔记用于承接 Chapter 11 的预习、问答和后续总结。
- 当前版本为预习版，目标是先把“算法交易到底在把什么自动化、哪些环节只是研究辅助、哪些环节会直接影响真实盈亏”讲清楚，降低正文阅读阻力。
- 如果你想先不读原文，可以先看配套讲义版：[ch11_algorithmic_trading_handout.md](/Users/gmet/Projects/learning/Investing-for-Programmers/notes/ch11_algorithmic_trading_handout.md)

## 本章信息来源

- 直接解析 PDF：已解析原书 PDF 本体
- 章节目录提取：已提取 Chapter 11 及其小节目录
- 页码样本抽取：已抽取 PDF 第 297, 298, 299, 300, 302, 304, 306, 307, 309, 311, 313, 315, 316, 319 页
- 回退方案：本章暂未使用回退方案

## 快速导航

1. 本章导读：这一章在讲什么、最重要的概念是什么、读完后应能回答什么
2. 学习优先级与启动：第一遍先抓哪条线、哪些地方不要急着卡住
3. 分节预习笔记：按 `11.1` 到 `11.4` 整理主线
4. 本章启动结论：第一遍进入这一章时最该先抓住什么

## 本章导读

### 本章主要内容

Chapter 11 表面上在讲：

1. nonfinancial data
2. catalysts
3. trading algorithms
4. backtesting
5. orders
6. brokers、exchanges 和执行

但它真正回答的是一个更完整的问题：

- 当你已经有数据、图表、risk management 和 AI 辅助之后，怎样把“一个交易想法”推进成“一个可执行、可回测、可下单的规则”？

所以这章的主线不是“写几段自动买卖代码”，而是：

1. 先找什么样的信息可能构成 edge
2. 再找什么样的 event 可以触发 price move
3. 然后把信号写成可回测的规则
4. 最后面对一个很现实的问题：
   - 真实世界里，order type、broker 和 execution 也会改变结果

### 本章结构

1. `11.1 Nonfinancial data`
2. `11.1.1 Big data by example`
3. `11.2 Catalysts`
4. `11.2.1 Mergers and acquisitions`
5. `11.2.2 Companies in distress`
6. `11.2.3 Earnings calls`
7. `11.2.4 Disasters`
8. `11.2.5 Interest rate changes`
9. `11.3 Trading algorithms`
10. `11.3.1 Backtesting`
11. `11.3.2 Complex trading signals`
12. `11.4 Orders`
13. `11.4.1 Exchanges vs. brokers`
14. `11.4.2 Order modifiers`
15. `11.4.3 Executing orders`

### 本章最重要的概念

#### 1. 算法交易不是“神秘自动赚钱”，而是把判断写成规则

这一章在把前面学过的东西往执行层推进：

- 你先有 thesis
- 再有数据
- 再有 signal
- 再把 signal 写成规则
- 然后用 backtest、order 和 execution 去检验这个规则能不能落地

也就是说，算法交易真正自动化的，是一套预先定义好的判断和动作，而不是“自动产生智慧”。

#### 2. nonfinancial data 之所以重要，是因为市场价格不只被财报推动

作者一开始就把视角从传统 financial statements 拉开，指出：

- social media
- traffic patterns
- product usage
- news flow
- 事件型信息

这些非财务数据也可能影响价格，甚至在某些时候影响更快、更猛。

关键不是“什么都抓”，而是：

- 先有一个投资 / 交易 thesis
- 再问什么额外数据可能帮助你验证它

#### 3. catalyst 是“会让价格突然加速变化”的触发器

这一章里很重要的一层是：

- 有些交易不是赌长期基本面慢慢显现
- 而是赌某个催化事件会让市场更快重估资产

比如：

- mergers and acquisitions
- companies in distress
- earnings calls
- disasters
- interest rate changes

#### 4. backtesting 只能告诉你“这套规则在历史里长什么样”，不能保证未来复制

作者用 SMA crossover 给了一个最小回测示例，这很适合作为入门例子。

但他也提醒了一个关键现实：

- 你在图上看到的 close price
- 不等于你真实执行能拿到的价格

这意味着：

- spread
- slippage
- fees
- timing

都可能让纸面结果和真实结果出现差异。

#### 5. order 和 execution 不是 plumbing，而是策略的一部分

这一章后半段特别重要，因为很多人会把 broker、exchange、market order、limit order 当成下单细节。

但作者其实在提醒：

- 你怎么买
- 你向谁下单
- 订单带什么 modifier

这些都会改变风险和成交结果。

### 读完本章后你应该能回答的问题

1. 为什么 nonfinancial data 会在现代市场里越来越重要
2. catalyst 在交易语境里到底指什么
3. backtesting 在帮你验证什么，又没有帮你验证什么
4. 为什么同一个 signal，换一种 order 或 execution 结果可能就变了
5. broker 和 exchange 在真实下单链路里各自负责什么

### 关键术语预告

- algorithmic trading
- nonfinancial data
- big data
- catalyst
- mergers and acquisitions
- distress investing
- earnings call
- backtesting
- simple moving average（SMA）
- crossover
- signal
- market order
- limit order
- order modifiers
- exchange
- broker
- leverage

### 本章与程序员能力的关系

- 这一章非常像把一个 hypothesis 转成可运行 workflow
- 你会用到程序员熟悉的几种能力：
  - 数据接入
  - 规则表达
  - 历史验证
  - API 调用
  - 执行与失败模式思考
- 对程序员来说，这章的重要性不在“开始高频交易”，而在“理解从研究到执行的完整链路到底多了哪些现实约束”

### 建议阅读方式

这一章建议第一遍先抓 4 件事：

1. 作者为什么先讲 nonfinancial data，而不是直接讲策略
2. catalyst 在交易里扮演什么角色
3. backtesting 的最小示例到底在证明什么
4. order / broker / exchange 为什么不是最后才补的操作细节

第一遍先不要急着卡住：

- 每一类 catalyst 的细节分类
- 每段 Python 代码的 API 语法
- 每种 order modifier 的经纪商实现差异

先抓住本章的因果链：

- thesis -> data -> catalyst -> signal -> backtest -> order -> execution

## 学习优先级与启动

### 这一章到底最重要的是哪部分

如果只问“Chapter 11 最核心的是哪几节”，我会给这个判断：

- **真正的核心主线是 `11.1 + 11.2 + 11.3.1 + 11.4`**

可以把它们这样理解：

- `11.1 Nonfinancial data`
  - edge 来源
  - 它决定你是不是只会看传统财务数据

- `11.2 Catalysts`
  - 事件触发
  - 它决定你会不会把“什么会让市场突然重估”纳入模型

- `11.3.1 Backtesting`
  - 验证层
  - 它决定你是不是把一个想法至少先放回历史里试一遍

- `11.4 Orders`
  - 执行层
  - 它决定你有没有意识到真实交易结果不只取决于 signal

### 第一遍先抓什么

第一遍最推荐先抓 4 条线：

1. `nonfinancial data` 解决的是“信息差从哪来”
2. `catalysts` 解决的是“为什么价格会突然动”
3. `backtesting` 解决的是“这套规则历史上是否成立过”
4. `orders and execution` 解决的是“纸面策略怎么变成真实成交”

### 第一遍不必卡住的地方

第一遍可以先不要求自己彻底吃透：

- 每一种套利玩法的细节
- 每个交易 API 的具体参数
- 复杂 signal 的数学构造

先把这章看成：

- 一次“从研究走向执行”的框架搭建

## 分节预习笔记

### `11.1 Nonfinancial data`

- Chapter 11 一开头就把视角从传统 financial data 拉开。
- Figure `11.1`（PDF 第 `298` 页）是这一节的关键图。
  - 更适合先看图，再回头看定义。
  - 它在展示多种数据源、更新频率和 trading model / algorithm 的关系。
- 这一节最重要的提醒之一是：
  - 市场价格不只被财务报表影响
  - 非财务信息在现代信息环境里可能传播更快
- PDF 第 `299` 页特别值得注意：
  - 作者把“过去信息慢、后来网络快、现在社交媒体更快”这条线拉了出来
  - 重点不是怀旧，而是在说明 data environment 变了

#### `11.1.1 Big data by example`

- 这一小节用 big data 例子来说明：
  - 不要为了“有很多数据”而收很多数据
  - 正确顺序是 thesis 先行
- PDF 第 `300` 页的例子值得第一遍记住：
  - Google / Waymo / robotaxi 方向
  - 先有一个行业判断
  - 再追问什么额外数据可能帮助验证 adoption 和商业化
- Renaissance Technologies 在这里更像一个象征：
  - 代表“把另类数据系统化”的一类做法
  - 不代表你第一步就该无目标抓全网数据

### `11.2 Catalysts`

- 作者在这里把 catalyst 讲成：
  - 会让 stock price 显著上行或下行的触发事件
- 这一节的核心不是背清单，而是训练你去问：
  - 什么事件会让市场突然重估？
- PDF 第 `302` 页建议先看定义，再看例子。
- Figure `11.2`（PDF 第 `302` 页）建议先看图，再回头看作者怎么解释事件链路。

#### `11.2.1 Mergers and acquisitions`

- M&A 是典型 catalyst。
- 它的交易意义不只是“并购是大新闻”，而是：
  - 市场会重新定价 target company
  - 同时也会重新评估 acquirer 的风险和整合能力

#### `11.2.2 Companies in distress`

- PDF 第 `304` 页的 distress 例子很重要。
- Figure `11.3`（PDF 第 `304` 页）更适合先看图，再看作者解释。
- 这一部分的重点不是“抄底破产公司”，而是理解：
  - 破产 / 重组 / 收购流程本身会带来事件型机会和事件型风险
- `stalking horse agreement` 是这一节值得记住的术语。
- 作者也明确提醒：
  - 破产股权通常很危险
  - 极少数 turnaround 不代表这是默认可复制策略

#### `11.2.3 Earnings calls`

- earnings call 在这里被放进 catalyst，不只是基本面跟踪。
- 因为财报电话会、管理层措辞和 guidance 变化，都可能直接引发短期价格重估。
- 第一遍只要先记住：
  - earnings call 不是静态数据表，而是事件窗口

#### `11.2.4 Disasters`

- PDF 第 `306` 页这里拿 wildfire 一类例子，提醒你：
  - 灾难并不只是新闻标题
  - 对某些公司是经营打击
  - 对另一些公司可能是订单或重建需求机会

#### `11.2.5 Interest rate changes`

- 利率变化也是事件型 catalyst。
- 作者这里的重点不是重新讲宏观，而是说明：
  - capital-intensive companies
  - 高估值成长公司
  - 某些疫情后高波动主题
  可能会对利率变化特别敏感

### `11.3 Trading algorithms`

- 这一节开始把前面的数据和事件推进成规则。

#### `11.3.1 Backtesting`

- 这是本章最像“最小可运行示例”的地方。
- 作者用 SMA crossover 做了一个非常入门但很有效的例子：
  - 短期 SMA 上穿长期 SMA -> buy
  - 短期 SMA 下穿长期 SMA -> sell
- `Listing 11.1`（PDF 第 `307` 页）
  - 更适合先看代码定义，再看它产生了哪些列
  - 作用是给数据加上 SMA 和 validation 列
- `Listing 11.2`（PDF 第 `309` 页）
  - 更适合先看例子，再理解参数
  - 作者拿 NVDA 的历史数据做回测
- `Listing 11.3`（PDF 第 `309-310` 页）
  - 更适合和结果表一起看
- `Table 11.1`（PDF 第 `310` 页）与 `Table 11.2`（PDF 第 `311` 页）
  - 建议先看结果，再回头看代码
  - 它们在帮你把“信号”变成“资金曲线 / 策略结果”
- 这一节真正要记住的不是某个参数，而是：
  - backtesting 至少能帮你避免完全凭感觉上策略

#### `11.3.2 Complex trading signals`

- 作者在这里往前再推一步：
  - 真实 signal 往往不只是一条均线交叉
  - 可能会组合多种 price、volume、event 或 alternative data
- 但作者也提醒了现实约束：
  - 图上的 close price 不等于真实成交价
  - signal 成立不等于 execution 无摩擦

### `11.4 Orders`

- 这一节的重要性比很多人想的更高。
- 因为真实交易世界里，决定结果的除了 signal，还有：
  - order type
  - broker
  - exchange
  - routing

#### `11.4.1 Exchanges vs. brokers`

- Figure `11.4`（PDF 第 `313` 页）是这一节最关键的图。
  - 更适合先看图，再看定义。
- 这一图想帮你厘清：
  - exchange 是撮合市场
  - broker 是你和市场之间的中介 / 接入口
- 这不是术语洁癖，而是会影响：
  - 费用
  - 路由
  - 杠杆
  - 可交易资产

#### `11.4.2 Order modifiers`

- `Table 11.3`（PDF 第 `315` 页）
  - 更适合先看表，再回头看名词解释
  - 这里整理了常见 order types / modifiers
- `Table 11.4`（PDF 第 `316` 页）
  - 建议和执行代码一起看
  - 有助于把“术语”连到“真实下单动作”

#### `11.4.3 Executing orders`

- PDF 第 `316` 页这里有 IBKR Trader Workstation API 例子。
- PDF 第 `319` 页有 Alpaca 的 `LimitOrderRequest` 例子。
- 这一部分的重点不是某一家券商 SDK，而是：
  - 当你把策略推进到实际下单时，工程问题和交易问题开始真正重叠

## 本章启动结论

如果把 Chapter 11 压成一句话，它真正想让你建立的是：

- 算法交易不是从“神秘策略”开始，而是从“有 thesis、有数据、有事件、有回测、有执行约束”的完整链路开始

所以第一遍进入本章时，最该先抓住的是 4 层意识：

1. edge 不只来自财务报表
2. 事件往往是 price move 的加速器
3. 回测只能降低盲目性，不能消灭现实摩擦
4. 下单方式本身就是策略的一部分
