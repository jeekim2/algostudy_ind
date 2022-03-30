class Human:
    def __init__(self, digest):
        self.digest = digest
        self.weight_gain = 0

    def eat(self, calorie):
        self.weight_gain += calorie // self.digest


class Bread:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Inventory:
    def __init__(self):
        self.head = Bread(None)
        self.tail = Bread(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push_left(self, bread_cal):
        new_bread = Bread(bread_cal)
        second_bread = self.head.next
        self.head.next = new_bread
        new_bread.prev = self.head
        new_bread.next = second_bread
        second_bread.prev = new_bread
        self.size += 1

    def push_right(self, bread_cal):
        new_bread = Bread(bread_cal)
        second_bread = self.tail.prev
        self.tail.prev = new_bread
        new_bread.next = self.tail
        new_bread.prev = second_bread
        second_bread.next = new_bread
        self.size += 1

    def pop_left(self):
        if self.size == 0:
            return 0
        target_bread = self.head.next
        self.head.next = target_bread.next
        target_bread.next.prev = self.head
        calorie = target_bread.data
        target_bread.next = None
        target_bread.prev = None
        self.size -= 1
        return calorie

    def pop_right(self):
        if self.size == 0:
            return 0
        target_bread = self.tail.prev
        self.tail.prev = target_bread.prev
        target_bread.prev.next = self.tail
        calorie = target_bread.data
        target_bread.next = None
        target_bread.prev = None
        self.size -= 1
        return calorie

    def get_size(self):
        return self.size


class VendMach:
    def __init__(self, types):
        self.first_inv = Inventory()
        self.second_inv = Inventory()
        self.types = types
        self.typeIdx = 0

    def arrange(self):
        while self.first_inv.get_size() < self.second_inv.get_size():
            self.first_inv.push_right(self.second_inv.pop_left())

    def create_bread(self):
        for _ in range(8):
            if self.first_inv.get_size() + self.second_inv.get_size() < 15:
                self.second_inv.push_right(self.types[self.typeIdx])
                self.arrange()
                self.typeIdx += 1
                if self.typeIdx >= len(self.types):
                    self.typeIdx = 0

    def firstOrder(self):
        self.arrange()
        bread = self.first_inv.pop_left()
        self.arrange()
        return bread

    def midOrder(self):
        self.arrange()
        bread = self.first_inv.pop_right()
        self.arrange()
        return bread

    def __midOrder(self):
        self.arrange()
        bread = self.first_inv.pop_right()
        self.arrange()
        return bread

    def lastOrder(self):
        self.arrange()
        bread = self.second_inv.pop_right()
        self.arrange()
        return bread

    def order(self, type):
        if type == "first":
            return self.firstOrder()
        if type == "last":
            return self.lastOrder()
        if type == "mid":
            return self.__midOrder()
        return 0


def solve():
    T = int(input())
    K = list(map(int, input().split()))
    D = list(map(int, input().split()))
    hong = Human(D[0])
    jay = Human(D[1])
    young = Human(D[2])
    nuri = Human(D[3])
    john = Human(D[4])
    vm = VendMach(K)
    for i in range(T):
        vm.create_bread()
        # hong.eat(vm.order("first"))
        hong.eat(vm.firstOrder())
        jay.eat(vm.order("mid"))
        # jay.eat(vm.__midOrder())
        young.eat(vm.order("last"))
        if i % 2 == 0:
            nuri.eat(vm.order("first"))
        else:
            nuri.eat(vm.order("no"))
        john.eat(vm.order("mid"))
        john.eat(vm.order("last"))

    print(hong.weight_gain)
    print(jay.weight_gain)
    print(young.weight_gain)
    print(nuri.weight_gain)
    print(john.weight_gain)
    return


if __name__ == "__main__":
    solve()
