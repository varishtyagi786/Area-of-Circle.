"""num = int(input('Enter a number: '))
# To take input from the user
#num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial  for negative numbers is ∞ ")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   
print('********************************************')"""
def factorial(n):
    return 1if(n==1 or n==0) else n*factorial(n-1);
num=int(input('Enter a Number: '))
print('Factorial of',num,'is',factorial(num))
