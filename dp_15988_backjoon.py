import sys

data = sys.stdin.read().rstrip().split("\n")
n = int(data[0])
data = data[1:]
data_list = []
for j in data:
    data_list.append(list(map(int, j.strip().split())))

result = 0

dp = [[0,0,0] for _ in range(n)]
dp[0][int(data_list[0].index(min(data_list[0])))] = min(data_list[0])
result += min(data_list[0])
min_index = int(data_list[0].index(min(data_list[0])))
for k in range(1,n):
    data_list[k][min_index] = float("inf")
    dp[k][int(data_list[k].index(min(data_list[k])))] = min(data_list[k])
    min_index = int(data_list[k].index(min(data_list[k])))
    result += min(data_list[k])
print(dp)