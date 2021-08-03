import collections
#x=collections.Counter(["hello","hello","hi"])#used to count no of iterable elements in a list,it is a subset of dictonary
#print(x)
#collect 10 names from the user using for loop and store it in counter and find the occurances
list=[]
for i in range(1,11):
    names=input("enter a name")
    list.append(names)
print(list)
x=collections.Counter(list)
print(x)