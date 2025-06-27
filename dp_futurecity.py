import heapq

n,m = map(int,input().split())
INF = float("inf")
highway = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            highway[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split())
    highway[a][b] = 1
    highway[b][a] = 1

x,z = map(int,input().split())



for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            highway[a][b] = min(highway[a][b],highway[k][b] + highway[a][k])

if highway[1][z] + highway[z][x] != INF:
    print(highway[1][z] + highway[z][x])
else:
    print(-1)






