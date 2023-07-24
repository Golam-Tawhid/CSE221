from collections import defaultdict, deque

def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = deque()
    bfsPth = []

    queue.append(start)
    visited[start] = True

    while queue:
        vrtx = queue.popleft()
        bfsPth.append(vrtx)

        for nhbr in graph[vrtx]:
            if not visited[nhbr]:
                queue.append(nhbr)
                visited[nhbr] = True

    return bfsPth

inp = open('Lab 4/Task 2/input2_2.txt','r')
out = open('Lab 4/Task 2/output2_2.txt','w')

n, m = map(int, inp.readline().strip().split())

graph = defaultdict(list)
for i in range(m):
    u, v = map(int, inp.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

bfs = bfs(graph, 1)
print(*bfs,file=out)
