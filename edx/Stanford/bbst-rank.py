tree = [5, 3, 8, 1, 4, 7, 9]


def Rank(root, key):
    """Ranks the nodes in a binary search tree.

    Args:
        root: The root node of the binary search tree.
        key: The key whose rank is to be determined.
    Returns:
        The rank of the key in the binary search tree.
    """
    if root is None:
        return 0
    if key == root:
        return Rank(tree[root] + 1, key)
    if key < root:
        return (
            size(
                tree[root] + 1,
            )
            + 1
            + Rank(tree[root] + 2, key)
        )
