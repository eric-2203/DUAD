class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    head: Node

    def __init__(self, head=None):
        self.head = head


    def push(self, data):
        node = Node(data, self.head)
        self.head = node

    def pop(self):
        self.head = self.head.next

    def print_info(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node =current_node.next


my_stack = Stack()
my_stack.push("First node")
my_stack.push("Second node")
my_stack.push("Third node")

my_stack.print_info()

print("--- Performing a Pop ---")

my_stack.pop()

my_stack.print_info()