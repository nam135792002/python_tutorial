import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(12, 39, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2024, 12, 20, 10, 5, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

print(date)
print(today)
print(time)
print(now)
