import sys

data = sys.stdin.read().rstrip().split("\n")
n,m = int(data[0].split()[0]), int(data[0].split()[1])
data_lines = [int(i) for i in data[1:]]

dp = [float("inf")] * 10001
# for i in data_lines:
#     dp[i] = 1
# for i in range(1,m+1):
#     for j in data_lines:
#         if i - j in data_lines or dp[i-j] != float("inf"):
#             dp[i] = min(dp[i],dp[i-j]+1)

# # 책에서 나타낸 정답. 조금 더 간결하고 가독성이 좋으며 효율적임.
# dp[0] = 0
# for i in range(n):
#     for j in range(data_lines[i],m+1):
#         if dp[j-data_lines[i]] != float("inf"):
#             dp[j] = min(dp[j],dp[j-data_lines[i]]+1)

if dp[m] == float("inf"):
    dp[m] = -1
print(dp[m])