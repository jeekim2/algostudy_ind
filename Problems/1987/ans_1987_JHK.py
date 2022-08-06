# https://www.acmicpc.net/problem/1987

import sys


def get_num(character):
    return ord(character) - ord("A")


def explore_tiles(Tiles, R, C, is_not_visited, idx):
    is_not_visited[get_num(Tiles[idx])] = False
    x, y = idx % C, idx // C
    addCnt = 0
    if x > 0:
        target_idx = idx - 1
        if is_not_visited[get_num(Tiles[target_idx])]:
            addCnt = max(addCnt, explore_tiles(Tiles, R, C, is_not_visited, target_idx))
    if x < C - 1:
        target_idx = idx + 1
        if is_not_visited[get_num(Tiles[target_idx])]:
            addCnt = max(addCnt, explore_tiles(Tiles, R, C, is_not_visited, target_idx))
    if y > 0:
        target_idx = idx - C
        if is_not_visited[get_num(Tiles[target_idx])]:
            addCnt = max(addCnt, explore_tiles(Tiles, R, C, is_not_visited, target_idx))
    if y < R - 1:
        target_idx = idx + C
        if is_not_visited[get_num(Tiles[target_idx])]:
            addCnt = max(addCnt, explore_tiles(Tiles, R, C, is_not_visited, target_idx))
    is_not_visited[get_num(Tiles[idx])] = True
    return addCnt + 1


def solve():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    Tiles = ""
    for _ in range(R):
        Tiles += input().rstrip()
    is_not_visited = [True] * (ord("Z") - ord("A") + 1)
    print(explore_tiles(Tiles, R, C, is_not_visited, 0))
    return


if __name__ == "__main__":
    solve()
