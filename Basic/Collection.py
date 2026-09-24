#List are used to store multiple items in a single variable
#list items are oredered,changable,allow duplicatvalue
#if you add new items to a list,the new items will be placed at the end of list.
#list is changable means you cand add ,remove,change items after that create list
mlist = ["red","yellow","green"] 
print(mlist)
print(type(mlist))

a = ['1','2','3']
print(a)
print(type(a))

#allow duplicat value
a = ["red","yellow","green","red"]
print(a)

#The list() constructor(convert) is used to create a list from another iterable such as a string, tuple, set, or range.
x = (10,20,30)
y = list(x)
print(y)

#access list items
#element in a list are accessed using indexing.python index start [0] this is give the first element,negative index allow access from the end[-1] this is last element
fruites = ["apple","banana","cherry","watermelon"]
print(fruites[2])
print(fruites[-3])
print(fruites[1:3])
print(fruites[-4:-2])
print(fruites[:2])
print(fruites[1:])#slice to end means last values not decalre
print(fruites[:-1])
print(fruites[-3:])

#if check items in list 
if "banana"in fruites:
    print("yes,'banana'in fruites list items")

#change list item using index value
fruites = ["apple","banana","cherry","watermelon"]
fruites[2] ="mango"
print(fruites)

#List methods
#append():adds an element at the end of the list
a = [1,2,3]
a.append(4)
print(a)

#appending list to list
a.append([5,6,7])
print(a)

#appending using loop
a =[]
for i in range(5):
    a.append(i)
print(a)#here list print
for i in range(5):
    print(i)#here i print

a1 =[]
for i in range(5):
    x =input("Enter value:")#user value list mein add hai
    a1.append(x)
print(a1)

#extend():This method is used to add items from one list to the end of another list ,It can work with various type of iterables such as List,string,tuple,set
n1 = [1,2,3,4]
n2 = ("ekta")
n1.extend(n2)
print(n1)
n3 = ("one","two","there","four")
n1.extend(n3)
print(n1)

#insert()The insert() method inserts an item at the specified index,it is uesd in editing list with huge amount of data,as inserting any missed value in the list is made easy with this funciton
fruites1 = ["apple","banana","mango","watermelon"]
fruites1.insert(2,"cherry")
print(fruites1)

#clear() this method is used to remove all elements from a list .it doesnot delete the list itself but clears its content
fruites1.clear()
print(fruites1)

#copy() creates a new copy of a list, so changes made to the copied list do not affect the original list.
#differnt way to copy the list like list(),slice operator,assignment operator
a = [1,2,3]
b = a[:]
print(b)

a =[10,20,30]#original list
b = a.copy()#copy list
print(a)
print(b)
b[0] = 200
print(b)
print(a)#outerlist new ->innerlist same

#Shallow copy makes a new copy of the outer object, but the inner objects remain shared.
a = [[1,2],[3,4]]#outerlist new ->innerlist same
b = a.copy()
print(b)
b[0][0] = 100
print(b)
print(a)

#Deep copy creates a completely independent copy of an object, including all nested objects.
import copy#outernewllist ->innernewlist
a = [[1,2],[3,4]]
b=copy.deepcopy(a)
b[0][0] = 40
print(a)
print(b)

#ex:
a = [10,20,[1,2,3],[4,5,6]]
b = a.copy()
print("origial copy:",a)
print("Copylist:",b)
b[2][0] =99
print(a)
print(b)

#ex:
import copy
marksheet={
    "studen1":"ekta",
    "marks":[50,60,70]
}
print(marksheet)
marksheet["marks"][0]=90#key:value
print(marksheet)

#count() is used to count how many times a particular value appears in a list, tuple, or string.
a = [1,2,3,4,5,3,4]
b=a.count(4)
print(b)

#using loop
a =[]
for i in range(4):
    x = input("enter value:")
    a.append(x)
print(a)
y = input("Enter a value whose you want to count:")
ans = a.count(y)
print("Frequany of:",y, "=",ans)

#index()this method is used you want to find the index of a specific items in a list.it has parameter element,start,end
a = ["car","honda","bus","car","truck"]
b = a.index("bus",0,4)
print(b)

a = ["car","honda","bus","car","truck"]
try:
    index =a.index("car")
    print("find the index:",index)
except ValueError:
    print("not present")

#sort() is used to arrange the elements of a list in ascending order by default.
a =[50,30,10,40,20]
a.sort()
print("This is ascending order:",a)
#To sort descending, use the keyword argument reverse = True:
a.sort(reverse=True)
print("This is descending order:",a)
#case insensitive sort
color = ["red","Yellow","green","White","black"]
color.sort(key=str.lower)
print(color)

#reverse() is used to reverse the order of elements in a list.
a = [1,2,3,4,5]
a.reverse()
print(a)

#pop() is used to remove an element from a list. By default, it removes the last element. If an index is specified, it removes the element at that index.
a.pop()
print(a)
a.pop(2)
print(a)

#remove() a specific items
b = [10,20,30,40,50]
b.remove(30)
print(b)

#del()keyword can also list del completely.
del a

#Example
list =[]
for i in range(5):
    x = input("enter element:")
    list.append(x)
print(list)
print("List length:",len(list))
b = list.copy()
print("Original list:",list)
print("Copy list:",b)
b [5] = 500
print("copy list:",b)
print("Original list:",list)
print("Comper two list:",list==b)
x =input("Enter element whose you want to count:")
ans =list.count(x)
print("Frequency of:",x,"=",ans)
i =input("Enter listvalue whose index you want to find:")
j=list.index(i)
print(f"{i} index is:",j,"Position")
a = int(input("Enter element index no you want to insert in list:"))
b = input("Enter element index value you want to insert in list:")
ans = list.insert(a,b)
print("Insert the list:",list)
r = input("Enter items whose you want to remove in the list:")
list.remove(r)
print(list)
list.reverse()
print("Reverse the list:",list)
list.sort()
print("Ascending order list:",list)
list.pop()
print("Last element remove in the list:",list)
x =int(input("enter indexno you want to delect:"))
del list[x]
print(list)
list.clear()
print(list)