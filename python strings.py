#strings
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#ex "yash" 

from os import remove


print("yash")

#Multiline Strings 
#use by using 3 quotes

a = '''Hello World , This is yash and i am learning python basics'''
print(a)

#slicing
#Specify the start index and the end index, separated by a colon

b = "Hello, World! This is Yash"
print(b[2:5]) 

#Slice From the Start
b = "Hello, World! This is Yash"
print(b[:5]) 

#Slice From the end
b = "Hello, World! This is Yash"
print(b[2:]) 

#Negative Indexing
b = "Hello, World! This is Yash"
print(b[-2:-5])

#Modify Strings
a = "Yash"
print(a.replace("Y", "J"))

#Concatenation STRING
#Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

#Booleans 
print(bool("Hello"))
print(bool(15))

#Python Lists
mylist = ["apple", "banana", "mango"]
print(mylist)

#List Length
mylist = ["apple", "banana", "mango"]
print(len(mylist))

#remove list
mylist = ["apple", "banana", "mango"]
print(remove[1])












