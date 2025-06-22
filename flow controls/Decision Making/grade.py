#4 subject marks  want to read from user

sub1=int(input("Enter your mark for sub1:"))
sub2=int(input("Enter your mark for sub2:"))
sub3=int(input("Enter your mark for sub3:"))
sub4=int(input("Enter your mark for sub4:"))
total=sub1+sub2+sub3+sub4
print("your mark is",total)
if(total>=180):
    print("You got A+")
elif(total>=160):
    print("You got A")
elif(total>=140):
    print("You got B+")
elif(total>=120):
    print("You got B")
elif(total>=100):
    print("You got C+")
else:
    print("you failed")