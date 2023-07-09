maxVal= float('-inf')
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    global maxVal
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        print(i,j,left,right)
        if left[i] <= right[j]:
            val = left[i] + (right[j] ** 2)
            maxVal = max(maxVal, val)
            merged.append(left[i])
            i += 1
        else:
            val = left[i] + (right[j] ** 2)
            maxVal = max(maxVal, val)
            merged.append(right[j])
            j += 1
        print(merged, maxVal)
        
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged


inp = open('Lab3/Task 2/input2.txt','r')
out = open('Lab3/Task 2/output2.txt','w')

n = int(inp.readline())
arr = list(map(int, inp.readline().strip().split()))

maxS = mergeSort(arr)
print(maxS, maxVal)