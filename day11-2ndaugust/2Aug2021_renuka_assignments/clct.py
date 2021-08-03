#named tuple
import collections
employees=collections.namedtuple("employees",["name","empid","salary"])
e1=employees("raju","1237","29387")
print(e1.name)
print(e1.empid)
print(e1.salary)
print(e1[0])