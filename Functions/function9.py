x=10   #global variable.defined outside of function and acessible everywhere

def myfunction():
    x=5     # local variable.Define inside of function and not acessible everywhere
    print("value of x is :",x)

print("value of x outside function is :",x)
myfunction()