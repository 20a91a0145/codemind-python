n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
t=int(input())
c=0
for i in range(len(l)):
    if l[i]<=t:
        c+=1
    else:
        c+=2
print(c)

    
    