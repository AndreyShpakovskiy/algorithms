from Node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert_node(self, root, element):
        if self.root is None:
            self.root = Node(element)
        else:

            if root is None:
                root = Node(element)
            elif root.data <= element:
                root.right = self.insert_node(root.right, element)
            elif root.data > element:
                root.left = self.insert_node(root.left, element)

        return root

    def print(self):
        if self.root is not None:
            self._print(self.root, 0)

    def _print(self, node, level):
        if node is not None:
            self._print(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self._print(node.right, level + 1)

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def pre_order(self, root):
        if root is not None:
            print(root.data)
            if root.left is not None:
                self.pre_order(root.left)
            if root.right is not None:
                self.pre_order(root.right)

    def post_order(self, root):
        if root is not None:
            if root.left is not None:
                self.pre_order(root.left)
            if root.right is not None:
                self.pre_order(root.right)
            print(root.data)

    def find(self, data):
        if self.root is None:
            return None
        else:
            return self._find(data, self.root)

    def _find(self, data, node):
        if data == node.data:
            print(node.data)
        elif data < node.data and node.left is not None:
            self._find(data, node.left)
        elif data > node.data and node.right is not None:
            self._find(data, node.right)
        else:
            print(node.data)
