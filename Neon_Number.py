n=int(input())
sqr=n*n
s=0
while sqr>0:
    s=s+sqr%10
    sqr=sqr//10
if (n==s):
    print('Neon Number')
else:
    print('Not Neon Number')