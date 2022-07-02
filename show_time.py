from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ", current_time)
today = now.strftime("%d/%m/%y")
print("Today's Date = ", today)
day = datetime.today().strftime("%A")
print("Day = ", day)
