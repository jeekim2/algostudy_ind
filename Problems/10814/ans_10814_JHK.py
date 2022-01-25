    # https://www.acmicpc.net/problem/10814

    import sys


    def merge(left, right):
        leftIdx = 0
        rightIdx = 0
        res = []
        while leftIdx < len(left) and rightIdx < len(right):
            if left[leftIdx][0] <= right[rightIdx][0]:
                res.append(left[leftIdx])
                leftIdx += 1
            else:
                res.append(right[rightIdx])
                rightIdx += 1
            # 실수했던 내용 - else 구문에서 순서가 꼬여버림.
            # if left[leftIdx][0] < right[rightIdx][0]:
            #     res.append(left[leftIdx])
            #     leftIdx += 1
            # elif left[leftIdx][0] > right[rightIdx][0]:
            #     res.append(right[rightIdx])
            #     rightIdx += 1
            # # else:
            #     res.append(left[leftIdx])
            #     res.append(right[rightIdx])
            #     leftIdx += 1
            #     rightIdx += 1

        while leftIdx < len(left):
            res.append(left[leftIdx])
            leftIdx += 1
        while rightIdx < len(right):
            res.append(right[rightIdx])
            rightIdx += 1

        return res


    def mergeSort(data):
        if len(data) < 2:
            return data
        return merge(mergeSort(data[: len(data) // 2]), mergeSort(data[len(data) // 2 :]))


    def solve():
        input = sys.stdin.readline
        N = int(input())
        InData = []
        for _ in range(N):
            age, name = input().split()
            InData.append(tuple([int(age), name]))
        ret = mergeSort(InData)

        for r in ret:
            print(f"{r[0]} {r[1]}")
        return


    if __name__ == "__main__":
        solve()
