x=float(input())
integer=int(x)
x=int((x-int(x))*100)
if x>=50:
    print(integer+1)
else:
    print(integer)