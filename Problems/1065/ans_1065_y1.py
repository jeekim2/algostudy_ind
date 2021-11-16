#https://www.acmicpc.net/problem/1065

#각 자리수의 등차 수열 : 한자리 수 - 1개 / 두자리 수 - 1개 / 세자리 수 - 계산 필요
#abc의 등차 수열 전제 조건: a + 2d (=c) < 10 , a + d(=b) < 10
#전제 조건 재정리 : 111a+12d <= abc || 89a-12d <=abc , d <= 4


def equal_diff(N):
    if N < 100:
        return N
    else:
        cnt = 99
        N_1st = (N//10)//10
        
        for i in range(1,N_1st+1):
            for j in range(1,5):
                if (111*i+12*j) <= N:
                    cnt+=1
                    print(cnt)
                if (111*i+12*j) <= N:
                    cnt+=1
                    print(cnt)
        return cnt               
    
if __name__ == "__main__":    
    # N = int(input())
    print(equal_diff(210))
        
   