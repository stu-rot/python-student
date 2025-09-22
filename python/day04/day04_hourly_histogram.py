#!/usr/bin/env python3
"""
Day04: 每小时请求量 CLI 直方图
"""
from datetime import datetime
from collections import defaultdict

def hourly_count(path):
    d = defaultdict(int)
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                raw = line.split("[")[1].split("]")[0]
                dt = datetime.strptime(raw, "%d/%b/%Y:%H:%M:%S %z")
            except (IndexError, ValueError):
                continue
            d[dt.hour] += 1
    return d

def histogram(hour_dict, scale=100):
    for h in range(24):
        count = hour_dict.get(h, 0)
        bars = "■" * (count // scale)
        print(f"{h:02d}:00  {bars} {count}")

def main():
    log = "/var/log/nginx/access.log"
    hourly = hourly_count(log)
    histogram(hourly, scale=100)   # 1 ■ = 100 次
    print(f"\nTotal requests: {sum(hourly.values())}")

if __name__ == "__main__":
    main()
