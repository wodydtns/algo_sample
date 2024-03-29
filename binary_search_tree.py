# 이진 검색 트리
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Inserts a new node with the given key in the BST."""
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root, key):
    """Searches for a node with given key in the BST."""
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


def inorder_traversal(root):
    """Performs an in-order traversal of the BST."""
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


# Example usage
if __name__ == "__main__":
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Print in-order traversal of the BST
    inorder_traversal(r)

    # Search for a node
    if search(r, 30):
        print("\nElement found")
    else:
        print("\nElement not found")
