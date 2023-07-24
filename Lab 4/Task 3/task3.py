from collections import defaultdict

def dfs(graph, start):
    visited = [False] * (len(graph) + 1)
    stack = [start]
    dfsPth = []

    while stack:
        vrtx = stack.pop()
        if not visited[vrtx]:
            dfsPth.append(vrtx)
            visited[vrtx] = True

            for nhbr in graph[vrtx][::-1]:
                if not visited[nhbr]:
                    stack.append(nhbr)

    return dfsPth


inp = open('Lab 4/Task 3/input3_2.txt','r')
out = open('Lab 4/Task 3/output3_2.txt','w')

n, m = map(int, inp.readline().strip().split())


graph = defaultdict(list)
for i in range(m):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

dfs_traversal = dfs(graph, 1)

print(*dfs_traversal,file=out)
