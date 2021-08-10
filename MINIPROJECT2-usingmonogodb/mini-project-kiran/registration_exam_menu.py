import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['registrationDb']
collection_name=mydatabase['registrations']
participants_list=[]
class ExamRegistration:
        def addParticipants(self,name,roll,college,mailid,exam_type,fee,reg_open_date,reg_closing_date):
            dict={"name":name,"roll":roll,"college":college,"mailid":mailid,"exam_type":exam_type,"fee":fee,"reg_open_date":reg_open_date,"reg_closing_date":reg_closing_date}
            participants_list.append(dict)
obj=ExamRegistration()

while(1):
    print("1.add participant:")
    print("2.view participant:")
    print("3.search participant:")
    print("4.delete participant")
    print("5.update participant")
    print("6.exit")   
        
    choice=int(input("enter your choice:"))

    if choice==1:
        name=input("Enter the name:")
        roll=input("Enter the rollno:")
        mailid=input("Enter the mailid:")
        college=input("Enter the college name:")
        exam_type=input("Enter the type of exam:")
        fee=input("enter the amount:")
        reg_open_date=input("Enter the registration opening date:")
        reg_closing_date=input("Enter the registration closing date:")
        obj.addParticipants(name,roll,college,mailid,exam_type,fee,reg_open_date,reg_closing_date)
        result=collection_name.insert_many(participants_list)
        print(result.inserted_ids)

    if choice==2:
        if choice==2:
            result=collection_name.find()
            for i in result:
                participants_list.append(i)
                print(i)

        
    if choice==3:
        n=input("enter the rollno:")
        k=collection_name.find({"roll":n})
        for i in k:
            print(i)
    if choice==4:
        pname=input("enter the name:")
        result=collection_name.delete_one({"name":pname})
        print(result.deleted_count)
    if choice==5:
        pnames=input("enter the participant name you have to update:")
        prollno=input("enter rollno:")
        pcollege=input("enter the college:")
        result=collection_name.update_one({"name":pnames},{"$set":{"roll":prollno,"college":pcollege}})
        print(result)
            
    if choice==6:
        break 