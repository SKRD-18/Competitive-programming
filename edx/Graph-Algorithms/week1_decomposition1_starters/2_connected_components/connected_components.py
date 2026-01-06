def number_of_components(adj):
    result = 0
    n = len(adj)  # n = number of vertices
    visited = [False] * n  # Only initialise once

    def dfs(x):
        visited[x] = True  # Mark the starting vertex as explored
        for neighbour in adj[x]:
            if not visited[neighbour]:  # not False = True
                dfs(neighbour)
        return 0  # Dead end

    for i in range(n):
        if not visited[i]:
            dfs(i)
            result += 1

    return result


if __name__ == "__main__":
    input = """
        4 2
        1 2
        3 2
        """

    data = list(map(int, input.strip().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
