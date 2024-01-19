class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order_traversal(self, node):
        if node:
            # Traverse the left subtree
            self.in_order_traversal(node.left)

            # Print the current node's data
            print(node.data, end=' ')

            # Traverse the right subtree
            self.in_order_traversal(node.right)

    def print_tree(self):
        # Start traversal from the root
        self.in_order_traversal(self.root)


# Example tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

# Print the tree using in-order traversal
tree.print_tree()