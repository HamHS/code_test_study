import heapq
import sys
input = sys.stdin.readline
INF = float("inf")

# 노드의 개수, 간선의 개수
n,m = map(int,input().split())
# 시작노드 번호
start = int(input())
# 각 노드에 연결된 노드에 대한 정보가 담긴 리스트
graph = [[] for i in range(n+1)]
# 최단거리 테이블 생성
distance = [INF] * (n+1)

# 모든 간선대 대한 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    # a 번 노드에서 b 번 노드로 가는 비용은 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기위해 경로는 0으로 하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now = heapq.heappop(q)

        # 이미 처리된 노드라면 무시.
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 인접노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 걸쳐 거리가 더 짧으면 거리 입력 후 큐에 저장
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])