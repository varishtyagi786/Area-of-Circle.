"""import os
location = input('ENTER PATH  ')
result=os.walk(location)
readable_result=[x for x in result]
print(readable_result)
folders=0
files=0
for x in readable_result:
    folders+=len(x[1])
    files+=len(x[-1])
print(f"FOLDERS-->{folders}\nFILES-->{files}")"""

import os
location = input('ENTER PATH  ')
term=input('ENTER A TERM: ')
result=os.walk(location)
readable_result=[x for x in result]
files_names=[]
for x in readable_result:
    for y in x[-1]:
        if term.lower() in y.lower():
            files_names.append(y)
for x in files_names:
    print(x)
print(f'TOTAL FILES ARE : {len(files_names)}')