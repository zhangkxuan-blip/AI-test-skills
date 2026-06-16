# Product Design Kit

一站式产品设计 skill：把"业务需求 + 平台截图"变成"可点击的高保真交互原型"。

## 5 步流程

| Step | 输出 | 工具 | 检查点 |
|---|---|---|---|
| 1. PRD | `output/prd.md` | LLM + `prd-template.md` | ✓ |
| 2. 低保真结构稿 | `output/wireframe/wireframe.md` + `flow.mmd` + 规则表 | LLM + `page-patterns.md` | ✓ |
| 3. 内部解析设计风格 | 默认不落文件，直接进入 Step 4；无外部风格时使用内置 Token | LLM (视觉) + 截图/风格文档 | - |
| 4. 高保真原型 | `output/prototype/` | `generate_prototype.py` + LLM | - |
| 5. 真机预览 | http://本机IP:8000 | `preview_server.py` (二维码) | - |

## 快速开始

```bash
# 1) 让 LLM 生成 PRD（在对话里完成，写到 output/prd.md）

# 2) 让 LLM 生成 Markdown 低保真结构稿（写到 output/wireframe/）
#    默认产物：
#    - output/wireframe/wireframe.md
#    - output/wireframe/flow.mmd
#    - output/wireframe/interaction-rules.md
#    - output/wireframe/data-rules.md

# 3) 让 LLM 看截图或设计风格文档，内部解析设计风格
#    默认不生成 Token 文件，直接进入 Step 4
#    如果没有提供外部风格，默认使用：
#    - references/design-token-guide.md
#    - references/icon-guide.md
#    - assets/default-design-tokens.json
#    - assets/default-tokens.css
#    只有用户明确要求“复用这套风格 / 输出 Token / 给前端或设计师复用”时，
#    才输出 output/design-tokens.json、tokens.css 和 token-analysis.md

# 4) 生成原型骨架
python scripts/generate_prototype.py \
    --tokens output/design-tokens.json \
    --pages "home,list,detail,form,me" \
    --out output/prototype \
    --force
#    然后让 LLM 把每个 pages/*.html 填充成真实 UI

# 5) 启动预览（终端打印二维码，手机扫码）
python scripts/preview_server.py output/prototype
```

## 文件结构

```
product-design-kit/
├── SKILL.md                          ← 主流程说明
├── README.md                         ← 你正在看
├── references/
│   ├── prd-template.md               ← Step 1 模板
│   ├── page-patterns.md              ← Step 2 页型库
│   ├── design-token-guide.md         ← 默认设计 Token 指南
│   ├── icon-guide.md                 ← Ant Design 图标规范
│   ├── token-extraction-guide.md     ← Step 3 提取方法论
│   ├── prototype-stack.md            ← Step 4 技术栈选型
│   └── interaction-patterns.md       ← Step 4 交互速查
├── assets/
│   ├── token-schema.json             ← Token JSON Schema
│   ├── default-design-tokens.json    ← 默认 Token JSON
│   ├── default-tokens.css            ← 默认 CSS 变量
│   └── prototype-template/           ← Step 4 起手模板
│       ├── index.html
│       ├── pages/home.html
│       ├── styles/{tokens,app}.css
│       └── scripts/router.js
└── scripts/
    ├── generate_prototype.py         ← 原型骨架生成
    ├── extract_tokens_helper.py      ← Token 校验/兜底
    └── preview_server.py             ← 本地预览 + 二维码
```

## 与 wireframe-generator 的关系

`wireframe-generator` 是这个 skill 的**前身**，仅覆盖 Step 2 + Figma 导出。
本 skill 涵盖端到端 5 步，可独立使用，也可在 Step 4 后调用 `wireframe-generator` 的 `html_to_svg.py` 把高保真页面导出 SVG 喂给 Figma/MasterGo 做精修。
