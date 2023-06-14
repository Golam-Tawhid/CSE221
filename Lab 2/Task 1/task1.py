inp= open('Lab 2/Task 1/input1.txt','r')
output_file= open('Lab 2/Task 1/input1.txt','w')

n,num=map(int, inp.readline().strip().split())

n_list=list(map(int, inp.readline().strip().split()))
d=0
for i in range(n):
    for j in range(i,n-1):
        if n_list[i]+n_list[j]==num and i!=j:
            print(i+1,j+1, file=output_file)
            d+=1
            break
if d==0:
    print("IMPOSSIBLE", file=output_file)

output_file.close()