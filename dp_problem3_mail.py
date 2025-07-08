import heapq

N,M,C = map(int, input().split())

line = [[] for _ in range(N+1)]

visited = [False for _ in range(N+1)]

for _ in range(M):
    X,Y,Z = map(int,input().split())
    line[X].append((Y,Z))

def send(start_number):
    q = []
    heapq.heappush(q, (start_number,0))

    max_time = 0
    total_city = -1

    while q:
        city,send_time = heapq.heappop(q)
        if not visited[city]:
            total_city += 1
        visited[city] = True
        if max_time < send_time:
            max_time = send_time

        for i in line[city]:
            all_dist = send_time + i[1]
            heapq.heappush(q,(i[0],i[1]))
            if max_time < all_dist:
                max_time = all_dist

    print(total_city, max_time)
send(C)