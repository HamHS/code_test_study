import sys

data = list(map(int,sys.stdin.read().rstrip().split("\n")))
data = data[1:]

MOD = 1000000009
MAX = max(data)
dp = [0] * (MAX + 1)

dp[1] = 1
if MAX > 1:
    dp[2] = 2
if MAX > 2:
    dp[3] = 4

for i in range(4,MAX+1):
    dp[i] = ( dp[i-1] + dp[i-2] + dp[i-3] ) % MOD

for i in data:
    print(dp[i])

# if 조건문 여러줄 전부 거쳐야 하는데 습관적으로 elif 로 씀.
# 처음에 접근은 좋았으나, 테스트 케이스 마다 반복해서 dp를 탐색하고 재정의 함으로 시간도 메모리도 부족하였음.
# 코드의 단순화,경량화를 신경 쓸 것. 또한 기초 문법 실수를 신경 쓸 것. 아무 생각없이 작성 후 넘어가지 말고, 의도를 생각하고 넘어갈 것.