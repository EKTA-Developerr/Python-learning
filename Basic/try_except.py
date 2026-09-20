#An exception is an unwanted or unexpected event which occurs during the executing of a program at runtime that disturb the noraml flow of the program.
#Types of error
#1.Syntax error:A Syntax Error occurs  when the code does not follow the syntax or rules of the python language..Python checks the syntax before executing the code.
if 10 >5:
    print("yes")

print("hello")

#2.Runtime error/Exception:A Runtime Error occurs while the program is running, even though the syntax of the program is correct.
a = 10
b = 5
print(a/b)

#common Built-in Exceptions
#python already proides  many bulit-in Exception.

#1.ZeroDivisionError:occure  when a number is divided by zero.

#2.valueError:occure when the value has correct general type but an inappropriate value is given.
# age = int("hello")

#3.TypeError:occure when an operation or function is used with an inappropriate data type.
# a = 10
# b ="20"
# print(a+b)

#4.IndexError:Occurs when we try to access an index that does not exist.
# number = [10,20,30,40]
# print(number[4])

#5.keyError:occurs when we try to access a dictionary key that does not exist.
# student ={
#     "name":"EKta",
#     "std":12
# }
# print(student["city"])

#6.NameError:occure when a variable or name is not defined.
# x = 10
# print(y)

#7.attribute Error:occure when trying to access an attribute that does not exist.
# name = ["hello","word"]
# print(name.uppercase())

#3.logicalError:A Logical Error occurs when the program runs successfully but produces an incorrect result because the logic or algorithm is wrong.
a =10
b = 20
print(a-b)

#Three main keywords
#1.try:this block check the error if the exists.
# 2.except:this block you handle the error.
#3.else:execute code when there is no error.
# 3.finally:this block always execute.
n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
try:
    div = n1/n2
    print(div)
except ZeroDivisionError:
    print("divide by zero isn't possiable")

finally:
    print("rest of the code")

# #
try:
    x = int(input("Enter no: "))
    print(x)
except ValueError:
    print("Please enter value")

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:
    print("progammer is completed!")

#
try:
    no = int(input("Enter divedno:"))

    div = 100/no
    print(div)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cann't divide by zero!")
else:
    print("Calculation complete")
finally:
    print("program finished")

#
def square(n):
    return n * n

# "2 4 5 7"
#       ↓
# split()
#       ↓
# ["2", "4", "5", "7"]
#       ↓
# map(int, nums)
#       ↓
# [2, 4, 5, 7]
#       ↓
# map(square, nums)
#       ↓
# square(2) → 4
# square(4) → 16
# square(5) → 25
# square(7) → 49
#       ↓
# [4, 16, 25, 49]
try:
    nums = input("Enter numbers: ").split()#string list

    nums = list(map(int, nums))#convert to  int

    result = map(square, nums)#apply square() to each number

    print(list(result))

except ValueError:
    print("Please enter numbers only!")

else:
    print("Square Calculated successfully!")

finally:
    print("Program finished!")

#
nums = [10,20,30,40,50]
try:
    no = int(input("Enter index no: "))
    print("Value:",nums[no],"is at index:",no)
except IndexError:
    print("Invalid index!")
except ValueError:
    print("Invalid value!")

#keyError
student = {
    "name": "Ekta",
    "age": 21,
    "course": "MCA",
    "city":"Goa"
}

try:
    key = input("Enter key: ")
    print("Value:", student[key])

except KeyError:
    print("Key not found!")

#raise is a Python keyword used to manually create and trigger an exception when a specific condition occurs
# raise is used to manually trigger an exception when a programmer-defined condition is not satisfied..
#Normally, Python raises an exception automatically.
#age = int("Abc")
#python automatically raises. valueError.But sometimes we want to tell Python when an error should occur.
#That's where raise is used.

age = 14
if age < 18:
    raise ValueError("age must be 18+ above")
print("Continue!")

#Usually, we don't want our entire program to crash.So we can combine raise with try-except.
try :
    age =13
    if age < 18:
        raise ValueError("age must be 18+ above")
    print("Eligible")
except ValueError as e:
    print("Error: ",e)

#
try:

    marks = 120
    if marks > 100:
        raise ValueError("Marks canot be grather than 100")
except ValueError as e:
    print("Error:",e)

#

def withdraw():
    total = 5000
    amount = int(input("Enter amount for withdraw: "))
    if amount > total:
        raise ValueError("Insufficient balance!")
    totalwithd =total - amount
    print("Remaining balance: ",totalwithd) 

try:
    withdraw()
except ValueError as e:
    print("Error:",e)

def marks(mark):
     if mark < 0 or mark > 100:
         raise ValueError("marks must be 0 to 100 between!")

try:
    marks(120)
except ValueError as e:
    print("Error:",e)

#A custom exception is a user-defined exception created by the programmer to handle a specific error or situation in a program.
#Python already has built-in exceptions like ValueError, TypeError, and IndexError. When these don't clearly describe a specific situation in our application, we can create our own exception.
# Built-in exception → Python gives it to us.
# Custom exception → We create it ourselves.
class InvalidageError(Exception):
    pass

try:
    age = int(input("Enter age:"))
    if age <= 18:
        raise InvalidageError("age must be 18+ above!")
    print("Eligiable")
except InvalidageError as e:
    print("Error:",e)

#
class InsufficientBalanceError(Exception):
    pass

def withdraw(totalbalance,amount):

    if amount > totalbalance:
        raise InsufficientBalanceError("Insufficient Balacne!!")

    if amount < 0:
        raise ValueError("Amount must be greather than 0!!")

    return totalbalance - amount

try:
    balance = 5000
    amount = int(input("Enter amount: "))
    remaining = withdraw(balance,amount)
except ValueError as e:
    print("Error: ",e)
except InsufficientBalanceError as i:
    print("Transaction Failed: ",i)
else:
    print("Withdrawal successful")
    print("Remaining balance:", remaining)

finally:
    print("Thank you for using our banking system")

#
class InvalidaMarksError(Exception):
    pass

def marksheet(marks):
    if marks < 0 or marks > 100:
        raise InvalidaMarksError("marks must be 0 to 100!!")
    if marks >=90 and marks < 100:
        print("Grade A")
    elif marks >=80 and marks <=89:
        print("Grade B")
    elif marks >=70 and marks <= 79:
        print("Grade C")
    elif marks >=60 and marks <=69:
        print("Grade D")
    else :
        print("Fail!")

try:
    marks = int(input("Enter marks: "))
    marksheet(marks)
except ValueError as e:
    print("Value Error: ",e)
except InvalidaMarksError as i:
    print("Custom Error:",i)
else:
    print("Mark is :",marks)
finally :
    print("Marksheet done")

#
class InvalidloginError(Exception):
    pass

def login(user,password):
    if user != "admin" and password != 1234:
        raise InvalidloginError("Username and password are wrong!")

    elif user != "admin":

        raise InvalidloginError("Username is wrong!")

    elif password != 1234:
        raise InvalidloginError("Password is wrong!")

    else:
        print("Successfully login")

try :
    user = input("Enter user: ")
    password = int(input("Enter password:"))
    login(user,password)

except ValueError as e:
    print("value Error: ",e)
except InvalidloginError as e:
    print("Custom Error: ",e)
else:
    print("You Successfully login")

finally:
    print("Thank you")