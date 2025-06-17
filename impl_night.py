# move = input()
# top = 4
# bottom = 4
# for i in move:
#     if i == "a":
#         top -= 2
#         bottom -= 2
#     elif i == "b":
#         top -= 1
#         bottom -= 1
#     elif i == "g":
#         top -= 1
#         bottom -= 1
#     elif i == "h":
#         top -= 2
#         bottom -= 2
#
#     if i == "1":
#         top = 0
#     elif i == "2":
#         top -= 2
#     elif i == "7":
#         bottom -= 1
#     elif i == "8":
#         bottom -= 2
# print(top + bottom)

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1
print(ord(input_data[0]),int(ord('a')))
result = 0
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

for step in steps:
    next_row = step[0] + row
    next_column = step[1] + column
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)