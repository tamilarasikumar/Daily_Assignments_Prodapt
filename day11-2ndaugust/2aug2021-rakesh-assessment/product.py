import datetime,time
from datetime import date
productlist=[]
class ProductDetails:
    def init(self,pname,description,price,manufucturer,mfd,ed):
        self.pname=pname
        self.description=description
        self.price=price
        self.manufacturer=manufacturer
        self.mfd=mfd
        self.ed=ed
    def validate(dict1):
        valpname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
        valdescription=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",dict1["description"])
        valprice=re.search("[1-9]{1}[1-9]{2,7}$",dict1["price"])
        valmanufacturer=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",dict1["manufacturer"])
        valmfd=re.search("^(?:[0-9]{2})?[0-9]{2}-(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])$",dict1["mfd"])
        valed=re.search("^(?:[0-9]{2})?[0-9]{2}-(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])$",dict1["ed"])
        if valname and valsalary and valpincode:
           return True
        else:
           return False   
    def addproductdetail(self,pname,description,price,manufucturer,mfd,ed):
        
        dict1={"pname":pname,"description":description,"price":price,"manufacturer":manufacturer,"mfd":mfd,"ed":ed} 
        productlist.append(dict1)
obj=ProductDetails()    
today=datetime.date.today()
while True:
    print("1.Add Product")
    print("2.View products")
    print("3.Search a product")
    print("4.List products that expire today")
    print("5.exit") 
    choice=int(input("Enter your choice : "))
    
    if choice==1:
      pname=input("Enter the Product name : ")
      description=input("Enter the Description : ")
      price=int(input("Enter the Price : "))
      manufacturer=input("Enter the manufacturer name : ")
      mfd=input("Enter the manufacturing date : ")
      ed=input("Enter the expiry date   YYYY-MM-DD : ")
    
      obj.addproductdetail(pname,description,price,manufacturer,mfd,ed)
    if choice==2:
        print(productlist)
    if choice==3:
        sname=input("Enter the product name to search : ")
        print(list(filter(lambda i:i["pname"]==sname,productlist)))
    if choice==4:
 
        current_time=time.localtime()
        tday=time.strftime("%Y-%m-%d",current_time)
        # ed=time.strftime("%d-%m-%y")
        #today=datetime.date.today()
        
        expirylist=(list(filter(lambda i:i["ed"]==str(tday),productlist)))    
        if len(expirylist)>0:
            print(expirylist)
        else:
            print("No records found")  
    if choice==5:
        break