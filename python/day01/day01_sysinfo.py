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
