# #Dictionaries are used to store data values in key:value pairs.
# #A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# #Dictionaries are written with curly brackets, and have keys and values:
# #As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# #create dic
# dic1 = {
#     "name":"student",
#     "marks":90,
#     "grade":"A"
# }
# print(dic1)

# #changable
# #Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# #dic()constuctor is used to create dict from another iterable like list ,string,tuple
# d =dict(name = "rani",age="30")
# print(d)

# #accessing items
# #you can access the items of a dict by reffers to its key name,inside square bracket or get() method
# thisdic ={
#     "month":"may",
#     "date" :30,
#     "year":2030
# }
# print(thisdic["date"])
# print("This is accessing using get()method:",thisdic.get("date"))

# #Get keys
# #The key()method will return a list of all key in dic.
# print(thisdic.keys())

# #The value()method will return a list of all value in dic
# print(thisdic.values())

# #items() is a dictionary method that returns all the key-value pairs of a dictionary as a view object.
# print(thisdic.items())

# #change the value 
# #you can change the value of a specific item by referring  ist key name
# di1 = {
#     "name":"rani",
#     "age":30,
#     "city":"Mumbai"
# }
# print(di1)
# di1["age"] = 50
# print(di1)

# #update()/change items
# #update():To add items(key:value) from another dict into the current dict use the this method,if the item doesnot exist the item will be add
# d1 ={"name":"king","age":30,"city":"Goa"}
# d2 = {"Student":"raj","marks":90}
# d1.update(d2)
# print("d1 and d2 both in single row:",d1)
# print("Only d2 here:",d2)

# d2.update(city="mumbai")
# print("Here i use update() method and add cityname:",d2)

# d2.update(city="rajkot")
# print("Here change city name:",d2)

# d1.update({"contury":"india"})
# print("d1 add conturyname:",d1)

# #remove dic
# #There are server way to remvoe dict but here using pop() remove items with spcifict key name
# d = {'name': 'king', 'age': 30, 'city': 'Goa', 'Student': 'raj', 'marks': 90, 'contury': 'india'}
# d.pop("age")
# print("Remove age:",d)

# #popitems this is remove last key:value
# d.popitem()
# print("Last items remove:",d)

# #del keyword also completely del 
# del d

# #loop throught
# di2 = {'name': 'king', 'age': 30, 'city': 'Goa', 'Student': 'raj', 'marks': 90, 'contury': 'india'}
# for i in di2:
#     print("Here print only keys:",i)

# for i in di2:
#     print("Here print only values:",di2[i])

# for i in di2.keys():
#     print(i)

# for i in di2.values():
#     print(i)

# for i in di2.items():
#     print(i)

# #clear()
# d = {"name": "Ekta", "age": 20}
# d.clear()
# print(d)

# #copy
# d1 = {"name": "Ekta", "age": 20}
# d2 = d1.copy()

# print(d2)

#ex:
dic ={}
for i in range(5):
    x =input("Enter key:")
    y = input("Enter value:")
    dic.update({x:y})
print(dic)

print("dic length:",len(dic))
print("dic type:",type(dic))
access = input("Enter key whose you want to access:")
ans = dic.get(access)
print(ans)

a2 = dic[access]
print(a2)

ans=dic.keys()
print("All keys print:",ans)

ans = dic.values()
print("All values print:",ans)

ans = dic.items()
print("Tuple in dic:",ans)



for i in dic:
    print(i)

for i in dic.keys():
    print("Keys:",i)

for i in dic.values():
    print("values:",i)

for i ,y in dic.items():
    print("keys:values:",i,y)

r = input("Enter key whose you want to remove(pop)")
ans1=dic.pop(r)
print(r ,"is remove dict:",ans1)

#change the key and values 
print("Dicitoay print:",dic)
key = input("enter the key to change the dictiorany:")
values = input("enter the new values:")

dic[key] = values
print("change the dictioary:",dic)

dic.popitem()
print("last items remove:",dic)

d = input("Enter key whose you want to delete:")
del dic[d]
print("After delete:",dic)

cop = dict(dic)
print("this is copy dic:",cop)

dic.clear()
print("This is clear:",dic)

dic1 = [40,50,30,30,10]
print("desending oreder:",dic1.sort(reverse=True))

a ={"strobarry":50,"mango":40,"watermelon":43,"kiwi":100}
rev =dict(sorted(a.items()))
print(rev)

rev = dict(sorted(a.items(),reverse=True))
print(rev) 


