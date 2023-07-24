def find_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent, parent[node])
    return parent[node]

def union_sets(parent, size, node1, node2):
    root1 = find_parent(parent, node1)
    root2 = find_parent(parent, node2)

    if root1 != root2:
        if size[root1] >= size[root2]:
            parent[root2] = root1
            size[root1] += size[root2]
        else:
            parent[root1] = root2
            size[root2] += size[root1]

# Read the number of test cases
T = int(input())

for case in range(1, T + 1):
    # Read the number of dual fights
    n = int(input())

    # Initialize disjoint sets and sizes
    parent = [i for i in range(2 * n + 1)]
    size = [1] * (2 * n + 1)

    # Process each dual fight
    for _ in range(n):
        u, v = map(int, input().split())
        union_sets(parent, size, u, v)

    # Find the maximum possible number of Vampires or Lykans
    max_members = max(size)

    # Print the result
    print(f"Case {case}: {max_members}")
