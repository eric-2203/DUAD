class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head
            
    
    def print_structures(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

fifth_node = Node("Soy el quinto")
fourth_node = Node("Soy el cuarto nodo", fifth_node)
third_node = Node("Soy el tercer nodo", fourth_node)
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structures()