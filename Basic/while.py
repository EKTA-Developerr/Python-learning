#while loop is used to execute a block  of statements repeatedly until a given condition is True.when the condidtion becomes false,the line immediately after the loop in the program is executed.
i = 0
while i <= 10:
    # i = i+1
    print(i)
    i+=1

#infinite while loop :An infinite while loop is a loop that never stops by itself because its condition always remains True.,It keeps printing forever until you manually stop the program.
# while True:
#     no = int(input("enter name: "))
#     if no ==0:
#         break

#     print("You entered:",no)

#The break keyword is used to break out a for loop, or a while loop.
n = 5

while n > 0:
    print(n)
    n -= 1

print("Countdown finished!")

#10 to 1 reverse no

no = int(input("enter no:"))
while no > 0:
    print(no)
    no-=1

#
n = 1
while n <=10:
    print(n)
    if n == 5:
        break

    n+=1

#1 to 10 print with continue
no = int(input("Enter no:"))

while no <= 10:
    if no == 5:
        no += 1
        continue

    print(no)
    no += 1

#factorial 5!
no = int(input("Enter  no: "))
i = 1
mul = 1
while i <= no:
    mul = mul * i #1*2*3*4*5 =120
    print(mul)
    i+=1

#table
no =int(input("enter table no"))
i = 1
while i <=10:
    print(no,"x",i,"=",no * i)
    i+=1

# for i in range(1,10):
#     for j in range(1,10):
#         print(i,"X",j,"=",(i*j))

#sum of even no
no = int(input("Enter no: "))
sum = 0
i = 2
while i <= no:
    if i % 2 == 0:
        print(i,end=" ")
        sum =sum +i
        i+=2
print("EVen sum: ",sum)

#product of even no
no = int(input("Enter value: "))
i = 1
mul = 1
while i <= no:
    if i % 2==0:
        print(i,end=" ")
        mul = mul * i
    i=i+1
print("\n Product of even: ",mul)

###basic
n = int(input("Enter n:"))
i = 1
while i <=n:
    print(i)
    i+=1

n = int(input("Enter revern n: "))
while n > 0:
    print(n)
    n-=1

#even no
n = int(input("enter no: "))
i=1
while i <=n:
    if i % 2 ==0:
        print("\n",i,end=" ")
    i+=1

#odd
n = int(input("Enter no for odd: "))
i = 1
while i <=n:
    if i % 2 != 0:
        print(i,end=" ")
    i+=1

#sum 1 to n
n = int(input("\n Enter value: "))
sum = 0
i =1
while i<=n:
    sum = sum +i
    i+=1
print("Sum from 1 to n digit: ",sum)

#sum of even no
n = int(input("Enter value: "))
i = 1
sum = 0
while i <=n:
    if i % 2==0:
        print(i,end=" ")
        sum = sum+i
    i+=1
print("Even sum: ",sum)

#count digit
digit = int(input("Enter digit: "))
count = 0
while digit >0:
    digit = digit //10
    count+=1
print("Total digit: ",count)

#sum digit &#square of sum digit
n = int(input("Enter digit: "))
sum = 0
while n!=0:
    rem = n% 10
    sum = sum+rem #sum = sum +(rem*rem)
    n = n//10
print("Sum digit: ",sum)
print("Sum of square digits: ",sum)

#rever number
n =int(input("Enter number:"))
rev = 0
while n!=0:
    rem = n % 10
    rev = (rev * 10) +rem
    n = n//10
print("Reverse: ",rev)
#Digit nikalna: % 10
#Digit hatana: // 10
#Reverse banana: rev * 10 + rem

#palidrom no
n = int(input("Enter palidrom no: "))
original = n
rev= 0
while n!=0:
    rem = n % 10
    rev = (rev * 10)+rem
    n = n//10

if original == rev:
    print(f"{rev}Palindrom no")
else:
    print("not palindrom no")

#armstong no 
n =int(input("Enter no for armstrongno:"))
sum = 0
orignal =n
while n!=0:
    rem = n % 10
    sum = sum +(rem*rem*rem)
    n = n//10

if orignal ==sum:
    print(orignal,"Armstorng no")
else:
    print("not armstrong no")

#
a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))

a = a + b
b = a - b
a = a - b

print("a =", a, "b =", b)


    


