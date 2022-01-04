A = int(input())
B = int(input())
C = int(input())
Ans = A*B*C
List=[]
List = str(Ans)
cnt_0 = 0
cnt_1 = 0
cnt_2 = 0
cnt_3 = 0
cnt_4 = 0
cnt_5 = 0
cnt_6 = 0
cnt_7 = 0
cnt_8 = 0
cnt_9 = 0

for i in range(0,len(List)):
    if List[i]=='0':
        cnt_0= cnt_0+1
    if List[i]=='1':
        cnt_1= cnt_1+1
    if List[i]=='2':
        cnt_2= cnt_2+1
    if List[i]=='3':
        cnt_3= cnt_3+1
    if List[i]=='4':
        cnt_4= cnt_4+1
    if List[i]=='5':
        cnt_5= cnt_5+1
    if List[i]=='6':
        cnt_6= cnt_6+1
    if List[i]=='7':
        cnt_7= cnt_7+1
    if List[i]=='8':
        cnt_8= cnt_8+1
    if List[i]=='9':
        cnt_9= cnt_9+1





print(cnt_0)
print(cnt_1)
print(cnt_2)
print(cnt_3)
print(cnt_4)
print(cnt_5)
print(cnt_6)
print(cnt_7)
print(cnt_8)
print(cnt_9)