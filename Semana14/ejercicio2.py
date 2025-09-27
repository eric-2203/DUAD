class Node:
    data: str
    next: "Node"
    tail: "Node"

    def __init__(self, data, next=None, tail=None):
        self.data = data
        self.next = next
        self.tail = tail

class Deque:
    def __init__(self, head=None, last=None):
        self.head = head
        self.last = last

    def push_left(self, data):
        node = Node(data, self.head)
        if self.head is not None:
            self.head.tail = node

        self.head = node

        if self.last is None:
            self.last = node

    def push_right(self, data):
        node = Node(data, None, self.last)
        if self.last is not None:
            self.last.next = node
        
        self.last = node

        if self.head is None:
            self.head = node

    def is_empty(self):
        try: 
            if self.head is None:
                raise IndexError
            elif self.last is None:
                raise IndexError
        except IndexError:
            print("Stack is empty.")

    def pop_left(self):
        if self.head is None:
            print("Deque is empty")
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.tail = None
            else:
                self.last = None

    def pop_right(self):
        if self.last is None:
            print("Deque is empty")
        else:
            self.last = self.last.tail
            if self.last is not None:
                self.last.next = None
            else:
                self.head = None

    def print_info(self):
        first_node = self.head
        while (first_node is not None):
            print(first_node.data)
            first_node = first_node.next


my_deque = Deque()

my_deque.is_empty()