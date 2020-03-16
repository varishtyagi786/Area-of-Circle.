amount = int(input('ENTER AMOUNT : '))
n2000 = amount//2000
amount = amount%2000
n500 = amount//500
amount = amount%500
n200 = amount//200
amount = amount%200
n100 = amount//100
amount = amount%100
n50 = amount//50
amount = amount%50
n20 = amount//20
amount = amount%20
n10 = amount//10
amount = amount%10
n5 = amount//5
amount = amount%5
n2 = amount//2
amount = amount%2
print('2000 RS NOTES : ',n2000)
print('500 RS NOTES : ',n500)
print('200 RS NOTES : ',n200)
print('100 RS NOTES : ',n100)
print('50 RS NOTES : ',n50)
print('20 RS NOTES : ',n20)
print('10 RS NOTES : ',n10)
print('5 RS NOTES : ',n5)
print('2 RS NOTES : ',n2)
print('1 RS NOTES : ',amount)