import datetime

utc_time = datetime.datetime(2024, 1, 1, 12, 0)
sp = utc_time - datetime.timedelta(hours = -3)

print(sp)

print(utc_time)