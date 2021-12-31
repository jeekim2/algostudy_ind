# https://www.acmicpc.net/problem/1300


def solve():
    N = int(input())
    B = int(input())

    nums = [[], []]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j in nums[0]:
                nums[1][nums[0].index(i * j)] += 1
            else:
                nums[0].append(i * j)
                nums[1].append(1)

    beforeVal = 0
    for i in range(1, N ** 2 + 1):
        if i in nums[0]:
            pos = nums[0].index(i)
            nums[1][pos] += beforeVal
            beforeVal = nums[1][pos]

    # binary search
    ref = sorted(nums[1])
    left = 0
    right = len(ref)
    while right - left > 1:
        mid = (left + right) // 2
        # if ref[mid] == B:
        #     ansIdx = nums[1].index(B)
        #     break
        if ref[mid] >= B:
            right = mid
        else:
            left = mid
    print(nums[0][nums[1].index(ref[right])])
    return


if __name__ == "__main__":
    solve()
