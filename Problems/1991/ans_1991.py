# https://www.acmicpc.net/problem/1991

# 일단은 dictionary로 풀었는데, 이진트리 class로 풀어봐야겠다.

# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
# 자식 노드가 없는 경우에는 .으로 표현한다.
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.


def preorder(root):
    # 전위순회
    global tree
    print(root, end="")
    if tree[root][0]:
        preorder(tree[root][0])
    if tree[root][1]:
        preorder(tree[root][1])
    return


def inorder(root):
    # 중위순회
    global tree

    if tree[root][0]:
        inorder(tree[root][0])
    print(root, end="")
    if tree[root][1]:
        inorder(tree[root][1])

    return


def postorder(root):
    # 후위순회
    global tree

    if tree[root][0]:
        postorder(tree[root][0])
    if tree[root][1]:
        postorder(tree[root][1])
    print(root, end="")
    return


def solve():
    N = int(input())
    global tree
    tree = {}

    for _ in range(N):
        root, left, right = map(str, input().split())
        if left == ".":
            left = None
        if right == ".":
            right = None
        tree[root] = [left, right]

    preorder("A")
    print()
    inorder("A")
    print()
    postorder("A")
    print()
    return


if __name__ == "__main__":
    solve()
