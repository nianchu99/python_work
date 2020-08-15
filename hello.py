#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'a test module'

__author__ = 'bowenkei'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello world')
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("too many arguments!")


if __name__ == '__main__':
    test()
    print("success")
"""
当我们在命令行执行hello模块文件时，Python解释器把一个特殊变量name置为main，而如果在其他地方导入hello模块时，if判断
将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
"""


