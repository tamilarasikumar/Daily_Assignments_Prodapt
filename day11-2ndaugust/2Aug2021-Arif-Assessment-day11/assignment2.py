import collections
import re
import time
emp_d={}
def timeDate():
    ti = time.localtime()
    current_clock = time.strftime("%Y-%m-%d %H:%M:%S",ti)
    return current_clock
 
while (1):
     print("enter your choice:")
     print("1.Add Employee")
     print("2.View Employee")
     print("3.Exit")
 
     choice = int(input("enter your choice: "))
 
     if choice == 1 :
         print("Add Employee is selected ")
         EmpID = input("enter  id : ")
         
         Empname = input("enter  name: ")
         
         EmpDesgination = input("enter  desgination: ")
         a = re.search("^[A-Za-z]$",EmpDesgination)
         
         Empsalary = input("enter salary : ")
         b = re.search("^[1-9]\d{5}$",Empsalary)
         
         Empaddress = input("enter address:")
         
         Emp_phoneNo = input("enter Phone_Number: ")
         c = re.match("^\+91?[6-9]\d{9}$",Emp_phoneNo)
       
         Emp_pincode = input("enter a pincode: ")
         d = re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",Emp_pincode)
 
         K= timeDate()
         dict1 = { "EmpId":EmpID,"Empname": Empname,"Empdesgination":EmpDesgination,
                   "Empsalary":Empsalary,"Empaddress":Empaddress,"Emp_phoneNo": Emp_phoneNo,
                   "Emp_pincode":Emp_pincode,"timeAdedOn":K}
    
         if len(emp_d)==0:
            emp_d = collections.ChainMap(dict1)
         else:
             emp_d=emp_d.new_child(dict1)
 
         
     if choice == 2:
         print(" view employee")
         print(emp_d.maps)
 
                 
         
     if choice == 3:
         print("exit")
         break
     