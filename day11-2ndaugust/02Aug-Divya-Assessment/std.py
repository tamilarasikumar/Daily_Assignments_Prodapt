#from newapicollection import Add_Student_Details
import re
std_list = [ ]
class students_details:
    def __init__(self,name,rollno,adminno,tamil,eng,maths,sci,social):
        self.name = name
        self.rollno = rollno
        self.adminno = adminno
        self.tamil = tamil
        self.eng     = eng
        self.maths  = maths
        self.sci = sci
        self.social = social
    def add_std_details (self,name,rollno,adminno,tamil,eng,maths,sci,social,tot_marks):
        tot_marks = tamil+eng+maths+sci+social
        dict1 = {"name":name,"rollno":rollno,"adminno":adminno,"tamil":tamil,"eng":eng,"maths":maths,"sci":sci,"social":social,"total":tot_marks}
        std_list.append(dict1)
sd = students_details()
while(True):
    
    print("1.ADD_STUDENt_DETAILS")
    print("2.SEARCH_STUDENT_DETAILS")
    print("3.DISPLAY ALL STUDENT DETAILS")
    print("4.PRINT ALL THE STUDENTS BASED ON RANKING")
    print("5.EXIT")
    choice = int(input("enter a choice: "))

    if choice == 1:
        name = input("enter a name: ")
        val = re.search("^[a-zA-Z]$",name)
        #print("Name: ",Ma.stu_Name(name))
        rollno = int(input("enter a Roll number: "))
        
        #print("rollNo: ",Ma.roll_no(roll_no))
        addminno = input("enter a ADMIN no: ")
        #print("Admin_no: ",Ma.addmission_no(Addmin_No))
        tamil = int(input("Tamil mark: "))
        eng = int(input("English mark: "))
        maths   = int(input("Maths mark: "))
        sci= int(input("Science mark: "))
        social = int(input("Social mark: "))
        sd.add_std_details(name,rollno,addminno,tamil,eng,maths,sci,social)
    if choice == 2:
        n = int(input("enter a roll no to search: "))
        print(list(filter(lambda i : i ["rollno"]==n,std_list)))

    if choice == 3:
        print(std_list)
        
        