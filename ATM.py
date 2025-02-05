import datetime
print('Welcome to SBI')
user_pin=1234
balance=10000
print('Insert your ATM Card')
print("""
    Select One of the languages
1.English
2.Kannada
3.Hindi""")
x=int(input())
if x==1:
	print('Selected Language is English')
if x==2:
	print('Selected Language is Kannada')
if x==3:
	print('Selected Language is Hindi')
pin=input('Enter the PIN:')
if len(pin)==4:
	if int(pin)==user_pin:
		print('''
               State Bank Of India
Select one option
1.Withdrawl
2.Balance
3.Mini Statement
4.PIN Change
5.Deposit
''')
x=int(input())
if x==1:
    print('Enter the amount')
    amount=int(input())
    if amount<=balance:
        balance=balance-amount
        print('Take the Cash',amount)
        print('Balance Amount is',balance)
    else:
        print('Insufficient Balance')
elif x==2:
    print('Available balance',balance)
elif x==3:
    current_date_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(
        f"""
            State Bank Of India
Date and Time:{current_date_time}
Balance:{balance}

 """   )
elif x==4:
    user_pin=int(input('set new pin'))
elif x==5:
    print('enter the amount')
    deposit=int(input())
    if deposit%100==0 and deposit>=0:
        print('cash accepted' ,deposit)
        balance=balance+deposit
        print('balance amount is',balance)
    else:
        print('please give multiples of hundred')
