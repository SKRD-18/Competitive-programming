import sys


def dfs(adj, used, order, x):
    # 1. Mark current node x as visited (used[x] = 1)
    used[x] = 1
    # 2. Iterate through neighbors of x.
    for neighbour in adj[x]:
        # If a neighbor is NOT visited, call dfs recursively.
        if used[neighbour] == 0:
            dfs(adj, used, order, neighbour)

    # 3. Post order add the current node after visiting all its neighbours (This is the critical step from Phase 1)
    order.append(x)  # this is the answer to the question


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if used[i] == 0:  # if a node is not visited
            dfs(adj, used, order, i)  # run dfs
    return order[::-1]


if __name__ == "__main__":
    input1 = """
        4 3
        1 2
        4 1
        3 1
        """
    input2 = """
        4 1
        3 1 
        """
    input3 = """
        5 7
        2 1
        3 2
        3 1
        4 3
        4 1
        5 2
        5 3
        """

    data = list(map(int, input3.strip().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=" ")
