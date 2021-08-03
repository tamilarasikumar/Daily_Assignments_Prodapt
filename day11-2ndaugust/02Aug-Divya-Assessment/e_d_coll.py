import collections
import re,time
emp_dict = [ ]
def timeDate():
    time1 = time.localtime()
    current_colck_time = time.strftime("%Y-%m-%d %H:%M:%S",time1)
    return current_colck_time

while (True):
     print("enter your choice:")
     print("1.ADD_EMPLOYEE")
     print("2.VIEW_EMPLOYEE")
     print("3.Highest Salary")
     print("4.EXIT")

     choice = int(input("enter your choice: "))

     if choice == 1 :
         print("You selected ADD_EMPLOYEE ")
         Emp_ID = input("enter emp id : ")
         val = re.search("^E\d{4}$",Emp_ID)
         Emp_name = input("enter emp name: ")
         
         Emp_Desgination = input("enter a desgination: ")
         val1 = re.search("^[a-zA-Z]$",Emp_Desgination)
         
         emp_salary = input("enter salary : ")
         val2 = re.search("^[1-9]\d{6}$",emp_salary)
         
         Emp_address = input("enter a address:")
         
         Emp_phone_No = input("enter a Phone_Number: ")
         val3 = re.match("^\+91?[6-9]\d{9}$",Emp_phone_No)
       
         Emp_pincode = input("enter a pincode: ")
         val4 = re.search("^6\d{5}$",Emp_pincode)

         T_D = timeDate()
         dict1 = { "Emp_Id":Emp_ID,"Emp_name": Emp_name,"Emp_desgination":Emp_Desgination,
                   "Emp salary":emp_salary,"Emp_address":Emp_address,"Emp_phone no": Emp_phone_No,
                   "Emp_pincode":Emp_pincode,"timededOn":T_D}
         emp_dict.append(dict1)

         
     if choice == 2:
         print("You selected to view employee Details")            
         print(emp_dict)
    
     if choice == 3:
         print("who has highest salary")
         print(list(filter(lambda i : i ["Emp salary"] > emp_salary,emp_dict)))

                 
         
     if choice == 4:
         print("EXIT")
         break
     else:
        print("Thank you")

 
    
    