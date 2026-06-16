# 原型工程模板

这是 `product-design-kit` skill 在 Step 4 复制并填充的起手模板。

## 怎么跑

```bash
# 方式 1：本地预览（推荐，含真机扫码）
python scripts/preview_server.py output/prototype

# 方式 2：纯静态
python -m http.server 8000 --directory output/prototype
```

## 目录约定

```
prototype/
├── index.html              # 入口 + iframe 路由器
├── pages/                  # 每个页面一个 HTML（独立可运行）
│   ├── home.html
│   ├── list.html
│   ├── detail.html
│   └── ...
├── styles/
│   ├── tokens.css          # 设计 Token (CSS 变量) ← 改这里改风格
│   └── app.css             # 全局基础样式
└── scripts/
    └── router.js           # 极简哈希路由
```

## 怎么改风格

打开 `styles/tokens.css`，改 `:root` 里的 CSS 变量。所有页面同步生效。

## 怎么加页面

1. 在 `pages/` 新建 `xxx.html`，复制 `home.html` 起手
2. 在 `scripts/router.js` 的 `routes` 加一行映射
3. 用 `<a href="#/xxx">` 跳转

## 怎么改交互

参考 `references/interaction-patterns.md` 速查，复制对应代码块改文案。
