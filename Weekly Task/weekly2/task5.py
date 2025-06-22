quantity=int(input("Enter your purchased quantity : "))
total_cost=quantity*100
if(total_cost>1000):
    discount=total_cost/10
    final_cost=total_cost-discount
else:
    final_cost=total_cost
print("you want to pay the cost",final_cost)