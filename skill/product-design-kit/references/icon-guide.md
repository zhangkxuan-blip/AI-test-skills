# 图标规范

> 本规范结合 Ant Design Icon 官方文档与本 skill 的后台产品场景沉淀。  
> 默认使用 Ant Design 图标体系；如果用户提供自有图标库，以用户图标库为准。

## 1. 图标来源

默认优先使用 `@ant-design/icons`。

Ant Design 官方图标包含三类主题：

| 主题 | 后缀 | 使用场景 |
|---|---|---|
| 线框风格 | `Outlined` | 后台系统默认首选，适合菜单、表格操作、工具栏 |
| 实底风格 | `Filled` | 强强调、状态标识、品牌识别 |
| 双色风格 | `TwoTone` | 成功/警告/引导等需要轻量强调的场景 |

## 2. 默认使用原则

- 后台页面默认使用 `Outlined`。
- 表格操作图标、工具栏图标、导航图标优先使用线框图标。
- 危险操作图标可以使用线框图标 + 危险色，不默认使用实底。
- 状态类图标可以结合颜色表达，但避免过多颜色同时出现。
- 图标应继承文字颜色，即使用 `currentColor`。

## 3. 尺寸

| Token | 值 | 用途 |
|---|---:|---|
| `icon.size.xs` | 12px | 表格内、标签内 |
| `icon.size.sm` | 14px | 菜单、树结构、辅助按钮 |
| `icon.size.md` | 16px | 常规按钮、工具栏、表单提示 |
| `icon.size.lg` | 20px | 空态、重点操作 |
| `icon.size.xl` | 24px | 页面级提示、插画辅助 |

默认后台原型使用 `14px` 或 `16px`，不要随意放大。

## 4. 颜色

| Token | 值 | 用途 |
|---|---|---|
| `icon.color.default` | `#657083` | 默认图标 |
| `icon.color.weak` | `#9EA7B8` | 弱提示 |
| `icon.color.disabled` | `#BFC9D5` | 禁用 |
| `icon.color.primary` | `#1764E8` | 选中、主操作 |
| `icon.color.success` | `#00B42A` | 成功 |
| `icon.color.warning` | `#FF8A1F` | 警告 |
| `icon.color.danger` | `#F53F3F` | 删除、错误 |

## 5. 间距

| 场景 | 规则 |
|---|---|
| 图标 + 文本按钮 | 图标与文字间距 4px |
| 树结构图标 + 文本 | 图标与文字间距 8px |
| 表格操作图标 | 图标间距 8px |
| 标签内图标 | 图标与文字间距 4px |

## 6. 常用图标映射

| 语义 | 推荐图标 |
|---|---|
| 新增 | `PlusOutlined` |
| 编辑 | `EditOutlined` |
| 删除 | `DeleteOutlined` |
| 搜索 | `SearchOutlined` |
| 筛选 | `FilterOutlined` |
| 设置 | `SettingOutlined` |
| 上传 | `UploadOutlined` |
| 下载 | `DownloadOutlined` |
| 返回 | `ArrowLeftOutlined` |
| 展开 | `DownOutlined` |
| 收起 | `RightOutlined` |
| 更多 | `MoreOutlined` |
| 关闭 | `CloseOutlined` |
| 成功 | `CheckCircleOutlined` |
| 警告 | `ExclamationCircleOutlined` / `WarningOutlined` |
| 错误 | `CloseCircleOutlined` |
| 信息 | `InfoCircleOutlined` |
| 刷新 | `ReloadOutlined` |
| 保存 | `SaveOutlined` |
| 预览 | `EyeOutlined` |
| 表格 | `TableOutlined` |
| 文件夹 | `FolderOutlined` / `FolderOpenOutlined` |
| 文件 | `FileOutlined` |
| 拖拽 | `DragOutlined` |

## 7. 高保真原型生成规则

当 Step 4 生成 HTML 原型时：

1. 若使用 React/Ant Design 技术栈，直接使用 `@ant-design/icons` 名称。
2. 若生成纯 HTML 原型，可使用等价 SVG、字符占位或 CSS 图标模拟，但命名需保留 Ant Design 语义。
3. 图标不应成为主要视觉装饰，优先服务于可识别性和操作反馈。
4. 禁用按钮中的图标必须同步灰化。
5. 危险操作图标只在 hover 或确认弹窗中加强危险色，不要在列表中大面积使用红色。

## 8. 双色图标规则

双色图标仅用于少量强调场景：

- 空态插画辅助
- 成功/警告/信息提示
- 新手引导
- 重要但非频繁出现的说明

默认 `twoToneColor` 使用品牌色或状态色。

## 9. 禁止事项

- 不要混用多套图标风格。
- 不要在同一操作区同时混用 Outlined、Filled、TwoTone。
- 不要把图标当作装饰密集堆叠。
- 不要用实底图标表达普通表格操作。
- 不要让图标颜色脱离语义，例如删除使用蓝色、成功使用红色。

