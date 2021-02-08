x=int(input())
i=0
h=0
while 2**i<=x:
    if 2**i==x:
        h=1
        break
    i+=1

if h==1:
    print("YES")

else:
    print("NO")