

## 基本知识点
* 字符串（以及数和元组）是不可变的（immutable），这意味着你不能修改它们（即只能替换为新值）
   
* 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
    ```py
    >>> print('%2d-%02d' % (3, 1))
    3-01
    >>> print('%.2f' % 3.1415926)
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
  'Age: 25. Gender: True'
   ```
   
* 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
    ```py
   >>> 'growth rate: %d %%' % 7
    'growth rate: 7 %'
   
   ```
    
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
 

* format()

另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：

```py
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'

# 指定宽度
>>> "{name:10}".format(name="Bob") 
'Bob  
     '
#同时指定宽度和精度
>>> "{pi:10.2f}".format(pi=pi) 
'      3.14'

#指定左对齐、右对齐和居中，可分别使用<、>和^
>>> print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi)) 
3.14 
   3.14 
      3.14 

# f 类似C#的$
>>> ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
print(f'{person} is {ages[person]} years old.')
```

如果变量与替换字段同名，还可使用一种简写。在这种情况下，可使用f字符串——在字符串前面加上f

```py
>>> from math import e 
>>> f"Euler's constant is roughly {e}." 
"Euler's constant is roughly 2.718281828459045." 

# 等价

>>> "Euler's constant is roughly {e}.".format(e=e) 
"Euler's constant is roughly 2.718281828459045."
```

替换字段名
```py
>>> "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3) 
'3 2 4 1' 

>>> fullname = ["Alfred", "Smoketoomuch"] 
>>> "Mr {name[1]}".format(name=fullname) 
'Mr Smoketoomuch'
```
转换标志

  三个标志（s、r和a）指定分别使用str、repr和ascii进行转换
```py
>>> print("{pi!s} {pi!r} {pi!a}".format(pi="π")) 
π 'π' '\u03c0' 
```

字符串查找

方法find在字符串中查找子串，字符串方法find返回的并非布尔值；in只能用于检查单个字符是否包含在字符串中。


* 切片 
 
    对序列执行切片操作时，返回的切片都是副本
 
1. 特列,如果开始索引超出总长度，返回空不会有异常,这种技巧可以用在条件拼接上
```py
>>>'apple'[6:]
''

>>>'apple'[6:1]
''
# 比如
>>>print(['apple'[i %3 *5:]+'orange'[i %5 *6:] or i for i in list(range(1,21))])
[1, 2, 'apple', 4, 'orange', 'apple', 7, 8, 'apple', 'orange', 11, 'apple', 13, 14, 'appleorange', 16, 17, 'apple', 19, 'orange']
```

2. 反转字符串
```py
>>> print("aStr"[::-1])

```

* 替换字符串
    replace：方法replace将指定子串都替换为另一个字符串，并返回替换后的结果
    translate ：它只能进行单字符替换；这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
    使用translate前必须创建一个转换表。这个转换表指出了不同Unicode码点之间的转换关系。
    
* string.capwords(s[, sep])
    使用split根据sep拆分s，将每项的首字母大写，再以空格为分隔符将它们合并起来

* print 打印多个表达式时候用逗号分隔，可以指定分隔符
也可以自定义分隔符
```py
>>> print("I", "wish", "to", "register", "a", "complaint", sep="_") 
I_wish_to_register_a_complaint
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
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个元组（tuple）。
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
    可以用来收集参数,如果没有可供收集的参数，params将是一个空元组
    ```py
    >>>def print_params(*params):
    >>>     print(params)

    >>> print_params(1, 2, 3)
        (1, 2, 3)
    >>> print_params()
    ()
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
*args是可变参数，args接收的是一个元组tuple；

**kw是关键字参数，kw接收的是一个字典dict。
```

```
以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
```

* 魔法交换值
两个值交换
```py
>>>a=1
>>>b=2
>>>a,b=b,a
# a=2 b=1

>>> a,b=0,a
#a=0 b=1
```

### 递归
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出


### 常用 string 函数
   1. title() 首字母大写，其他小写
   2. capitalize() 首字母大写，其他小写
   3. upper() 全部转大写
   4. strip() 去除两侧（不包括内部）空格的字符串，原序列不变
   5. find() 在一个较长的字符串中查询子字符串，返回子串所在位置最左端索引，没有找到返回-1
   6. count() 
   7. startswith()

### 赋值魔法 

* 序列解包 

```py
# 1. 交换多个变量的值
>>> x, y, z = 1, 2, 3
>>> x, y = y, x 
>>> print(x, y, z) 
2 1 3

# 2. 返回元组（或其他序列或可迭代对象）的函数或方法时很有用
>>> values = 1, 2, 3 
>>> values 
(1, 2, 3) 
>>> x, y, z = values 
>>> x 
1 
#3. 从字典中解包一个itme可以使用popitem,这点可以类似es6写法
>>> scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'} 
>>> key, value = scoundrel.popitem() 
>>> key 
'girlfriend' 
>>> value 
'Marion
```
要解包的序列包含的元素个数必须与你在等号左边列出的目标个数相同，否则Python将引发异常，当然我们也可以借助*
```py
>>> a, *b, c = "abc" 
>>> a, b, c 
('a', ['b'], 'c') 

>>> name = "Albus Percival Wulfric Brian Dumbledore" 
>>> first, *middle, last = name.split() 
>>> middle 
['Percival', 'Wulfric', 'Brian'] 
```
### 条件和条件语句
用作布尔表达式（如用作if语句中的条件）时，下面的值都将被解释器视为假： 
False   None   0   ""   ()   []   {}
而其他各种值都被视为真包括特殊值True，这和js的判断一样

循环语句中else它仅在没有调用break时才执行
```py
from math import sqrt 
for n in range(99, 81, -1):  
   root = sqrt(n) 
   if root == int(root): 
 print(n) 
 break 
else: 
   print("Didn't find it!")
```


### 作用域

函数globals来访问全局变量返回一个包含全局变量的字典

函数locals返回一个包含局部变量的字典

函数vars返回一个看不见全局字典


### 类
类时多继承，但是尽量避免使用多继承

私有方法或属性：要让方法或属性成为私有的（不能从外部访问） ，只需让其名称以两个下划线打头即可

```py
class Secretive:  
   def __inaccessible(self): 
 print("Bet you can't see me ...") 
   def accessible(self): 
 print("The secret message is:") 
 self.__inaccessible()
```

* callable(object) 判断对象是否是可调用的（如是否是函数或方法） 
* getattr(object,name[,default]) 获取属性的值，还可提供默认值 
* hasattr(object, name) 确定对象是否有指定的属性 
* isinstance(object, class) 确定对象是否是指定类的实例 
* issubclass(A, B) 确定A是否是B的子类 
* random.choice(sequence) 从一个非空序列中随机地选择一个元素 
* setattr(object, name, value) 将对象的指定属性设置为指定的值 
* type(object) 返回对象的类型 

> 抽象类

你使用@abstractmethod来将方法标记为抽象的——在子类中必须实现的方法
```py
# 标准库（如模块collections.abc）提供了多个很有用的抽象类
from abc import ABC, abstractmethod  
class Talker(ABC): 
   @abstractmethod 
   def talk(self): 
 pass 

```

抽象类（即包含抽象方法的类）最重要的特征是不能实例化


### Exception

Exception 几乎所有的异常类都是从它派生而来的
AttributeError 引用属性或给它赋值失败时引发
OSError 操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
IndexError 使用序列中不存在的索引时引发，为LookupError的子类
KeyError 使用映射中不存在的键时引发，为LookupError的子类
NameError 找不到名称（变量）时引发
SyntaxError 代码不正确时引发
TypeError 将内置操作或函数用于类型不正确的对象时引发
ValueError 将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
ZeroDivisionError 在除法或求模运算的第二个参数为零时引发

warnings.filterwarnings(action,category=Warning, ...) 用于过滤警告
warnings.warn(message, category=None) 用于发出警告


### standard library
 查看函数文档 print(range.__doc__)
 列出模块成员 dir(copy)
 模块的路径   print(copy.__file__)




### File

read / readline
```py
# 在while循环中使用readline
with open(filename) as f:
while True:
line = f.readline()
if not line: break
process(line)
```
对于大文件读取可以使用fileinput 实现延迟行迭代