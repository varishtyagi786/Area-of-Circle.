num=int(input("Enter a number "))
year = num // 365 
num %= 365
week = num//7
num%=7
days = num
print("Years = ",year, "\nWeeks = ",week, "\nDays = ",days) 