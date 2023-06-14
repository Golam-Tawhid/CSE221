inp = open('Lab 2/Task 1/input1.txt','r')
output_file = open('Lab 2/Task 1/input1.txt','w')

n,num=map(int, inp.readline().strip().split())

n_list=list(map(int, inp.readline().strip().split()))
print(n_list)

dict= {}
for i in range(n):
    if(dict.get(n_list[i])):
        dict[n_list[i]].append(i)
    else:
        dict[n_list[i]] = [i]
    # dict.append([n_list[i],i+1])
print(dict)
n_list.sort()

l,r= 0, n-1

while l<r:
    if n_list[l]+n_list[r]==num:
        print(dict[n_list[l]]+1,dict[n_list[r]]+1, file=output_file)
        break
    elif n_list[l]+n_list[r]>num:
        r-=1
    else:
        l+=1
