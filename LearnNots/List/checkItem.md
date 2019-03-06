
# **List-1**

## 判断item在list存在

定义数据源
```py 	
# List of string 
list_str = ['Hi' , 'hello', 'at', 'this', 'china', 'from']
```

* [方法1] 利用in 操作符

    elem in LIST

    It will return True, if element exists in list else return false.

 i.e.
```py
# check if element exist in list using 'in'

if 'at' in list_str :
    print("Yes, 'at' found in List : " , listOfStrings)

# check if element NOT exist in list using 'in'
if 'time' not in list_str :
    print("Yes, 'time' NOT found in List : " , listOfStrings)

```
* [方法2]: count() 函数 

    list.count(elem)
    统计某个元素在列表中出现的次数
 i.e.

 ```py
 #  check if element exist in list using count() function

if list_str.count('at') > 0 :
    print("Yes, 'at' found in List : " , listOfStrings)

 ```


* [方法3]: any() 函数
利用自带的any函数 i.e.

``` py
'''    
check if element exist in list based on custom logic
Check if any string with length 5 exist in List
'''
result = any(len(elem) == 5 for elem in list_str)
if result:
    print("Yes, string element with size 5 found")

```
除了里面直接跟条件外，可以简化提供阅读性，也可以用函数  i.e.

```py

def checkIfMatch(elem):
    if len(elem) == 5:
        return True;
    else :
        return False;


result = any(checkIfMatch for elem in list_str)
if result:
        print("Yes, string element with size 5 found")
```

当然也可以用类似的三目运算格式

```py

result = any(True if len(elem) == 5 else False for elem in list_str)
if result:
        print("Yes, string element with size 5 found")

```