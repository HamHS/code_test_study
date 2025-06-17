import sys

data = sys.stdin.read().rstrip().split("\n")
N = int(data[0])
M = int(data[2])
n_list = list(map(int,data[1].split()))
m_list = list(map(int,data[3].split()))

# # 집합 자료형
# # for i in m_list:
# #   if i in n_list:
# #       print("Yes")
# #   else: print("No") 라는 쉬운 방법이 있지만, 데이터가 천만개 이상일 경우가 있으니
# #   배운 탐색법(이진탐색,트리탐색)으로 풀어 보자.
## 이진 탐색
# def find_part(array,target,start,end):
#     if start > end:
#         return print("No")
#     mid = (start+end) // 2
#     if array[mid] == target:
#         return print("Yes")
#     elif target > array[mid]:
#         find_part(array, target, mid+1, end)
#     else:
#         find_part(array, target, start, mid-1)
#
#
# n_list.sort()
# m_list.sort()
#
# for num in m_list:
#     find_part(n_list,num,0,N)

# # 계수 정렬
# parts = [False] * 10001
# for i in n_list:
#     parts[i] = True
# # for i in input().split():
# #   array[int(i)] = True 형식으로 입력과 동시에 변환도 가능
# for i in m_list:
#     if parts[i]:
#         print("Yes")
#     else:
#         print("No")

