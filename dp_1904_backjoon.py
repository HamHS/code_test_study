import sys

n = int(sys.stdin.read().rstrip())

if n == 1 :
    print(1)
elif n == 2:
    print(2)
else:
    x, y = 1, 2
    for i in range(3,n+1):
        x, y = y, x+y % 15746
    print(y)
    
# 모듈러 문제. 15746 안나눠줘서 시간초과 + 메모리 부족 뜸. 입출력 조건 잘 읽을 것.