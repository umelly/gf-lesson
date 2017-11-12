# -*- coding:utf-8 -*-

"""函数"""

def func1(a, b=1, c=2, *args, **kwargs):
    print "a is", a
    print "b is", b
    print "c is", c
    print "args is", args
    print "kwargs is", kwargs

# 错误, 带默认值的参数一定要定义在后面
# SyntaxError: non-default argument follows default argument
# def func1(a=1, c):
#     pass

# 错误, 实参也是同上规则
# SyntaxError: non-keyword arg after keyword arg
# func1(c=20, 10)
