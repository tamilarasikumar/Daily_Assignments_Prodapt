studentlist=[]
class StudentDetails:
    #def __init__(self,name,rollno,admin,english,hindi,maths,science,social):
        #self.name=name
        #self.rollno=rollno
        #self.admino=admin
        #self.english=english
        #self.hindi=hindi
        #self.maths=maths
        #self.sciene=science
        #self.social=social
    def addstudentdetail(self,name,rollno,admin,english,hindi,maths,science,social):
        totalmarks=english+hindi+maths+science+social
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"admin":admin,"english":english,"hindi":hindi,"maths":maths,"science":science,"social":social}
        studentlist.append(dict1)
        
    def validate(dict1):

        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
        valmarks=re.search("[0-9]{0,5}$",dict1["total"])
        valrollno=re.search("[0-9]{0,9}$",dict1["rollno"])
        if valname and valmarks and valrollno:
            return True
        else:
            return False
obj=StudentDetails()
while(True):
    print("1.Add student")
    print("2.search students using roll no")
    print("3.display student like API")
    print("4.Ranking")
    print("5.Exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("enter your name")
        rollno=int(input("enter your rollno"))
        admino=int(input("enter admission number"))
        english=int(input("enter your english marks"))
        hindi=int(input("enter your hindi marks"))
        maths=int(input("enter your maths marks"))
        science=int(input("enter your science marks"))
        social=int(input("enter your social marks"))
        obj.addstudentdetail(name,rollno,admino,english,hindi,maths,science,social)
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=int(input("enter roll no to search"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True)) 
        
    

               