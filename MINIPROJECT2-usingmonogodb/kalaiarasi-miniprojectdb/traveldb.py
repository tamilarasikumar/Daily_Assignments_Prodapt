import re
import logging
import pymongo
import time
import smtplib
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/ProductDb")
    mydatabase=client['TravelDb']
    collection_name=mydatabase['travels']

    tlist=[]
    travelist=[]
    def validation(name,emailid,mobilenum,tripdate):
        vname=re.search("^[A-Za-z]{2,25}$",name)
        vmail=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",emailid)
        vmob=re.search("^(\+91)?[0]?(91)?[6-9]\d{9}$",mobilenum)
        vdate=re.search("^[0-9]{2}\s[0-9]{2}\s[0-9]{4}",tripdate)
        if vname and vmail and vmob and tripdate:
            return True
        else:
            return False
    class Customerdetail:
        def __init__(self):
            name=''
            address=''
            mobilenum=''
            emailid=''
        def addcustomerdetail(self,name,address,mobilenum,emailid):
            name="name"
            address="address"
            mobilenum="mobilenum"
            emailid="emailid"
            return self.addcustomerdetail
    class Trip(Customerdetail):
        def __init__(self):
            tripid=''
            tripdate=''
            tripcost=''
            tripid=''
        def addtrip(self,tripdate,tripcost,tripplan,tripid):
            tripid="tripid"
            tripdate="tripdate"
            tripcost="tripcost"
            tripplan="tripplan"
        
            return self.addtrip

    obj=Trip()
    if(__name__=='__main__'):
        while(True):
            print("1. add trip")
            print("2. view the details")
            print("3. search using customer name")
            print("4. Display the customer details who have trip today")
            print("5. change the trip plan")
            print("6. Delete the trip")
            print("7. send an email")
            print("8. exit")

            choice=int(input("enter ur choice:"))
             
            if choice==1:
                name=input("enter your name:")
                address=input("enter your add:")
                mobilenum=input("enter your mobilenum:")
                emailid=input("enter your emailid:")
                
                tripid=input("enter the tripid:")
                tripcost=input("enter your cost:")
                tripplan=input("enter your pla:")
                tripdate=input("enter your date:")
                
            
                x=validation(name,emailid,mobilenum,tripdate)
                if x:
                    obj.addcustomerdetail(name,address,mobilenum,emailid)
                    obj.addtrip(tripdate,tripcost,tripplan,tripid)
                    dict1={"name":name,"address":address,"mobilenum":mobilenum,"emailid":emailid,"tripdate":tripdate,"tripcost":tripcost,"tripid":tripid,"tripplan":tripplan}
                    travelist.append(dict1)
                    r=collection_name.insert_one(dict1)

                else:
                    logging.error("please enter valid data!")
            if choice==2:
                r=collection_name.find()
                for i in r:
                    tlist.append(i)
                print(tlist)

            if choice==3:
                a=input("enter name:")
                r=collection_name.find({"name":a})
                for i in r:
                    print(i)



            if choice==4:
                r=collection_name.find()
                for i in r:
                    tlist.append(i)
                currenttime=time.localtime()
                currentclock=time.strftime("%d %m %Y",currenttime)
                print(list(filter(lambda i: i["tripdate"]==currentclock,tlist)))
        
            if choice==5:
                c=input("enter the tripid:")
                newplan=input("enter the newplan:")
                results=collection_name.update_many({"tripid":c},{"$set":{"tripplan":newplan}})
                print("updated")

            
            if choice==6:
                d=input("enter id to delete:")
                results=collection_name.delete_many({"tripid":d})
                print("deleted")

                
            if choice==7:
                r=collection_name.find()
                for i in r:
                    tlist.append(i)
                    message="Thank for u choosing AB Travels.we make your travel memorable and fun."
                    connection =smtplib.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.login("kalai.iprimed@gmail.com","Kalai@2404")
                    message="Thank for u choosing AB Travels.we make your travel memorable and fun."
                    print(message)
                    connection.sendmail("kalai.iprimed@gmail.com",i["emailid"],message)
                    connection.quit()
                    print("email send")
                
            if choice==8:
                break
                                        
except:
    logging.error("please enter correct data")

     