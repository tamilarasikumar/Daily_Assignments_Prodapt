import collections
d1 = collections.OrderedDict()
d1["name"] ="divya"
d1["empid"]= 4977
d1["salary"]= 30000

for key,value in d1.items():
    print(key,value)