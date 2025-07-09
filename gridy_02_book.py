data = input()
result = int(data[0])

for i in data[1:]:
    i = int(i)
    if result == 1 or result == 0 or i == 1 or i == 0:
        result += i
    else:
        result *= i
print(result)