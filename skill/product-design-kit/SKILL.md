---
name: "product-design-kit"
description: "产品设计端到端工具包：从业务需求生成 PRD、低保真线框图、设计 Token、可点击高保真交互原型。当用户进行产品设计、需要 PRD/原型图/交互稿、提到产品经理工作流、需要把想法变成可演示原型时调用。"
---

# Product Design Kit · 产品设计端到端工具包

## 这是什么

一站式把 **「业务需求」** 变成 **「可在浏览器/手机上点击演示的高保真交互原型」**，全流程 AI 驱动，不依赖 MasterGo / Figma。

## 何时调用

- 产品经理写 PRD、画原型
- 需要快速给老板/客户演示一个"能点的"产品想法
- 需要把竞品/平台风格"复刻"到自己的原型上
- 启动新功能设计，需要从 0 到 1 出方案

## 核心流程（5 步）

```
[输入] 业务需求 + 平台/竞品截图 (2~5 张)
   ↓
Step 1  生成 PRD                    → output/prd.md
   ↓ 用户确认
Step 2  生成低保真结构稿            → output/wireframe/wireframe.md
   ↓ 用户确认
Step 3  从截图反推设计 Token         → output/design-tokens.json
   ↓
Step 4  生成高保真可交互原型         → output/prototype/
   ↓
Step 5  本地起服务 + 二维码真机预览  → http://localhost:8000
```

每一步都有明确产物，用户可在 Step 1、Step 2 后的检查点修订需求。

---

## Step 1 · 生成 PRD

**目标**：把模糊的业务需求变成结构化文档。

**做法**：
1. 引导用户讲清「用户是谁 / 解决什么问题 / 核心场景 / 成功指标」
2. 套用 `references/prd-template.md` 输出
3. 写到 `output/prd.md`，列出页面清单

**输出最少包含**：
- 背景与目标
- 用户角色 & 场景
- 功能清单 (P0/P1/P2)
- 页面清单（这一项是 Step 2 的输入）
- 业务规则（异常/边界）
- 成功指标

**检查点**：列出页面清单后停下来，等用户确认页面范围再进入 Step 2。

---

## Step 2 · 生成低保真结构稿

**目标**：对齐信息架构、页面关系、字段、校验和交互规则，**不关心视觉**。

**默认输出格式**：Markdown + Mermaid + 轻量页面架构预览。

低保真阶段禁止陷入像素级布局、颜色、圆角、间距、图标等视觉细节。此阶段只回答：
- 这个页面有哪些区域？
- 每个区域有哪些字段和按钮？
- 用户从哪里进、点哪里、跳到哪里？
- 有哪些状态、校验、异常和权限规则？

**做法**：
1. 加载 `references/page-patterns.md`，匹配每个页面的页型（列表/详情/表单/弹窗/仪表盘等）
2. 输出 `output/wireframe/wireframe.md`：逐页描述页面结构、模块、字段、按钮和状态
3. 输出 `output/wireframe/flow.mmd`：用 Mermaid 描述页面跳转和关键流程
4. 输出 `output/wireframe/page-architecture.md`：用 ASCII/盒模型展示每个页面的大致区域关系
5. 输出 `output/wireframe/page-architecture.html`：可选的轻量浏览器预览，只展示页面架构，不写视觉细节
6. 输出 `output/wireframe/interaction-rules.md`：集中描述交互、校验、异常和状态规则
7. 输出 `output/wireframe/data-rules.md`：集中描述字段、枚举、唯一性和删除约束

**Markdown 结构约束**：
- 页面用 `## P-xx 页面名` 分节
- 每个页面固定包含：页面目标、入口、页面结构、字段/按钮、状态、交互说明
- 字段和规则优先用表格，不要写长段散文
- 页面跳转统一写到 `flow.mmd`
- 页面区域关系统一写到 `page-architecture.md`
- 校验、异常、状态机统一写到 `interaction-rules.md`
- 数据字段、枚举、唯一性和删除约束统一写到 `data-rules.md`

**页面架构预览约束**：
- 只画区域框架，不画真实 UI 细节
- 允许使用灰色盒子、标题、区域名、箭头和弹窗归属线
- 禁止写颜色体系、圆角、阴影、图标、真实按钮样式和表格细节
- 目标是帮助用户快速判断“页面大概长什么结构”，不是让用户挑视觉

**什么时候才生成详细 HTML 线框**：
- 用户明确要求“可视化低保真图”且接受修改成本
- 页面结构过于复杂，轻量架构预览仍难以理解
- 需要给非产品/非研发人员做视觉走查

即便生成 HTML，也只能作为**页面架构预览**或辅助预览，不作为 Step 2 的主交付物。

**检查点**：让用户走查 `wireframe.md`、`flow.mmd`、`page-architecture.md/html` 和规则表，确认信息架构无误后再进入 Step 3。

---

## Step 3 · 内部解析设计风格

**目标**：从平台/竞品截图或用户提供的设计风格文档中解析视觉规则，让后续高保真原型"长得像"目标平台。

**默认规则**：Step 3 默认只做内部解析，不生成文件，不打断用户；解析完成后直接进入 Step 4。

**做法**：
1. 让用户提供 2~5 张目标风格截图，或提供设计风格文档
2. 内部分析并提取以下风格规则（详见 `references/token-extraction-guide.md` 与 `references/design-token-guide.md`）：
   - **颜色**：主色、辅色、文字 1/2/3、背景 1/2、边框、状态色
   - **字体**：字号阶梯、行高、字重
   - **间距**：4/8/12/16/24/32/48 等阶梯
   - **圆角**：sm/md/lg/full
   - **阴影**：card/dialog/dropdown
   - **组件状态**：按钮、树结构、标签、警告提示、交互反馈
   - **图标规范**：默认遵循 `references/icon-guide.md`
3. 若用户没有提供设计风格文档，默认使用 `assets/default-design-tokens.json` 和 `assets/default-tokens.css`
4. 将解析结果直接用于 Step 4 的高保真 HTML 原型

**什么时候才生成文件**：
- 用户明确要求“这套风格要复用”
- 用户要求“保存成风格规范 / 输出 Token / 给前端或设计师复用”
- 同一套风格将用于多个项目或多次迭代

此时再输出：
- `output/design-tokens.json`
- `output/tokens.css`
- `output/token-analysis.md`

**关键**：颜色用取色器精度可达 95%；间距/圆角靠"目测+常见数值族"，置信度 60~80%，用户可一眼修正。

---

## Step 4 · 生成高保真可交互原型

**目标**：产出一个真能跑、能点、能在手机上预览的多页面原型。

**默认技术栈**：`Tailwind CSS + Alpine.js + 单文件 HTML`
- 改 Token 就改风格（CSS 变量驱动）
- 不用编译，扔到任何服务器/手机浏览器都能开
- 复杂场景可升级到 React + shadcn/ui，详见 `references/prototype-stack.md`

**做法**：
1. 复制 `assets/prototype-template/` 到 `output/prototype/`
2. 把 Step 3 解析得到的 Token 注入 `styles/tokens.css`；若没有外部风格，使用 `assets/default-tokens.css`
3. 按 Step 2 的线框 + Step 1 的 PRD，逐页生成真实 UI（每页一个 HTML 文件）
4. 图标默认遵循 Ant Design 图标语义与 `references/icon-guide.md`
5. 用 Alpine.js 实现交互（点击、跳转、表单、模态、Tab 切换、动画过渡）
6. 必须覆盖三组状态：默认 / 加载（skeleton）/ 空 / 错误
7. 引用 `references/interaction-patterns.md` 里的常见模式

**默认视觉规范**：
- 设计 Token：`references/design-token-guide.md`
- 默认 Token JSON：`assets/default-design-tokens.json`
- 默认 CSS 变量：`assets/default-tokens.css`
- 图标规范：`references/icon-guide.md`

**输出结构**：
```
output/prototype/
├── index.html            # 入口 + 路由
├── pages/
│   ├── home.html
│   ├── list.html
│   ├── detail.html
│   └── ...
├── styles/
│   ├── tokens.css        # 设计 Token (CSS 变量)
│   └── app.css
├── scripts/
│   └── router.js         # 哈希路由
└── README.md             # 怎么跑、怎么改
```

---

## Step 5 · 本地预览 + 真机扫码

**目标**：5 秒内打开真机预览。

**做法**：
1. 运行 `python scripts/preview_server.py output/prototype`
2. 脚本自动：
   - 启动本地 HTTP 服务（端口 8000）
   - 检测本机局域网 IP
   - 在终端打印**二维码**，手机扫码即可在浏览器里点击体验
3. 修改任何 HTML/CSS 后刷新即可

---

## 与其它工具的关系

| 你之前问的 | 在本流程的位置 |
|---|---|
| MasterGo / Figma AI | **可选备选路径**：当需要设计师介入精修时，把 Token + 线框 + Prompt 喂过去（旧 `wireframe-generator` 的 Figma 导出依然可用） |
| ProtoPie / Framer | 复杂物理动效/手势时使用，本 skill 默认不依赖 |
| v0.dev / Lovable | 本 skill 的离线版思路，质量取决于 Prompt 工程 |

## 失败兜底

- 截图模糊或风格不统一 → 让用户补充截图，或允许"通用现代风"
- 复杂业务组件（多维表格、流程图） → 用近似简化版 + 注释 `<!-- 实际开发用 X 组件库 -->`
- 用户拒绝某一步检查点 → 回到上一步修订，不要硬推
