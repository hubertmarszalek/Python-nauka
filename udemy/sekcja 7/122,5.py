from datetime import datetime, date

# utworzenie obiektu datetime z daty
datetimeObj = datetime(2021, 3, 8)
print("date(): ", datetimeObj.date())         # 2021-03-08
print("time(): ", datetimeObj.time())         # 00:00:00
print("timestamp(): ", datetimeObj.timestamp())
print("weekday(): ", datetimeObj.weekday())   # 0 = poniedziałek
print("today(): ", datetime.today())
print("year: ", datetimeObj.year)
print("hour: ", datetimeObj.hour)
print("minute: ", datetimeObj.minute)
print("second: ", datetimeObj.second)
print("microsecond:", datetimeObj.microsecond)
print("format: ", datetimeObj.strftime("%m/%d/%Y %H:%M:%S"))

# ============================================
# porównywanie dat i czasów
# ============================================

datetime1 = datetime(2025, 5, 30, 23, 59, 0)
datetime2 = datetime(2025, 5, 30, 23, 59, 10)

print(datetime1 > datetime2)   # False
print(datetime1 < datetime2)   # True
print(datetime1 == datetime2)  # False
print(datetime2 == datetime2)  # True

date1 = date(2019, 4, 16)
date2 = date(2020, 11, 3)

print(date1 > date2)   # False
print(date1 < date2)   # True
print(date1 == date2)  # False
print(date2 == date2)  # True
