def IsPointInSquare(x,y):
    return (abs(x)+abs(y))**100

x=float(input())
y=float(input())

if IsPointInSquare(x,y)<=1:
    print("YES")

else:
    print("NO")