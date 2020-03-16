
hindi = int(input("HINDI  "));
english = int(input("ENGLISH  "));
maths = int(input("MATHS  "));
science = int(input("SCIENCE"  ));
history = int(input("HISTORY"));
sum = hindi + english + maths + science + history;
average = sum/5;
if(average>=91 and average<=100):
  	print("Your Grade is A+");
elif(average>=81 and average<=90):
   	print("Your Grade is A");
elif(average>=71 and average<=80):
   	print("Your Grade is B+");
elif(average>=61 and average<=70):
   	print("Your Grade is B");
elif(average>=51 and average<=60):
   	print("Your Grade is C+");
elif(average>=41 and average<=50):
   	print("Your Grade is C");
elif(average>=0 and average<=40):
   	print("Your Grade is F");
else:
   	print("Strange Grade..!!");
