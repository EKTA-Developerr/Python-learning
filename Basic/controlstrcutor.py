# #python is uesd to excute certain block of code based on condition.
# #1. if Statement:Executes a block of code only when the condition is True.
# #else :Executes a bolck of code only when the condtion is False.
# #ladder statement(elif keyword):An if-elif-else ladder is a decision-making statement used to check multiple conditions sequentially.
# #if → checks the first condition
# # elif → checks the next conditions
# # else → runs when none of the conditions are True
# # Only the first True condition is executed.
# #Nested if-else is an if-else statement written inside another if or else statement. It is used to check an additional condition after checking the first condition.
# #if-else inside another if-else = Nested if-else.
# #
# # Even /odd no
# no =int(input("Enter no:"))
# if no % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# #Postive/negative/zero
# no =int(input("enter number:"))
# if no > 0:
#     print("Postive")
# elif no < 0:
#     print("Negative")
# else:
#     print("zero")

# #voteing
# voteage = int(input("Enter age"))
# if voteage >=18:
#     print("Eligible to vote")
# else:
#     print("not Eligible to vote")

# #largetst no
# n1 = int(input("enter no1:"))
# n2 = int(input("enter no2:"))
# n3 = int(input("enter no3:"))
# if n1 >= n2 and n1 >= n3:
#     print(n1,"is largest no")
# elif n2 >= n1 and n2 >= n3:
#     print(n2,"is largest no")
# else:
#     print(n3,"is largest no") 

# #Number Classification
# no = int(input("Enter no:"))
# if no > 0:
#     if no % 2 ==0:
#         print("Postive Even no")
#     else:
#         print("Postive ODD no")
# elif no < 0:
#     if no % 2 == 0:
#         print("Negative Even no")
#     else:
#         print("negative ODD no")
# else:
#     print("zero")

# #Student Grade System
# marks =int(input("Enter marks"))
# if marks >=90 and marks <=100:
#     print("A+")
# elif marks >=80 and marks <=89:
#     print("A")
# elif marks >=70 and marks <=79:
#     print("B")
# elif marks >=60 and marks <=69:
#     print("C")
# elif marks >=40 and marks <=59:
#     print("D")
# else:
#     print("Fail")

# #Login System
# user = input("enter username:")
# password = input("Enter password:")
# if user =="admin" and password =="1234":
#     print("login succesfully")
# elif user == "admin" and password !="1234":
#     print("invalid password")
# elif user !="admin" and password =="1234":
#     print("invalid user!")
# else:
#     print("Invalid all!") 

# #Shopping discount
# amount  = int(input("enter amount:"))
# if amount >=0 and amount <=999:
#     print("no discount")
# elif amount >=1000 and amount <=4999:
#     print("Total amoutnt:",amount)
#     calamount = (amount * 10)/100
#     price = amount -calamount
#     print("Disount is 10%")
#     print("Total amount:",price)
# elif amount >=5000 and amount <=9999:
#     print("total amount:",amount)
#     caluamount = (amount * 20)/100
#     price =amount -caluamount
#     print("Discount is 20%")
#     print("caluamount is:",caluamount)

#     print("Total price:",price)
# else :
#     print("total amount:",amount)
#     caluamount =(amount * 30)/100
#     price = amount -caluamount
#     print("Discount is 30%")
#     print("caluamount is:",caluamount)
#     print("total price:",price)

# n1 = int(input("Enter n1:"))
# n2 = int(input("Enter n2:"))
# n3 = int(input("Enter n3:"))

# if n1 ==n2==n3:
#     print("Three are same")
# elif n1 == n2 !=n3:
#     print("Two are smae")
# else:
#     print("All no are different")

# #ATM
# balance = int(input("Enter balance: "))
# pin = input("Enter pin: ")

# if pin == "1234":
#     amount = int(input("Enter withdrawal amount: "))
#     print("withdraw amount:",amount)

#     if amount <= 0:
#         print("Invalid amount")

#     elif amount > balance:
#         print("Insufficient account balance")

#     elif amount % 100 != 0:
#         print("Enter amount in multiples of 100")

#     else:
#         balance = balance - amount
#         print("Please collect your amount")

#         print("Remaining balance:", balance)
# else:
#     print("Pin invalid!")

# #Nested if_else
# pin = input("Enter pin: ")

# if pin == "1234":
#     print("Pin correct")

#     balance = int(input("Enter balance: "))
#     takeamount = int(input("Enter withdrawal amount: "))

#     print("Withdrawal amount is:", takeamount)

#     if takeamount > 0:
#         if takeamount <= balance:
#             balance = balance - takeamount
#             print("Withdrawal successful")
#             print("Remaining balance:", balance)
#         else:
#             print("Insufficient balance")
#     else:
#         print("Invalid withdrawal amount!")

# else:
#     print("Invalid PIN!")

#Python does not have a traditional switch-case statement like C, C++, or Java. Instead, Python 3.10+ provides match...case, which can be used for switch-like decision making.
#match...case is a Python control-flow statement used to compare a value against multiple patterns and execute the code block of the first matching case.
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesdady")
    case 3:
        print("wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturaday")
    case _:
        print("Sunday")

#
day = int(input("Enter day number:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Sunday")

#
pin = input("Enter pin:")
match pin:
    case "1234":
        print("Pin correct")

        print("\n-------ATM menu-------------")
        print("1.Check balacne")
        print("2.withdraw")
        print("3.Exit")

        choice = int(input("Enter choice:"))

        match choice:
            case 1:
                balance = 50000
                print("Total balance is:",balance)
            case 2:
                balance = 50000
                print("Total balance is:",balance)

                withdrwa = int(input("Enter withdrawl amount:"))
                if withdrwa > 0:
                    if withdrwa <= balance:
                        balance = balance -withdrwa
                        print("withdrawal successfully")
                        print("Remaing balance:",balance)
                    else:
                             print("Insufficient balance")
                else:
                    print("Invalid withdrawal amount!")
            case 3:
                print("Thank you  for using ATM")

            case _:
                print("Invalid choice!")
    case _:
        print("Invalid pin!")   

#
std = int(input("enter std:"))
group = input("enter group:")
per = float(input("enter per:"))
if std == 11 or std == 12:
    print("high-secondery students")
    if group == "A" :
        if per <=80:
            print("you are not eligiable to doctor")
        else:
             print("You become Doctor")
    else :
        print("You become Enginers")
else:
    if std == 9 or std == 10:
        print("you are secondary student")
        if per >= 90 and per <= 100:
            print("A+ Grade")
        elif per >= 75:
            print("A Grade")
        elif per >= 56:
            print("B Grade")
        elif per >= 35:
            print("C Grade")
        else:
            print("Fail")
    else:
        print("primary students")

    