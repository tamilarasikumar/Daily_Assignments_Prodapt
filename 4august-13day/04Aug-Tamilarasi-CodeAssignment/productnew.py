import time,logging
import re,csv
from datetime import date
try:
    header=["name","description","price","manufactureDate","expireDate"]
    productlist=[]
    class ProductDetails:
        def addPro_Det(self,name,description,price,manufactureDate,expireDate):
            dict={"name":name,"description":description,"price":price,"manufactureDate":manufactureDate,"expireDate":expireDate}
            productlist.append(dict)
    obj=ProductDetails()

    def validate(vname,vdescription,vprice):
        name1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",vname)
        description1=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",vdescription)
        price1=re.match("[0-9]{0,7}$",vprice)
        if name1 and description1 and price1:
            return True
        else:
            return False
        
# obj=ProductDetails()
#today=datetime.date.today()

    while(True):
        print("1.Add Product")
        print("2.View all the Product")
        print("3.Search Product based on name")
        print("4.List all the Today Expire Product")
        print("5.Save the File")
        print("6.Exit")
        option=int(input("Enter your option :"))
        if option==1:
            vname = input("Enter the name of the product:")
            vdescription =  input("Enter the description of the product:")
            vprice=input("Enter the price of the product:")
            if validate(vname,vdescription,vprice):
                manufactureDate=input("Enter the manufacturing data of the product:")
                expireDate=input("Enter the expire data of the product:")
                obj.addPro_Det(vname,vdescription,vprice,manufactureDate,expireDate)
            else:
                logging.error("Check your name, description and price")
            
        if option==2:
            print(productlist)

        if option==3:
            pname=input("Ënter the  product name to search:")
            print(list(filter(lambda i:i["name"]==pname,productlist)))

        if option==4:
            current_time=time.localtime()
            tday=time.strftime("%d.%m.%Y",current_time)
            expire=(list(filter(lambda i:i["expireDate"]==str(tday),productlist)))
            print(expire)

        if option==5:
            with open("product.csv","w+",encoding="UTF8",newline="") as p:
                writer=csv.DictWriter(p,fieldnames=header)
                writer.writeheader()
                writer.writerows(productlist)    

        if option==6:
            break
except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("Code Completed Successfully")
