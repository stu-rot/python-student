#!/usr/bin/env python3

"""
第一天到第三天课程的总结
"""
import platform, sys, os
from collections import Counter


def sys_info():
    # print("=== Day system info  ===")
    print("系统：", platform.system(), platform.release())
    print("Python_info:", platform.python_version())


def file_count(path):
    # print("=== Day02 nginx_log_file count lines ===")
    try:
        with open(path, "r", encoding="utf-8", errors="ingore") as f:
            return len(f.readlines())
    except FileNotFoundError:
        print(f"❌ 文件不存在:{path}")
        return 0


def top_ips(path, n=10):
    # print("=== Day03 nginx_log_file TOP-n IP ===")
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            ips = [line.split()[0] for line in f if line.strip()]
        return Counter(ips).most_common(n)
    except FileNotFoundError:
        print(f"❌ 文件不存在:{path}")
        return []


def main():
    sys_info()
    log = "/var/log/nginx/access.log"
    print("=== Day02 nginx_log_file count lines ===")
    print(f"{log} 共 {file_count(log)} 行")
    print("=== Day03 nginx_log_file TOP-n IP ===")
    for ip, cnt in top_ips(log, 10):
        print(f"{ip:<15} {cnt:>6}")


if __name__ == "__main__":
    main()
