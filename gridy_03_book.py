data = input()
zero = 0
one = 0
temp = data[0]

for j,i in enumerate(data[1:]):
    if temp != i or j == len(data)-2:
        if temp == "0":
            zero += 1
        else:
            one += 1
        temp = i

print(min(zero,one))
