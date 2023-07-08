def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1


# Read input
inp = open('Lab3/Task 3/input3.txt','r')
out = open('Lab3/Task 3/output3.txt','w')

N= int(inp.readline())
numbers = list(map(int, inp.readline().strip().split()))


sorted=quickSort(numbers, 0, N - 1)

# Print the sorted list
print(*numbers, file=out)
