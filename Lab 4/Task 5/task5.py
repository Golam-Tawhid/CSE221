from collections import defaultdict, deque

def bfs(grph, strt, dest):
    queue = deque()
    visited = [False] * (len(grph) + 1)
    parent = [0] * (len(grph) + 1)

    queue.append(strt)
    visited[strt] = True

    while queue:
        current = queue.popleft()

        for nhbr in grph[current]:
            if not visited[nhbr]:
                queue.append(nhbr)
                visited[nhbr] = True
                parent[nhbr] = current

    path = []
    while dest != strt:
        path.append(dest)
        dest = parent[dest]
    path.append(strt)

    return path[::-1]

inp = open('Lab 4/Task 5/input5_1.txt','r')
out = open('Lab 4/Task 5/output5_1.txt','w')

n, m, d = map(int, inp.readline().strip().split())

grph = defaultdict(list)
for _ in range(m):
    u, v = map(int, inp.readline().strip().split())
    grph[u].append(v)
    grph[v].append(u)

short_pth = bfs(grph, 1, d)
min_time = len(short_pth) - 1

print("Time:", min_time, file=out)
print("Shortest Path:", *short_pth,file=out)
