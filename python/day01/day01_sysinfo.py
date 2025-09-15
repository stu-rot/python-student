#!/usr/bin/env python3
"""
运维 day1： 打印当前系统与python版本信息
"""

import platform


def main():
    print("___ 运维脚本___")
    print("操作系统：", platform.system(), platform.release())
    print("python版本:", platform.python_version())
    print("___ 脚本结束 ___")


if __name__ == "__main__":
    main()

# 显示结果：
[root@test1 day01]# ./day01_sysinfo.py 
___ 运维脚本___
操作系统： Linux 3.10.0-1160.119.1.el7.x86_64
python版本: 3.6.8
___ 脚本结束 ___
