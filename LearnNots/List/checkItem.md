
# **List-1**

## 判断item在list存在

定义数据源
```py 	
# List of string 
listOfStrings = ['Hi' , 'hello', 'at', 'this', 'there', 'from']
```

* [方法1] 利用in 操作符

    elem in LIST

    It will return True, if element exists in list else return false.

 i.e.
```py
# check if element exist in list using 'in'

if 'at' in listOfStrings :
    print("Yes, 'at' found in List : " , listOfStrings)

# check if element NOT exist in list using 'in'
if 'time' not in listOfStrings :
    print("Yes, 'time' NOT found in List : " , listOfStrings)

```
* [方法2]: count() 函数 

    list.count(elem)
    统计某个元素在列表中出现的次数
 i.e.

 ```py
 #  check if element exist in list using count() function

if listOfStrings.count('at') > 0 :
    print("Yes, 'at' found in List : " , listOfStrings)

 ```


* [方法3]: any() 函数

 i.e.

``` py

'''    
check if element exist in list based on custom logic
Check if any string with length 5 exist in List
'''
result = any(len(elem) == 5 for elem in listOfStrings)
if result:
    print("Yes, string element with size 5 found")

```
除了里面跟条件外也可以用函数 
 i.e.

```py

def checkIfMatch(elem):
    if len(elem) == 5:
        return True;
    else :
        return False;


result = any(checkIfMatch for elem in listOfStrings)
if result:
        print("Yes, string element with size 5 found")
```

当然也可以用类似的三目运算格式

```py

result = any(True if len(elem) == 5 else False for elem in listOfStrings)
if result:
        print("Yes, string element with size 5 found")

```