# Chapter 12 笔记: Private equity: Investing in start-ups

## 笔记说明

- 本笔记用于承接 Chapter 12 的预习、问答和后续总结。
- 当前版本为预习版，目标是先把“私募股权 / start-up 投资和公开市场股票投资到底差在哪、投资人到底在看什么、风险主要堆在哪”讲清楚，降低正文阅读阻力。
- 如果你想先不读原文，可以先看配套讲义版：[ch12_private_equity_investing_in_startups_handout.md](/Users/gmet/Projects/learning/Investing-for-Programmers/notes/ch12_private_equity_investing_in_startups_handout.md)

## 本章信息来源

- 直接解析 PDF：已解析原书 PDF 本体
- 章节目录提取：已提取 Chapter 12 及其小节目录
- 页码样本抽取：已抽取 PDF 第 321, 322, 323, 324, 325, 327, 328, 329, 330, 332, 333, 334, 336, 337, 338, 339, 340, 341, 342, 343, 344 页
- 回退方案：本章暂未使用回退方案

## 快速导航

1. 本章导读：这一章在讲什么、最重要的概念是什么、读完后应能回答什么
2. 学习优先级与启动：第一遍先抓哪条线、哪些地方不要急着卡住
3. 分节预习笔记：按 `12.1` 到 `12.3` 整理主线
4. 本章启动结论：第一遍进入这一章时最该先抓住什么

## 本章导读

### 本章主要内容

Chapter 12 表面上在讲：

1. start-up 从 pre-seed 到 IPO 的演化
2. venture capital、angel networks、sovereign wealth funds
3. valuation、dilution、scoring

但它真正回答的是一个更根本的问题：

- 如果你不是在二级市场买成熟公司的股票，而是在更早期、更不透明、更不流动的阶段投资 start-up，应该怎样换一套投资视角？

所以这章的主线不是“创业者怎么融资”，而是：

1. 先从投资人视角看 start-up 生命周期
2. 再理解不同投资载体怎样参与私募股权
3. 最后面对估值、稀释和打分这些现实问题

### 本章结构

1. `12.1 From idea to initial public offering`
2. `12.1.1 The first minimum viable product (pre-seed)`
3. `12.1.2 Validating the business model (seed)`
4. `12.1.3 Scaling a start-up: The shift to institutional investment`
5. `12.1.4 Exits: The final transition`
6. `12.2 Investment vehicles`
7. `12.2.1 Venture capital`
8. `12.2.2 Angel networks`
9. `12.2.3 Sovereign wealth funds`
10. `12.3 Assessing start-ups`
11. `12.3.1 Valuation`
12. `12.3.2 Dilution`
13. `12.3.3 Scoring`

### 本章最重要的概念

#### 1. private equity 的核心区别不是“更早买”，而是更不透明、更不流动、更依赖人和路径

在 start-up 投资里，你买到的是非公开市场上的所有权份额。

这意味着：

- 没有像公开市场那样随时交易的价格
- 很多信息并不标准化
- 退出时间很长
- 失败概率极高

所以这章本质上是在教你：

- 从“看报表和价格”切换到“看人、看 business model、看融资路径和 exit 可能性”

#### 2. start-up 的每一轮融资，对应的不是同一种风险

作者把 pre-seed、seed、Series A/B/C 拉开，是为了说明：

- 每个阶段的风险、关注点和投资人类型都不一样

例如：

- pre-seed 更像在赌 founder、vision 和 MVP
- seed 开始验证 business model
- Series A/B/C 更像在赌 scale、execution 和 exit

#### 3. VC 并不是“慢慢赚分红”的耐心资本

本章非常重要的一点是：

- VC 要的是高增长和 exit
- 慢增长、稳定盈利、长期发小额分红，不是它的典型游戏

这也是为什么作者专门讲：

- exit
- fail fast
- illiquidity
- why slow profitable businesses may not fit VC expectations

#### 4. valuation 和 dilution 在 start-up 世界里都充满假设

作者给了 DCF 和 dilution 的 Python 小例子，但这章并没有把它们神化成“精确答案”。

真正想强调的是：

- start-up 估值高度依赖假设和谈判
- 每一轮融资会改变 cap table 和 ownership
- 账面估值好看，不代表投资回报就稳

#### 5. scoring 的目的不是制造神准模型，而是把高不确定性拆成可比较维度

到了 `12.3.3 Scoring`，作者在把主观判断尽量结构化。

可考虑的维度包括：

- incubator / accelerator
- founders
- existing investors
- clients / partnerships
- country of origin
- domain
- regulations
- economic moat
- capital intensity
- burn rate
- business model
- network effects
- north star metrics

### 读完本章后你应该能回答的问题

1. 为什么 private equity / start-up 投资和公开市场股票投资是两套不同心智
2. pre-seed、seed、Series A/B/C 最核心的风险差异是什么
3. 为什么 VC 会高度在意 exit，而不是慢慢拿回报
4. valuation 和 dilution 在这类投资里分别在解决什么问题
5. 为什么 start-up 评分模型更多是在结构化判断，而不是算出真相

### 关键术语预告

- private equity
- pre-seed
- seed
- Series A / B / C
- MVP
- incubator
- IPO
- exit
- venture capital（VC）
- limited partner（LP）
- carry fee
- special purpose vehicle（SPV）
- cap table
- valuation
- discounted cash flow（DCF）
- dilution
- burn rate
- economic moat
- north star metrics

### 本章与程序员能力的关系

- 这一章很像把“技术人看产品”的视角切换成“投资人看公司”的视角
- 你会用到程序员熟悉的几种能力：
  - scenario thinking
  - assumption modeling
  - cap table / ownership 这种结构化建模
  - 把主观判断拆成 scoring 维度
- 对程序员来说，这章的重要性不在“去做 VC”，而在“知道早期公司为什么难投、难估、难退出”

### 建议阅读方式

这一章建议第一遍先抓 4 件事：

1. start-up 生命周期和普通公司投资到底差在哪
2. exit 为什么是 VC 逻辑的核心
3. VC、angel network、SPV 各自在干什么
4. valuation、dilution、scoring 分别是在回答什么

第一遍先不要急着卡住：

- 每种估值方法的金融细节
- 每个 LP / GP 费用结构的法律文本
- 每个 scoring 维度的量化口径

先抓住本章的因果链：

- founder / idea -> stage -> funding vehicle -> ownership / exit -> valuation / dilution / scoring

## 学习优先级与启动

### 这一章到底最重要的是哪部分

如果只问“Chapter 12 最核心的是哪几节”，我会给这个判断：

- **真正的核心主线是 `12.1 + 12.1.4 + 12.2.1-12.2.2 + 12.3`**

可以把它们这样理解：

- `12.1`
  - 生命周期视角
  - 它决定你是不是在用错误的阶段预期看 start-up

- `12.1.4 Exits`
  - 回报逻辑
  - 它决定你能不能理解 VC 为什么那么在意速度和结果

- `12.2.1 Venture capital` 与 `12.2.2 Angel networks`
  - 资金组织方式
  - 它决定你能不能看懂 private equity 的参与路径

- `12.3`
  - 判断框架
  - 它决定你会不会把 start-up 评估只做成“感觉不错”

### 第一遍先抓什么

第一遍最推荐先抓 4 条线：

1. pre-seed 到 Series C 的风险是怎样变化的
2. VC 为什么不是给慢增长公司设计的
3. VC fund / SPV / angel syndicate 分别在怎么组织资本
4. DCF、dilution、scoring 为什么在 start-up 世界里都只是辅助框架

### 第一遍不必卡住的地方

第一遍可以先不要求自己彻底吃透：

- 每个 fund 的法律结构
- DCF 的推导细节
- 如何给 scoring 精确权重

先把这章看成：

- 一次“把 start-up 投资放回风险和路径里理解”的框架搭建

## 分节预习笔记

### `12.1 From idea to initial public offering`

- Chapter 12 一开头就明确切换到 investor view。
- PDF 第 `322` 页值得先看定义：
  - private equity 是私下持有、非公开交易的 ownership
- 这一节最重要的价值是：
  - 把创始人视角换成投资人视角

#### `12.1.1 The first minimum viable product (pre-seed)`

- PDF 第 `322-324` 页是 pre-seed 例子。
- Fred 这个朋友创业的场景很值得保留：
  - 这里更适合先看例子，再回头看概念
- 第一轮最该抓的是：
  - pre-seed 不是在看稳定财务数据
  - 更像在看 founder、vision、执行力和能否撑到 MVP
- 作者也明确提醒：
  - pre-seed 是 high-risk / high-reward
  - 统计上大多数钱都收不回来

#### `12.1.2 Validating the business model (seed)`

- PDF 第 `325` 页开始进入 seed。
- 这里的重要例子是 incubator demo day 和 TAM / SAM / SOM。
- 这一节在提醒你：
  - seed 不只是“产品有了”
  - 还要开始证明市场和 business model 说得通

#### `12.1.3 Scaling a start-up: The shift to institutional investment`

- PDF 第 `327-328` 页把注意力转向 institutional investors。
- 这一节最关键的变化是：
  - 风险降低了一点
  - 但资金需求急剧放大
- Series A/B/C 的重点开始从“做出东西”转向：
  - scale
  - retention
  - expansion
  - path to profitability

#### `12.1.4 Exits: The final transition`

- 这是本章很重要的一节。
- Table `12.1`（PDF 第 `328-329` 页）
  - 更适合先看表，再看作者解释
  - 它在总结几类 exit 和对应场景
- 这一节最关键的提醒是：
  - VC 要的是 exit
  - 不是慢慢拿回报
- 作者也很清楚地指出：
  - illiquidity 会给投资人施加压力
  - slow growth 和 already profitable 的公司不一定是 VC 最想要的标的

### `12.2 Investment vehicles`

- 这一节在回答：
  - 如果你真想参与 private equity，通常是通过哪些资本组织形式进入？

#### `12.2.1 Venture capital`

- Figure `12.1`（PDF 第 `332-333` 页）
  - 更适合先看图，再回头看名词
  - 它在讲 LP -> VC fund -> start-up -> carry / fee 的资金流结构
- 这一节最该记住的是：
  - 顶级 VC 通常不对普通散户开放
  - minimum ticket size 很高
  - 你看到的是 pooled capital，而不是“给某一家 start-up 直接打电话投资”

#### `12.2.2 Angel networks`

- Figure `12.2`（PDF 第 `334` 页）
  - 更适合先看图，再看解释
  - 它在讲 lead investor、SPV、LP 和 cap table 的关系
- 这一节的重要术语是：
  - syndicate
  - lead investor
  - SPV
- 它的现实意义是：
  - 给 smaller check size 的投资者一个进入更早期项目的方式

#### `12.2.3 Sovereign wealth funds`

- PDF 第 `335-336` 页这一节更像扩展视野。
- 它提醒你：
  - start-up ecosystem 也会被国家级资本和政策导向影响

### `12.3 Assessing start-ups`

- 这一节开始把“感觉”推进成更结构化的判断。

#### `12.3.1 Valuation`

- `Listing 12.1`（PDF 第 `337` 页）
  - 更适合先看代码示例，再看它背后的假设
  - 它用 Python 做了一个 start-up DCF 的最小示例
- 但作者也紧接着在 PDF 第 `338` 页提醒：
  - 参数全都可以被争论
  - 风险很难被完全量化
- 所以这里更像：
  - 用模型帮助思考
  - 不是制造精确幻觉

#### `12.3.2 Dilution`

- `Listing 12.2`（PDF 第 `339` 页）
  - 更适合先看结果意义，再回头看代码
  - 它演示每一轮融资后 founder ownership 如何下降
- 这一节最重要的不是“稀释很坏”，而是：
  - 稀释是融资增长的代价
  - 关键看 ownership 减少和 company value 增长之间是否匹配

#### `12.3.3 Scoring`

- PDF 第 `340-344` 页是这一节的重点范围。
- 这里最值得记住的是作者列出的多个非财务打分维度。
- PDF 第 `344` 页的 summary 式清单很适合第二轮回看：
  - incubator / accelerator
  - founders
  - investors
  - clients / partnerships
  - country of origin
  - domain
  - regulations
  - economic moat
  - capital intensity / burn rate
  - business model
  - network effect
  - north star metrics

## 本章启动结论

如果把 Chapter 12 压成一句话，它真正想让你建立的是：

- start-up 投资不是“买更早的股票”，而是在高不确定、长锁定期、强路径依赖的环境里评估人、赛道、资本结构和退出可能性

所以第一遍进入本章时，最该先抓住的是 4 层意识：

1. stage 决定你在赌什么
2. exit 决定 VC 为什么这么看重速度和增长
3. 资金载体决定你以什么方式参与
4. valuation / dilution / scoring 只是帮助你结构化判断，不是替你消灭不确定性
