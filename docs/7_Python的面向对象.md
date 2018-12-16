7 Python 的面向对象

> 标题： Python 的面向对象
>
> 视频时长：60 分钟
>
> 链接： [Python 的面向对象](https://segmentfault.com/l/1500000016729186?r=bPAnfw)

# 概念

举 猫、建筑为例，讲解对象的概念。

# 基本语法

设定一个猫

```py
class Cat(object):
    pass
```

建模： mood, hungry, energy, name

通过对 变量和函数添加 \_\_ 前缀，实现私有效果。

静态变量，不需要加 self 关键字

静态方法前，加 `@staticmethod`

```py
class Cat(object):
    count = 0 #静态变量
    @staticmethod
    def get():
        print(Cat.count) #访问静态变量

```

# 面向对象的继承和多态

继承也很熟悉

```py
class Hero(object):
    def __init__(self,hp,mp):
        self.hp = hp
        self.mp =mp

class Chen(Hero):
    def __init__(self,hp,mp,skin):
        super().__init__(hp,mp)
        self.skin = skin
```

组合，组合优先于继承，后续讲。

# HttpServer

例子复杂多了，这个没跟上。
