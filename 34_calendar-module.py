import calendar

date = input().split()
print(list(calendar.day_name)[calendar.weekday(int(date[2]),int(date[0]),int(date[1]))].upper())
