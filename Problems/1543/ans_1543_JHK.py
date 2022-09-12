# https://www.acmicpc.net/problem/1543


def catch_word(start, Sentence, Word):
    for idx in range(len(Word)):
        if Word[idx] != Sentence[start + idx]:
            return False
    return True


def solve():
    Sentence = input()
    Word = input()
    i = 0
    cnt = 0
    while i <= len(Sentence) - len(Word):
        if Sentence[i] == Word[0]:
            if catch_word(i, Sentence, Word):
                cnt += 1
                i += len(Word)
                continue
        i += 1
    print(cnt)
    return


if __name__ == "__main__":
    solve()
