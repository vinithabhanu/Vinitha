a =input('enter a string:')
i=0
count=o
while i<len(a):
      if a[i] in  "aeiouAEIOU":
           count+=1
      i=i+1
 print(count)