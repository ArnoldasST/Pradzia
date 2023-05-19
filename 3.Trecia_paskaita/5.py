import datetime
while True:
    try:
        t = int(input('įvesk laiką sekudėmis: '))
        break
    except ValueError:
        print('Netinkamas formatas, prašau pakartoti')
z = input('Įvesk žodį: ')
t1 = datetime.datetime.now()
while True:
    t2 = datetime.datetime.now()
    time_diff = t2 - t1
    if time_diff.seconds >= t:
        print(z)
        t1 = datetime.datetime.now()