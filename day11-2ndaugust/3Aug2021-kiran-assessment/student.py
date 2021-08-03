
studentslist=[]
class studentDetails:
    def addStudentsDetails(self,name,rollno,admno,english,hindi,maths,science,social):
        totalmarks=english+hindi+maths+science+social
        dict1={"total":totalmarks,"name":name,"rollno":rollno,"admno":admno,"english":english,"hindi":hindi,"maths":maths,"science":science,"social":social}
        studentslist.append(dict1)
obj=studentDetails()
    def validate(dict1):
        valname=re.search("^[A-Z]{1}[a-z]{0,25}$",dict1["name"])
        valrollno=re.search("^[1-9]{1}[0-9]{6}$",dict1["rollno"])
  


while(1):
    print("1.add student:")
    print("2.search student details with rollno:")
    print("3.list the student api with marks")
    print("4.students with their rank:")
    print("5.exit:")

    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter the student name:")
        rollno=input("enter the student rollno:")
        admno=input("enter the student admno:")
        english=int(input("enter the english marks:"))
        hindi=int(input("enter the hindi marks:"))
        maths=int(input("enter the maths marks:"))
        science=int(input("enter the science marks:"))
        social=int(input("enter the socialmarks:"))
        obj.addStudentsDetails(name,rollno,admno,english,hindi,maths,science,social)
    if choice==2:
        print(studentslist)
    if choice==3:
        srollno=int(input("enter rollno to search:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentslist)))
    if choice==4:
        print(sorted(studentslist,key=lambda i:i['total'],reverse=True))