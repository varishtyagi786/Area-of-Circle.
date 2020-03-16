
hindi=float(input('Enter a marks of HINDI: '))
eng=float(input('Enter a marks of ENGLISH: '))
math=float(input('Enter a marks of MATHS: '))
sci=float(input('Enter a marks of SCIENCE: '))
sst=float(input('Enter a marks of S.ST: '))
per=(hindi+eng+math+sci+sst)/5
print('The minimum PERCENTAGEshould be: 50')
print("Your PERCENTAGE is: ",per)
if(per>=90):
    print('The GRADE is : A1')
elif(per<=90 and per>=80):print('The GRADE is: A2')
elif(per<=80 and per>=70):print('The GRADE is: B1')
elif(per<=70 and per>=60):print('The GRADE is: B2')
elif(per<=60 and per>=50):print('The GRADE is: C')
else:print('You are FAIL')

"""
name=input('ENTER YOUR NAME: ')
hindi=int(input('Enter marks of hindi: '))
eng=int(input('Enter eng marks: '))
maths=int(input('Enter maths marks: '))
sci=int(input('Enter sci marks: '))
sst=int(input('Enter sst marks: '))
total=hindi+eng+sci+maths+sst
per=total/5
print('Hello Mr.',name)
print('Your percentage is:  ',per)"""
