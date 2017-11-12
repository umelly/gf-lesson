# -*- coding:utf-8 -*-

"""数据结构
python内置的四种数据结构: 列表list,元组tuple,字典dict,集合set

### 列表 
- Mutable 可变的数据类型
- 可添加,编辑,删除,搜索列表中的项目
- 添加元素 mylist.append(1)/mylist.insert(0, 1)
- 编辑元素 mylist[0] = 1
- 删除元素 del mylist[0]
- 列表的切片
  - mylist[:N]
  - mylist[N:]
  - mylist[M:N]
  - mylist[::STEP]
- 列表是是指针对象

### 元组
- Immuable 不可变数据类型
- 除了不可编辑元素项以外, 其他和列表类似

### 字典
- 一个key对应一个value, key是不同的，同key赋值会被覆盖
- 字典对象也是指针对象,作为参数传入函数被编辑,自身也会改边

### 集合
- 无序，没有索引操作
- 有in, not in操作
- 可以做交集,并集,异或等运算

### 序列
- 是多个数据结构的特性
- 列表，字符串，元组都有序列的特性
- 可in, not in操作
- 可以被索引操作 obj[M]/obj[M:N]/obj.index(V)

### 数字 int

### 字符 str
- "h ".strip() 去前后空白字符 \t,\n,空格都是空白字符
- "H".lower() 大写变小写字母
- "h".upper() 小写边大写字母
- "1".ljust(2, "0") "10" 用字符0填补原字符以达到2位, 原字符左移
- "1".rjust(2, "0") "01" 用字符0填补原字符以达到2位，原字符右移

### 浮点数 float
- 由于浮点数精度问题,不要用浮点数比较大小, 转成decimal对象比较大小
"""

mylist = ["a", "b", "c"]

mylist.append("d")
print mylist

mylist.insert(0, "0")
print mylist

mylist[0] = "1"
print mylist

del mylist[0]
print mylist

print mylist[2:] # index=2到最后一个元素
print mylist[:-2] # 最前一个元素到逆向index=2 ("d","c","b",)就是这个"b"
print mylist[1:3] # index=1到index=3, 包含前面元素, 不包含后面元素
print mylist[::-1] # 最前到最后面一个元素, 逆向


mydict = {"a":1, "b":2, "c":3}

mydict["d"] = "4"
print mydict

del mydict["d"]
print mydict

def edit_dict(d):
    d["z"] = 44

# 字典传入方法进行编辑后自身发生了改变
edit_dict(mydict)
print mydict


myset1 = set([1,2,3])
myset2 = set([3,4,5])

print myset1 & myset2
print myset1 | myset2
print myset1 ^ myset2
print myset1 - myset2
# print myset1 + myset2 无+操作， str和list都有+操作，表示连接
