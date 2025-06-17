# import sys
#
# data = int(sys.stdin.read().rstrip())
#
# dp = [0] * max(4,data+1)
# dp[2] = 1
# dp[3] = 1
# for i in range(4,data+1):
#     if i % 2 == 0 and i % 3 == 0:
#         dp[i] = min(dp[i-1],dp[i//2],dp[i//3]) + 1
#     elif i % 2 == 0:
#         dp[i] = min(dp[i-1],dp[i//2]) + 1
#     elif i % 3 == 0:
#         dp[i] = min(dp[i-1],dp[i//3]) + 1
#     else:
#         dp[i] = dp[i-1] + 1
# print(dp[data])


# 이 방법이 더 깔끔함 !
import sys

data = int(sys.stdin.read().rstrip())

dp = [0] * (data+1)
for i in range(2,data+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
print(dp[data])