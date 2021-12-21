#https://www.acmicpc.net/problem/1065

#각 자리수의 등차 수열 : 한자리 수 - 1개 / 두자리 수 - 1개 / 세자리 수 - 계산 필요
#abc의 등차 수열1(d:양수): a + 2d (=c) < 10 -> 100의 자리 바뀔 때마다 +4
#abc의 등차 수열2(d:음수): a - 2d >=0 -> a/2


def AP(MAX):
    cnt=0
    n = str(MAX)
    
    if (len(n)<3):
        cnt = MAX
    else:
        cnt = 99
        for i in range(100,MAX+1):
            str_i = str(i)
            if ((int(str_i[0])-int(str_i[1]))==(int(str_i[1])-int(str_i[2]))):
                cnt+=1
    return cnt                               
    
if __name__ == "__main__":    
    MAX = int(input())
    print(AP(MAX))
        
   