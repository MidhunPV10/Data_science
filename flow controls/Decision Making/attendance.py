
classes=int(input("Enter number of classes held:"))
attended=int(input("Enter number of classes you attended:"))
attend_per=(attended/classes)*100
print("percentace of class attended by you is",attend_per)
if(attend_per>=75):
    print("You are allowed to sit in exam")
else:
    print("You are not allowed to sit in exam")