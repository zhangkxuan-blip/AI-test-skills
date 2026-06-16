#!/usr/bin/env python3
"""
generate_prototype.py · 用 Token + 页面清单生成原型骨架

主要逻辑由 LLM 负责，本脚本只做：
  1. 复制 prototype-template 到目标目录
  2. 把 design-tokens.json 注入 styles/tokens.css
  3. 根据 pages 列表生成空 HTML 文件占位
  4. 更新 router.js 的 routes 表

用法：
    python scripts/generate_prototype.py \
        --tokens output/design-tokens.json \
        --pages "home,list,detail,form,me" \
        --out output/prototype
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = SKILL_ROOT / "assets" / "prototype-template"


def render_tokens_css(tokens: dict) -> str:
    """把 Token JSON 转成 CSS 变量定义。"""
    def v(x):
        return x["value"] if isinstance(x, dict) and "value" in x else x

    color = tokens.get("color", {})
    text  = color.get("text", {})
    bg    = color.get("bg", {})
    status = color.get("status", {})

    font = tokens.get("font", {})
    sizes = font.get("size", {})
    weights = font.get("weight", {})
    lh = font.get("line_height", {})

    radius = tokens.get("radius", {})
    shadow = tokens.get("shadow", {})
    motion = tokens.get("motion", {})
    duration = motion.get("duration", {})

    spacing = tokens.get("spacing", [4, 8, 12, 16, 20, 24, 32, 40, 48, 64])

    lines = [
        "/* Auto-generated from design-tokens.json. Do not edit by hand. */",
        ":root {",
        f"  --color-primary:   {v(color.get('primary', '#1677FF'))};",
        f"  --color-secondary: {v(color.get('secondary', '#722ED1'))};",
        f"  --color-text-1: {v(text.get('1', '#1F1F1F'))};",
        f"  --color-text-2: {v(text.get('2', '#595959'))};",
        f"  --color-text-3: {v(text.get('3', '#BFBFBF'))};",
        f"  --color-bg-1: {v(bg.get('1', '#FFFFFF'))};",
        f"  --color-bg-2: {v(bg.get('2', '#FAFAFA'))};",
        f"  --color-border: {v(color.get('border', '#E5E7EB'))};",
        f"  --color-success: {v(status.get('success', '#52C41A'))};",
        f"  --color-warning: {v(status.get('warning', '#FAAD14'))};",
        f"  --color-danger:  {v(status.get('danger',  '#FF4D4F'))};",
        f"  --font-family: {v(font.get('family', \"'PingFang SC', system-ui, sans-serif\"))};",
        f"  --font-size-xs:   {sizes.get('xs', 12)}px;",
        f"  --font-size-sm:   {sizes.get('sm', 14)}px;",
        f"  --font-size-base: {sizes.get('base', 16)}px;",
        f"  --font-size-lg:   {sizes.get('lg', 18)}px;",
        f"  --font-size-xl:   {sizes.get('xl', 24)}px;",
        f"  --font-size-2xl:  {sizes.get('2xl', 32)}px;",
        f"  --font-weight-normal: {weights.get('normal', 400)};",
        f"  --font-weight-medium: {weights.get('medium', 500)};",
        f"  --font-weight-bold:   {weights.get('bold', 600)};",
        f"  --line-height-tight:  {lh.get('tight', 1.25)};",
        f"  --line-height-normal: {lh.get('normal', 1.5)};",
    ]
    for i, val in enumerate(spacing):
        lines.append(f"  --space-{i+1}: {val}px;")
    lines += [
        f"  --radius-sm:   {radius.get('sm', 4)}px;",
        f"  --radius-md:   {radius.get('md', 8)}px;",
        f"  --radius-lg:   {radius.get('lg', 12)}px;",
        f"  --radius-full: {radius.get('full', 9999)}px;",
        f"  --shadow-card:   {shadow.get('card',   '0 1px 3px rgba(0,0,0,.08)')};",
        f"  --shadow-hover:  {shadow.get('hover',  '0 4px 12px rgba(0,0,0,.12)')};",
        f"  --shadow-dialog: {shadow.get('dialog', '0 8px 32px rgba(0,0,0,.16)')};",
        f"  --duration-fast: {duration.get('fast', 150)}ms;",
        f"  --duration-base: {duration.get('base', 250)}ms;",
        f"  --duration-slow: {duration.get('slow', 400)}ms;",
        f"  --easing: {motion.get('easing', 'cubic-bezier(0.4, 0, 0.2, 1)')};",
        "}",
    ]
    return "\n".join(lines) + "\n"


def render_routes_js(pages: list) -> str:
    """生成 router.js 的 routes 表。"""
    routes = {f"#/{p}": f"pages/{p}.html" for p in pages}
    if pages:
        routes["#/"] = f"pages/{pages[0]}.html"
    body = ",\n    ".join(f"'{k}': '{v}'" for k, v in routes.items())
    return f"""window.AppRouter = {{
  routes: {{
    {body}
  }},
  init(frameId = 'app-frame') {{
    const frame = document.getElementById(frameId);
    if (!frame) return console.error('[router] frame not found');
    const navigate = () => {{
      const path = location.hash || '#/';
      frame.src = this.routes[path] || this.routes['#/'];
    }};
    navigate();
    window.addEventListener('hashchange', navigate);
  }}
}};
"""


def stub_page_html(name: str) -> str:
    title = name.capitalize()
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="../styles/tokens.css">
  <link rel="stylesheet" href="../styles/app.css">
  <script src="https://cdn.tailwindcss.com"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
</head>
<body class="bg-bg-2">
  <main class="app-container">
    <h1 class="text-xl font-semibold text-text-1">{title}</h1>
    <p class="text-text-2 mt-2">TODO: LLM 在此填充该页面真实内容（参考 PRD + 线框图 + Token）。</p>
  </main>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tokens", required=True, help="design-tokens.json 路径")
    ap.add_argument("--pages", required=True, help="逗号分隔的页面 ID，如 home,list,detail")
    ap.add_argument("--out", required=True, help="输出目录")
    ap.add_argument("--force", action="store_true", help="存在则覆盖")
    args = ap.parse_args()

    tokens_file = Path(args.tokens)
    if not tokens_file.exists():
        print(f"[错误] 找不到 Token 文件: {tokens_file}")
        return 1

    out = Path(args.out)
    if out.exists():
        if not args.force:
            print(f"[错误] 输出目录已存在，加 --force 覆盖: {out}")
            return 1
        shutil.rmtree(out)

    if not TEMPLATE_DIR.exists():
        print(f"[错误] 模板目录不存在: {TEMPLATE_DIR}")
        return 1

    shutil.copytree(TEMPLATE_DIR, out)

    tokens = json.loads(tokens_file.read_text(encoding="utf-8"))
    (out / "styles" / "tokens.css").write_text(render_tokens_css(tokens), encoding="utf-8")

    pages = [p.strip() for p in args.pages.split(",") if p.strip()]
    pages_dir = out / "pages"
    pages_dir.mkdir(exist_ok=True)
    for p in pages:
        f = pages_dir / f"{p}.html"
        if not f.exists() or args.force:
            f.write_text(stub_page_html(p), encoding="utf-8")

    (out / "scripts" / "router.js").write_text(render_routes_js(pages), encoding="utf-8")

    print(f"[OK] 原型骨架已生成: {out}")
    print(f"     页面: {', '.join(pages)}")
    print(f"     运行: python scripts/preview_server.py {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
