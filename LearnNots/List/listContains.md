# **List-2**

## 检查两个list的包含关系
本节主要总结一个list所有或者部分元素在另一list的问题

数据源
```py

list1 = ['Hi' ,  'hello', 'at', 'this', 'china', 'from']
list2 = ['china' , 'hello', 'Hi']

```

* [方法1] all()函数
检验一个list2所有元素都包含在另一个list1中，即list1包含list2的所有元素

```py
# check if list1 contains all elements in list2
result =  all(elem in list1  for elem in list2)

if result:
    print("Yes, list1 contains all elements in list2")    
else :
    print("No, list1 does not contains all elements in list2"
```
上面代码利用list推导式 和list的in操作符

* [方法2] issuperset() 函数
方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False
即：函数判断集合 lsit2 的所有元素是否都包含在集合 lsit1 中

```py

result = set(list1).issuperset(set(list2)) 
if result:
    print("Yes, list1 contains all elements in list2")    
else :
    print("No, list1 does not contains all elements in list2"

```

* [方法3] any()函数
检查list1是否包含部分list2元素

```py

result =  any(elem in list1  for elem in list2)
 
if result:
    print("Yes, list1 contains any elements of list2")    
else :
    print("No, list1 contains any elements of list2")

```

* [方法4] 交集方式

```py
# list推导式
exist = [i for i in list1 if i in list2]

# 利用集合intersection()返回集合的交集
exist = list(set(list1).intersection(set(list2)))
# 
```
intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。


* [方法4] 求差集，在list1中但不在list2中
``` py
# list推导式
ret = [i for i in list1 if i not in list2]

# 利用集合intersection()返回集合的交集
 ret = list(set(list1).difference(set(list2)))

```
