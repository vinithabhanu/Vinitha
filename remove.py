#remove digits from string
a=input("user@123#admin:")
out='123'
for char in a:
    if not '0'<=char<='9':
        out+=char
    print(out)
    