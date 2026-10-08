#now we check leap year or not
year=int(input("enter year for check leap year or not"))
if(year%400==0 and year%100==0 ):
    print(year,"year is leap year")
elif(year%4==0 and year%100!=0):
    print(year, "year is leap year")
else:
    print(year,"year is not leap year")

#shortcut method is 
year1=int(input("enter your year"))
if(year1%4==0):
    print(year1,"year is leap year")
else:
    print(year1,"year is not leap year")