import pymongo,logging
client = pymongo.MongoClient("mongodb://localhost:27017/")

mydatabase= client["Employee1Db"]
Collection_name =mydatabase["Employee1"]
clist=[]
class Customer:
    def addCustomer(self,name,mobileNumber,emailId,dish1,dish2,dish3,dish4,dish5,num1,num2,num3,num4,num5):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"name":name,"mobileNumber":mobileNumber,"emailId":emailId,"dish1":dish1,"dish2":dish2,"dish3":dish3,"dish4":dish4,"dish5":dish5,"num1":num1,"num2":num2,"num3":num3,"num4":num4,"num5":num5,"AddOn":current_time}
        clist.append(dict1)
k=Customer()
def validate(name,mobileNumber,emailId):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        mobileNumber1=re.search("^(\+91)[6-9]\d{9}$",mobileNumber)
        print(mobileNumber1)
        emailId1=re.search( "[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailId)
        print(emailId1)   
        if name1 and  mobileNumber1 and emailId1:
            return True
        else:
            return False  
try:
    if __name__=="__main__":            
        while(True):
            print("1.Add Customer")
            print("2. view Customer")
            print("3.search customer using name")
            print("4.delete customer")
            print("5.update customer")
            print("6.Exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                name = input("Enter the name of Customer:")
                mobileNumber=input("Enter the mobilenumber:")
                emailId=input("Enter the email:")
                if validate(name,mobileNumber,emailId):
                    dish1=input("Enter the dish1:")
                    dish2=input("Enter the dish2 :")
                    dish3=input("Enter the dish3 :")
                    dish4=input("Enter the dish4 :")
                    dish5=input("Enter the dish5 :")
                # while(1):
                #     print("1) Massla dosa")
                #     print("2) rice")
                #     print("3) chicken")
                #     print("4) roti")
                #     print("5) paneer")
                #     option=int(input(("enter a optin: ")))
                #     if option==1:
                #         print("please enter how many how many masala dosa u wnat to eat")
                #         num1 = int(input("Enter the number of dish1:"))
                #     if option==2
                #         print("please enter how many how many masala dosa u wnat to eat")
                    num1 = int(input("Enter the number of dish1: "))
                    num2 = int(input("Enter the number of dish2: "))
                    num3 = int(input("Enter the number of dish3: "))
                    num4= int(input("enter the number of dish4:"))
                    num5=int(input("enter the number of dish5:"))
                #if validate(name,mobileNumber,emailId):
                    k.addCustomer(name, mobileNumber, emailId, dish1, dish2, dish3, dish4, dish5,num1,num2,num3,num4,num5)
                    result = Collection_name.insert_many(clist)
                    print(result.inserted_ids)
                else:

                    print("Please enter correct infomation ")
                    continue
                
            if choice==2:
                result = Collection_name.find()
                li=[]
                for i in result:
                    li.append(i)
                print(li)
               
            if choice==3:
                p = input('enter the customer name')
                result = Collection_name.find({"name":p})
                li = []
                for i in result:
                    li.append(i)

            if choice==4:
                q= input('enter the customer name')
                result=Collection_name.delete_one({'name':q})
                print(result.deleted_count)

            if choice==5:
               result=Collection_name.update_one({'name':'Arif'},{"$set":{"name":"raju"}})
               print(result)
            if choice==6:
                break
except:
    logging.error("something went wrong")               

