sub1=float(input("Enter mark of subect1 :"))
sub2=float(input("Enter mark of subject2 :"))
sub3=float(input("Enter mark of subject3 :"))
sub4=float(input("Enter mark of subject4 :"))
sub5=float(input("Enter mark of subject5 :"))
average=(sub1+sub2+sub3+sub4+sub5)/5
if(average>=90):
    print("You got A+")
elif(average>=80):
    print("You got A")
elif(average>=70):
    print("You got B+")
elif(average>=60):
    print("You got B")
elif(average>=50):
    print("You got C+")
else:
    print("You falied")
