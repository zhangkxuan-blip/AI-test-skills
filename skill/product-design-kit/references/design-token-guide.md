# 默认设计 Token 指南

> 本指南基于用户提供的设计规范图沉淀，作为 `product-design-kit` 的默认视觉规范。  
> 当用户没有提供新的设计风格文档时，Step 4 默认按本规范生成高保真原型。  
> 当用户提供新的设计风格文档时，以用户新文档为准。

## 1. 设计原则

- 后台产品优先保证信息密度、稳定性和可读性。
- 主色用于关键行动、链接、选中态和焦点态，不要滥用。
- 中性色承担页面层级、文本层级、边框、背景和禁用状态。
- 控件反馈必须覆盖默认、悬停、按下、禁用四类状态。
- 复杂页面优先使用轻量边框和浅背景区分层级，避免重阴影和强装饰。

## 2. 品牌色

| Token | 值 | 用途 |
|---|---|---|
| `color.brand.bg` | `#EAF5FF` | 品牌浅背景、弱选中背景 |
| `color.brand.1` | `#B7DCFF` | 浅蓝色块 |
| `color.brand.2` | `#7DBAF5` | 辅助蓝 |
| `color.brand.hover` | `#2F7EF7` | 悬停态 |
| `color.brand.normal` | `#1764E8` | 主按钮、主链接、选中态 |
| `color.brand.click` | `#0D4EC9` | 按下态 |

## 3. 辅色

| Token | 值 | 用途 |
|---|---|---|
| `color.success` | `#00B42A` | 成功、启用、正向反馈 |
| `color.success.line` | `#7BE188` | 成功边框/浅线 |
| `color.success.bg` | `#E8FFEA` | 成功提示背景 |
| `color.warning` | `#FF8A1F` | 警告、待处理 |
| `color.warning.line` | `#FFCF8B` | 警告边框/浅线 |
| `color.warning.bg` | `#FFF7E8` | 警告提示背景 |
| `color.danger` | `#F53F3F` | 删除、错误、危险操作 |
| `color.danger.line` | `#FF9A9A` | 错误边框/浅线 |
| `color.danger.bg` | `#FFECE8` | 错误提示背景 |

## 4. 中性色

| Token | 值 | 用途 |
|---|---|---|
| `color.gray.0` | `#1D2531` | 一级文本 |
| `color.gray.1` | `#657083` | 二级文本 |
| `color.gray.2` | `#9EA7B8` | 三级文本、说明 |
| `color.gray.3` | `#E1E7ED` | 边框 |
| `color.gray.4` | `#EDF1F5` | 分割线、禁用、大背景 |
| `color.gray.5` | `#F7F9FA` | 控件禁用背景 |
| `color.gray.6` | `#BFC9D5` | 禁用文本、图标 |
| `color.gray.active` | `#EBF5FF` | 选中背景 |
| `color.gray.hover` | `#F2F7FF` | 悬停背景 |

## 5. 字体

| 平台 | 字体 |
|---|---|
| Windows | `Microsoft YaHei` |
| macOS / iOS | `PingFang SC` |
| Web 兜底 | `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` |

### 字号与行高

| Token | 字号 | 字重 | 行高 | 用途 |
|---|---:|---:|---:|---|
| `font.h1` | 24px | 700 | 36px | 页面大标题 |
| `font.h1.regular` | 24px | 400 | 36px | 大标题弱化 |
| `font.h2` | 16px | 700 | 24px | 区块标题 |
| `font.h2.regular` | 16px | 400 | 24px | 常规标题 |
| `font.body` | 14px | 700 | 22px | 强调正文 |
| `font.body.regular` | 14px | 400 | 22px | 正文 |
| `font.caption` | 12px | 700 | 20px | 表格表头、标签 |
| `font.caption.regular` | 12px | 400 | 20px | 辅助说明 |

## 6. 间距

| Token | 值 | 用途 |
|---|---:|---|
| `space.1` | 4px | 图标与文字间距、小间距 |
| `space.2` | 8px | 控件内小间距、列表项间距 |
| `space.3` | 12px | 表单项内部、按钮间距 |
| `space.4` | 16px | 区块内边距 |
| `space.5` | 20px | 中等模块间距 |
| `space.6` | 24px | 页面内容边距 |
| `space.8` | 32px | 大区块间距 |

## 7. 圆角

| Token | 值 | 用途 |
|---|---:|---|
| `radius.xs` | 2px | 细小标签、线框控件 |
| `radius.sm` | 4px | 按钮、输入框、标签 |
| `radius.md` | 6px | 选择器、菜单项、侧栏项 |
| `radius.lg` | 8px | 弹窗、卡片 |
| `radius.full` | 9999px | 胶囊标签、头像 |

## 8. 按钮

每个模块只能有一个一级按钮作为主操作。

| 类型 | 默认 | 悬停 | 按下 | 禁用 |
|---|---|---|---|---|
| 一级按钮 | 蓝底白字 | 更亮蓝底 | 深蓝底 | 浅灰底灰字 |
| 二级按钮 | 白底蓝字蓝边 | 浅蓝背景 | 蓝边加深 | 灰边灰字 |
| 三级按钮 | 白底灰边黑字 | 蓝边蓝字 | 深蓝边 | 灰边灰字 |
| 图标按钮 | 纯图标/浅边框 | 蓝色强调 | 蓝色加深 | 灰色不可点 |

### Button Token

| Token | 值 |
|---|---|
| `button.height.sm` | 28px |
| `button.height.md` | 32px |
| `button.padding.x` | 12px |
| `button.radius` | 4px |
| `button.primary.bg` | `#1764E8` |
| `button.primary.hover` | `#2F7EF7` |
| `button.primary.active` | `#0D4EC9` |
| `button.disabled.bg` | `#F7F9FA` |
| `button.disabled.text` | `#BFC9D5` |

## 9. 树结构

用于文件夹、分类目录、组织架构等多级结构。

| 状态 | 表现 |
|---|---|
| 默认 | 白底，左侧箭头/图标 + 文本 |
| 悬停 | 浅灰蓝背景 |
| 点击/选中 | 浅蓝背景，文字主蓝 |
| 禁用 | 文本和图标灰化 |
| 复选 | 右侧或左侧展示 checkbox |

### Tree Token

| Token | 值 |
|---|---|
| `tree.item.height` | 28px |
| `tree.indent` | 16px |
| `tree.icon.size` | 14px |
| `tree.gap.icon_text` | 8px |
| `tree.item.radius` | 4px |
| `tree.active.bg` | `#EBF5FF` |
| `tree.hover.bg` | `#F2F7FF` |

## 10. 交互反馈

### 控件交互反馈

所有可交互控件至少覆盖：

- 默认
- 悬停
- 点击/按下
- 禁用

### 完整信息反馈

用于文本过长、图标含义不清、按钮含义需补充说明的场景。

| 组件 | 用途 |
|---|---|
| Tooltip | 悬停展示完整文本或图标含义 |
| Popover | 展示较长说明或可操作内容 |
| Message | 操作后轻量反馈 |
| Modal | 需要用户确认的强反馈 |
| Alert | 页面级警告反馈 |

### 操作结果反馈

| 类型 | 使用场景 |
|---|---|
| Message | 成功、失败、轻量提醒 |
| Modal | 删除、上线、下线等需确认的操作 |
| Alert | 页面顶部重要警告，不自动消失 |

## 11. 警告提示

| 类型 | 图标 | 背景 | 用途 |
|---|---|---|---|
| 错误提示 | 红色感叹号 | `#FFECE8` | 阻断、失败、危险说明 |
| 成功提示 | 绿色对勾 | `#E8FFEA` | 成功、已完成 |
| 警告提示 | 橙色感叹号 | `#FFF7E8` | 重要但非阻断信息 |

## 12. 标签

标签用于信息选择、筛选、分类和状态表达。

| Token | 值 |
|---|---|
| `tag.height` | 22px |
| `tag.padding.x` | 8px |
| `tag.radius` | 2px |
| `tag.gap.icon_text` | 4px |

### 标签色

可用色系：

- 蓝
- 青
- 绿
- 黄绿
- 黄
- 橙
- 红
- 灰
- 粉
- 紫

默认生成后台原型时，标签应优先使用浅色背景 + 彩色文字/边框，不使用高饱和实底。

