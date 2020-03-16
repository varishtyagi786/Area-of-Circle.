"""hindi=int(input("Enter marks of the hindi subject: "))
english=int(input("Enter marks of the english subject: "))
maths=int(input("Enter marks of the maths subject: "))
science=int(input("Enter marks of the science subject: "))
SSt=int(input("Enter marks of the SSt subject: "))
avg=(hindi+english+maths+science+SSt)/5
print('Average is: ',avg)
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
elif(avg>=50 and avg<60):
    print("Grade: E")
else:print('Result Fail')"""




name=input('Enter your name: ')
print('Please enter your marks in CGPA')
hindi=float(input('Enter Hindi marks: '))
english=float(input('Enter English marks: '))
math=float(input('Enter Maths marks: '))
sci=float(input('Enter Science marks: '))
sst=float(input('Enter S.St marks: '))
total=hindi+english+math+sci+sst
print('Hi',name,', Your Total Grade is: ',total*2/10)
print('Percentage is : ',total/5*9.5)
print('Total Marks is: ',total*9.5)
