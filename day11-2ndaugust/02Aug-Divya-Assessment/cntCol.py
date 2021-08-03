import collections
c = [ ]
for i in range(2):
    n = input("enter a name: ")
    c.append(n.lower())
x = collections.Counter(c)
print(x)
