inp = open('Lab 2/Task 1/input1.txt','r')
output_file = open('Lab 2/Task 1/output1.txt','w')

n,num=map(int, inp.readline().strip().split())

n_list=list(map(int, inp.readline().strip().split()))

dict= {}

for i,val in enumerate(n_list):
    a= num - val
    if a in dict:
        b= dict[a]
        print(b+1, i+1, file= output_file)
        output_file.close()
        inp.close()
        exit(0)

    dict[val]=i
    
print('IMPOSSIBLE', file=output_file)
output_file.close()