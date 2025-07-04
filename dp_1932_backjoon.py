import sys

data = sys.stdin.read().rstrip().split("\n")
n = int(data[0])
data_list = [list(map(int,i.split())) for i in data[1:]]

dp = [[0] * (i+1) for i in range(n)]
dp[0] = data_list[0]

for i in range(1,n):
    for j in range(i+1):
        if j-1 < 0:
            dp[i][j] = dp[i - 1][j] + data_list[i][j]
        elif j + 1 > i:
            dp[i][j] = dp[i-1][j-1] + data_list[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + data_list[i][j]

print(max(dp[n-1]))