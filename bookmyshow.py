print('welcome to book my show')
name = input('please enter your name:-')
seats = int(input('please enter the no of seats,you want to book'))
category = int(input('please select 1.diamond /n,2.gold /n,3.silver'))
if category == 1:
    amount=seats*200
elif category ==2:
    amount=seats*150
elif category ==3:
    amount=seats*100
print(f'hi{name}you have booked{seats}seats and total amount is {amount}')