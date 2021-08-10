import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/") #esttablishin connection
mydb=client['HospitalDB']#database
collection_name=mydb['Hospitals']#collection
li1=[]
li2=[]
li3=[]
def SearchHospitalSno():
    n=input("Enter serial number to be searched :")
    res=collection_name.find({"Serial number":n})
    for i in res:
        li1.append(i)
    print(li1)

def SearchHospitalcity(n): 
    try:
        n=input("Enter city to be searched :")
        res=collection_name.find({"City:":n})
        for i in res:
            li2.append(i)
        print(li2)
        
    except:
        print("no results found")


def SearchName(n): 
    try:
        n=input("Enter name to be searched :")
        res=collection_name.find({"Patinet's Name":n})
        for i in res:
            li3.append(i)
        print(li3) 
       
    except:
        print("no results found")
            