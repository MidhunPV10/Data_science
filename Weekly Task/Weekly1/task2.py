password=input("Enter your password :")
if(len(password)>=8)&('0'in password or '1'in password or '2'in password or '3'in password or '4'in password or
                      '5'in password or '6'in password or' 7'in password or '8'in password or '9'in password):
    print("password is valid")
else:
    print("password is not valid")
