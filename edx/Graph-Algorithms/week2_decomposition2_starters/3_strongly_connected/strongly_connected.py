import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    result = 0

    adj_rev = [[] for _ in range(len(adj))]
    for node in range(len(adj)):
        for neighbor in adj[node]:
            adj_rev[neighbor].append(node)

    # global variable t, to store finishing times
    t = 0
    # global variable s, for leaders in second pass, current source vertex
    s = 0
    # set leaders to store leaders of each SCC
    leaders = dict()
    visited = [False] * len(adj)
    # record the finishing times of each node
    f = dict()

    def dfs_first_pass(graph, node):
        visited[node] = True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs_first_pass(graph, neighbour)
        nonlocal t
        t += 1
        f[node] = t  # set node's finishing time

    def dfs_second_pass(graph, node):
        visited[node] = True
        leaders[node] = s  # set leader of the node
        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs_second_pass(graph, neighbour)

    # count down
    for i in range(len(adj) - 1, -1, -1):
        if not visited[i]:
            s = i
            dfs_first_pass(adj_rev, i)

    # Sort the f in decreasing order of finishing times
    sorted_desc = dict(sorted(f.items(), key=lambda item: item[1], reverse=True))

    print(f"finishing times: {f}")

    # reset the visited array for the second pass
    visited = [False] * len(adj)
    for key in list(sorted_desc.keys()):
        if not visited[key]:
            s = key
            dfs_second_pass(adj, key)
            result += 1

    return result


if __name__ == "__main__":
    # Apply Kosaraju's algorithm
    input1 = """
        4 4
        1 2
        4 1
        2 3
        3 1
        """
    input2 = """
        5 7
        2 1
        3 2
        3 1
        4 3
        4 1
        5 2
        5 3
        """
    # the below code is just boilerplate to read the input
    data = list(map(int, input2.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
