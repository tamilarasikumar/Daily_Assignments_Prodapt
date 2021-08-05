import re,csv,logging
try:
    header=["totalmarks","name","rollno","adminno","english","tamil","maths","science","social"]
    studentlist=[]
    class StudentDetails:
        #def __init__(self,name,rollno,adminno,english,tamil,maths,science,social):
            # self.name=name
            # self.rollno=rollno
            # self.adminno=adminno
            # self.english=english
            # self.tamil=tamil
            # self.maths=maths
            # self.science=science
            # self.social=social
        

        def addstudentdetial(self,name,rollno,adminno,english,tamil,maths,science,social):
            totalmarks=english+tamil+maths+science+social
            dict1={"totalmarks":totalmarks,"name":name,"rollno":rollno,"adminno":adminno,"english":english,"tamil":tamil,"maths":maths,"science":science,"social":social}
            studentlist.append(dict1) 
    obj1=StudentDetails()  

    def validate(vname,vrollno):
        name1=re.search("([a-z]+)([a-z]+)*([a-z]+)*$",vname)
        rollno1=re.search("[0-9]{0,7}$",vrollno)
        if name1 and rollno1:
            return True
        else:
            return False


    # obj1=StudentDetails()     #create object for student
    while(True):
        print("1.Add Student")
        print("2.Display studets using API")
        print("3.Search Students based on rollno")
        print("4.Ranking")
        print("5.Save into File:")
        print("6.Exit")

        option=int(input("Enter your option :"))
    
        if option==1:
            vname = input("Enter the name of the student: ")
            vrollno=input("Ënter the RollNo:")
            if validate(vname,vrollno):
                adminno= int( input("Enter the Admin number: "))
                english= int (input("Enter the English marks  subject: "))
                tamil= int (input("Enter the Tamil marks subject: "))
                maths= int (input("Enter the Maths marks subject: "))
                science= int (input("Enter the Science marks subject: "))
                social= int (input("Enter the Social marks  subject: "))
                obj1.addstudentdetial(vname,vrollno,adminno,english,tamil,maths,science,social)
            else:
                logging.error("Check your name and rollno")
                
        if option==2:
            print(studentlist)
        if option==3:
            srollno=int(input("Ënter the rollno to search:"))
            print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
        if option==4:
            print(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
        if option==5:
            with open("student1.csv","w+",encoding="UTF8",newline="") as s:
                writer=csv.DictWriter(s,fieldnames=header)
                writer.writeheader()
                writer.writerows(studentlist)
        if option==6:
            break
except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("Code Completed Successfully")
          

        

        
