n=int(input())
s=0
prod=1
n1=n
while (n>0):
    b=n%10
    s=s+b
    prod=prod*b
    n=n//10
if(s==prod):
    print('Spy Number')
else:
    print('Not Spy Number')