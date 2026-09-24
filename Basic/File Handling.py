# File Handling in python is the process of creating,opening,reding,writing,modifying and closing files using python code
#It allow your program to store data permanently(in text files,binary files,csv files)
#when a python program runs.all the data you create(like variable,list,user input)is stored in RAM(memory).
#RAM=Temporary memory when the program closes -->all data is lost,when the computer shuts down -->data is gone.
#why file handling is needed?
#To store data permanently on the disk(hard drive),The data stays saved,you can use it later
#opening a File
#open file we can use open()function
#syntax: file =open("filename.txt",mode)
#mode:-Modes are the different operations(such as read,write,append)that specify how a file should be accessed when using the open() function.
# "r"=Read(file must exist)
# "w"=Write(create a new file or over write existing)
# "a"=Append(add content to end of the file)
# "r+"=Read and write
# "w+"=Write and read
# "a+"=read and append and of file
#
#writelines():write multiple string in the list form,#all data replace how to old data safe and add new data i tell in nex example.
list = ["Name:Nirali\n",
        "course:12std\n",
        "schoole:I.P.Mission\n",
        "year:2026"
    ]
with open("ekta.txt","w")as f:
    f.writelines(list)
    print("DATA ENTER Successfully")
with open("ekta.txt","r")as f:
    print(f.read())

#append():Append mode is used to add new data at the end of an existing file without deleting the old data.
with open("ekta.txt","a")as f:
    f.write("\nsemester:1")
    f.write("\nsubject:maths")
    print("Append the data")

with open("ekta.txt","r")as f:
    ans =f.read()
    print(ans)

#
with open("ekta.txt","w")as f:
    list=[]
    for i in range(5):
        name = input("Enter name:")
        list.append(name+"\n")
    f.writelines(list)

with open("ekta.txt","r")as f:
    print(f.read())

#read,By default the read() method returns the whole text, but you can also specify how many characters you want to return:
file = open("ekta.txt","r")
data = file.read(5)
print(data)
file.close()

#using the with statement ,autoumaticlly close the file
with open("ekta.txt","r") as f:
    print(f.read())

#readline():this file method reads a line of data one by one read
with open("ekta.txt","r") as f:
    print(f.readline())

#readlines():This file method read all line from the file but in list format
with open("ekta.txt","r") as f:
    data = f.readlines()
    print(data)
    print("Number of length:",len(data))

#you can read file line by line throught the for loop
with open("ekta.txt") as f:
    for line in f:
        print(line.strip())

# r+ read with write,r+ does not automatically mean append.
# In your code, it writes at the end because f.read() moved the pointer to the end.
# if i have add data in begining using of seek(0)
# seek(0) = move the file pointer to position 0 (the beginning of the file).
# With r+, writing from the beginning can overwrite existing characters. It does not insert new text before the old text.
# 
try:
   with open("ekta.txt","r+") as f:
       data = f.read()
       print(data)
       f.write("Sem:1")
except FileNotFoundError:
    print("file not found!")
#
with open("ekta.txt","r+") as f:
    print(f.read())
    f.seek(0)
    f.write("subject:python")

# w+ write withh read
# w+ existing file ka old data delete/overwrite kar deta hai.
with open("ekta.txt","w+")as f:
    f.write("Name:ekta\n")
    f.write("Course:MCA\n")

    f.seek(0)
    print(f.read())

#
with open("ekta.txt","w+")as f:
    f.write("Name:ekta\n")
    f.write("Course:MCA\n")

    f.seek(0)
    print(f.readlines())

#a+ = apend with read
with open("ekta.txt","a+")as f:
    f.write("sem:1\n")
    f.write("Collage:GLS\n")
    f.seek(0)
    print(f.readline())
    print(f.readlines())

#tell() tells you the current position of the file pointer.
with open("ekta.txt","r")as f:
    print(f.tell())
    print(f.read(4))
    print(f.tell())

#flush() is a file method used to force buffered data to be written to the file immediately.
#You usually don't need to call flush() manually when using: with open(...)as f:because when the with block finishes, Python closes the file and handles the buffered data.
#with → automatically handles the file closing and ensures pending buffered data is handled. 
#flush() → manually tells Python to write buffered data immediately.
with open("ekta.txt","a+")as f:
    f.write("Hello eveyone!")
    f.flush()
    print("Data finish")
    f.seek(0)
    print(f.read())

#truncate() is a file method used to remove the contents of a file after a specified position.(Extra content remove/delete)
file = open("ekta.txt","r+")
data = file.truncate(5)
print("file size:",data)
file.seek(0)
print("file contenct:",file.read())
file.close()

#os.remove() is used to permanently delete a file from the computer.
import os
os.remove("ekta.txt")
print("File deleted!")

import os

if os.path.exists("ekta.txt"):
    print("File exists")
else:
    print("File does not exist")

import os

size = os.path.getsize("studen.txt")

print("File size:", size, "bytes")

#rename
# import os

# os.rename("ekta.txt", "student2.txt")

# print("File renamed successfully")

#make folder
import os
if not os.path.exists("mca"):
    os.mkdir("mca")
    print("Create folder")
else:
    print("folder already exists")

#delete folder
import os
os.rmdir("mca")
print("delete floder")

#os.listdir() — See Files and Folders
import os
ans=os.listdir("Basic")
print(ans)

#os.getcwd() — Get Current Working Directory
import os

path = os.getcwd()

print(path)

#import os

if os.path.isfile("ekta.txt"):
    print("It is a file")
else:
    print("File does not exist")

#practice EXample

try:
    with open("studen.txt","w")as f:
        f.write("Name:Ekta\n"),
        f.write("Course:MCA\n"),
        f.write("Univercity:GLS\n")

    with open("studen.txt","r")as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File not found!")
else:
    print("Data insert successfully in the file")


try:
    lines = [
        "Name:Ekta\n",
        "Course:MCA\n",
        "Sem:1\n"
    ]

    with open("studen.txt", "w") as f:
        f.writelines(lines)

    print("Data written successfully!")

except TypeError:
    print("Invalid data for writelines!")

#
with open("studen.txt","a")as f:
    f.write("subject:Python\n")
    f.write("marks:50\n")
    print("datainsert")

#
with open("studen.txt","a")as f:
    line = ["skill:python\n","skill:java\n","skill:panda\n"]
    f.writelines(line)
    print("Datainsert!")

#
try:
    with open("studen.txt", "r") as f:
        data = f.read(5)
        print(data)

except FileNotFoundError:
    print("File not found!")

else:
    print("File read successfully!")

#
try:
    with open("studen.txt","r")as f:
        data = f.readline()
        data1 = f.readlines()
        print("First line read:",data)
        print(data1)
        print(len(data1))
except FileNotFoundError:
    print("File not Found!")
else:
    print("File read successfully!")

#
with open("studen.txt ") as f:
    for line in f:
        print(line.strip())