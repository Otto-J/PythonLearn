8 Python 的异常处理

> 标题： Python 的异常处理
>
> 视频时长：41 分钟
>
> 链接： [Python 的异常处理](https://segmentfault.com/l/1500000016885332?r=bPAnfw)

# 概念

# 语法

```py
try:
    except 某些错误 as e:
        #do
    except 又一个错误 as e:
        #do
    finallly:
        # 无论是否异常

```

## 自定义异常

```py
class myErr(Exception):
    def __init__(self,message,status):
        super().__init__(message,status)
        self.message = message
        self.status = status
```

# 主动抛出异常

通过`raise`主动抛出异常。

-   依赖错误
-   内部错误
-   输入不可用

24' 未完待续。
