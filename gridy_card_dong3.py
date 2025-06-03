import sys
input = sys.stdin.read()
n = input.strip().split("\n")
m = []
for i in n:
    m.append(list(map(int,i.split())))
m = m[1:]
minimum = 0
for j in m:
    minimum = max(min(j),minimum) # 이 부분이 포인트 minimum 계속 업데이트 해서 시간,공간 최적화
print(minimum)
