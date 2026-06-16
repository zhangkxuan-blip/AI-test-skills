# 设计 Token 提取指南

> 用于 Step 3。把"截图"翻译成"可被代码消费的 JSON"。

## 提取顺序

```
颜色 → 字体 → 间距 → 圆角 → 阴影 → 动效
(易)                              (难)
```

颜色取色器精度可达 ±5；越往后越靠"目测+常见值族"。

## 1. 颜色 (Color)

### 1.1 必抽取

| Token | 含义 | 提取方法 |
|---|---|---|
| `color.primary` | 主品牌色 | 主 CTA 按钮 / 选中态 / Logo |
| `color.success` | 成功 | 成功 Toast、绿色徽章 |
| `color.warning` | 警告 | 黄色提示 |
| `color.danger` | 错误/危险 | 删除按钮、错误提示 |
| `color.text.1` | 主文字 | 标题/正文，通常 #1F1F1F~#262626 |
| `color.text.2` | 次文字 | 描述、副标题，通常 #595959~#8C8C8C |
| `color.text.3` | 弱文字 | 占位、禁用，通常 #BFBFBF |
| `color.bg.1` | 主背景 | 页面背景，通常 #FFFFFF |
| `color.bg.2` | 次背景 | 卡片背景、模块底，通常 #FAFAFA~#F5F5F5 |
| `color.border` | 边框 | 通常 #E5E7EB~#D9D9D9 |

### 1.2 提取技巧
- **优先取按钮、选中态、链接** —— 这是品牌色 95% 出现的位置
- **不要从插画/图标取主色** —— 可能是装饰色
- 取到 HEX 后**截断到合理精度**：`#1677FF` 而不是 `#1677FE`

## 2. 字体 (Typography)

### 2.1 字号阶梯（4~6 级即可）

| Token | 典型值 (px) | 用途 |
|---|---|---|
| `font.size.xs` | 12 | 辅助说明、标签 |
| `font.size.sm` | 14 | 正文 |
| `font.size.base` | 16 | 主要内容 |
| `font.size.lg` | 18 | 小标题 |
| `font.size.xl` | 24 | 中标题 |
| `font.size.2xl` | 32 | 大标题 |

### 2.2 字重
- 中文：`400 (Regular)` / `500 (Medium)` / `600 (SemiBold)`
- 西文：可能多一档 `700 (Bold)`

### 2.3 行高
- 紧密：1.2~1.3（标题）
- 标准：1.5~1.6（正文）
- 宽松：1.7+（长文阅读）

## 3. 间距 (Spacing)

### 3.1 选择阶梯族（二选一）

**4 倍族（推荐，主流）**：4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64

**8 倍族（Material 系）**：8 / 16 / 24 / 32 / 40 / 48 / 64

### 3.2 提取
- 测量卡片内边距、按钮内边距、图标和文字间距
- 把测量值**对齐到最近的阶梯值**（如 14px → 16px）

## 4. 圆角 (Radius)

| Token | 典型值 | 出现位置 |
|---|---|---|
| `radius.sm` | 4px | 标签、徽章 |
| `radius.md` | 8px | 按钮、输入框 |
| `radius.lg` | 12~16px | 卡片、模态 |
| `radius.full` | 9999px | 头像、Pill 按钮 |

## 5. 阴影 (Shadow)

| Token | 典型值 | 用途 |
|---|---|---|
| `shadow.card` | `0 1px 3px rgba(0,0,0,.08)` | 静态卡片 |
| `shadow.hover` | `0 4px 12px rgba(0,0,0,.12)` | 悬浮 |
| `shadow.dialog` | `0 8px 32px rgba(0,0,0,.16)` | 模态/抽屉 |

## 6. 动效 (Motion)

| Token | 典型值 | 用途 |
|---|---|---|
| `motion.fast` | 150ms | 微交互（hover） |
| `motion.base` | 250ms | 一般过渡 |
| `motion.slow` | 400ms | 模态/页面切换 |
| `motion.easing` | `cubic-bezier(.4,0,.2,1)` | 标准缓动 |

## 输出格式（统一 JSON）

写到 `output/design-tokens.json`：

```json
{
  "$schema": "../assets/token-schema.json",
  "meta": {
    "platform": "iOS / Web / Android",
    "source": ["screenshots/1.png", "screenshots/2.png"],
    "generated_at": "2026-06-10"
  },
  "color": {
    "primary": { "value": "#1677FF", "confidence": "high" },
    "text": { "1": "#1F1F1F", "2": "#595959", "3": "#BFBFBF" },
    "bg":   { "1": "#FFFFFF", "2": "#FAFAFA" },
    "border": "#E5E7EB",
    "status": {
      "success": "#52C41A",
      "warning": "#FAAD14",
      "danger":  "#FF4D4F"
    }
  },
  "font": {
    "family": "PingFang SC, system-ui, sans-serif",
    "size": { "xs":12, "sm":14, "base":16, "lg":18, "xl":24, "2xl":32 },
    "weight": { "normal":400, "medium":500, "bold":600 },
    "line_height": { "tight":1.25, "normal":1.5 }
  },
  "spacing": [4, 8, 12, 16, 20, 24, 32, 40, 48, 64],
  "radius": { "sm":4, "md":8, "lg":12, "full":9999 },
  "shadow": {
    "card":   "0 1px 3px rgba(0,0,0,.08)",
    "hover":  "0 4px 12px rgba(0,0,0,.12)",
    "dialog": "0 8px 32px rgba(0,0,0,.16)"
  },
  "motion": {
    "duration": { "fast":150, "base":250, "slow":400 },
    "easing": "cubic-bezier(.4,0,.2,1)"
  }
}
```

## 置信度标记

不确定的值标 `"confidence": "low"`，让用户校准：

```json
"radius": {
  "md": { "value": 8, "confidence": "low", "note": "可能是 6 或 8" }
}
```

## 失败兜底（截图不够时）

如果用户只给了一张截图或截图风格混乱，直接套用以下平台默认 Token：

- iOS：参考 Apple HIG，用系统色 `#007AFF`
- Material 3：用 `#6750A4` 紫，圆角 12，阴影柔和
- Ant Design：`#1677FF` 蓝，圆角 6
- 微信小程序：`#07C160` 绿，圆角 4

并在输出里注明 `meta.fallback: "ant-design"`。
