import sys
from collections import deque
n,m = map(int,input().split())
ice_board = sys.stdin.read().strip().split("\n")
visited = [[False for i in range(m)] for i in range(n)]
iced_drink = 0
def find_zero(board,x,y,visited):
    visited[x][y] = True
    queue = deque([(x, y)])
    while queue:
        x1, y1 = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x1 + dx, y1 + dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == "0" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if ice_board[i][j] == "0" and visited[i][j] == False:
            find_zero(ice_board,i,j,visited)
            iced_drink += 1

print(iced_drink)
