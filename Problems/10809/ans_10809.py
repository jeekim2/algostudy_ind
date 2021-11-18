# https://www.acmicpc.net/problem/10809
# 문제 : 알파벳 문자로만 이루어진 단어 S가 주어지고, 각 알파펫이 처음 등장하는 위치 출력. 알파벳이 없는 경우, -1 출력

import sys

def solve():
    input = sys.stdin.readline
    words = str(input())
    alphabet = list(map(chr,range(97,123))) # ascii 코드 생성 - chr 사용
    array = []

    # 방법 (1) - index별 비교하기
    for i in range(97,123):        
        if chr(i) in words:
            index_num = words.index(chr(i))
            array.append(index_num)
        else:
            array.append(-1)

    # 방법 (2) - find 함수 사용 (미완성)
#    index_num = words[i].find(str(alphabet))
#    print(index_num)

    print(array)

if __name__ == "__main__":
    solve()