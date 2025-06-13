def binary_search(array,start,end,target):
    if start > end:
        return False
    mid = (end+start)//2
    if array[mid] == target:
        return mid
    elif target > array[mid]:
        binary_search(array,mid+1,end,target)
    elif target < array[mid]:
        binary_search(array,start,mid-1,target)
    