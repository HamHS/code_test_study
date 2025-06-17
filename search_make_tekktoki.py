import sys

data = sys.stdin.read().rstrip().split("\n")
data[0].split()
N, M = map(int, data[0].split())
rices = list(map(int, data[1].split()))

start = 0
end = max(rices)

result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for i in rices:
        if i > mid:
            total += i - mid
    if total < M:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)


