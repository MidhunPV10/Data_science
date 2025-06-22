salary=int(input("Enter your salary:"))
service=int(input("Enter you year of experience:"))

if(service>=5):
    bonus = salary * 0.05
    print("bonus is",bonus)
else:
    print("no bonus your salary is",salary)
