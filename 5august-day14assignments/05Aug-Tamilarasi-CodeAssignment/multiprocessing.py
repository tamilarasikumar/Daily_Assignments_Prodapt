#########   Process Threading    #########
import threading,time,logging
try:
    def primeNo():
        for num in range(2,500):
            #time.sleep(1)
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print("Prime Number:",num)
    def printPalindrome():
        for num in range(10,500):
            #time.sleep(1)
            temp = num
            reverse = 0
            while(temp > 0):
                Reminder = temp % 10
                reverse = (reverse * 10) + Reminder
                temp = temp //10
            if(num == reverse):
                print("Palindrome Number:",num)
    if(__name__=='__main__'):  
        t1=threading.Thread(target=primeNo)     #create the processs
        t2=threading.Thread(target=printPalindrome)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("*********CODE COMPLETED*********")
except Exception:
    logging.error("Something Wrong!")


