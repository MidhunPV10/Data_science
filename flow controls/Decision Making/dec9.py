largest_number=int(input("Enter a number over 100 :"))
smallest_number=int(input("Enter a number under 10 :"))
if(largest_number>100 and smallest_number<10):
    times=largest_number//smallest_number
    print(smallest_number,"goes into",largest_number,times,"times")
else:
    print("invalid number.Please check the given largest number is above 100 and smallest number is under 10")