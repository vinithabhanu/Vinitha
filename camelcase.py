a = input('hello my name is abhi:')
i=0
out=' '
temp=True
while i<len(a):
    if a[i]== ' ':
        temp=True
         temp and 'a'<=a[i]<='z':
             out+ =char(ord(a[i])-32)
             temp=False
    else:
         out+=a[i]
         temp=False
         i+=1
print(i)