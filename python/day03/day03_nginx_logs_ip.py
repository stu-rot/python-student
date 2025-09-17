#!/usr/bin/env python3
# 告诉内核“用当前 $PATH 里第一个 python3 来解释本文件”。
# 好处：跨平台，比写死 /usr/bin/python3 更灵活。
# Windows 忽略这行，Linux 下给文件加执行位后可直接 ./day03_nginx_logs_ip.py 运行。
"""
day03: 统计nginx access.log top 10 ip
"""
from collections import Counter
#Counter 是“高性能哈希计数器”，一行代码就能完成“单词→出现次数”的统计，比手动 dict.get(k,0)+1 简洁高效。
import sys
# 后面要用 sys.exit(1) 在文件找不到时退出并返回非 0 状态码，告诉 shell“程序异常结束”。
# sys.exit(1) 是整个进程立即终止，并返回退出码 1 给操作系统。
# 无法额外使用：continue / break 只能用在循环体内部，影响的是当前循环的迭代或循环本身，不会结束整个程序，也无法向 shell 返回退出码。
# 如果你想“跳过错误继续处理下一个文件”，用 continue；
# 如果想“跳出当前循环继续执行后面代码”，用 break；
# 只有当真正需要“程序异常退出并告诉操作系统”时，才用 sys.exit(非 0)。


def top_ips(path, n=10):
    # 返回出现次数最多的前10个ip地址
    # 封装成函数，方便单元测试或被别的脚本导入。
    # n=10 给默认值，想 Top 20 就传 n=20，不用改源码。
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
    # with 语句自动关文件，哪怕中途抛异常也会调 f.close()。
    # encoding="utf-8" 强制按 UTF-8 解码，防止系统 locale 是 GBK 时中文路径或日志行乱码。
    # errors="ignore" 遇到非法字节直接丢弃，不至于整行抛 UnicodeDecodeError 中断程序。（生产里也可换成 "replace" 用 � 替代）
        # 提取每行第一个字段
        ips = [line.split()[0] for line in f if line.strip()]
        ‘’‘
        列表推导式一行完成三件事：
        a. line.strip() 去掉行尾 \n 和空格；空行会变成 ''，下面 if line.strip() 直接过滤掉。
        b. line.split() 默认按任意空白切分，返回列表；nginx 日志里第 1 个字段正好是远程 IP。
        c. 把每行提取到的 IP 收集进列表 ips，为 Counter 准备数据。
        坑：split() 不带参数时连续空格会合并；如果日志用固定宽度字段且出现空列，要用 split(' ') 或正则。
        ’‘’
    return Counter(ips).most_common(n)
    “”“
    Counter(ips) 把列表转成哈希表 → {'192.168.58.102': 5, '192.168.58.1': 4}。
    .most_common(n) 返回按次数降序的前 n 个元组列表：[('192.168.58.102', 5), ...]，直接拿来循环打印即可。
    时间复杂度 O(n log n)（内部用堆），对日志几十万行秒级完成。
    ”“”


if __name__ == "__main__":
# Python 入口保护：只有当脚本被直接执行时下面代码才跑；
# 当模块被 import 时不会触发，方便以后单元测试或复用函数。
    log_file = "/var/log/nginx/access.log"
    try:
        for ip, count in top_ips(log_file, 10):
            print(f"{ip:<15} {count:>6}")
    except FileNotFoundError:
        print("文件未找到，检查路径")
        sys.exit(1)
“”“
try: ... except FileNotFoundError:
文件不存在时 open() 会抛 FileNotFoundError，捕获后给出友好提示并 sys.exit(1)，避免堆栈跟踪吓哭用户。
返回码 1 让脚本在 Shell 判断里可感知失败：if [$? -ne 0 ]; then ... fi

for ip, count in top_ips(log_file, 10):
拆包元组，ip 拿到地址字符串，count 拿到整数次数。
想输出 Top 20 就改 top_ips(log_file, 20)，无需动函数内部。

print(f"{ip:<15} {count:>6}")
f-string 格式化：
:<15 左对齐，占 15 列，IP 不足补空格，列对齐好看；
:>6 右对齐，占 6 列，次数靠右，数字位数不同也能对齐。
旧版本 Python 可以用 format() 方法代替。
”“”
