#https://www.acmicpc.net/problem/2447

def Print_star(Num):
    N = int(Num/3)
    if Num == 3:
        Pattern = ["***","* *","***"]
        return Pattern
    else:
        Unit = Print_star(N)
        blank = [i.replace("*"," ") for i in Unit]
        Pattern=[""]*Num
        for i in range(Num):
            j = i%N
            if (i >= N) & (i < 2*N):
                Pattern[i] = Unit[j]+blank[j]+Unit[j]
            else:
                Pattern[i] = Unit[j]*3             
 
        return Pattern      
        
        
if __name__=="__main__":
    Num = int(input())
    Star = Print_star(Num)
    for i in Star:
        print(i)