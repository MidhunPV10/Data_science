text=input("Enter a text :")
if(text[0]>='a')&(text[0]<='z')|(text[0]>='A')&(text[0]<='Z')|(text[0]=='_'):
    print("Valid identifier")
else:
    print("Invalid identifier")
