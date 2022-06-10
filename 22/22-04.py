import datetime as dt


temp_days = input()
days = dt.timedelta(int(temp_days))
today = dt.datetime.today()
print((today + days).day, (today + days).month)

