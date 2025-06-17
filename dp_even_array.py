import sys

data = sys.stdin.read().rstrip().split("\n")
N = int(data[0])
food_ware = [int(i) for i in data[1].split()]

dp = [0] * (N+1)
dp[0] = food_ware[0]
dp[1] = max(food_ware[1],food_ware[0])
for i in range(2,N):
    dp[i] = max(dp[i-1],dp[i-2]+food_ware[i])

print(dp[N-1])