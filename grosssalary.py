name=input("ENTER YOUR NAME  ")
address=input("ENTER YOUR ADDRESS  ")
salary=float(input("ENTER SALARY  "))
basicsalary=float(input("ENTER BASIC SALARY  "))
ods=basicsalary/30
print("One DAY SALARY",basicsalary/30)
tp=int(input("Enter total present"))
print("TOTAL PRESENT  ",tp)
ab=30-tp
sickl=int(input("Total sick leaves: "))

hra = salary*40/100
print("HRA",hra)
da=salary*90/100
print("D.A",da)
ta=salary*10/100
print("T.A",ta)
pf=salary*12/100
print("PF",pf)
grosssalary=ods*(tp+sickl)+hra+da+ta
print("GROSS SALARY",grosssalary)
net=grosssalary-pf
print("NET SALARY",net) 