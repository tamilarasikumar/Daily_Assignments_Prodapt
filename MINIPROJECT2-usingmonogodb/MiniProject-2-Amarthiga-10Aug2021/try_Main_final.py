from sentinelsat import SentinelAPI
import pandas as pd

#For validation-Custom module 
from test1 import validation1

#For sending email-External modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import logging
from datetime import datetime
import pytz
import glob

logging.basicConfig(filename='logoutsession.log', level=logging.INFO)

std_time = pytz.utc
time = pytz.timezone("Asia/Kolkata")
#Connect to MongoDB
import pymongo


customer =pymongo.MongoClient("mongodb+srv://Amar_24:Amar2421@cluster0.g6gs1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DataBase = customer["SentinelAPI_DB"]
collection = DataBase["sentinel"]

query= []

class sentinel:
    def login(self,user, password, api):
        self.user=user
        self.password=password
        self.api = api
        api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
    
    def user_query(self,lat,long,footprint,product):
        self.lat=lat
        self.long=long
        self.footprint =footprint
        self.product = product

        


class sendemail:
    def Sendotp(self,useremail):
        self.useremail=useremail
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("amarproject2021@gmail.com", "Geo@2124")
        message= "Your One Time Password for the login session is 234566"
        connection.sendmail("amarproject2021@gmail.com",useremail,message)
        print("OTP has sent to user email ID")
        connection.quit()

class sendattachment(sendemail):
    def content(self,mail_content, sender_address, useremail):
        self.mail_content =mail_content
        self.sender_address =sender_address
        self.useremail =useremail

    def content_mail(message):
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = useremail
        message['Subject'] = 'Logged out from Session'

        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'logoutsession.log'
        attach_file = open(attach_file_name, 'rb')
        payload = MIMEBase('application', 'log',Name=attach_file_name)
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, useremail, text)
        session.quit()
        print('Logged out.')

class queryDB:
    def add_query(self, satellite, p_type, lat1, long1):
        self.satellite = satellite
        self.p_type = p_type
        self.lat1 = lat1
        self.long1 = long1
        # self.OData=OData
        # self.datasize = datasize
        
        
        sentidetails = {"Satellite_Name":satellite, "Product_Type":p_type, "Latitue": lat1, "Longitude":long1 }


        query.append(sentidetails)
       

Q = sentinel()
M = sendattachment()
QD =queryDB()
while(True):
    print("\n")
    print("Welcome to SentinalAPI")
    print("\n")
    print("1. Login to the page: ")
    print("2. Verify user identity: ")
    print("3. Query Satellite Data with latitude and longitude: ")
    print("4. View the available satellite data related to your querry: ")
    print("5. Query for OData and Data size: ")
    print("6. Add to Database: ")
    print("7. Display All the deatails: ")
    print("8. Search: ")
    # print("9. Update any field: ")
    print("9. Log Out the session")

    selection = int(input("Enter your choice: "))

    if selection == 1:
        print("\n")
        print("Please enter your login credentials: ")

        user = input("Type your User Name: ")
        password = input("Type your password: ")
        useremail = input("Type your email address: ")
        api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

        try:
            user_email = validation1.Valid3(useremail)
        
            print("Check email for otp")
            print("Click option 2 and verify your user identy to login")
        except:
            print("Try again")

        M.Sendotp(useremail)
        Q.login(user, password, api)

    if selection ==2:
        otpass =(input("Enter OTP: "))
        onetime=validation1.otp(otpass)

    if selection ==3:
        print("Now, you can query with latitude and longitude: ")
        lat=float(input("Enter latitude: "))
        long=float(input("Enter latitude: "))
        footprint = 'POINT(%s %s)' % (lat, long)
        product = api.query(footprint, 
                    date=('NOW-14DAYS', 'NOW'), 
                    platformname='Sentinel-2', 
                    producttype= 'S2MSI1C', 
                    area_relation='Contains',
                    limit=1
                    )

        Q.user_query(lat,long,footprint,product)

        # for value in product.values():
        #     tile = value['tileid']
            #print(value)
    if selection ==4:
        for value in product.values():
            tile = value['tileid']
            print(tile)
        print("\n")
        product_gdf = api.to_dataframe(product)
        print(product_gdf)

        product_gjson = api.to_geojson(product)
        print(product_gjson)

        # query.append(tile)
        # print(query)

    if selection ==5:
        product_odata = api.get_product_odata
        product_size =api.get_products_size
        print(product_odata)
        print(product_size)

    
    if selection ==6:
        satellite = "Sentinel-2"
        p_type='S2MSI1C'
        lat1 = lat
        long1 = long
        
        QD.add_query(satellite, p_type, lat1, long1)

    if selection ==7:
        print(query)
        collection.insert_many(query)

    if selection ==8:
        n = input("Enter satellite Name: ")
        findD = collection.find({'Satellite_Name':n})
        for n in findD:
            print(n)


    if selection ==9:
        logging.info(datetime.now(time).strftime("Last logged out session date and timing %d-%m-%y and Time %H:%M:%S"))
        for n in glob.glob('log*.log'):
            print(n)

        mail_content = """Dear user,
        Your last logged out session file is attached here. For the security reasons, we are sending this email.
        If it is not you, report to us.
        
        Regards,
        SentinelAPI"""
        sender_address = 'amarproject2021@gmail.com'
        sender_pass = 'Geo@2124'

        M.content_mail()
        print("Exited")
        break















        
           









        






