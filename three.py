
#write a program to check whwther entered character is number or upper case or lower case or special character
a=str(input("Enter a characher"))
if a in "01234567":
     ptint("digit")
elif a>='A' and a<='Z':
    print("uppercase")
elif a>='a' and a<='z':
    print("lowercase")
else:
        print("special character")
        