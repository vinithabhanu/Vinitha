st = input('good morning')
i=0
while i<len(a):
    if st[i] not in st[i+1]:
        print(st[i])
        break
    i+=1
