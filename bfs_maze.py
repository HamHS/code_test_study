import sys
from collections import deque

read_lines = sys.stdin.read().strip().split()
n, m = int(read_lines[0]), int(read_lines[1])
maze = read_lines[2:]
graph = [list(map(int, list(row))) for row in maze]


def bfs(x, y):
    queue = deque([(x, y)])
    move_patten = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        x, y = queue.popleft()

        for dx, dy in move_patten:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return print(graph[n - 1][m - 1])

bfs(0, 0)