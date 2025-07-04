import sys

data = sys.stdin.read().rstrip().split("\n")
n = int(data[0])
data = data[1:]

data_list = [list(map(int, i.strip().split()))for i in data]

result = 0

dp = [[0]*3 for _ in range(n)]
dp[0] = data_list[0]
for i in range(1,n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + data_list[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + data_list[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + data_list[i][2]
print(min(dp[-1]))

# 다 풀고 문제 다시 읽어 보기
# dp 문제를 잘못 풀어서 그리디로 풀지 말것. min 값 n 번만큼 일일히 탐색하지 말것.
# dp 문제에서 dp 를 너무 자주 초기화 하지 말것.
# 틀린 가장 큰 문제는 국지 최적의 해와 전체 최적의 해가 같지 않음을 인지 하지 못했음. 최솟값만 계속 더하는게 아니라, 다른 경우의 수에서
#>전체값이 최소값이 나올 수 있다는걸 망각함