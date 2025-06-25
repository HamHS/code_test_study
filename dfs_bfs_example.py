from collections import deque

# def dfm(graph,start,visited):
#     print(start,end=" ")
#     visited[start] = True
#     for i in graph[start]:
#         if not visited[i]:
#             visited[i] = True
#             dfm(graph,i,visited)
#
# result = ""
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited = [False] * 9
# dfm(graph,1,visited)



def bfm(graph,start,visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
bfm(graph,1,visited)