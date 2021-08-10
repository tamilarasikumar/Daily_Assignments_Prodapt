import smtplib   ,logging,writereadmodule
logging.basicConfig(filename='error1.log',level=logging.ERROR)
def mailing():         

    message=writereadmodule.bill
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login("ridhimathur10@gmail.com","ridhima@10")
    connection.sendmail("ridhimathur10@gmail.com",writereadmodule.email,message)
    logging.info("Mail sent")
    print("Sending email")  