# https://www.acmicpc.net/problem/1181
# 문제 : 알파벳 소문자로 이루어진 N개의 단어가 들어올 경우, 아래 조건에 따라 정렬
# (1) 길이가 짧은 것부터, (2) 길이가 같으면 사전 순으로
# 입력 : 첫줄 = 단어 개수 N, 둘째 줄= N개의 소문자 단어
# 추력 : 초전에 따라 정렬하는 단어 출력

N = int(input())
List = []

for _ in range(N):
    List.append(input())

########################################시간 초과됨###########################
# for i in range(N):
#     for j in range(i+1,N):
#         if len(List[i])>len(List[j]):
#             List[i],List[j] = List[j],List[i]
#         elif len(List[i])==len(List[j]) and List[i] > List[j]:
#             List[i],List[j] = List[j],List[i]


List = list(set(List)) #중복제거
List.sort() #알파벳순
List.sort(key=len)  #길이순
for i in List:
    print(i, end ="\n")