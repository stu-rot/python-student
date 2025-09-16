#!/usr/bin/env python3
# 在当前变量环境中找到python3 解释器执行
#比#!/usr/bin/python3 通用，防止python安装时不知道按到哪里

"""
读取 nginx 日志行数
"""
import sys
# 只用到 sys.exit(1) 这一句，用于在“文件不存在”时给 Shell 返回非 0 退出码，方便脚本链式调用。
# 如果后面想接 argparse、logging 再往里加即可。

def count_line(path):
    # 返回文件行数
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return len(f.readlines())
‘’‘
with 语句保证文件描述符一定会被关闭。
encoding="utf-8"：nginx 默认日志是 ASCII/UTF-8，但如果有非法字节（比如被刷入二进制垃圾）会抛 UnicodeDecodeError，所以加 errors="ignore" 直接跳过，保证脚本不崩。
f.readlines() 一次性把文件全部读进内存，返回 list，len() 即行数。
优点：代码最短；
缺点：大文件（几个 GB）会瞬间吃光内存。
’‘’

if __name__ == "__main__":
    # 只有直接运行脚本时才执行；被别的模块 import 时不会意外跑业务逻辑。
    # 约定俗成，写库/脚本两用代码时必须加。
    log_file = "/var/log/nginx/access.log"
    # nginx日志位置
    try: 
        total = count_line(log_file) 
        print(f"{log_file} 共有 {total} 行")
    except FileNotFoundError:
        print("文件不存在，请检查路径！")
        sys.exit(1)
‘’‘
异常处理
try:
total = count_line(log_file)
print(f"{log_file} 共有 {total} 行")
except FileNotFoundError:
print("文件不存在，请检查路径！")
sys.exit(1)
只抓 FileNotFoundError，其余异常（权限不足、EINTR 等）继续抛，方便调试。
sys.exit(1) 让 Shell 拿到 $? = 1，可被监控脚本或 Ansible 识别为失败。
错误信息写到 stderr 更规范：print("文件不存在，请检查路径！", file=sys.stderr)
’‘’
