num=int(input('enter a number:'))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print('it is a perfect number')
else:
    print('it is not a perfect number')
