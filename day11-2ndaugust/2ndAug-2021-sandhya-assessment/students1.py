import re
studentlist=[]
class StudentDetails:
    def Stu(self,name,rollno,admin,english,maths,social,hindi,biology):
        self.name=name
        self.rollno=rollno
        self.admin=admin
        self.english=english
        self.maths=maths
        self.social=social
        self.hindi=hindi
        self.biology=biology
    def addstudentdetail(self,name,rollno,admin,enlish,maths,social,hindi,biology):
        totalmarks=english+maths+social+hindi+biology
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"maths":maths,"social":social,"hindi":hindi,"biology":biology}
        studentlist.append(dict1)
obj1=StudentDetails()
while(True):
    print("1. Add Student:")
    print("2. display:")
    print("3.search the roll no :")
    print("4.ranking:")
    print("5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter the student name:")
        rollno=(input("enter the roll no:"))
        admin=int(input("enter the admin:"))
        english=int(input("enter the english marks:"))
        maths=int(input("enter the maths marks:"))
        social=int(input("enter the social marks:"))
        hindi=int(input("enter the hindi marks:"))
        biology=int(input("enter the biology marks:"))
        v=re.search("^[1-9]",rollno)
        if rollno:
            print(rollno)
        else:
            print("Invalid rollno")
        v1=re.search("^[21-100]",marks)
        obj1.addstudentdetail(name,rollno,admin,english,maths,social,hindi,biology)
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=int(input("enter the rollno to search:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,reverse=True,key=lambda i:i['total']))
    if choice==5:
        break
    
