import math
n=int (input())
for x in range(n+1):
    a=math.factorial(2*x)
    b=math.factorial(x+1)
    c=math.factorial(x)
    d=a//(b*c)
    print(d,end=' ')
