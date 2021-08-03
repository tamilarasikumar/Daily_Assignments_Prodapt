import time
# %H=hours
# %M=months
# %S=seconds
# %h=month(August)
# %m=month
current_time=time.localtime()
print(current_time)
current_time_clock=time.strftime("%Y-%m-%d %H:%M:%S",current_time)
print(current_time_clock)
#display all the employess who has a salary greater than the amount specified by the user by using list comprehension
#create a menu driven application
#                1.add students(sname,srollno,admno,marks for 5 subjects(oops))
#                2.search the student details with rollno
#                3.list the student api with marks
#                4.print all the students based on ranking(sum of marks)
#