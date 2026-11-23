class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Public method to initiate inorder traversal
    def print_inorder(self):
        print("Inorder Traversal:   ", end="")
        self._inorder(self.root)
        print()

    # Public method to initiate preorder traversal
    def print_preorder(self):
        print("Preorder Traversal:  ", end="")
        self._preorder(self.root)
        print()

    # Public method to initiate postorder traversal
    def print_postorder(self):
        print("Postorder Traversal: ", end="")
        self._postorder(self.root)
        print()

    # Recursive inorder traversal: Left -> Root -> Right
    def _inorder(self, node):
        if node is None:
            return

        self._inorder(node.left)
        print(node.data, end=" ")
        self._inorder(node.right)

    # Recursive preorder traversal: Root -> Left -> Right
    def _preorder(self, node):
        if node is None:
            return

        print(node.data, end=" ")
        self._preorder(node.left)
        self._preorder(node.right)

    # Recursive postorder traversal: Left -> Right -> Root
    def _postorder(self, node):
        if node is None:
            return

        self._postorder(node.left)
        self._postorder(node.right)
        print(node.data, end=" ")


# Main demonstration
if __name__ == "__main__":
    # Create the following binary tree:
    #
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #

    tree = BinaryTree()

    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    # Execute all traversals
    print("--- Tree Traversal Demonstration ---")
    tree.print_inorder()
    tree.print_preorder()
    tree.print_postorder()
    print("------------------------------------")