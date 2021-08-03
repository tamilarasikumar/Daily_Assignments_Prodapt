import collections

employees = collections.namedtuple('employee',['name','empID','salary'])
e1 = employees("divya","4977","30000")
print(e1)
