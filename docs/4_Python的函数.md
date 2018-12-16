4 Python 的函数

> 标题： Python 的函数
>
> 视频时长：70 分钟
>
> 链接： [Python 的函数](https://segmentfault.com/ls/1650000017333471/l/1500000016456649?r=bPAnfw)

# 大纲

## 函数的定义

-   Q: 函数是什么？
-   A: 函数是一段代码，完成一个功能。

语法：

```python
def 函数名(arg1,arg2,...)
    do sth
    [return 某个值]

函数名()
```

## 传值 传引用

对于引用类型，可以在内部或者改变。从而影响运行结果。

## 函数调用详解

要理解函数调用过程，需要理解 `the runtime stack`，可以叫做运行时或者栈。

栈会保存两类东西：

-   call frames。记录函数名和离开的地方
-   局部变量的储存

call frame 用来跟踪函数调用过程，函数调用时候创建 call frame，函数结束销毁 call frame.

代码运行到函数调用地方，会把 Frame 压倒栈顶，当函数结束，把 frame 弹出栈，运行指针回到原来的地方。

## 局部作用域

如果想在内部使用外部的变量，使用`global`关键字。不鼓励使用。

## 递归函数

自己调用自己。必须要有递归出口。

```python
def fact(n):
    if n == 1:
        return 1
    return n* fact(n-1)

fact(3)
```

## 可变参数、关键字参数

可变参数，转换为元组 tuple

```python
def 函数(arg1,arg2,*arg3):
    num = arg1+arg2
    for i in arg3:
        num += arg3[i]

print(1,2,3,4,5)
```

关键字参数
允许传入 0 个或多个参数，自动转换为 dict.

```python
def info(name,age,**kw):
    pirnt(kw)

info('bob',16,city='beijing')
```

## 栈

```python
list = []
def push(elem):
    list.append(elem)

def top():
    return list[-1]

def size():
    return len(list)

def pop():
    if size() >0:
        return list.pop(-1)
    else:
        return None
```
