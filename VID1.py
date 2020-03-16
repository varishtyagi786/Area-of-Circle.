vid=input('Do you have VID card (Yes/No)')
if vid.strip().casefold()=='yes':
    age=int(input('Enter your age: '))
    if age>=18:print('You can vote.')
    else:print('You are not eligible for vote')
elif vid.strip().casefold()=='no':
    print('You can not vote. If you want to vote then please bring your VID')
else:print('Invalid Choice')