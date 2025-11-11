# Stack: LIFO (Last in First Out) data structure implementation
from typing import Optional

# Directed graph representation using adjacency list
G: dict[int, list[int]] = {0: [1, 2], 1: [2], 2: [3], 3: []}


def dfs_reach(
    G: dict[int, list[int]], s: int
) -> tuple[set[int], dict[int, int | None]]:
    visited: set[int] = set()
    parent: dict[int, Optional[int]] = {s: None}

    def dfs(u: int) -> None:
        # 1) mark u as visited
        visited.add(u)
        # 2) for each v in G(u) , if v not visited: dfs(v)
        for v in G[u]:
            if v not in visited:
                parent[v] = u  # record tree edges u -> v
                dfs(v)

    dfs(s)
    return visited, parent


# quick checks
# print(dfs_reach(G, 0))  # expect {0,1,2,3}
# print(dfs_reach(G, 1))  # expect {1,2,3}
# print(dfs_reach(G, 3))  # expect {3}


def reconstruct_path(parent: dict[int, Optional[int]], t: int) -> list[int]:
    if t not in parent:  # unreachable from source
        return []
    path = []
    cur = t
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


# Try from source 0
visited, parent = dfs_reach(G, 0)
print("visited:", visited)  # expect {0,1,2,3}
print("parent:", parent)  # e.g., {0:None, 1:0, 2:0 or 1, 3:2}
print("path 0->3:", reconstruct_path(parent, 3))  # expect a valid path like [0,2,3]

# Try from source 1
visited1, parent1 = dfs_reach(G, 1)
print("visited from 1:", visited1)  # expect {1,2,3}
print("path 1->3:", reconstruct_path(parent1, 3))  # expect [1,2,3]
print("path 1->0:", reconstruct_path(parent1, 0))  # expect [] (unreachable)
