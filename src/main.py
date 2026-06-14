#!/usr/bin/env python3
"""石霜鹰眼 - 内核级安全监控系统入口"""

import asyncio
import sys
import os

# 将项目根目录添加到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.scanner import AsyncScanner
from src.core.detector import KernelDetector

async def main():
    scanner = AsyncScanner()
    detector = KernelDetector()
    await asyncio.gather(
        scanner.run(),
        detector.run()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] 用户中断，正在退出...")
