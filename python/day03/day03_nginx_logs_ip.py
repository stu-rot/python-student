#!/usr/bin/env python3
"""
day03: 统计nginx access.log top 10 ip
"""
from collections import Counter
import sys


def top_ips(path, n=10):
    # 返回出现次数最多的ip
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        # 提取每行第一个字段
        ips = [line.split()[0] for line in f if line.strip()]
    return Counter(ips).most_common(n)


if __name__ == "__main__":
    log_file = "/var/log/nginx/access.log"
    try:
        for ip, count in top_ips(log_file, 10):
            print(f"{ip:<15} {count:>6}")
    except FileNotFoundError:
        print("文件未找到，检查路径")
        sys.exit(1)
