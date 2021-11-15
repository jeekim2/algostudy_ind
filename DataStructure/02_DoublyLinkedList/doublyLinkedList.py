class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        dummy = Node("Dummy")
        self.head = dummy
        self.tail = dummy
        self.current = None
        self.num_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.num_data += 1

    def first(self):
        if self.num_data == 0:
            return None
        self.current = self.head.next  # head is always dummy
        return self.current.data

    def last(self):
        if self.num_data == 0:
            return None
        self.current = self.tail
        return self.current.data

    def next(self):
        if self.current is None and self.num_data != 0:
            return self.first()
        elif self.current == self.tail:
            return None
        self.current = self.current.next
        return self.current.data

    def before(self):
        if self.current is None and self.num_data != 0:
            return self.last()
        self.current = self.current.prev
        if self.current == self.head:
            return None
        return self.current.data

    def popFirst(self):
        if self.num_data == 0:
            return None
        else:
            pop_data = self.first()
            self.current.next.prev = self.head
            self.head.next = self.current.next
            self.current = None
            self.num_data -= 1
            return pop_data

    def popLast(self):
        if self.num_data == 0:
            return None
        else:
            pop_data = self.last()
            self.tail = self.current.prev
            self.tail.next = None
            self.current = None
            self.num_data -= 1
            return pop_data

    def insert(self, data):
        if self.current == None or self.current == self.tail:
            self.append(data)
        else:
            new_node = Node(data)
            new_node.next = self.current.next
            new_node.prev = self.current
            new_node.next.prev = new_node
            self.current.next = new_node
