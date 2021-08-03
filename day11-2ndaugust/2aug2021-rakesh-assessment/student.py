import re
studentlist=[]
class StudentDetails:
    def init(self,name,rollno,admin,english,hindi,maths,science,social):
        self.name=name
        self.rollno=rollno
        self.admin=admin
        self.english=english
        self.hindi=hindi
        self.maths=maths
        self.science=science
        self.social=social
    def addstudentdetail(self,name,rollno,admin,english,hindi,maths,science,social):
        totalmarks=english+hindi+maths+science+social
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"hindi":hindi,"maths":maths,"science":science,"social":social} 
        studentlist.append(dict1)
    def validate(dict1):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
        valrollno=re.search("[0-9]{0,7}$",dict1["rollno"])
        valadmin=re.search("[0-9]{0,5}$",dict1["admin"])
        if valname and valrollno and valadmin:
           return True
        else:
           return False
obj=StudentDetails()        
while True:
    print("1.add student")
    print("2.search student")
    print("3.display")
    print("4.ranking")
    print("5.exit") 
    choice=int(input("Enter your choice : "))
    # obj=StudentDetails()
    if choice==1:
      name=input("Enter the name : ")
      rollno=int(input("Enter the roll no : "))
      admin=int(input("Enter the admission no : "))
      english=int(input("Enter the marks of English : "))
      hindi=int(input("Enter the marks of Hindi : "))
      maths=int(input("Enter the marks of maths : "))
      science=int(input("Enter the marks of Science : "))
      social=int(input("Enter the marks of Social : "))
     #obj=StudentDetails()
      obj.addstudentdetail(name,rollno,admin,english,hindi,maths,science,social)
    if choice==3:
        print(studentlist)
    if choice==2:
        srollno=int(input("Enter the rollno to search : "))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
    if choice==5:
        break