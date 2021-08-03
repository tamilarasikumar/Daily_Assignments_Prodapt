import re
import time
studlist=[]
class Student:
    def studentdetails():
        pass
         
class marks:
    def marks():
        pass
        
    

   
class studentdetails(Student,marks):
    def addstudentdetails(self,name,rollno,admin,english,chemistry,maths,physics):
        total=eng+hindi+maths+science
        current_local_time=time.strftime("%Y-%M-%d %H:%M:%S",time.localtime())
        dict1={"name":name,"rollno":rollno,"admin":admin,"english":english,"chemistry":chemistry,"maths":maths,"physics":physics,"total":total,"addedon":current_local_time}
        studentlist.append(dict1)
obj1=studentdetails()
while(True):
    print("1. Add Students:")
    print("2. display student details: ")
    print("3. search student using roll number")
    print("4. Ranking")
    print("5. exit")
    choice=int(input("enter your choice: "))
    
    if choice==1:
        name=input("Enter your name: ")
       
        rollno=(input("enter your rollno: "))
       
        admin=(input("enter your admin: "))
        
        eng=int(input("enter english marks: "))
        hindi=int(input("enter chemistry marks: "))
        maths=int(input("enter maths marks: "))
        science=int(input("enter physic marks: "))
        def validation():
            a=re.search("^[A-Za-z]",name)
            b=re.search("^[0-9",rollno)
            c=re.search("^[0-9]",admin)
            if a and b and c:
                return[(name),int(rollno),int(admin)]
            else:
                print("wrong entered")    
        
    obj1.addstudentdetails(name,rollno,admin,english,chemistry,maths,physics)
        
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=int(input("Enter roll number to search: "))
        print(list(filter(lambda i:i["rollnum"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
    if choice==5:
        break