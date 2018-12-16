6 Python 的常用数据结构

> 标题： Python 的常用数据结构
>
> 视频时长：66 分钟
>
> 链接： [Python 的常用数据结构](https://segmentfault.com/l/1500000016653718?r=bPAnfw)

注： 6 分开始正文。

# 数据结构的概念

主讲 Python 自带的数据结构

# Tuple 元组

## 元组概念

不可变的 List。
不可以 append，insert，，pop
不可以 a[i]=新值

不可变是一门艺术。会简单可靠。不用考虑线程安全。thread safe。

## 元组的 CURD

### create

```py
t = (1,'b',True,3.14)
```

是圆括号，不是方括号。
创建了就不可变

## read

```py
a[1]
a[0:2]
len(a)
```

## update delete

无，不可变

# Dict 字典，哈希表

## 什么是 Dict

key:value,键值对。

## Dict 的 CURD

### create

```py
dict = {'a':1,'b':True}
dict['c']='good'
```

### read

```py
print(dict)
dict[变量名]
key in dict #查找
len(dict)
```

访问一个不存在的 key，会报错。

### update

`dict['name'] = '新值'`

### delete

```py
dict.pop(key)
```

# Set 集合

key 的集合，不能重复，不存储 value，数学集合的概念

## Set 的 CURD

```python
# create

s = set([1,'b',True])
s = set([1,1,1,2,3]) // {1,2,3}
s.add('new')

# read
keys in s
# update
#s.add

# delete
s.remove(key)
```

## 其他操作

-   交集 `s1& s2`
-   并集 `s1 | s2`
-   差集 `s1 - s2`

# 实战

略。
