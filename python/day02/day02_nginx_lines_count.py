#!/usr/bin/env python3
"""
读取 nginx 日志行数
"""
import sys


def count_line(path):
    # 返回文件行数
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return len(f.readlines())


if __name__ == "__main__":
    log_file = "/var/log/nginx/access.log"
    try:  # ❶ 缩进对齐（原多空格）
        total = count_line(log_file)  # ❷ 去掉冒号 :
        print(f"{log_file} 共有 {total} 行")
    except FileNotFoundError:
        print("文件不存在，请检查路径！")
        sys.exit(1)
