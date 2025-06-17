#sort 1 jsut use sort or understand basic ( ˇ͈ᵕˇ͈ ) ¨̮♡⃛/
# import sys
#
# N  = list(map(int,sys.stdin.read().strip().split()))
# numbers = N[1:]
#
# for i in range(N[0]):
#     for j in range(i + 1, N[0]):
#         if numbers[i] < numbers[j]:
#             numbers[j],numbers[i] = numbers[i],numbers[j]
#
# print(numbers)
#
# # or just use sort. sorted(list,reverse = True)

#sort2 lambda
# import sys
#
# N  = sys.stdin.read().strip().split("\n")
# number_list = [list(map(int, line.split())) for line in N[1:]]
# result = sorted(number_list,key=lambda x:x[1])
# print(result)


# exchange two things ◟( ˘ ³˘)◞
# import sys
#
# lines = sys.stdin.read().strip().split('\n')
# int_lines = [list(map(int, line.split())) for line in lines]
# K = int_lines[0][1]
# first_list = int_lines[1]
# second_list = int_lines[2]
#
# for _ in range(K):
#     a_min_number = min(first_list)
#     b_max_number = max(second_list)
#     if b_max_number > a_min_number:
#         first_list[first_list.index(a_min_number)] = b_max_number
#         second_list[second_list.index(b_max_number)] = a_min_number
#
# print(sum(first_list))

# # I found that index is not important Σ(￣□￣;) so we can use below
# n,k = map(int,input().split())
# first_list = list(map(int, input().split()))
# second_list = list(map(int, input().split()))
#
# first_list.sort()
# second_list.sort(reverse=True)
#
# for i in range(k):
#     if first_list[i] < second_list[i]:
#         first_list[i], second_list[i] = second_list[i], first_list[i]
#     else:
#         break
#
# print(sum(first_list))