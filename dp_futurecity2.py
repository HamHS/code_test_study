n,m = map(int,input().split())
inf = float("inf")

graph = [[inf] * (n+1) for i in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X,K = map(int,input().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[k][j]+graph[i][k])
if graph[K][1] + graph[X][K] != inf:
    print(graph[K][1] + graph[X][K])
else:
    print(-1)