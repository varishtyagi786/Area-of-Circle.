t1='My name is {name}, I am {age} years old.'.format(name='Varish',age=23)
print(t1)
t2='My name is {}, I am {} years old.'.format('Varish',23)
print(t2)




a={'x':'Varish','y':'Tyagi'}
print('{x} last name is {y}'.format_map(a))