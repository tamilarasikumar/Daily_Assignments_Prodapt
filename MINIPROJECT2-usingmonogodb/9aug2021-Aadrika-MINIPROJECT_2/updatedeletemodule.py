import pymongo ,writereadmodule
client=pymongo.MongoClient("mongodb://localhost:27017/") #esttablishin connection
mydb=client['HospitalDB']#database
collection_name=mydb['Hospitals']#collection

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
        res=collection_name.update_one({"Serial Number":sno}, {"$set":{"Patinet's Name":name} })
        print("name updated")
    if n==2:
        age=input("Enter updated age for patient :")
        res=collection_name.update_one({"Serial Number":sno}, {"$set":{"Patinet's Age:":age} })
    if n==3:
        bg=input("Enter updated bloodgroup for patient :")
        res=collection_name.update_one({"Serial Number":sno}, {"$set":{"Patient's Blood Group:":bg} })
    if n==4:
        city=input("Enter updated city for patient :")
        res=collection_name.update_one({"Serial Number":sno}, {"$set":{"City:":city} })
    if n==5:
        phone=input("Enter updated phonr for patient :")
        res=collection_name.update_one({"Serial Number":sno}, {"$set":{"Phone number:":phone} })
    if n==6:
        mail=input("Enter updated email for patient :")
        res=collection_name.update_one({"Serial Number":sno}, {"$set":{"E-Mail:":mail} })
    if n==7:
        drname=input("Enter updated doctor name for patient :")
        res=collection_name.update_one({"Serial Number":sno}, {"$set":{"Doctor's Name:":drname} })
    



def deleting():
    sno=input("enter serial number of patient to delete :")
    res=collection_name.delete_one({"Serial Number":sno})
    print(res.deleted_count)
    print("record deleted")