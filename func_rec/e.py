def IsPointInCircle(x,y,xc,yc,r):
    return (abs(x-xc))**2+(abs(y-yc))**2
x=float(input())
y=float(input())
xc=float(input())
yc=float(input())
r=float(input())
if IsPointInCircle(x,y,xc,yc,r)<=r**2:
    print("YES")
else:
    print("NO")