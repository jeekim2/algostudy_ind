class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        dummy = Node("Dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.before = None
        self.Num_data = 0

    # Adding
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.Num_data += 1

    # delete
    def delete(self):
        pop_data = self.current.data
        if self.current == self.tail:
            self.tail = self.before
        self.before.next = self.current.next
        self.current = self.before
        self.Num_data -= 1
        return pop_data

    # Search
    def first(self):
        if self.Num_data == 0:
            return None
        self.before = self.head
        self.current = self.head.next

        return self.current.data

    def next(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next

        return self.current.data

    # Modify
    def insert(self, data):
        if self.current != None:
            new_node = Node(data)
            new_node.next = self.current.next
            self.current.next = new_node
