#!/usr/bin/env python3
"""
preview_server.py · 启动本地预览服务并打印二维码

用法：
    python scripts/preview_server.py [目录]
    python scripts/preview_server.py output/prototype --port 8000

依赖（可选，无则降级为不打印二维码）:
    pip install qrcode[pil]
"""
import argparse
import http.server
import socket
import socketserver
import sys
from pathlib import Path


def get_lan_ip() -> str:
    """获取本机局域网 IP（不依赖外网）"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def print_qrcode(url: str) -> None:
    """终端打印二维码（缺依赖时降级）"""
    try:
        import qrcode
    except ImportError:
        print("(提示: pip install qrcode[pil] 可在终端打印二维码)")
        return
    qr = qrcode.QRCode(border=1)
    qr.add_data(url)
    qr.make(fit=True)
    qr.print_ascii(invert=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="原型本地预览服务")
    ap.add_argument("directory", nargs="?", default="output/prototype",
                    help="原型目录 (默认 output/prototype)")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()

    target = Path(args.directory).resolve()
    if not target.exists():
        print(f"[错误] 目录不存在: {target}")
        return 1

    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(
        *a, directory=str(target), **kw
    )

    ip = get_lan_ip()
    url_local = f"http://localhost:{args.port}"
    url_lan = f"http://{ip}:{args.port}"

    print("=" * 60)
    print(f"  原型预览服务已启动")
    print(f"  目录: {target}")
    print("-" * 60)
    print(f"  本机访问: {url_local}")
    print(f"  局域网:   {url_lan}  (手机扫码 ↓)")
    print("=" * 60)
    print_qrcode(url_lan)
    print("\n按 Ctrl+C 停止服务\n")

    try:
        with socketserver.TCPServer(("", args.port), handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止")
    except OSError as e:
        print(f"[错误] 端口 {args.port} 被占用: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
