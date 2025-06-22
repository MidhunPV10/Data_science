password=input("Enter a password : ")
upper=False
lower=False
digit=False
special=False
for i in password:
    if i.islower():
        lower=True
    elif i.isupper():
        upper=True
    elif i.isdigit():
        digit=True
    elif i in "@!#$%&*":
        special=True

if len(password)>=8 and len(password)<=13 and upper and lower and digit and special:
    print("Valid password")
else:
    print("Invalid password")


