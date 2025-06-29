import sys

data = list(map(int,sys.stdin.read().rstrip().split("\n")))
T = data[0]
test_list = data[1:]
max_number = max(test_list)
dp = [0] * max(6,(max_number + 1))
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6,max_number+1):
    dp[i] = dp[i-1] + dp[i-5]

for j in test_list:
    print(dp[j])

# range 할때 마지막 범위는 포함하지 않음으로 +1 붙히기. 이 값을 포함 하나 안하나 한번 더 생각하기.