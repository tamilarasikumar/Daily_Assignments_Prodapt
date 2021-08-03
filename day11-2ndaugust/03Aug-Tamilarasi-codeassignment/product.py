import time,datetime,re
from datetime import date
productlist=[]
class ProductDetails:
    def addProductDetails(self,name,description,price,manufactureDate,expireDate):
        dict={"name":name,"description":description,"price":price,"manufactureDate":manufactureDate,"expireDate":expireDate}
        productlist.append(dict)

obj=ProductDetails()
today=datetime.date.today()
while(True):
    print("1.Add Product")
    print("2.View all the Product")
    print("3.Search Product based on name")
    print("4.List all the Today Expire Product")
    print("5.Exit")
    option=int(input("Enter your option :"))
    if option==1:
        name = input("Enter the name of the product:")
        description =  input("Enter the description of the product:")
        price=int(input("Enter the price of the product:"))
        manufactureDate=input("Enter the manufacturing data of the product:")
        expireDate=input("Enter the expire data of the product:")
        obj.addProductDetails(name,description,price,manufactureDate,expireDate)
        def validate(name,price):
            name1=re.search("[A-Z]{1}[^A-Za-z]{0,25}$",name)
            price1=re.search("[0-9]{0,7}$",price)
            if name1 and price1:
                return True
            else:
                return False

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
        break
