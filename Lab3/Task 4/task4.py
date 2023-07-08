def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def findKthSmallest(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    if pivot_index == k - 1:
        return arr[pivot_index]
    elif pivot_index > k - 1:
        return findKthSmallest(arr, low, pivot_index - 1, k)
    else:
        return findKthSmallest(arr, pivot_index + 1, high, k)


# Read input
N = int(input())
numbers = list(map(int, input().split()))
Q = int(input())

# Process queries
for _ in range(Q):
    K = int(input())
    kth_smallest = findKthSmallest(numbers, 0, N - 1, K)
    print(kth_smallest)
