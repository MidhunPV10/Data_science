first_side=int(input("Enter the length of first side:"))
second_side=int(input("Enter the length of second side:"))
third_side=int(input("Enter the length of third side:"))
if(first_side==second_side==third_side):
    print("Triangle is an equilateral triangle")
elif(first_side==second_side)or(second_side==third_side)or(first_side==third_side):
    print("Triangle is an isosceles triangle")
else:
    print("Triangle is an scalane triangle")
