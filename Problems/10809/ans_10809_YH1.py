#https://www.acmicpc.net/problem/10809

def solve():
    s = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for x in alphabet:
        if x in s:
            result.append(s.index(x))
        else:
            result.append(-1)
    print(" ".join(map(str,result)))

def solve2(): #유니코드 이용해서 풀기
    s = input()
    result = [-1]*26 # Alphabet 갯수
    for i in range(len(s)):
        if result[ord(s[i])-ord('a')] == -1: #중복된 문자 skip
            result[ord(s[i])-ord('a')] = i
    for x in result:
        print(x, end = ' ')    
if __name__=="__main__":
    solve2()