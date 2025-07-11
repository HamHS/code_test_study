INF = float("inf")

n = int(input())
m = int(input())
#2차원 그래프를 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는값을 0으로 만듬
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 선에 대한 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],(graph[k][b]+graph[a][k]))

# 결과 출력
for a in range(1,n+1):
    for n in range(1,n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()