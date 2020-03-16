amount=float(input('Enter the amount: '))
rate=float(input('Enter the rate: '))
time=float(input('Enter the time: '))
si=amount*rate*time/100
print('The simple interest is: ',si)
print('Total amount to be given: ',si+amount)