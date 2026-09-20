#set are used to store maltiple items in single values.
#set are unoredered,unchagable ,unindexed and don't allow duplicate values.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#The value True and 1 are consider the same value.False and 0 are consider the same value.
createset = {"apple","banana","mango",True,1,False,0}
print(createset)#duplicate items remove

#set()constructor are used to create set from another iterable like string,list,tuple
f_set = set(("red","yellow","green"))
print(f_set)

#Access items
#you can't access items in a set by referring to an index or a key.
#But you can loop thought the set items using a for loop or ask specific value is present in set using in operator.
sset = {"teacher","doctor","farmer","tailor"}
for i in sset:
    print(i)

print("tailor"in sset)

#add items :once you create set then after you can't cange items but add and remove items is allow
#add():you can add items in set
t_set ={"apple","banana","cherry","watermelon"}
t_set.add("orange")
print(t_set)

#add items from another set into current set
s_set1 = {1,2,3,4}
s_set2 = {5,6,7}
s_set1.update(s_set2)
print(s_set1)

#remove items
#remove()and discard()
#if the items is doesnot exist in set remove() method raise in error.
#if the items is doesnot exist in set discard() method isnot raise in error. 
s_set1.remove(3)
print(s_set1)
s_set1.discard(3)
print(s_set1)

#pop() this method is used remove items but this method remove any random items becase set is unindex items
x=s_set1.pop()
print(x)
print(s_set1)

#clear() empty set
s_set1.clear()
print(s_set1)

#del is completely del set
del s_set2
# print(s_set2)

#join set
#union() is a Python set method used to combine two or more sets and return all unique elements from them.
#union() combines sets and removes duplicate values.shortcut | pipe operator.Symbol 'U'
set1 = {1,2,3,4}
set2 ={4,5,6,7}
print(set1.union(set2))
print(set1|set2)

#multiple join set
set1_1 ={"apple","banana","orange","cherry"}
set2_1 = {1,2,3,4}
set3_1 = {"sunday","monday","tuesday","wednesday"}
set4_1 ={"red","yellow","green","black"}
ans = set1_1.union(set2_1).union(set3_1).union(set4_1)
print(ans) 
print("This is pipe operator:",set1_1|set2_1|set3_1|set4_1)

#intersection():This method return a new set with an element that is common to all set, we can also get intersections using'&'operator,
a = {1,2,3,4,5}
b ={4,5,6,7,8}
print("Commna to all set items:",a.intersection(b))
print("This is operator '&' through print:",a&b)

#intersection_update() is a Python set method That updates the original set by keeping only the elements that are common in both sets.
#It keeps common elements and updates the original set.
a = {1,2,3,4}
b = {3,4,5,6}
a.intersection_update(b)
print(a)
print(b)#intersection_update:common element is stay in original set but update original set ok.

#difference() is a Python set method that returns the elements that are present in the first set but not present in the second set.'-'operator is using in shortcut.
a = {10,20,30,40}
b = {30,40,50,60}
c = a.difference(b)
print("Differemce:",c)
print(a-b)

#difference_update:common element is remove original set
#Intersection_update = Common ko KEEP ✅
#Difference_update = Common ko REMOVE ❌

#Symmetric Difference = Common elements REMOVE +  unique elements KEEP
a1 ={1,2,3,4,5}
a2={3,4,5,6}
print(a1.symmetric_difference(a2))

#  The easiest memory trick
# Union →  Keep ALL
# Intersection →  Keep COMMON
# Difference → Remove COMMON from A
# Symmetric Difference →  Remove COMMON from BOTH
# ALL → COMMON → ONLY → NOT COMMON.

