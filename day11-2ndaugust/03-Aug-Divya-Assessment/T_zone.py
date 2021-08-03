import pytz
from datetime import datetime, timezone

std_time = pytz.utc
print("indian time zone")
time_zone = pytz.timezone("Asia/kolkata")
print(datetime.now(std_time))
print(datetime.now(time_zone))
print(datetime.now(time_zone).strftime("%Y-%h-%d %H:%M:%S"))
print("south korea time zone")
time_zone = pytz.timezone("Asia/Seoul")
print(datetime.now(std_time))
print(datetime.now(time_zone))
print(datetime.now(time_zone).strftime("%Y-%h-%d %H:%M:%S"))

print("canada time zone")
time_zone = pytz.timezone("Canada/Central")
print(datetime.now(std_time))
print(datetime.now(time_zone))
print(datetime.now(time_zone).strftime("%Y-%h-%d %H:%M:%S"))
