# https://www.acmicpc.net/problem/1655

import sys


class Heap:
    def __init__(self):
        self.data = [0]
        self.size = 0

    def pop(self):
        self.size -= 1
        if self.size > 0:
            res = self.data[1]
            self.data[1] = self.data.pop()
            self.heapify(1)
            return res
        return self.data.pop()

    def push(self, data):
        self.size += 1
        self.data.append(data)
        target = self.size
        while target != 1 and self.priorChk(target):
            target = target // 2

    def top(self):
        return self.data[1]


class MaxHeap(Heap):
    def heapify(self, idx):
        leftLeaf = idx * 2
        rightLeaf = idx * 2 + 1
        bigest = idx
        if self.size >= leftLeaf and self.data[bigest] < self.data[leftLeaf]:
            bigest = leftLeaf
        if self.size >= rightLeaf and self.data[bigest] < self.data[rightLeaf]:
            bigest = rightLeaf

        if bigest != idx:
            self.data[idx], self.data[bigest] = self.data[bigest], self.data[idx]
            self.heapify(bigest)

    def priorChk(self, target):
        parent = target // 2
        if self.data[parent] >= self.data[target]:
            return False
        self.data[parent], self.data[target] = self.data[target], self.data[parent]
        return True


class MinHeap(Heap):
    def heapify(self, idx):
        leftLeaf = idx * 2
        rightLeaf = idx * 2 + 1
        smalst = idx
        if self.size >= leftLeaf and self.data[smalst] > self.data[leftLeaf]:
            smalst = leftLeaf
        if self.size >= rightLeaf and self.data[smalst] > self.data[rightLeaf]:
            smalst = rightLeaf

        if smalst != idx:
            self.data[idx], self.data[smalst] = self.data[smalst], self.data[idx]
            self.heapify(smalst)

    def priorChk(self, target):
        parent = target // 2
        if self.data[parent] <= self.data[target]:
            return False
        self.data[parent], self.data[target] = self.data[target], self.data[parent]
        return True


def solve():
    input = sys.stdin.readline
    N = int(input())
    overMid = MinHeap()
    underMid = MaxHeap()
    for _ in range(N):
        t = int(input())
        if underMid.size == 0:
            underMid.push(t)
        elif overMid.size >= underMid.size:
            if t <= overMid.top():
                underMid.push(t)
            else:
                underMid.push(overMid.pop())
                overMid.push(t)
        else:
            if underMid.top() < t:
                overMid.push(t)
            else:
                overMid.push(underMid.pop())
                underMid.push(t)
        print(underMid.top())

    return


if __name__ == "__main__":
    solve()
