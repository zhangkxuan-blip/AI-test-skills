# 高保真原型技术栈选型

> 用于 Step 4。不同复杂度选不同栈，避免大材小用或力不从心。

## 决策矩阵

| 场景 | 复杂度 | 推荐栈 | 文件数 |
|---|---|---|---|
| 演示用、3~10 页 | 低 | **Tailwind + Alpine.js + 单文件 HTML** ⭐默认 | 5~15 |
| 中等、10~30 页 | 中 | Tailwind + Alpine + 哈希路由 | 20~50 |
| 完整产品、需交付前端 | 高 | React + Vite + shadcn/ui | 项目级 |
| iOS 风格强烈 | 中 | Framework7 | 20~40 |
| Material 3 安卓风 | 中 | Material Web Components | 20~40 |

## 默认栈：Tailwind + Alpine.js

### 为什么选这个组合

- **Tailwind**：原子化 CSS，CDN 一行引入；用 CSS 变量驱动 Token 改风格
- **Alpine.js**：15KB，写在 HTML attribute 里就能做交互（`x-data` / `x-show` / `x-on:click`），不用打包
- **零构建**：双击 HTML 就能开，扔 GitHub Pages / Vercel 30 秒上线

### CDN 引入

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Prototype</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
  <link rel="stylesheet" href="../styles/tokens.css">
  <link rel="stylesheet" href="../styles/app.css">
</head>
```

### Token 注入 Tailwind

在每个 HTML 顶部加：

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: 'var(--color-primary)',
          'text-1': 'var(--color-text-1)',
          'text-2': 'var(--color-text-2)',
          'bg-1':   'var(--color-bg-1)',
          'bg-2':   'var(--color-bg-2)',
        },
        borderRadius: {
          sm: 'var(--radius-sm)',
          md: 'var(--radius-md)',
          lg: 'var(--radius-lg)',
        },
        boxShadow: {
          card: 'var(--shadow-card)',
          dialog: 'var(--shadow-dialog)',
        }
      }
    }
  }
</script>
```

之后写 `class="bg-primary rounded-md shadow-card"`，改 `tokens.css` 全局生效。

## 升级路径

### 升级到 React + shadcn/ui（高复杂度）

触发条件：
- 页面数 > 30
- 有复杂状态管理（购物车、表单流）
- 后续要直接交付给前端开发

```bash
npm create vite@latest prototype -- --template react-ts
cd prototype && npx shadcn-ui@latest init
```

把 Token JSON 转成 `tailwind.config.ts` 的 theme 配置。

### iOS 风格 → Framework7

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/framework7@8/framework7-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/framework7@8/framework7-bundle.min.js"></script>
```

自带 iOS 导航条、Sheet、Action Sheet 等原生组件，省去手撸成本。

### Material 3 → Material Web

```html
<script type="importmap">
{
  "imports": { "@material/web/": "https://esm.run/@material/web/" }
}
</script>
<script type="module">
  import '@material/web/all.js';
</script>
```

## 不要选的栈（产品经理场景）

| 栈 | 原因 |
|---|---|
| Vue/Nuxt 完整项目 | 学习成本高，PM 改不动 |
| Next.js + 数据库 | 过度工程，原型不需要后端 |
| Webflow / Framer | 黑盒，无法用 Token 驱动 |
| 纯 React（无 shadcn） | 要自己写一堆基础组件 |

## 性能/兼容性底线

- 真机预览：iOS 14+ / Android 8+ Chrome
- 单页加载 < 2s（CDN 命中后）
- 移动端首屏 LCP < 2.5s（不要内联 base64 大图）
