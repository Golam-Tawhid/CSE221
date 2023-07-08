# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = mergeSort(left)
#     right = mergeSort(right)

#     return merge(left, right)

# def merge(left, right):
#     merged = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1

#     while i < len(left):
#         merged.append(left[i])
#         i += 1

#     while j < len(right):
#         merged.append(right[j])
#         j += 1

#     return merged

def findMaxSum(arr):
    # s_arr = mergeSort(arr)
    # print(s_arr)
    maxS = float('-inf')

    for i in range(len(arr) - 2, 0, -1):
        val = arr[i] + (arr[i+1] ** 2)
        maxS = max(maxS, val)

    return maxS

inp = open('Lab3/Task 2/input2.txt','r')
out = open('Lab3/Task 2/output2.txt','w')

N= int(inp.readline())
A = list(map(int, inp.readline().strip().split()))

maxS = findMaxSum(A)
print(maxS, file=out)
