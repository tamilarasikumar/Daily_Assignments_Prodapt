employeedict={}
from os import name
import re,collections,time
def getdatetime():
    time1=time.localtime()
    currenttime=time.strftime("%y-%m-%d %H:%M:%S",time1)
    return currenttime
def addEmployee():
    id=input("enter the id:")
    name=input("enter the name:")
    designation=input("enter the designation:")
    salary=input("enter the salary:")
    address=input("enter the address:")
    pincode=input("enter the pincode:")
    timedate1=getdatetime()
    dict1={"id":id,"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode,"addOn":timedate1}
    return dict1
def validate(dict1):
    valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
    valsalary=re.search("[0-9]{0,7}$",dict1["salary"])
    valpincode=re.search("(^5)[0-9]{5}$",dict1["pincode"])
    if valname and valsalary and valpincode:
        return dict1
    else:
        return False
while(1):
    print("1. add employee")
    print("2. view employee")
    print("3. exit")
    option=int(input("enter your option:"))
    if option==1:
        a=addEmployee()
        if validate(a):
            dict1=validate(a)
            if len(employeedict)==0:
                employeedict=collections.ChainMap(dict1)
            else:
                employeedict=employeedict.new_child(dict1)
    if option==2:
        print(employeedict.maps)
    if option==3:
        break