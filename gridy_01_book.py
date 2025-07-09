import sys
N = int(input())
data = list(map(int,sys.stdin.read().rstrip().split()))
data = sorted(data)

result = 0
count = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

# 문제를 풀다가 너무 길고 복잡해지면 과감히 처음부터 할 것. 출제자 의도를 다시 생각하기.