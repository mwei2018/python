# 一等函数


## 1. 高阶函数

接受函数作为参数，或者把函数作为结果返回的函数是高阶函数

在函数式编程中最为常见的高阶函数有map，filter, reduce 和apply。如果想使用不定量参数调用函数，可以编写fn(*args,**keywords)

python3 中map和filter的返回生成器，因此替代品式生成器表达式

all和any也是内置的规约函数

    all(iterable)
    any(iterable)


## 2. 匿名函数

