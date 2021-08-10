
import sys
import logging
import bookeduserinfo
import buyticket
import emailall
import pymongo

logging.basicConfig(filename="movie.log",level=logging.DEBUG)
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["moviedb"]
moviee=mydb["movies"]
Booked_seat = 0
prize_of_ticket = 0
Total_Income = 0

Row = int(input('Enter number of Row - \n'))
Seats = int(input('Enter number of seats in a Row - \n'))
Total_seat = Row*Seats
Booked_ticket_Person = [[None for j in range(Seats)] for i in range(Row)]


class chart:

    #@staticmethod
    def chart_maker():
        seats_chart = {}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Seats):
                seats_in_row[str(j+1)] = 'S'
            seats_chart[str(i)] = seats_in_row
        return seats_chart

class_call = chart()
table_of_chart = chart.chart_maker()

while(True):
    print('1. Show the seats: ')
    print("2. Buy a Ticket and entering details in database" )
    print("3. Show booked Tickets User Info from database: ")
    print("4. Update booked ticket in database : ")
    print("5. Cancel your booked ticket: ")
    print("6. Exit: ")
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Enter valid choice")
        logging.error("User entered wrong choice")
        continue

    if choice==1:
        if Seats < 10:

            for seat in range(Seats):
                print(seat, end='  ')
            print(Seats)
        else:
            for seat in range(10):
                print(seat, end='  ')
            for seat in range(10, Seats):
                print(seat, end=' ')
            print(Seats)
        if Seats < 10:
            for num in table_of_chart.keys():
                print(int(num)+1, end='  ')
                for no in table_of_chart[num].values():
                    print(no, end='  ')
                print()
        else:
            count_num = 0
            for num in table_of_chart.keys():
                if int(list(table_of_chart.keys())[count_num]) < 9:
                    print(int(num)+1, end='  ')
                else:
                    print(int(num)+1, end=' ')
                count_key = 0
                for no in table_of_chart[num].values():
                    if int(list(table_of_chart[num].keys())[count_key]) <= 10:
                        print(no, end='  ')
                    else:
                        print(no, end='  ')
                    count_key += 1
                count_num += 1
                print()
        print('Vacant Seats = ', Total_seat - Booked_seat)
        print()
        
    if choice==2:
        a=buyticket.BuyTicketEnjoy(Row,Seats,table_of_chart,Booked_seat,Total_Income,Booked_ticket_Person)
        # email=input("Enter your email id:")
        result=moviee.insert_one(a)
        print(result.inserted_id)
        
        
        
        # connection=smtplib.SMTP("smtp.gmail.com",587)
        # connection.starttls()
        # connection.login("hariompateldada@gmail.com","Sparsh@01")
        # message="Your ticket has been booked"
        # connection.sendmail("hariompateldada@gmail.com",email,message)
        # print("Email has sent succesfully")
        # connection.quit()
        emailall.emailAll()
        logging.info("Customer buyed ticket")
    
    if choice==3:
        # Enter_row = int(input('Enter Row number - \n'))
        # Enter_column = int(input('Enter Column number - \n'))
        # if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
        #     if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
        #         person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
        #         print('Name - ', person['Name'])
        #         print('Phone number - ', person['Phone_No'])
        #         print('Gender - ', person['Gender'])
        #         print('Age - ', person['Age'])
        #         #print('Phone number - ', person['Phone_No'])
        #         print('Ticket Prize - ', '$', person['Ticket_prize'])
        #     else:
        #         print()
        #         print('---**---  Vacant seat  ---**---')
        # else:
        #     print()
        #     print('***  Invalid Input  ***')
        # print()
        # logging.info("customer information showned")
        bookeduserinfo.BookedUserInfo(Row,Seats,table_of_chart,Booked_ticket_Person)
        # result=moviee.insert_one(a)
        # print(result.inserted_id)
    if choice==4:
        Name=input("enter your name")
        Phone_No=input("enter phone number to modify")

        res=moviee.update_one({"Name":Name}, {"$set":{"Phone_No":Phone_No} })  
        print("Data has been modified") 
    if choice==5:
        Name=input("Enter name:")
        r2=moviee.delete_one({"Name":Name})
        print("Ticket cancelled")
    if choice==6:
        sys.exit()



    