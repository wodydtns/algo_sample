# B Tree
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for the number of keys)
        self.keys = []  # An array of keys
        self.children = []  # An array of child pointers
        self.leaf = leaf  # Is true when the node is leaf. Otherwise false

    def traverse(self):
        """
        A function to traverse all nodes in a subtree rooted with this node
        """
        i = 0
        for i in range(len(self.keys)):
            # If this is not a leaf, then before printing key[i],
            # traverse the subtree rooted with child C[i].
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")

        # Print the subtree rooted with the last child
        if not self.leaf:
            self.children[i + 1].traverse()

    def insertNonFull(self, k):
        """
        A utility function to insert a new key in the subtree rooted with this node.
        The assumption is, the node must be non-full when this function is called
        """
        i = len(self.keys) - 1

        if self.leaf:
            # If this is a leaf node
            self.keys.append(0)
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            # If this node is not leaf
            while i >= 0 and self.keys[i] > k:
                i -= 1

            # See if the found child is full
            if len(self.children[i + 1].keys) == 2 * self.t - 1:
                # If the child is full, then split it
                self.splitChild(i + 1, self.children[i + 1])

                # After split, the middle key of C[i] goes up, and C[i] is split into two.
                # See which of the two is going to have the new key
                if self.keys[i + 1] < k:
                    i += 1
            self.children[i + 1].insertNonFull(k)

    def splitChild(self, i, y):
        """
        A utility function to split the child y of this node. i is the index of y in
        the child array C[]. The Child y must be full when this function is called
        """
        t = self.t
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[: t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def traverse(self):
        """
        The main function that traverses the nodes in a B-Tree
        """
        if self.root is not None:
            self.root.traverse()

    def insert(self, k):
        """
        The main function that inserts a new key in the B-Tree
        """
        root = self.root
        if (
            len(root.keys) == 2 * self.t - 1
        ):  # If root is full, then the tree grows in height
            s = BTreeNode(self.t, False)
            self.root = s
            s.children.insert(0, root)  # Former root becomes the child of new root
            s.splitChild(0, root)  # Split the old root and move 1 key to the new root
            s.insertNonFull(
                k
            )  # New root has two children now, insert new key to appropriate child
        else:
            root.insertNonFull(k)  # If root is not full, call insertNonFull for root


# Example usage
b_tree = BTree(3)  # A B-Tree with minimum degree 3
keys = [10, 20, 5, 6, 12, 30, 7]
