

## 格式化
   
   * 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
   ```py

   >>>print('%2d-%02d' % (3, 1))
3-01
   >>>print('%.2f' % 3.1415926)
3.14   
   
   ```

   * Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
   ```py
   >>> ord('A')
    65
    >>> ord('中')
    20013
    >>> chr(66)
    'B'
    >>> chr(25991)
    '文'
   ```

   * 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
   ```py
   >>> 'Age: %s. Gender: %s' % (25, True)
`   'Age: 25. Gender: True'
   ```
   
 * 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
    
 * 原始字符串用前缀r表示: 比如输出路径, 原始字符串不能以单个反斜杠结尾( 换而言之，原始字符串的最后一个字符不能是反
斜杠 )
 ```py
 >>> print(r'C:\nowhere') 
C:\nowhere 
>>> print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz') 
C:\Program Files\fnord\foo\bar\baz\frozz\bozz 

# 但如果要指定以反斜杠结尾的原始字符串（如以反斜杠结尾的DOS路径）技巧是将反斜杠单独作为一个字符串 
>>> print(r'C:\Program Files\foo\bar' '\\') 
C:\Program Files\foo\bar\
 ```
 

```py
 >>> 'growth rate: %d %%' % 7
    'growth rate: 7 %'
   
 ```
* format()

另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

```py
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

* 反转字符串
```py
>>> print("aStr"[::-1])

```

## dict和set


### dict

* dict 中如果key 不存中，dict 就会报错（keyError）
    要避免key不存在的错误，有两种办法，
        一是通过in判断key是否存在
        二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
        （同理这和list中索引取不存在索引就会报索引超界，这时候我们可以利用get（）方法）

* dict内部存放的顺序和key放入的顺序是没有关系的

* dict 和 list 比较

     * dict有以下几个特点 
        1. 查找和插入的速度极快，不会随着key的增加而变慢；
        2. 需要占用大量的内存，内存浪费多。
     * 而list相反：
        1. 查找和插入的时间随着元素的增加而增加；
        2. 占用空间小，浪费内存很少。

    所以，dict是用空间来换取时间的一种方法。dict的key必须是不可变对象，通过key计算位置的算法称为哈希算法（Hash）。

* dict的key设计很讲究，比如用元组作为key
* dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
* 对字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序
```py
>>> sorted(d.items(),key=lambda x:x[1])

#请按alist中元素的age由大到小排序
>>> alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
>>> def sort_by_age(list1):
      return sorted(alist,key=lambda x:x['age'],reverse=True)
```

 ### set   
 
 * set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
 要创建一个set，需要提供一个list作为输入集合
 ``` py
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}

 ```
 场景使用：可以list去重

 set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
```py
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2  #A,B 中相同元素
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
>>> s1 ^ s1  #A,B 中不同元素
{1, 4}
```

## 函数

定义默认参数要牢记一点：默认参数必须指向不变对象！
```py
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

###  可变参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict



* 可变参数
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
```py
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
* 关键字参数
关键字参数有什么用？它可以扩展函数的功能

```py
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
 # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
```
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
```py
def person(name, age, *, city, job):
    print(name, age, city, job)

```
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

调用方式如下：
```py
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
```
要注意定义可变参数和关键字参数的语法：
```
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。
```

```
以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
```
### 递归
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出


### 常用 string 函数
   title() 首字母大写，其他小写
   capitalize() 首字母大写，其他小写
   upper() 全部转大写
   strip() 去除两侧（不包括内部）空格的字符串，原序列不变
   find() 在一个较长的字符串中查询子字符串，返回子串所在位置最左端索引，没有找到返回-1
   count() 
   startswith()