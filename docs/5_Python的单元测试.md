5 Python 的单元测试

> 标题： Python 的单元测试
>
> 视频时长：68 分钟
>
> 链接： [Python 的单元测试](https://segmentfault.com/l/1500000016534088?r=bPAnfw)

2 分开始讲，5 分 30 开始正文。

# 软件测试的概念

验证软件的正确性、完整性、安全性，降低系统风险。

-   单元测试
-   集成测试
-   性能测试
-   UAT 用户验收测试
-   etc.

推崇 DevOps .

为什么需要单元测试

-   检测 bug
-   节约成本
-   提高可靠性

怎么写单元测试

-   测输入输出
-   测异常
-   测路径覆盖 code coverage 代码的所有分支，一般 80%

非常重要的指标，80% 覆盖。

# 单元测试框架

## unittest 单元测试

py3 已经自带了，不需要安装。
语法：

```python
import unittest
# 看到 5_unittest.py
```

运行单元测试：

```bash
# python -m unittest discover 目录 代码文件匹配
python -m unittest discover ./ '*_test.py'
```

## mock 伪造返回

注：在 node 里很常见，前后端分离进行联调的时候。

两个关键概念：

-   拦截。stub 阻断方法的调用
-   伪造返回 mock

代码略

# 几个关键函数

-   setUp
-   tearDown
-   assertTure(x)
-   assertFalse(x)
-   assertEqual(a,b)
-   assertNotEqual(a,b)
-   mock

单元测试还是挺懵的，很多概念没有接触过。

至少意识里先重视单元测试吧，感觉 node 里也有很多测试，一样没用过。
