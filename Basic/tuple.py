# #Tuples are used to store multiple items in a single variable.
# #Tuple items are ordered, unchangeable, and allow duplicate values.
# #Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# #When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# #Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# #create tuple with one item
# #To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# t = ("red",)
# print(t)
# print(type(t))

# #tuple() constructor is used to create a tuple from another iterable such as string,list,tuple
# l = [10,20,30]
# t = tuple(l)
# print(t)

# #access tuple items by using index number
# t = ("red","yellow","green","purple","grey","white","black")
# print(len(t))
# print(t[4])
# print(t[-3])
# print(t[3:6])
# print("All tuple retrive:",t[::-1])#all tuple print
# print(t[0:3])
# print(t[:2])
# print(t[-5:-1])
# print(t[-4:])

# #change tuple value
# #Tuple are unchangable(immutable),meaning that you canot change,add or remove items once the tuple is created.
# #You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# t = ("apple","red","banana")
# l = list(t)
# print(t)
# l[1] = "cherry"
# t = tuple(l)
# print(t)

# #append() use here
# thist = ("apple","red","banana")
# y = list(thist)
# y.append("mango")
# thist = tuple(y)
# print(thist)

# #Tuples are unchangeable, so you cannot remove items from it
# #Convert the tuple into a list, remove "apple", and convert it back into a tuple:
# thist = ("apple","red","banana","mango")
# y = list(thist)
# y.remove("red")
# thist = tuple(y)
# print(thist)

# #del tuple completely
# del thist

# #loop through a tuple
# thistuple = ("red","yellow","white","black")
# for i in thistuple:
#     print(i)

# for i in range(len(thistuple)):
#     print(thistuple[i])

# #join two or more tuple using +concatenation operator
# ftuple = ("red","white","black")
# stuple = (1,2,3,4)
# thrid = ftuple + stuple
# print(thrid)

#ex:
t =()
for i in range(5):
    x =input("enter elemtnt in tuple:")
    l = list(t)
    l.append(x)
    t =tuple(l)
print(t)

print("Type of this :",type(t))
print("Lenght of dic:",len(t))

re = input("Enter element whose you remove:")
l = list(t)
l.remove(re)
t = tuple(l)
print(re,"is remove in dict",t)

cou = input("Enter whose you want to count:")
ans = t.count(cou)
print("Fequency use",cou,"=",ans)

x = int(input("Enter index value you want to insert element:"))
y = input("Enter value you want to insert element value:")
l =list(t)
l.insert(x,y)
a = tuple(l)
print("insert succesfully:",a)

z = list(t)
z.reverse()
t = tuple(z)
print("reverse tuple:",t)

#program marge all methods 
a =()
for i in range(5):
    x = input("enter in iteam in tuple")
    b = list(a)
    b.append(x)
    a= tuple(b)
    print(a)

y =input("enter values whose you want to find index no  in tuple:")
ans = a.index(y)
print(ans)

x = input("enter value to remove in tuple:")
y =  list(a)
y.remove(x)
a = tuple(y)
print(a)

print("length of the tuple:",len(a))

print("max value in tuple:",max(a))

print("min values in tuple:",min(a))

 
x = input("enter values whose you want to count:")
ans = a.count(x)
print("frequency of :",x,"=",ans)

x =int(input("enter the index no then you want to insert in tuple"))
z = input("enter the index values you want to insert in tuple")
y = list(a)
y.insert(x,z)
a = tuple(y)
print(a)

y = list(a)
y .reverse()
a = tuple(y)
print(a)

y = list(a)
y.sort()
a= tuple(y)
print(a)

y = list(a) 
y .pop(x)
a = tuple(y)
print("last iteam is remove:",a)

##
#second program
user =()
for i in range(5):
        x = input("enter iteam in tuples:")
        temp = list(user)
        temp.append(x)
        user= tuple(temp)
print(user)
                                                #or
user =("red","yellow","pink","red","white")
print(user)

print("length of tuple:",len(user))

x = input("enter the iteam to count:")
ans = user.count(x)
print("Total iteam count", x ,"=",ans)

x = input("enter index iteam whose you want to index:  ")
ans = user.index(x)
print(x,"found is",ans)

print("max values:",max(user))

print("min values:",min(user))

sortt = list(sorted(user))
print("sorted:",sortt)

revers = list(reversed(user))
print("Reversed iteams:",revers)