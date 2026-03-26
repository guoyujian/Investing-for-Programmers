# Chapter 7 笔记: Risk management

## 笔记说明

- 本笔记用于承接 Chapter 7 的预习、问答和后续总结。
- 当前版本为预习版，目标是先把“风险管理到底在解决什么问题、哪些风险需要分类和量化、怎样把风险意识落到组合动作里”讲清楚，降低正文阅读阻力。
- 如果你想先不读原文，可以先看配套讲义版：[ch07_risk_management_handout.md](/Users/gmet/Projects/learning/Investing-for-Programmers/notes/ch07_risk_management_handout.md)

## 本章信息来源

- 直接解析 PDF：已解析原书 PDF 本体
- 章节目录提取：已提取 Chapter 7 及其小节目录
- 页码样本抽取：已抽取 PDF 第 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 180, 185, 188, 191, 195, 197, 199, 203 页
- 回退方案：本章暂未使用回退方案

## 快速导航

1. 本章导读：这一章在讲什么、最重要的概念是什么、读完后应能回答什么
2. 学习优先级与启动：先读哪里、重点抓什么、为什么这章是全书的风险地基
3. 分节预习笔记：按 `7.1` 到 `7.6` 整理主线
4. 第一轮讲义速览小结：这一轮最该留下什么、第二轮该重点补什么
5. 本章收束：这一章真正要留下来的风险管理意识

## 第一轮讲义速览小结

- 当前状态：第一轮 `简读 / 速览`（讲义）已完成，第二轮待回原文细读
- 这一轮最重要的收获：
  1. 风险管理的目标不是避免亏损，而是控制伤害、避免一次出局
  2. 风险必须拆成不同来源，不能只说“风险很大”
  3. `VaR` 和 `correlation` 帮你获得风险数量级感，但不能替代判断
  4. 你自己的行为偏差也是风险源
  5. 风控最终一定要落到组合动作，比如分散、对冲和再平衡
- 第二轮回原文最值得重点补的部分：
  1. `7.1 Ukemi` 的风险哲学和风险矩阵
  2. `7.2.1 Value at risk (VaR)` 的定义、Listing 7.1 和 Figure 7.4
  3. `7.2.2 Correlation` 的统计表和相关性例子
  4. `7.4.3 Pair trading` 与 `7.4.4 Risk pairing`
  5. `7.6.3 Rebalancing`
- 第二轮实践建议：
  - 给自己现有或假想的 3-5 个持仓列一个最小风险矩阵
  - 手工比较一组高相关资产和一组低相关资产
  - 为一个简化组合写出再平衡触发条件

## 本章导读

### 本章主要内容

Chapter 7 看起来会让人以为它只是在讲：

1. 止损（stop-loss）
2. 风险指标（VaR、correlation）
3. 对冲（hedging）
4. 组合优化（portfolio optimization）

但它真正回答的是一个更基础的问题：

- 如果市场不会按我的 thesis 走，我怎么限制损失、理解暴露、保住继续活下去的能力？

所以这一章的主线不是“预测风险”，而是：

1. 先承认风险一定存在
2. 再把风险拆分类、做测量、做人因管理
3. 最后把风险控制落实到单个资产和整个组合

### 本章结构

1. `Ukemi`
2. `Generating risk profiles for individual stocks`
3. `The human factor`
4. `Hedging`
5. `Nonfinancial risk`
6. `Portfolio optimization`

更细的小节结构是：

1. `7.1 Ukemi`
2. `7.1.1 Stop-loss`
3. `7.1.2 Risk classification`
4. `7.1.3 Risk measurement`
5. `7.2 Generating risk profiles for individual stocks`
6. `7.2.1 Value at risk (VaR)`
7. `7.2.2 Correlation`
8. `7.3 The human factor`
9. `7.3.1 Negligence`
10. `7.3.2 Risk avoidance`
11. `7.3.3 Resilience`
12. `7.4 Hedging`
13. `7.4.1 Derivatives`
14. `7.4.2 Diversification`
15. `7.4.3 Pair trading`
16. `7.4.4 Risk pairing`
17. `7.5 Nonfinancial risk`
18. `7.5.1 Markets`
19. `7.5.2 Economic data`
20. `7.5.3 Assessing nonfinancial risk`
21. `7.6 Portfolio optimization`
22. `7.6.1 Markowitz-efficient portfolio`
23. `7.6.2 Shiller P/E ratio`
24. `7.6.3 Rebalancing`

### 本章最重要的概念

#### 1. 风险管理不是为了“避免所有亏损”，而是为了“摔得起”

作者用 `ukemi` 开场，非常有意思。它来自武道语境，强调的不是“永远不摔”，而是：

- 摔的时候别把自己摔废

放到投资里就是：

- 你不可能消灭风险
- 但你可以设计仓位、止损、对冲、分散和再平衡，让一次错误不至于把你打出局

#### 2. 风险不是一个词，而是一组不同来源的暴露

这一章很重要的动作是把风险拆开：

- 市场风险
- 行业风险
- 个股风险
- 宏观和非金融风险
- 人因风险

如果不拆开，风险管理很容易变成空话；一旦拆开，你才知道该在哪一层做动作。

#### 3. 风险既要分类，也要测量

Chapter 7 不是只停在概念层。作者开始引入：

- `stop-loss`
- `risk matrix`
- `Value at Risk (VaR)`
- `correlation`
- `Sharpe ratio`

但这些指标的作用不是让你装得更专业，而是帮助你回答：

- 一天可能亏多少
- 这个资产和别的资产会不会一起跌
- 我承担的波动和回报是否划算

#### 4. 人不是风控系统外部的观察者

这一章有个很重要的提醒：

- 风险不只来自市场，也来自你自己

比如：

- 疏忽（negligence）
- 逃避风险判断（risk avoidance）
- 在波动中失去执行纪律

所以风控不只是数学问题，也是行为问题。

#### 5. 风控最终要落实到组合层，而不是停在单个资产

单个资产的 thesis 可能没错，但整个组合依然可能：

- 暴露在同一种宏观风险上
- 高度相关
- 在极端行情下同步受损

所以这一章后半段把视角推向：

- diversification
- pair trading
- risk pairing
- efficient portfolio
- rebalancing

这才是作者真正想让你形成的组合意识。

### 读完本章后你应该能回答的问题

1. `ukemi` 在投资风险管理里到底强调什么
2. `stop-loss`、风险分类、风险测量分别负责什么
3. `VaR` 和 `correlation` 为什么会成为单资产风险画像的基础工具
4. 为什么“人因风险”也是风险管理的一部分
5. 对冲、分散、pair trading、risk pairing 分别在解决什么问题
6. 为什么宏观和非金融数据也会改变组合风险
7. Markowitz、Shiller CAPE、rebalancing 在这一章里各自扮演什么角色

### 关键术语预告

- 风险管理（risk management）
- 受身 / 安全摔法（ukemi）
- 止损（stop-loss）
- 风险分类（risk classification）
- 风险测量（risk measurement）
- 风险矩阵（risk matrix）
- 风险画像（risk profile）
- 风险价值（Value at Risk, VaR）
- 相关性（correlation）
- 协方差（covariance）
- 忽视 / 疏忽（negligence）
- 风险回避（risk avoidance）
- 韧性（resilience）
- 对冲（hedging）
- 衍生品（derivatives）
- 分散化（diversification）
- 配对交易（pair trading）
- 风险配对（risk pairing）
- 非金融风险（nonfinancial risk）
- 宏观数据（economic data）
- 马科维茨有效组合（Markowitz-efficient portfolio）
- 夏普比率（Sharpe ratio）
- 席勒市盈率（Shiller P/E ratio, CAPE）
- 再平衡（rebalancing）

### 少量关键原文

- 原文短摘录：`Ukemi`
  - 位置：PDF 第 168 页，`7.1 Ukemi`
  - 中文解释：作者借用“安全摔法”的概念，强调投资里先学会控制损失，再谈进攻
  - 我的补充理解：这是整章最好的总标题，风控不是不许失败，而是失败时别被淘汰

- 原文短摘录：`Value at Risk`
  - 位置：PDF 第 174 页，`7.2.1 Value at risk (VaR)`
  - 中文解释：作者开始引入能帮助你估计亏损区间的风险指标
  - 我的补充理解：这一段更像是在教你获得“数量级感”，不是让你相信数字能完全控制风险

- 原文短摘录：`rebalancing`
  - 位置：PDF 第 200 页，`7.6.3 Rebalancing`
  - 中文解释：组合管理不能只在买入那一天完成，后续还要持续校准暴露
  - 我的补充理解：这把风控真正落回日常动作，而不是停留在纸面模型

### 本章与程序员能力的关系

- 这一章特别像“给研究系统补容错层”
- 你会自然用到程序员熟悉的几个视角：失败模式、暴露面、监控阈值、异常处理、回退策略
- `VaR`、`correlation`、宏观指标、再平衡规则，都可以看成风险观测和控制逻辑
- 对程序员来说，这章的重要性不只是学几个金融名词，而是学“系统设计为什么必须先考虑 failure modes”

### 建议阅读方式

这一章建议 `精读`，但第一轮最值得抓的是：

1. `7.1 Ukemi`
2. `7.2.1 Value at risk (VaR)`
3. `7.2.2 Correlation`
4. `7.3 The human factor`
5. `7.4 Hedging`
6. `7.5 Nonfinancial risk`
7. `7.6.1 Markowitz-efficient portfolio`
8. `7.6.3 Rebalancing`

这里真正重要的不是把所有公式都算熟，而是先建立：

- 风险管理是全书的生存层
- 指标只是服务于判断，不是取代判断
- 单资产风控和组合风控是两层不同问题

## 学习优先级与启动

### 这一章到底最重要的是哪部分

如果只问“Chapter 7 最核心的是哪几节”，我会给这个判断：

- **真正的核心主线是 `7.1 + 7.2 + 7.3 + 7.6`**

可以把它们这样理解：

- `7.1 Ukemi`
  - 心态重点
  - 它决定你把风险管理理解成“躲开波动”，还是“控制伤害”

- `7.2 Generating risk profiles for individual stocks`
  - 单资产重点
  - 它决定你能不能开始量化理解某个资产的风险暴露

- `7.3 The human factor`
  - 行为重点
  - 它决定你会不会把自己也纳入风险源

- `7.6 Portfolio optimization`
  - 组合重点
  - 它决定你能不能把风控真正推进到整个 portfolio 层

`7.4 Hedging` 和 `7.5 Nonfinancial risk` 也重要，但更像是在给上面这条主线补工具和背景。

### 第一遍先抓什么

如果你第一遍不想被公式压住，最推荐先抓 4 件事：

1. 作者为什么要用 `ukemi` 做开场
2. `VaR` 和 `correlation` 分别想回答什么问题
3. 为什么“人因风险”会单独成节
4. 为什么风险管理最终一定要走到再平衡

### 第一遍不必卡住的地方

第一遍可以先不要求自己彻底吃透：

- Monte Carlo 的每个计算细节
- 协方差和相关系数的手算过程
- Markowitz 优化的数学推导
- Shiller CAPE 的历史争议

先抓这些内容“在系统里干什么”，第二轮再补“怎么算得更扎实”。

## 分节预习笔记

### `7.1 Ukemi`

- 这一节的核心不是“避免所有跌幅”，而是建立风险管理的基本态度
- `stop-loss` 是最直观的第一层动作：不是证明 thesis 错了才动作，而是先限制损失扩大
- 风险分类和风险矩阵在这一节开始出现，帮助你把“风险很大”拆成更具体的层次
- 其中一个特别值得记住的例子是：
  - Figure 7.2 把一个 AI startup 的风险拆成内部经营、组织、市场和外部环境几个层次
  - 具体包括 `mismanagement`、`lack of funding`、`lack of engineers`、`demand lost`、`regulatory risk`、`political risk`、`high energy prices`、`disruptor`
  - 它想说明的不是“AI 很危险”，而是成长型 / 创业型公司往往会同时受多类风险夹击，而且这些风险可能彼此放大
- Figure 7.3 的风险矩阵则把这些风险进一步放进：
  - 发生概率（likelihood）
  - 伤害程度（harm severity）
  - 例如反 AI 运动可能不常见，但一旦形成政策或社会推动，伤害可能很大；高能源价格则更现实，会持续抬高 AI 成本、拖慢扩张
- 作者随后又给了一个更贴近组合管理的例子：
  - 假设持有 `Coca-Cola`、`Apple`、`Pfizer`
  - 再问“如果中美贸易战升级会怎样”
  - 经过快速研究后，可以认为 `Apple` 受到的潜在伤害更大，因此风险等级更高
- 这组例子真正想训练的是：
  - 先列风险清单
  - 再做优先级排序
  - 最后把排序结果转成具体持仓关注和动作
- 一个值得记住的图是：
  - Figure 7.1（PDF 第 169 页）：止损如何跟着上涨而上移
  - Figure 7.2（PDF 第 172 页）：AI startup 的高层风险模型
  - Figure 7.3（PDF 第 173 页）：风险矩阵

### `7.2 Generating risk profiles for individual stocks`

- 这一节是在给单个资产做“风险画像”
- `VaR` 负责帮助你估计在给定置信区间下可能损失多少
- 作者用 Monte Carlo simulation 帮你看到“未来结果分布”，而不是给出一个单点预测
- 对照原文时要注意：
  - `VaR` 的定义在 PDF 第 174-175 页
  - 原书这里没有先给一个很显眼的封闭公式，而是用 Listing 7.1（PDF 第 175-176 页）展示 Monte Carlo 的做法
  - Figure 7.4（PDF 第 176 页）展示模拟结果图
- `correlation` 则帮助你理解两个资产是否容易一起动
- 这里的例子很重要：
  - 作者用 `MSFT / AMZN / GOOGL` 这类大科技股展示高相关性
  - 又用 `WMT / NVDA` 这类风格差异更大的组合帮助你体会相关性差别
- Figure 7.4（PDF 第 176 页）和 Table 7.1-7.5（PDF 第 178-180 页）是第二轮应重点回看的图表

### `7.3 The human factor`

- 这一节特别值得程序员认真读，因为它像在讲“系统的错误不只来自外部输入”
- `negligence` 指的是你明明该做检查，却因为懒惰、粗心或过度自信没有做
- `risk avoidance` 不是健康的谨慎，而是回避面对真正需要评估的风险
- `resilience` 更像是在强调：
  - 市场和 thesis 不按你预期走时，你能不能保持动作能力

### `7.4 Hedging`

- 这一节不是让你变成衍生品交易员，而是让你知道：
  - 对冲是在主动买保险或做反向暴露
- 作者提到：
  - `derivatives`
  - `diversification`
  - `pair trading`
  - `risk pairing`
- 这里最好理解的，不一定是复杂期权，而是：
  - 为什么两边同时布局能减少纯方向性暴露
- 读 `pair trading` 时先别被术语拦住：
  - 多头（`long position`）就是先买入，赌价格上涨
  - 空头（`short position`）就是先卖出借来的资产，赌价格下跌
- `pair trading` 的原书例子很具体：
  - `Company A` 和 `Company B` 同属 AI 板块
  - 你看好 `A` 的增长潜力，看空 `B` 的相对表现
  - 做法是做空 `100 美元` 的 `B`，再把这笔钱拿去买入 `A`
  - 如果 AI 热潮继续，`A` 大涨而 `B` 涨得较少，你仍可获利
  - 如果 AI 板块整体下跌，但 `B` 跌得更惨，空头盈利可以抵消多头损失
  - 真正危险的是 thesis 错了：`A` 变弱而 `B` 变强，这时两边都会伤到你
- 这一段真正想说明的是：
  - 你不是在押整个市场方向
  - 而是在押两个相关资产的相对强弱
- Figure 7.5（PDF 第 188 页）适合第二轮回看 long-short / pair trade 的示意

### `7.5 Nonfinancial risk`

- 这一节在提醒你：公司研究做得再细，也不代表组合不会被外部环境一起冲击
- 作者开始拉进：
  - 市场状态
  - 宏观数据
  - 非金融风险评估
- 这里最值得第二轮回看的图：
  - Figure 7.6（PDF 第 191 页）：收益率曲线
  - Figure 7.7（PDF 第 191 页）：失业率
- 这一节真正想训练的是：
  - 别把风险只想成“公司基本面风险”

### `7.6 Portfolio optimization`

- 这一节把前面的风险意识推进到 portfolio 层
- `Markowitz-efficient portfolio` 在作者这里不是为了教你做学术推导，而是帮助你理解：
  - 回报与风险不是单看单个资产，而是看组合结果
- `Shiller P/E ratio` 被拉进来，是为了给市场整体估值提供一个长期背景
- `rebalancing` 则是最落地的动作：当组合漂移后，你如何把它拉回风险边界
- 第二轮重点图表：
  - Figure 7.8（PDF 第 195 页）
  - Figure 7.9（PDF 第 197 页）
  - Table 7.6（PDF 第 197 页）
  - Figure 7.10（PDF 第 199 页）
  - Table 7.7（PDF 第 203 页）

## 本章收束

如果把 Chapter 7 压成一句话，它真正想留下的是：

- 投资不是先追求收益最大化，而是先建立“出错时还能继续活下去”的系统

所以这一章真正该带走的，不是某个单独公式，而是 4 层意识：

1. 风险一定会发生
2. 风险要分类、量化、监控
3. 你自己也是风险源
4. 风控最终要落实到组合动作和持续再平衡
