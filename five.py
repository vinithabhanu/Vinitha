#arithmetic operations
a=int(input("enter 1st  number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter character:"))
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='**':
    print(a**b)
elif c=='/':
    print(a/b)
elif c=='//':
    print(a//b)
elif c=='%':
    print=(a%b)
else:
    print("enter arithemetic operator")