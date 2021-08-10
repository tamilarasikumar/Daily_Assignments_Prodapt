from mailing import mailing
import writereadmodule,pymongo
import searchingmodule ,updatedeletemodule
import logging 
client=pymongo.MongoClient("mongodb://localhost:27017/") #esttablishin connection
mydb=client['HospitalDB']#database
collection_name=mydb['Hospitals']#collection
logging.basicConfig(filename='error1.log',level=logging.ERROR)

while True:
    print("\n")
    print("Simple Hospital Management System \n")
    #print("\n")
    print("1.WRITE RECORD\n2.SHOW ALL RECORDS\n3.MODIFY BY SERIAL NUMBER")
    print("4.DELETE BY SERIAL NUMBER\n5.SEARCH BY NAME\n6.SEARCH BY CITY\n7.SEARCH BY SERIAL NUMBER")
    print("8.Send email\n9.Exit")
    ch=int(input("\nPLEASE ENTER YOUR CHOICE:--"))
    try:
        if ch==1:
            writereadmodule.WriteHospital()
        if ch==2:
            writereadmodule.ReadHospital()
        if ch==3:
            writereadmodule.modifyDetails()
        if ch==4:
            writereadmodule.deleting()
        if ch==5:
            searchingmodule.SearchName()
        if ch==6:  
           searchingmodule.SearchHospitalcity()
        if ch==7:
            searchingmodule.SearchHospitalSno()
        if ch==8:
            mailing.mailing()
        if ch==9:
            break
            
    except:
       logging.error("you have entered wrong choice")