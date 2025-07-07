import sys

data = list(map(int, sys.stdin.read().rstrip().split("\n")))

T = data[0]


dp = [[0] * 3 for i in range(max(4,T+1))]

dp[1][1] = data[1]
dp[1][2] = data[1]
if T > 1:
    dp[2][1] = data[1] + data[2]
    dp[2][2] = data[2]

for i in range(3, T+1):
    dp[i][1] = dp[i - 1][2] + data[i]
    dp[i][2] = max(dp[i - 2]) + data[i]

print(max(dp[T]))

# 출력 제한 ( 숫자의 범위 ) 마지막에 확인 하기