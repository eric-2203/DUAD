class Node:
    data: str
    right: "Node"
    left: "Node"

    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self, main=None):
        self.main = main

    def add_node(self, data):
        node = Node(data)

        if self.main is None:
            self.main = node

        elif self.main is not None:
            if node.data < self.main.data:
                if self.main.left is None:
                    self.main.left = node

            elif node.data > self.main.data:
                if self.main.right is None:
                    self.main.right = node

    def print_info(self):
        first_node = self.main
        print(f"Main node data: {first_node.data}")
        if first_node.left is not None:
            print(f"Left node data: {first_node.left.data}")
        else:
            print("Node is empty")
            
        if first_node.right is not None:
            print(f"Right node data: {first_node.right.data}")
        else:
            print("Node is empty")

my_tree = BinaryTree()
my_tree.add_node(50)
my_tree.add_node(20)
my_tree.add_node(30)


my_tree.print_info()