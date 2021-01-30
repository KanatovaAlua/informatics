x=int(input())
a="The next number for the number {0} is {1}."
b="The previous number for the number {0} is {1}."
print(a.format(x, x+1))
print(b.format(x, x-1))
