print('Welcome to Mybus...')
dist=input('''select destination by entering 1.for Delhi 2.for Mumbai 3.for Chennai 4.for Hyderabad:-''')
adult_seats=int(input("number of adults:-1"))
child_seats=int(input('number of childrens:-')) 
category=input('enter \n 1 for AC \n 2 for Non AC \n:-')
distance={'1':2000,'2':800,'3':350,'4':500}
if category=='1':
    adult_price=10
    child_price=5
elif category=='2':
    adult_price=5
    child_price=3
 total_price=distance[dest]*(adult_price'adult_seats+child_price*child_seats')
    print('the total amount is:-',total_price,'rupee')
    confirm=input('enter "yes" for confirm or press any othe key to cancel:-')
if confirm =='Yes':
    print('your transaction successfull')
print('Thank You---\n visit again---\n Happy Journey---\n')
else:
    print('your transaction cancelled')
    print('Thank You---visit again---')
