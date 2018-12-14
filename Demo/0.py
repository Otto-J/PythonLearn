#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# 以上两行似乎是2.x的惯例，不使用不影响

import os

def main():
    print("Hello World!")
    print("来自Bob\"的问候")
    print('来自Alice\'的问候')
    print('''
        一行
        两行
        三行
    ''')

    foo(5, 10)

    print('=' *10)
    print('这将执行'+ os.getcwd())

    counter = 0
    counter += 1

    food = ['apple', '杏', 'pear']

    for i in food:
        print('我爱吃'+ i)

    print('数到10')
    for i in range(10):
        print(i)

def foo(param1, secondParam):
    res = param1 + secondParam
    print('%s 加 %s 等于 %s' % (param1, secondParam, res))
    if res < 50:
        print('这个')
    elif res >= 50 and (param1 == 42 or secondParam == 24):
        print("那个")
    else:
        print("恩")
    return res # 单行注释

'''
多行注释
'''

if __name__ == '__main__':
    main()
