import math
def distance(x1,y1,x2,y2):
    a=math.sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)
    return '%.5f'%a


x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(distance(x1,y1,x2,y2))