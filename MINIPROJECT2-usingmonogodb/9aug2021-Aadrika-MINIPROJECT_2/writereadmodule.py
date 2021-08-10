import time, pymongo
import logging
from validation import validation_of_Patients
logging.basicConfig(filename='error1.log',level=logging.ERROR)

client=pymongo.MongoClient("mongodb://localhost:27017/") #esttablishin connection
mydb=client['HospitalDB']#database
collection_name=mydb['Hospitals']#collection

li=[]
# headercontent=["Serial number","Patinet's Name" ,"Patinet's Age:","Patinet's Sex (Male/Female)","Patinet's Height:","Patinet's Weight(In Kgs)","Patient's Blood Group:","Fathers Name:","Address:","City:","Phone number:","E-Mail:","Doctor's Name:", "Disease Name:","Bill Amount: Rs.","added"]

hospitallist=[]
class Hospital:
    def _init_(self):
        self.sno=0
        self.name=' '
        self.age=0
        self.sex=""
        self.email=" "
        self.fname=" "
        self.address=''
        self.city=''

        self.height=0
        self.weight=0
        self.doctor=''
        
        self.bill=0

        self.pno=0
        self.bgroup=''
        self.dname=''

    def Input(self):
        while(True):
            self.sno=input("Enter Serial number:")
            self.name=input("Enter Patinet's Name:")
            self.age=input("Enter Patinet's Age:")
            self.sex=input("Enter Patinet's Sex (Male/Female):")
            self.height=input("Enter Patinet's Height:")
            self.weight=input("Enter Patinet's Weight(In Kgs):")
            self.bgroup=input("Enter Patient's Blood Group:")
            self.fname=input("Enter Fathers Name:")
            self.address=input("Enter Address:")
            self.city=input("Enter City:")
            self.pno=input("Enter Phone number:")
            self.email=input("Enter E-Mail:")
            self.doctor=input("Enter Doctor's Name:")
            self.dname=input("Enter Disease Name:")
            self.bill=input("Enter Bill Amount: Rs.")
            if validation_of_Patients(self.sno ,self.name ,self.pno, self.email):
        
                current_local_time=time.strftime("%H:%M:%S",time.localtime())
                dict1={"Serial number":self.sno,"Patinet's Name":self.name ,"Patinet's Age:":self.age,"Patinet's Sex (Male/Female)":self.sex,"Patinet's Height:":self.height,"Patinet's Weight(In Kgs)":self.weight,"Patient's Blood Group:":self.bgroup,"Fathers Name:":self.fname,"Address:":self.address,"City:":self.city,"Phone number:":self.pno,"E-Mail:":self.email,"Doctor's Name:":self.doctor, "Disease Name:":self.dname,"Bill Amount: Rs.":self.bill,"added":current_local_time}
                
                return dict1
            else:
                print("enter valid information ")
                continue
            break
       
    def Output(self):
        print ("SERIAL NUMBER:-",self.sno)
        print ("PATIENT'S NAME:-",self.name)
        print ("PATIENT'S AGE:-",self.age)
        print ("PATIENT'S SEX:-",self.sex)
        print ("PATIENT'S HEIGHT:-",self.height)
        print ("PATIENT'S WEIGHT:-",self.weight)
        print ("PATIENT'S BLOOD GROUP:-",self.bgroup)
        print ("FATHERS NAME:-",self.fname)
        print ("ADDRESS:-",self.address)
        print ("CITY:-",self.city)
        print ("CONTACT NUMBER:-",self.pno)
        print ("E-MAIL ADDRESS:-",self.email)
        print ("DISEASE NAME:-",self.dname)
        print ("DOCTOR'S NAME:-",self.doctor)
        print ("BILL AMOUNT:-",self.bill)


ob=Hospital()

def WriteHospital():
    
    res=ob.Input()
    collection_name.insert_one(res)
    print("record saved")
    print("your details are")
    ob.Output()
    
  
def ReadHospital():
    res=collection_name.find()
    for i in res:
        print(i)

    

def modifyDetails():
    
    sno=input("ENTER SERIAL NUMBER TO MODIFY:--")
    print ("\n")
    print ("____________________________________________ " )
    print ("|  ......... ENTER YOUR CHOICE ..........  | " )
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ " )
    print ("\n")
    print ("WHAT DO YOU WANT TO MODIFY:")        
    print ("1.PATIENT'S NAME")
    print ("2.PATIENT'S AGE")
    print ("3.PATIENT'S BLOOD GROUP:-")
    print ("4.CITY:-")
    print ("5.CONTACT NUMBER:-")
    print ("6.E-MAIL ADDRESS:-")
    print ("7.DOCTOR'S NAME:-")
 
    n=int(input("::--"))  
    if n==1:
        name=input("Enter updated name for patient :")
        collection_name.update_one({"Serial Number":sno}, {"$set":{"Patinet's Name":name} })
        print("name updated")
    if n==2:
        age=input("Enter updated age for patient :")
        collection_name.update_one({"Serial Number":sno}, {"$set":{"Patinet's Age:":age} })
    if n==3:
        bg=input("Enter updated bloodgroup for patient :")
        collection_name.update_one({"Serial Number":sno}, {"$set":{"Patient's Blood Group:":bg} })
    if n==4:
        city=input("Enter updated city for patient :")
        collection_name.update_one({"Serial Number":sno}, {"$set":{"City:":city} })
    if n==5:
        phone=input("Enter updated phonr for patient :")
        collection_name.update_one({"Serial Number":sno}, {"$set":{"Phone number:":phone} })
    if n==6:
        mail=input("Enter updated email for patient :")
        collection_name.update_one({"Serial Number":sno}, {"$set":{"E-Mail:":mail} })
    if n==7:
        drname=input("Enter updated doctor name for patient :")
        collection_name.update_one({"Serial Number":sno}, {"$set":{"Doctor's Name:":drname} })
    



def deleting():
    sno=input("enter serial number of patient to delete :")
    res=collection_name.delete_one({"Serial Number":sno})
    print(res.deleted_count)
    print("record deleted") 