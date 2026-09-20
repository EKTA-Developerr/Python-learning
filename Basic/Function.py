#A function is resuable block of code that performs a specific task.
#def keyword is uesd to defined or create a function in python.
#A function call is used to execute the code inside function.

def first():
    print("HEllo python")
first()

#user-defined function:A user-defined function is a function created by the user to perform specific tasks in a program.
#Types of user-defined function
#1.with argument ,no return value
#2.with argument ,with return value
#3.no argument,no return value
#4.no argument,with return value
#Argument: The actual value passed to a function when it is called.
#Parameter: A variable written inside the function parentheses that receives a value.
#1.with argument ,no return value:A function with arguments and no return value accepts values from the function call but does not return a value to the caller.
#ex
def greet(name):
    print("hello",name)
greet("python!")

#2.with argument,with return value:now the function recevie a value AND send value back.
def add(a,b):
    return a+b
ans = add(10,20)
print("sum: ",ans)

#3.no argument,no return value:the function doesn't receive anything and doesn't return anything
def welcome():
    print("HEllo eveyone!")
welcome()

#4.no argument,with returen value:The function doesn't receive anythin but but it return value
def message():
    return "HEllO guys!!"

#calling the function and storing the return value
#you can store the returned value in a variable or use it directly.
mes = message()
print(mes)

#print() → shows the value on the screen.
#return → sends the value back from the function.
#Argument → goes INTO the function
#Return   → comes OUT of the function
def mul(a,b):
    return a*b
ans = mul(4,5)#postional argument(fix)
print("Multiple: ",ans)

def add(a,b,c):
    return a+b+c
sum = add(10,20,30)
print("ADD three value: ",sum)

#function + if/else
def evenno(n):
    if n % 2==0:
        return "EVEN"
    else:
        return "ODD"
result = evenno(10)
print(result)

#find the largest of two numbers.
def largno(a,b):
    if a > b:
        return a,"large no"
    else:
        return b,"large no"
result = largno(10,20)
print("Lagest no: ",result)

#find the largest of three numbers.
def largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
result = largest(20,10,4)
print("Largest no: ",result)

#Function Argument Types
#1.Default arguments:A default argument is a predefined value used when the function call does not provide a value.
def greet(name="Python"):
    print("Hi!",name)
greet()

#3.keyword argument:A keyword argument is an argument passed to a function by explicitly writing the parameter name.
#order doesn't matters.
def student(name,age):
    print("My name is", name,"I am",age,"year old.")
student(age=20,name="nita")#keyword argument

# *args allows a function to accept any number of positional arguments.
#This function accepts only 2 arguments.
#But what if we want to pass 2, 3, 4, or 10 numbers?Use *args:
#Inside the function, args behaves like a tuple.
#So we can loop through it:
#Why use *args?
#Because we don't know beforehand how many positional arguments the user will give.args is a tuple, we can use a for loop.
def show(*args):
    for x in args:
        print(x)
show(10,20,30,40,50)

def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
result =add(10,20,30,40,50)
print("ADD: ",result)

#*args with noramal parameters

#
def sum_numbers(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
result = sum_numbers(10,20,30)
print(result)

#*args collects any number of positional arguments into a tuple, which we can process using a loop.
def multi(*no):
    mul = 1
    for i in no:
        mul =  mul * i
    return mul
result = multi(2,3,4,5)
print("Multi: ",result)

#**kwargs allows a function to accept a variable number of keyword arguments, which are stored inside the function as a dictionary.
def student(**kwargs):
    for index,values in kwargs.items():
        print(index,values)
student(name="Ekta",age =21,city ="uk")

#both use *args,**kwargs
def subject(*args, **kwargs):
    print("Collect positional arguments:")

    for i in args:
        print(i)

    print("\nKeyword arguments (**kwargs):")

    for key, value in kwargs.items():
        print(f"{key} = {value}")


subject("Python", "ML", "Java", "C", "C++")

subject(first="Ekta", last="Davdra", initial="P")

#A lambda function is a small anonymous(without name) function.
#synatax = lambda arguments: expression
add= lambda a,b:a+b
print(add(5,5))

#
square = lambda n :n*n
print(square(5))

#value_if_true if condition else value_if_false
even_odd=lambda n :"EVEN"if n% 2==0 else"ODD"
print(even_odd(40))

postive_negative = lambda n :"Postive"if n > 0 else"Negative"
print(postive_negative(39))

cube = lambda x : x*x*x
print(cube(3))

#The map() is used to apply a function to every element of an iterable,it return a map onject which you usually convert into a list.
 #lis
#  ↓
# [1, 2, 3, 4, 5]
#  ↓
# map(squar, lis)
#  ↓
# squar(1), squar(2), squar(3), squar(4), squar(5)
#  ↓
# 1, 4, 9, 16, 25
#  ↓
# list()
#  ↓
# [1, 4, 9, 16, 25]
def squar(n):
    return n*n
lis = [1,2,3,4,5]
ans = map(squar,lis)
print(list(ans))

#Double each number
def double(n):
    return n *2
nums=[1,2,3,4,5]
ans = map(double,nums)
print(list(ans))

#Add 10 to every number
def add(n):
    return n + 10
no = [1,2,3,4,5,6]
ans = map(add,no)
print(list(ans))

#convet into string
def conver(n):
    return str(n)
no = [1,2,3,4,5]
ans = map(conver,no)
print(list(ans))

#using map():map(lambda x: operation, collection)
marks = [50,60,40,70]
result = map(lambda x:x+10,marks)
print(list(result))

#
no = [4,5,6,73,2]
result = map(lambda n :n*n*n,no)
print(list(result))

#
str = ["hello","world","python"]
result = map(lambda x :x.upper(),str)
print(list(result))

#
nums = [1,2,3,4,5]
result = map(lambda x :"EVEN"if x % 2==0 else "ODD",nums)
print(list(result))

#
nums = [20,30,10,4,5,49,8]
result = map(lambda x :"HIGH"if x > 20 else"LOW",nums)
print(list(result))

#
a =[10,20,30,40]
b = [1,2,3,4]
result = map(lambda x,y: x + y,a,b)
print(list(result))

#The filter() function creates a list of items for which a function returns True:
#odd no
a1 = [1,2,3,4,5,6,7,8,9,10]
result = filter(lambda x :x % 2!=0,a1)
print(list(result))

#greater than 50
no =[10,30,5,34,5,80,89,69,90]
result = filter(lambda x:x<=50,no)
print(list(result))

#postive no
nums = [-2,3,-5,-14,4,5,8]
result =filter(lambda x:x>0,nums)
print(list(result))

marks = [35, 67, 42, 89, 25, 90, 55]
result = filter(lambda x:x>=60,marks)
print(list(result))

#reduce() repeatedly applies a function to the elements of a collection and reduces them to one single value.
# It is available in the functools module.Combines elements into one value
#[1, 2, 3, 4, 5]
#  1 + 2
#    ↓
#    3 + 3
#      ↓
#      6 + 4
#        ↓
#        10 + 5
#           ↓
#           15
from functools import reduce
nums = [1,2,3,4,5]
result = reduce(lambda x,y:x+y,nums)
print(result)

#producrt all element
from functools import reduce
nums =[10,20,30,40,50]
result = reduce(lambda x,y:x*y,nums)
print(result)

#find largest no
from functools import reduce
nums = [10, 45, 23, 89, 34, 67]
result = reduce(lambda x,y:x if x > y else y,nums)
print(result)