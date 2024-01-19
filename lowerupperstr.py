a = input('enter a character:')
a=65
ord('a')=97
i=0
out=' '
while i<len(a):
    if 'a'<=a[i]<='z':
         out+=char(ord(a[i])-32)
    else:
        out+=a[i]
    i+=1
print(i)
  
    

