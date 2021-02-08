x=input()
if x.count('f')==0:
    pass
elif x.count('f')==1:
    print(x.find('f'))
elif x.count('f')>1:
    print(x.find('f'), x.rfind('f'))
