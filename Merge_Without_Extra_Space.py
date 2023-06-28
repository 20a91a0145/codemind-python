t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    print(*sorted(p+q))