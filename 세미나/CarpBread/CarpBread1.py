class Human:
    def __init__(self, DF):
        self.digestFacter = DF
        self.weight = 0
        return

    def eat(self, calorire):
        self.weight += calorire // self.digestFacter
        return


class Node:
    def __init__(self, calorie):
        self.calorie = calorie
        self.prev = None
        self.next = None
        return


class Inventory:
    def __init__(self):
        self.HeadNode = Node(None)
        self.TailNode = Node(None)
        self.HeadNode.next = self.TailNode
        self.TailNode.prev = self.HeadNode
        self.__size = 0
        return

    def push_left(self, data):
        NewNode = Node(data)
        NextNode = self.HeadNode.next
        NewNode.next = NextNode
        NewNode.prev = self.HeadNode
        self.HeadNode.next = NewNode
        NextNode.prev = NewNode
        self.__size += 1
        return

    def push_right(self, data):
        NewNode = Node(data)
        NextNode = self.TailNode.prev
        NewNode.prev = NextNode
        NewNode.next = self.TailNode
        self.TailNode.prev = NewNode
        NextNode.next = NewNode
        self.__size += 1
        return

    def pop_left(self):
        if self.__size >= 1:
            TargetNode = self.HeadNode.next
            SecondNode = TargetNode.next
            data = TargetNode.data
            self.HeadNode.next = TargetNode.next
            SecondNode.prev = self.HeadNode
            self.__size -= 1
            return data
        return 0

    def pop_right(self):
        if self.__size >= 1:
            TargetNode = self.TailNode.prev
            SecondNode = TargetNode.prev
            data = TargetNode.data
            self.TailNode.prev = TargetNode.prev
            SecondNode.next = self.TailNode
            self.__size -= 1
            return data
        return 0

    def get_size(self):
        return self.__size
        # private
        # public
        # protected


class VendingMachine:
    def __init__(self, Types):
        self.Types = Types
        self.FirstInv = Inventory()
        self.SecondInv = Inventory()
        self.TypeIdx = 0
        return

    def arrange(self):
        while self.FirstInv.get_size() < self.SecondInv.get_size() + 1:
            self.FirstInv.push_right(self.SecondInv.pop_left())
        return

    def create(self):
        i = 0
        while i < 8:
            if self.FirstInv.get_size() + self.SecondInv.get_size() > 15:
                break
            self.SecondInv.push_right(self.Types[self.TypeIdx])
            self.TypeIdx += 1
            if self.TypeIdx >= len(self.Types):
                self.TypeIdx = 0
            while self.FirstInv.get_size() < self.SecondInv.get_size() + 1:
                self.FirstInv.push_right(self.SecondInv.pop_left())
        return

    def deliverFirst(self):
        data = self.FirstInv.pop_left()
        self.arrange()
        return data

    def deliverLast(self):
        data = self.SecondInv.pop_right()
        self.arrange()
        return data

    def deliverMid(self):
        data = self.FirstInv.pop_right()
        self.arrange()
        return data

    def deliver(self, order):
        if order == "first":
            return self.deliverFirst()
        if order == "last":
            return self.deliverLast()
        if order == "mid":
            return self.deliverMid()
        return 0


def solve():
    T = int(input())

    K = list(map(int, input().split()))
    D = list(map(int, input().split()))

    hong = Human(D[0], order1)
    jay = Human(D[1], order2)
    young = Human(D[2])
    nuri = Human(D[3])
    john = Human(D[4], order5)

    VM = VendingMachine(K)

    for _ in range(T):
        VM.create()
        hong.eat(VM.deliver(hong.order()))
        jay.eat(VM.deliver("mid"))
        young.eat(VM.deliver("last"))

        i = 0
        if i % 2 == 0:
            nuri.eat(VM.deliver("first"))
        i += 1
        john.eat(VM.deliver(john.order()))
        # john.eat(VM.deliver(john.order()))
    # 1. order가 사람에 종속되지않음.
    print(hong.weight)
    print(jay.weight)
    print(young.weight)
    print(nuri.weight)
    print(john.weight)
    return


if __name__ == "__main__":
    solve()
