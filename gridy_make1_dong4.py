n,k = map(int,input().split())
count = 0
while n > 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

# while True:
#     target = (n//k) * k
#     count += (n-target)
#     while target > 1:
#         target //= k
#         count += 1
#     if target < 2:
#         break
#print(count)
# 몫과 나머지를 이용한 방식.
