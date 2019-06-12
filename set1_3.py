a=int(input())
n=a
reverse=0
while(n!=0):
    b=n%10
    reverse=reverse*10+b
    n=n//10
print(reverse)
