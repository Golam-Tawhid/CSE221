def divide(arr):
    if len(arr)<=1:
        return arr
    else:
        mid= len(arr)//2
        arr1 = divide(arr[:mid])
        arr2 = divide(arr[mid:])
        print(arr1,arr2)
        return solution(arr1,arr2)

def solution(arr1, arr2):
    global count
    i, j= 0,0
    fin=[]
    while i<len(arr1) or j<len(arr2):
        print(i,j,arr1,arr2)
        if i>= len(arr1):
            fin.extend(arr2[j:])
            count+=1
            j+=1
        
        else:
            if arr1[i] < arr2[j]:
                fin.append(arr[i])
                i+=1

            else:
                fin.append(arr2[j])
                count+=1
                j+=1
    return fin







inp = open('Lab3/Task 1/input1.txt','r')
out = open('Lab3/Task 1/output1.txt','w')
#Lab3/Task 1/input1.txt

n= int(inp.readline())
arr = list(map(int, inp.readline().strip().split()))
count = 0
final= divide(arr)
print(final)
print(count)