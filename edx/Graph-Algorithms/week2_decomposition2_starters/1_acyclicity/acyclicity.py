import sys

sys.setrecursionlimit(2000)  # max depth of recursion


def acyclic(adj):
    n = len(adj)
    visited = [False] * n  # Only initialise once; global variable

    def dfs(x):
        visited[x] = True  # Mark the starting vertex as explored
        rec_stack.add(x)  # Add to recursion stack
        for neighbour in adj[x]:
            if neighbour in rec_stack:
                return 1  # Found it immediately
            if not visited[neighbour]:  # not False = True
                if dfs(neighbour) == 1:
                    return 1  # Found it deeper in the recursion
        rec_stack.remove(x)  # Remove the last element from recursion stack
        return 0  # Dead end

    for i in range(n):  # loop through all nodes
        if not visited[i]:
            rec_stack = set()
            if dfs(i) == 1:
                return True

    return False


if __name__ == "__main__":
    input = """
        4 4
        1 2
        4 1
        2 3
        3 1
        """

    # this graph has no cycle
    input1 = """
        5 7
        1 2
        2 3
        1 3
        3 4
        1 4
        2 5
        3 5
        """

    data = list(map(int, input1.strip().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
