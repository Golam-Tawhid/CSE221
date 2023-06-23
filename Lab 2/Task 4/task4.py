def find_max(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    left_max = find_max(arr, low, mid)
    right_max = find_max(arr, mid + 1, high)

    return max(left_max, right_max)

inp = open('Lab 2\Task 4\input4,txt', 'r')
out = open('Lab 2\Task 4\output4.txt', 'w')

n = int(inp.readline().strip())
arr= list(map(int, inp.readline().strip().split()))

max_val = find_max(arr, 0, len(arr) - 1)

print(max_val, file=out)
out.close()