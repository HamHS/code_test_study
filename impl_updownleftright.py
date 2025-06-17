location = [1,1]
N = int(input())
moves = list(input().split())
for i in moves:
    if i == "L" and location[1] > 2:
        location[1] -= 1
    elif i == "R" and location[1] <= N:
        location[1] += 1
    elif i == "U" and location[0] > 1:
        location[0] -= 1
    elif i == "D" and location[0] < N:
        location[0] += 1
print(*location)

# x,y = 1,1
# dx = [0,0,-1,-1]
# dy = [-1,-1,0,0]
# move_types =["L","R","U","D"]
# 이런식으로 하고
#반복문 중첩 moves + move_types
# if i == move_types[i]:
#     nx = x + dx[i]
#     ny = y + dy[i]
# if nx <1 ...:
#     continue
#범위 벗어날때 무시하는식으로
# x , y = nx, ny