#!/usr/bin/env python3
"""
extract_tokens_helper.py · Token 提取辅助工具

注意：核心的"看图反推 Token"由 LLM（具备视觉能力的多模态模型）完成。
本脚本只做：
  1. 校验 LLM 输出的 design-tokens.json 是否符合 schema
  2. 对未填值的字段套用平台默认 fallback
  3. 把 16 进制颜色规整化（大写、补全 6 位）

用法：
    python scripts/extract_tokens_helper.py validate output/design-tokens.json
    python scripts/extract_tokens_helper.py fallback output/design-tokens.json --platform ant
"""
import argparse
import json
import re
import sys
from pathlib import Path

PLATFORM_PRESETS = {
    "ant": {
        "color": {
            "primary": "#1677FF",
            "text":   {"1": "#1F1F1F", "2": "#595959", "3": "#BFBFBF"},
            "bg":     {"1": "#FFFFFF", "2": "#FAFAFA"},
            "border": "#E5E7EB",
            "status": {"success": "#52C41A", "warning": "#FAAD14", "danger": "#FF4D4F"},
        },
        "radius": {"sm": 2, "md": 6, "lg": 8, "full": 9999},
    },
    "ios": {
        "color": {
            "primary": "#007AFF",
            "text":   {"1": "#000000", "2": "#3C3C43", "3": "#8E8E93"},
            "bg":     {"1": "#FFFFFF", "2": "#F2F2F7"},
            "border": "#C6C6C8",
            "status": {"success": "#34C759", "warning": "#FF9500", "danger": "#FF3B30"},
        },
        "radius": {"sm": 6, "md": 10, "lg": 14, "full": 9999},
    },
    "material": {
        "color": {
            "primary": "#6750A4",
            "text":   {"1": "#1C1B1F", "2": "#49454F", "3": "#79747E"},
            "bg":     {"1": "#FFFFFF", "2": "#FFFBFE"},
            "border": "#CAC4D0",
            "status": {"success": "#198754", "warning": "#F59E0B", "danger": "#B3261E"},
        },
        "radius": {"sm": 4, "md": 12, "lg": 16, "full": 9999},
    },
    "wechat": {
        "color": {
            "primary": "#07C160",
            "text":   {"1": "#191919", "2": "#888888", "3": "#B2B2B2"},
            "bg":     {"1": "#FFFFFF", "2": "#EDEDED"},
            "border": "#DEDEDE",
            "status": {"success": "#07C160", "warning": "#FA9D3B", "danger": "#FA5151"},
        },
        "radius": {"sm": 2, "md": 4, "lg": 8, "full": 9999},
    },
}

REQUIRED_TOP = ["color", "font", "spacing", "radius"]
HEX = re.compile(r"^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")


def normalize_hex(s):
    if not isinstance(s, str):
        return s
    if HEX.match(s):
        if len(s) == 4:
            s = "#" + "".join(c * 2 for c in s[1:])
        return s.upper()
    return s


def walk_normalize(obj):
    if isinstance(obj, dict):
        return {k: walk_normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [walk_normalize(x) for x in obj]
    return normalize_hex(obj)


def deep_merge(base, override):
    for k, v in override.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            deep_merge(base[k], v)
        else:
            base[k] = v
    return base


def cmd_validate(path: Path) -> int:
    if not path.exists():
        print(f"[错误] 文件不存在: {path}")
        return 1
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"[错误] JSON 解析失败: {e}")
        return 1

    missing = [k for k in REQUIRED_TOP if k not in data]
    if missing:
        print(f"[错误] 缺少必需字段: {missing}")
        return 1

    color = data["color"]
    for k in ["primary", "text", "bg"]:
        if k not in color:
            print(f"[错误] color.{k} 缺失")
            return 1

    print(f"[OK] {path} 校验通过")
    print(f"     主色: {color['primary'] if isinstance(color['primary'], str) else color['primary'].get('value')}")
    print(f"     间距阶梯: {data['spacing']}")
    return 0


def cmd_fallback(path: Path, platform: str) -> int:
    if platform not in PLATFORM_PRESETS:
        print(f"[错误] 未知平台: {platform}（可选: {list(PLATFORM_PRESETS)}）")
        return 1

    preset = PLATFORM_PRESETS[platform]
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = {}

    # 用 preset 补全缺失字段
    for k, v in preset.items():
        if k not in data:
            data[k] = v
        elif isinstance(v, dict):
            for k2, v2 in v.items():
                if k2 not in data[k]:
                    data[k][k2] = v2

    data.setdefault("font", {
        "family": "system-ui, sans-serif",
        "size":   {"xs": 12, "sm": 14, "base": 16, "lg": 18, "xl": 24, "2xl": 32},
        "weight": {"normal": 400, "medium": 500, "bold": 600},
        "line_height": {"tight": 1.25, "normal": 1.5},
    })
    data.setdefault("spacing", [4, 8, 12, 16, 20, 24, 32, 40, 48, 64])
    data.setdefault("shadow", {
        "card":   "0 1px 3px rgba(0,0,0,.08)",
        "hover":  "0 4px 12px rgba(0,0,0,.12)",
        "dialog": "0 8px 32px rgba(0,0,0,.16)",
    })
    data.setdefault("motion", {
        "duration": {"fast": 150, "base": 250, "slow": 400},
        "easing":   "cubic-bezier(0.4, 0, 0.2, 1)",
    })
    data.setdefault("meta", {})
    data["meta"]["fallback"] = platform

    data = walk_normalize(data)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] 已基于 [{platform}] 补全 Token: {path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="校验 Token JSON")
    v.add_argument("file", help="design-tokens.json 路径")

    f = sub.add_parser("fallback", help="基于平台预设补全缺失字段")
    f.add_argument("file", help="design-tokens.json 路径")
    f.add_argument("--platform", default="ant", choices=list(PLATFORM_PRESETS))

    args = ap.parse_args()
    p = Path(args.file)

    if args.cmd == "validate":
        return cmd_validate(p)
    if args.cmd == "fallback":
        return cmd_fallback(p, args.platform)
    return 1


if __name__ == "__main__":
    sys.exit(main())
