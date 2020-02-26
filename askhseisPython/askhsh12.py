import datetime
from dateutil.relativedelta import relativedelta
i=0
while(i==0):
    dt =  datetime.datetime.now().time().strftime("%H:%M:%S");
    today = datetime.date.today()
    date_entry = input('Enter a date in DD-MM-YYYY format')
    day, month, year = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    if(str(date1-today).startswith("-")):
      print("Give Future Date")
    else:
        diff = (date1 - today).days
        i=1
        FMT = '%H:%M:%S'
        s2 = '00:00:00'
        tdelta = datetime.datetime.strptime(s2, FMT)- datetime.datetime.strptime(str(dt), FMT)
        print("Days and time till given time : "+str((date1 - today) +tdelta))
        date_after_month = date1+ relativedelta(months=1)
        print("Month Has : " + str((date_after_month - date1).days))
