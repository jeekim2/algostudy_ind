# https://www.acmicpc.net/problem/16434

import sys


class Hero:
    def __init__(self):
        self.atk = 0
        self.MaxHp = 0
        self.CurHp = 0

    def reset(self, hp, atk):
        self.atk = atk
        self.MaxHp = hp
        self.CurHp = hp
        return

    def fight(self, enemyHp, enemyAtk):
        HitCnt = self.CurHp // enemyAtk
        AttackCnt = enemyHp // self.atk
        if self.CurHp % enemyAtk != 0:
            HitCnt += 1
        if enemyHp % self.atk != 0:
            AttackCnt += 1
        if AttackCnt <= HitCnt:
            self.CurHp -= enemyAtk * (AttackCnt - 1)
            return True
        else:
            return False

    def heal(self, potionHp, potionAtk):
        self.atk += potionAtk
        self.CurHp += potionHp
        if self.CurHp > self.MaxHp:
            self.CurHp = self.MaxHp
        return


def explore_dungeon(hero: Hero, Rooms):
    for t, atk, hp in Rooms:
        if t == 1:
            if not hero.fight(hp, atk):
                return False
        else:
            hero.heal(hp, atk)
    return True


def solve():
    input = sys.stdin.readline
    N, ATK = map(int, input().split())
    Rooms = tuple(tuple(map(int, input().split())) for _ in range(N))
    hero = Hero()
    MinLimitHp = 1
    MaxLimitHp = 1
    while True:
        hero.reset(MaxLimitHp, ATK)
        if explore_dungeon(hero, Rooms):
            break
        else:
            MinLimitHp = MaxLimitHp
            MaxLimitHp *= 2
    while MaxLimitHp - MinLimitHp > 1:
        CurHp = (MinLimitHp + MaxLimitHp) // 2
        hero.reset(CurHp, ATK)
        if explore_dungeon(hero, Rooms):
            MaxLimitHp = CurHp
        else:
            MinLimitHp = CurHp
    print(MaxLimitHp)
    return


if __name__ == "__main__":
    solve()
