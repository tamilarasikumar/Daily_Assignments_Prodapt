employeedict={}
from os import name
import re,collections,time
def getTimeAndDate():
    time1=time.localtime()
    currenttime=time.strftime("%Y-%m-%d%H:%M:%S",time1)
    return currenttime
def addEmployee():
    id=input("enter your id number")
    designation=input("enter your designation")
    name=input("enter your name")
    salary=input("enter your salary")
    address=input("enter your address")
    pincode=input("enter your pincode")
    timedate=getTimeAndDate()
    dict1={"id":id,"designation":designation,"name":name,"salary":salary,"address":address,"pincode":pincode,'addedOn':timedate}
    return dict1
def validate(dict1):
    name=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
    salary=re.search("[0-9]{0,7}$",dict1["salary"])
    pincode=re.search("^(5)[0-9]{5}$",dict1["pincode"])
    if name and salary and pincode:
        return True
    else:
        return False
while(True):
    print("1.AddEmployee")
    print("2.ViewEmployee")
    print("3.Exit")
    choice=int(input("enter your choice"))
    if choice==1:
        a=addEmployee()
        if validate(a):
            if len(employeedict==0):
                employeedict=collections.ChainMap(a)
            else:
                employeedict=employeedict.new_child(a)
    if choice==2:
        print(employeedict.maps)
    if choice==3:
        break