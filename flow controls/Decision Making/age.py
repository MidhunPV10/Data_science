#calculate age
#inputs
#current_year
#current month
#current_date
#birthyear
#birthmonth
#birthdate

current_year = int(input("Enter current year: "))
current_month = int(input("Enter current month: "))
current_day = int(input("Enter current day: "))
birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))
age = current_year - birth_year
if(current_month < birth_month):
    age-=1
else:
    if(current_month == birth_month):
        if(current_day < birth_day):
            age-=1
print("Your age is:", age)


