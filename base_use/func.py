#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python的函数调用是引用传递
# 定义函数
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return (mylist,"haha")

# 调用函数
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)


# 默认参数和可变参数

# 默认参数
# 有默认值的参数后面不能再跟无默认值的参数
def printinfo(name, age=35):
    print("Name: ", name)
    print("Age ", age)
    return

# 调用
# 如果调换了参数的顺序，则必须把参数名都带上
printinfo(age=50, name="miki")
printinfo(name="miki")

# 可变参数
def printinfo(arg1, *vartuple):
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

# 调用
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数
# 可以使用lambda关键字来创建小的匿名函数。这些函数被称为匿名，因为它们不是以标准方式通过使用def关键字声明。
# Lambda形式可以采取任何数量的参数，但在表现形式上只返回一个值。它们不能包含命令或多个表达式。
# 匿名函数不能直接调用打印，因为需要lambda表达式。
# lambda函数都有自己的命名空间，并且不能访问变量高于在其参数列表和那些在全局命名空间的变量。

# 定义
sum2 = lambda arg1, arg2: arg1 + arg2    #lambda表达式

# 调用
print("Value of total : ", sum2(10, 20))
print("Value of total : ", sum2(20, 20))

# 返回多个值
tup = lambda x, y: (x+1, y+1)
c = tup(2, 3)
(a, b) = tup(2, 3)

print(a, b)
print(c[0], c[1])

# 利用lambda可以实现类似于scala中的高阶函数效果：
def outfunc(func, x, y):
    c = func(x, y)
    print(c)
    return
outfunc(lambda x, y: x+y, 10, 2)

