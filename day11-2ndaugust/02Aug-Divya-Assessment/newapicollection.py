import collections
import re
std_details =[ ]
class Add_Student_Details:
    def stu_Name(self,name):
        return name
    def roll_no(self,rollno):
        return rollno
    def addmission_no(self,admin_no):
        return admin_no
class Marks(Add_Student_Details):
    def marks(self,Tamil,Eng,Maths,Science,Social):
        return Tamil,Eng,Maths,Science,Social
ASD = Add_Student_Details()
Ma = Marks()

while(True):
    
    print("1.ADD_STUDENt_DETAILS")
    print("2.SEARCH_STUDENT_DETAILS USING ROLL NO")
    print("3.DISPLAY ALL STUDENT DETAILS")
    print("4.PRINT ALL THE STUDENTS BASED ON RANKING")
    choice = int(input("enter a choice: "))

    if choice == 1:
        name = input("enter a name: ")
        val = re.search("^[a-zA-Z]$",name)
        print("Name: ",Ma.stu_Name(name))
        roll_no = int(input("enter a Roll number: "))
        
        print("rollNo: ",Ma.roll_no(roll_no))
        Addmin_No = input("enter a ADMIN no: ")
        print("Admin_no: ",Ma.addmission_no(Addmin_No))
        TMark = int(input("Tamil mark: "))
        EMark = int(input("English mark: "))
        MMark = int(input("Maths mark: "))
        ScMark = int(input("Science mark: "))
        SoMark = int(input("Social mark: "))
        marks= Ma.marks(TMark,EMark,MMark,ScMark,SoMark)
        tot = TMark+EMark+ScMark+SoMark

        details = {"Name":name,"rollno":roll_no,"admission no":Addmin_No,"Marks":marks,"total":tot}
        # if len(std_details)==0:
        #     std_details = collections.ChainMap(details)
        # else:
        #     std_details = std_details.new_child(details)
        std_details.append(details)
    if choice == 2:
        # n = int(input("enter a Roll_no : "))
        # #print("enter a name: ",name)
        # if n == roll_no:
        #     d = Ma.stu_Name(name)
        #     d1 = Ma.roll_no(roll_no)
        #     d2 = Ma.addmission_no(Addmin_No)
        #     d3 = Ma.marks(TMark,EMark,MMark,ScMark,SoMark)
        #     print("Name: ",d)
        #     print("Roll Number: ",d1)
        #     print("Admission Number: ",d2)
        #     print("All subjects marks: ",d3)
        #     #print(ASD.stu_Name(name))
        n = int(input("enter a roll no to search: "))
        print(list(filter(lambda i : i ["rollno"]==n,std_details)))
        
    if choice == 3:
        print("list of marks")
        print(std_details)
    if choice == 4:
        # des = Ma.marks(TMark,EMark,MMark,ScMark,SoMark)
        # des_mark = tuple(sorted(des,reverse=True))
        # print(des_mark)
        # m = 0
        # if len(marks)>0:
        #     print(ASD.stu_Name(name))
        print(sorted(std_details,key = lambda i:i["total"],reverse=True))
        break
    else:
        print("Next")


            
    


