studentlist=[]
class StudentDetails:   
    def addstudent(self,name,rollno,admino,hindi,english,maths):
        totalmarks=hindi+english+maths
        dic={"total":totalmarks,"name":name,"rollno":rollno,"admino":admino,"hindi":hindi,"english":english,"maths":maths}
        studentlist.append(dic) 


obj1=StudentDetails()

while(True):
    print("1)Add student:")
    print("2)search student rollno:")
    print("3)display student api:")
    print("4)ranking:")
    print("5)exit:")
    choice=int(input("enter a option:"))
   
    if choice==1:
        name=input("enter name:")
        rollno=int(input("enter roll no:"))
        admino=int(input("enter admino no:"))
        hindi=int(input("enter hindi marks:"))
        maths=int(input("enter maths marks:"))
        english=int(input("enter english marks:"))
        obj1.addstudent(name,rollno,admino,hindi,english,maths)

    if choice==2:
        srollno=int(input("enter the rollno to search:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    
    if choice==3:
        print(studentlist)

    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True))

    if choice==5:
        break