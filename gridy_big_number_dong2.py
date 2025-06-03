n,m,k = map(int,input().split())
number_list = list(map(int,input().split()))
number_list.sort(reverse=True)
first_number = number_list[0]
second_number = number_list[1]
result = 0
while m != 0:
    if m > k:
        for j in range(k):
            if m == 0:
                break
            result += first_number
            m -= 1
    elif m < k:
        for j in range(m):
            if m == 0:
                break
            result += first_number
            m -= 1
    result += second_number
    m -= 1
print(result)

#count = (m // (k + 1)) * k + (m % (k + 1))  # first가 더해지는 총 횟수
#result = count * first + (m - count) * second 이 방법이 더 효율적