cat day01_sysinfo.py
#!/usr/bin/env python3
"""
运维 day1： 打印当前系统与python版本信息
"""

import platform
# 导入标准库模块
'''
platform 属于 Python 标准库，安装 Python 后就自带，无需额外 pip install。
它封装了大量获取“当前操作系统 / 编译器 / Python 解释器”信息的函数，例如 platform.system():当前系统版本、platform.release()：当前解释器、platform.python_version()：python版本 等。
'''

# def 语法模板:
'''
def 函数名([参数1, 参数2, ...]):
    """可选的文档字符串（docstring）"""
    函数体
    return 返回值   # 没有 return 时默认返回 None
'''

def main():
# def 是 define 的缩写，用来“定义一个函数”
# 这里函数名叫 main，括号里没有任何参数，所以调用时写成 main() 即可。
# 冒号 : 表示“函数头”结束，接下来所有缩进（默认 4 个空格）都属于函数体。
# 注意：def 只是“定义”，此时函数体里的代码不会立即执行；必须等到“调用”时才跑。
    print("___运维脚本___")
    # 输出信息到终端：___运维脚本___
    print("操作系统：", platform.system(), platform.release())
    print("python版本:", platform.python_version())
    print("___ 脚本结束 ___")


if __name__ == "__main__":
‘’‘
这是 Python 的“脚本入口”惯用法。
每个 .py 文件被解释器加载时，都会把特殊变量 __name__ 设成：
 当文件直接被运行（python xxx.py）时，__name__ 等于 "__main__"；
 当文件被别的文件 import 时，__name__ 等于它自己的文件名（模块名）。
因此这段判断的意思是：
 “如果我是被用户直接运行的主程序，而不是被别人导入的库，就执行 main() 函数。”
好处：
 既能让脚本“双击/命令行”直接跑，又能在被别的程序 import 时不自动打印信息。
 把真正干活的代码封装到 main() 里，测试、复用都更方便。
’‘’
    main()

# 显示结果：
[root@test1 day01]# ./day01_sysinfo.py 
___运维脚本___
操作系统： Linux 3.10.0-1160.119.1.el7.x86_64
python版本: 3.6.8
___ 脚本结束 ___

或者是在linux上给.py文件加执行权限
[root@test1 day01]# chmod +x day01_sysinfo.py 
后续运行可以直接./day01_sysinfo.py 运行文件
