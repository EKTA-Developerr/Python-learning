#basic assignment variable
x = "ekta"
print(x)
#dynamic variable
x = 10
x = "ekta Davara"
print(x)
#multiple variable assignment multiple value in single line
x ,y,z =100,200,300
print(x,y,z)

#multiple variable assignment same value in single line
x =y=z ="red"
print(x)
print(y)
print(z)
print(x,y,z)

#multiple variable assign multiple value in sigle line different values
x,y,z="ekta",2.43,2
print(x,y,z)

#type casting variable & geting variable type
x = 10
y = str(x)
print(y,type(y))

# f-string method
name="ekta"
age=20
print("Name is {0} age is {1}".format(name,age))#old style
print(f"Name is { name} age is { age}")#new style

#local variable
def Teacher():
    x1 = input("Enter student name:")
    y1 = int(input("Enter student age:"))
    print(f"Name is {x1} age is {y1}")

Teacher()
#print("output----",x1,y1)#this is global variable
#Global variable
x = "Python is high level programming language"
def language():
    x = "Python is slow language as compare to java"
    print("Inside funtion:",x)
language()
print("Outside funtion:",x)

#global keyword
y = "Python"
def test():
    global y
    y = "java"
    print("inside function:",y)
test()
print("Ouside function:",y)
print(y)

#arithmetic operator
#simple calculator
import math
def calcultor():
    n1 = int(input("First no: "))
    n2 = int(input("Second no: "))

    print("Addition:",n1 + n2)
    print("Substraction: ",n1 - n2)
    print("Divison: ",n1 / n2)
    print("Module: ",n1 % n2)
    print("floor division:",n1//n2)
    print("Power: ",n1 * n1 *n1)
    print("Square: ",n1 *n1)
    print("Square root:",math.sqrt(n1))

calcultor()

#student marksheet
def marksheet():
    math = int(input("Enter math marks:"))
    science = int(input("enter science marks:"))
    english =int(input("enter english marks:"))
    total = math + science + english 
    per = (total/300)*100
    print("Total marks: ",total)
    print("Per: ",per)

    #relation operator use here
    if per >=80 and per <= 100:
        print("Grade A")
    elif per >=70 and per <=80:
        print("Grade B")
    elif per >=60 and per <=70:
        print("Grade C")
    elif per >=40 and per <=60:
        print("Grade D")
    else:
        print("Fail")
marksheet()

#assignment operator
x = int(input("Enter no:"))
x += 10
print("After x+=10:",x)

x *= 5
print("After x *=:(x =x*5)",x)

x -= 4
print("After x-=4:",x)

x %=3
print("After x%=3:",x)
x //= 2
print("After x//=2:",x)
x**=2
print("After x**=2:",x)

#relational operator
def largno():
    n1 = int(input("Enter no1:"))
    n2 = int(input("Enter no2:"))
    n3 = int(input("Enter no3:"))
    if n1 > n2 and n1 > n3:
        print(f"{n1} is large")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is large")
    else:
        print(f"{n3} is large")

largno()

#logical operator
def ATM():

    total = 50000

    while True:
        pin = int(input("Enter PIN: "))

        if pin == 1234:
            print("Correct PIN")
            break
        else:
            print("Incorrect PIN. Try again.")

    amount = int(input("Enter amount: "))

    if amount > total:
        print("Insufficient Balance")
    else:
        balance = total - amount
        print("Total:", total)
        print("Remaining Balance:", balance)
ATM()

age = int(input("Enter age:"))
student =input("Do you student:")
price = int(input("enter price:"))

if age >= 60 or student == "yes":
    dicount = 20
    discount_amount = price * dicount/100
    finalprice = price - discount_amount
    print("Discount:",discount_amount)
    print("Final price:",finalprice)
else:
    print("No dicount!")
    print("Final price:",price)

#
username = input("enter username:")
password = int(input("Enter password:"))
if username == "admin" and password == 1234:
    print("Login succesfully!")
else:
    print("invalid username & password!")

#Identity Operator
x = "hello"
y = x
print(x is y)
print(x == y)

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)


#memobership operator
fruits = ["apple","banana","cherry"]
print("banana" in fruits)
print("mango" in fruits)
print("mango" not in fruits)

#string datatype
s1 = "ekta"
s2 = 'ekta'
s3 = """hy how are,
you i am fine"""
print(s1)
print(s2)
print(s3)

#acessing char in string
s = "Davadra"
print(s[0])
print(s[5])
print(s)

#string modify
a = "ekta"
print(a.upper())#uper case
b = "Ekta D "
print(b.lower())#lower case
print(b.strip())#this function remove space staring and ending
print(b.replace("D","B"))

c ="hello world"
print(c.split())#split() is a string method used to divide a string into multiple parts and return them as a list.
s = "hy i am python!"
print(s.split())

#String Concatenation
a = "ekta"
b = "davadra"
print(a +" " +b)

#slicing string is range of char you can disaply range wise ,like [2:4]startindex,lastindex,step value
s = "Hello world!"
print(s[2:8])
#slice from start means start value not declare ok
print(s[:8])
#slice to the end means last value not declare ok
print(s[2:])
#negative index to start the slice from the end of the string
print(s[-8:-2])
#all string retrieve
print(s[:])
print(s[::])

list = [1,2,3,4,5]
print(list[::-1])#reversing list startindex,lastindex are empty step is-1.
print(list[::-2])#every second element print hoga

#String methods
#1.capitalize() to convert first char to uppercase
text = "python is hight-level Programming language"
print(text.capitalize())

#2.casefold() convert string into lowercase
print(text.casefold())

#3.center() is center align string center(len,char)
print(text.center(60,"-"))

#4.count()
print(text.count('e'))

#5.encode() conver string into bytes using a specified encoding format"UTF-8 ,ASCII
print(text.encode())

#6.startswith() The startswith() method returns True if the string starts with the specified value, otherwise False.
print(text.startswith("ekta"))
print(text.startswith("python"))

#7.endswith()
print(text.endswith("programming"))
print(text.endswith("language"))

#8.expantabs() specified number of whitespace
name = "h\te\tl\tl\to"
print(name.expandtabs())
print(name.expandtabs(4).center(30))

#9.find()method returns -1 if the value is not found.(rfind)(lfind)
print(text.find("ekta"))
print(text.find("python"))

#10.index() method raises an exception if the value is not found.(rindex)(lindex)
# print(text.index("ekta"))
print(text.index("python"))

#11 isalnum() method True if all charaters are alphanumeric,means alphabet letter ,number(0-9)
name = "ekta20"
print(name.isalnum())

#12. isalpha() all charater are alphabet letter
name = "ekta"
print(name.isalpha())

#12.isdecimal() all character are decimal(0-9)
n = "123"
print(n.isdecimal())

#13.isdigit() all character are digit.
print(n.isdigit())

#14 isidentifier()A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
text = "hellow"
print(text.isidentifier())
text = "1hellow"
print(text.isidentifier())

#15.islower()all character are lower case other false.
text = "Hello everyone!"
print(text.islower())
text ="hello" 
print(text.islower())


#16.isnumeric() all character are numeric not -1 or 3.14 ect.
n = "123"
print(n.isnumeric())

#17.isprintable() all character are printable otherwise false
n = "how#1 are\n you!"
print(n.isprintable())

#18.isspace() True if all the characters in a string are whitespaces, otherwise False.
n = "                 "
print(n.isspace())

#19.istitle() all first letter is uppercase and next letter(rest letter)is lowercase
n1 = "Ekta"
print(n1.istitle())

n2 = "ekta"
print(n2.istitle())

#20 isupper()all character are uppercase
name = "EKTA"
print(name.isupper())

#21.join()method takes all items in an iterable and joins them into one string.
tuple =("red","yellow","green")
x = "#".join(tuple)
print(x)

#22.ljust() left justify  -left align string
color = "red"
x = color.ljust(20)
print(x,"is dark color")

#23.rjust() right justify
color = "Red is dark color"
x = color.rjust(20)
print(x)
print(x.strip())#remove staring ending spaces

#24.lstrip(),rstrip()remover left side and rightside space
n = "    banana    "
print(n.lstrip())
print(n.rstrip())#removing only rightside space

#25.swapcase()conver upper to lowercase all letter chang
txt ="Good Moring!"
print(txt.swapcase())
