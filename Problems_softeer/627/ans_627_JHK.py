# https://softeer.ai/practice/info.do?idx=1&eid=627

from ast import Is
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def enqueue(self, data):
        NewNode = Node(data)
        NewNode.next = self.head.next
        NewNode.prev = self.head
        self.head.next = NewNode
        NewNode.next.prev = NewNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return -1
        TarNode = self.tail.prev
        TarNode.prev.next = self.tail
        self.tail.prev = TarNode.prev
        self.size -= 1
        return TarNode.data


def get_idx(h, w):
    return h * W + w


def get_color(h, w):
    return Paint[get_idx(h, w)]


def check_boundary(h, w, defcolor):
    # idx = get_idx(h, w)
    if (
        h > 0
        and Paint[get_idx(h - 1, w)] == defcolor
        and not is_visisted[get_idx(h - 1, w)]
    ):
        queue.enqueue((h - 1, w))
        is_visisted[get_idx(h - 1, w)] = True
    if (
        h < H - 1
        and Paint[get_idx(h + 1, w)] == defcolor
        and not is_visisted[get_idx(h + 1, w)]
    ):
        queue.enqueue((h + 1, w))
        is_visisted[get_idx(h + 1, w)] = True
    if (
        w > 0
        and Paint[get_idx(h, w - 1)] == defcolor
        and not is_visisted[get_idx(h, w - 1)]
    ):
        queue.enqueue((h, w - 1))
        is_visisted[get_idx(h, w - 1)] = True
    if (
        w < W - 1
        and Paint[get_idx(h, w + 1)] == defcolor
        and not is_visisted[get_idx(h, w + 1)]
    ):
        queue.enqueue((h, w + 1))
        is_visisted[get_idx(h, w + 1)] = True


def solve():
    global H, W, Paint, queue, is_visisted
    input = sys.stdin.readline
    H, W = map(int, input().split())
    Paint = []
    for _ in range(H):
        Paint += list(map(int, input().split()))
    Q = int(input())
    cmd = []
    for _ in range(Q):
        cmd.append(tuple(map(int, input().split())))
    queue = Queue()
    for h, w, c in cmd:
        h -= 1
        w -= 1
        is_visisted = [False] * H * W
        queue.enqueue((h, w))
        is_visisted[get_idx(h, w)] = True
        defcolor = get_color(h, w)
        while queue.size != 0:
            h, w = queue.dequeue()
            Paint[get_idx(h, w)] = c
            check_boundary(h, w, defcolor)
    for i, v in enumerate(Paint):
        if i != 0 and i % W == 0:
            print()
        print(v, end=" ")
    return


if __name__ == "__main__":
    solve()
