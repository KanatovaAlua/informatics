def IsPointInSquare(x,y):
    if x<=1 and x>=-1 and y<=1 and y>=-1:
        return "YES"
    else:
        return "NO"
x=float(input())
y=float(input())
print(IsPointInSquare(x,y))

