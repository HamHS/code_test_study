# 논리적 구조화는 거의 성공하였으나, 마무리가 미흡 또한 구현 단계에서 애를먹음. 실력이 부족함. 좀 더 풀어볼것.
# i번째가 마지막일때의 최댓값을 갱신하는것을 떠올렸으나, 구현방법을 몰라 포기하여 틀림.
# 시간에 집착하여 피로감을 무시함. -> 체력과 시간분배, dp 문제를 더 풀어 볼 것
import sys

data = sys.stdin.read().rstrip().split("\n")
n= int(data[0])
data_lines = [int(i) for i in data[1].split()]

dp = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if data_lines[j] < data_lines[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))