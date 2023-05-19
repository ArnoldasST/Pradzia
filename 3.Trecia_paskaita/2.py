import datetime

now = datetime.datetime.today()
print(now)
print(now - datetime.timedelta(days=5))
print(now + datetime.timedelta(hours=8))
data = now.strftime("%Y %m %d, %H:%M:%S")
print(data)

