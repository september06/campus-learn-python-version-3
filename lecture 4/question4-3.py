import calendar
str1 = input("Enter a date in mod dd/mm/yyyy:  ")
day = int(str1[:2])
month = int(str1[3:5])
year =int(str1[6:])
print(day)
print(month)
print(year)
day_in_week = calendar.weekday(year, month, day)
if(day_in_week == 0):
    print("Monday")
elif(day_in_week == 1):
    print("Tuesday")
elif (day_in_week == 2):
    print("Wednesday")
elif(day_in_week == 3 ):
    print("Thursday")
elif(day_in_week == 4):
    print("Friday")
elif(day_in_week == 5):
    print("Saturday")
elif(day_in_week == 6):
    print("Sanday")	
	
input("Enter a date in mod dd/mm/yyyy:  ")