#A for loop is used to repeat a block of code for each item in a sequence or a specified number of times.
#rang():The range()function is commonly used with for loop to generate a sequence of number.it can take three argruments range(start,stop,step)
#rang(start):where the sequence starts
#range(stop):Where the sequence stops(this is not inclued)
#range(step):how much the number increases or decreases
for i in range(1,10,2):
    print(i,end=" ")

for i in range(10,0,-2):
    print("\n",i,end=" ")



#the continue statement is used to skips the remaining code in the current iteration and jumps directly to the next iteration of the loop.
# it does not terminate the loop it just move control the loop next cycle.
for i in range(1,11):
    if i == 5:
        continue
    print("\n continue statment:",i,end="")

#The break statement is used inside for loop ,while loop it is immediately terminates the loop,regardles the loop condition is true or false.
list = [1,2,3,4,5]
f = 5
for i in range(len(list)):
    if list[i]==f:
        print(f,"is found at index",i)
        break
else:
    print(f,"not found")

for i in range(5):
    if i == 3:
        break
    print(i)

#The else keyword in a for loop executes a block of code when the loop finishes normally.
#The else block will NOT be executed if the loop is stopped by a break statement.
#enumerate() is a Python function used in a loop to get both the index and the value of each item at the same time.
#enumerate() = index + value together
list = ["red","yellow","pink","black","white","greay"]
for index,value in enumerate(list):
    print(f"Index{index}:{value}")

for index,value in enumerate(list,start=1):
    print(f"Index{index}:{value}")

#1 to 20 print EVen or odd
for i in range(0,21):
    if i % 2 == 0:
        print(f"{i} is EVEN")
    else:
        print(f"{i} is ODD")


for i in range(10,0,-1):
    print("Reverse number:",i)

sum =0
for i in range(0,11):
    sum +=i
    print("Totalsum:",sum)

#User se ek number lo aur uska multiplication table 1–10 print karo.
no = int(input("Enter no:"))
for i in range(1,11):
    print(no,"*",i,"=",no * i)

#1 se 100 tak sirf numbers jo 5 se divisible hain, print karo.
for i in range(1,101):
    if i % 5 ==0:
        print("Divisible of 5:",i)

n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
n3 = int(input("Enter n3:"))

if n1 > n2 and n1 > n3:
    print(f"{n1} is largest")
elif n2 >n1 and n2 > n3:
    print(f"{n2}is largest")
else:
    print(f"{n3}is largest")

#nested for loop
x =[1,2]
y = [3,4]
for i in x:#outer loop only onetime execute while inner loop doesnot complete
    for j in y:#inner loop execute many time
        print(i,j)

for i in range(1,21):#outer 1 to 21
    for j in range(1,11):#inner 1 to 10
        print(i,"*",j,"=",i*j)
    print()

# 1. Kitni ROWS hain?
#         ↓
# 2. Har row me kitne SPACES?
#         ↓
# 3. Har row me kitne STARS/NUMBERS?
#         ↓
# 4. Outer loop = ROW
# 5. Inner loop = SPACES / STARS / NUMBERS
#Square Pattern
for i in range(5):#5 line
    print("lines",i)
    for j in range(5):#5 star in line(innerloop)
        print("*",end=" ")
    print()#space

#Rightside triangle
#Same Number Pattern
for i in range(1,6):
    for j in range(i):
        print(i,end=" ") 
    print()

print("----------------")
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()

for i in range(1,6):
    for space in range(5-i):
        print(" ",end=" ")

    for j in range(i):
        print(i,end=" ")
    print()
print("----------------")

for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end=" ")

    for j in range(i):
        print(i,end=" ")
    print()


#Right Triangle — Numbers
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Inverted Number Pattern
print("---------------")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#
for i in range(1,6):
    for space in range(5-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("---------------")

for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#left side traingle decrement/increment
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

print("------------------")
#right side traingle decrement/increment
for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()
print("------------------")
#
for i in range(1,6):
    for space in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()

# Same Number Pyramid,,
#Spaces = 5 - i
#Stars  = 2*i - 1
#i badhta hai → spaces kam hote hain → stars(no) badhte hain.
for i in range(1,6):
    for space in range(5-i):
        print(" ",end=" ")

    for j in range(2 * i - 1):
        print(i,end=" ")
    print()

#
for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end=" ")

    for j in range(2 * i -1):
        print(i,end=" ")
    print()

#Inverted Pyramid
for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end=" ")
    for j in range(2 * i -1):
        print(i,end=" ")
    print()

for i in range(1,6):
    for space in range(5-i):
        print(" ",end=" ")

    for j in range(2 * i - 1):#repeating hai 
        print(i,end=" ")
    print()

#Number Pyramid
for i in range(1,6):
    for space in range(5-i):
        print(" ",end=" ")

    for j in range(1,2 *i):#odd count no print 1,3,5,7
        print(j,end=" ")
    print()

for i in range(5,0,-1):
    for space in range(5 -i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(j,end=" ")
    print()

#Floyd's Triangle
no =1
for i in range(1,6):
    for j in range(i):
        print(no,end=" ")
        no+=1
    print()

#
for i in range(1,6):
    for j in range(i):
        if j % 2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()#1 
        #   1 0
        #   1 0 1
        #   1 0 1 0

#
#i =1
#j =0 innerloop
#(1+0) % 2==1 ans 1 odd first row print 1
#i=2 j =0,1
#(2+0) %2==1 ans 0 even second row print 0
#(2 + 1)%2==1 ans 1 odd second row position 0 1
#i = 3 j = 0,1,2
#(3+0)%2==1 ans 1 odd thrid row 1
#(3+1)%2==1 ans 0 even thrid row position 1 0
#(3+2)%2==1 ans 1 odd thrid row position 1 0 1

for i in range(1,6):
    for j in range(i):
        if (i+j) % 2== 1:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
