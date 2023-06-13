inp= open('input2.txt','r')
output_file= open('output2.txt','w')

n= inp.readline()
n_list=list(map(int, inp.readline().strip().split()))

m= inp.readline()
m_list=list(map(int, inp.readline().strip().split()))

i,j=0,0

f_list=[]

while i<int(n) and j<int(m):
    if n_list[i]==m_list[j]:
        f_list.append(n_list[i])
        f_list.append(m_list[j])
        i+=1
        j+=1
    elif n_list[i]<m_list[j]:
        f_list.append(n_list[i])
        i+=1
    else:
        f_list.append(m_list[j])
        j+=1
print(f_list)