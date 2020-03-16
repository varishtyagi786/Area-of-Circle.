movies=['DDLJ','HUM SATH','BEWAFA','SANAM','SAUDAGAR','SAU DIN SAAS KE','KHILADI','KHATARNAK','KHATRI','GHAYAL','GHAR','BAGHWAN','BARSAAT','MUNTY','ANGAARE','AURAT']
movies_new=[title for title in movies if title.startswith('B')]
print(movies_new)