class Node:

    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

class BinaryTree:
    def __init__(self, main=None):
        self.main = main

    def add_node(self, data):
        print(f"Adding: {data}")
        node = Node(data)

        if self.main is None:
            self.main = node
            print("Main node has been assigned")
            return

        current_node = self.main
        while current_node is not None:
            if node.data < current_node.data:
                if current_node.left is None:
                    current_node.left = node
                    print(f"{data} has been added to the left of {current_node.data}")
                    break
                current_node = current_node.left

            elif node.data > current_node.data:
                if current_node.right is None:
                    current_node.right = node
                    print(f"{data} has been added to the right of {current_node.data}")
                    break
                current_node = current_node.right

    def print_info(self, node=None):
        if node is None:
            node = self.main

        if node.left is not None:
            self.print_info(node.left)

        print(f"Node data: {node.data}")

        if node.right is not None:
            self.print_info(node.right)

    def print_structure(self, node=None, parent=None, direction="Main"):
        if node is None:
            node = self.main

        if parent is None:
            print(f"{direction}: {node.data}")
        else:
            print(f"{direction} of {parent.data}: {node.data}")

        if node.left is not None:
            self.print_structure(node.left, node, "Left")

        if node.right is not None:
            self.print_structure(node.right, node, "Right")



my_tree = BinaryTree()
my_tree.add_node(50)
my_tree.add_node(20)
my_tree.add_node(70)
my_tree.add_node(80)

print("Binary tree has been created. Printing nodes: ")

my_tree.print_structure()