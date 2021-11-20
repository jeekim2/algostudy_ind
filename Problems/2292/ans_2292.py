#https://www.acmicpc.net/problem/2292

#1개의 육각형 > +6개의 육각형 : 1개 변마다 1개의 육각형 인접
#6개의 육각형 > +12개의 육각형 : 육각 지점 *2 인접
#12개의 육각형 > +18개의 육각형 : 육각 지점 *2 + 나머지*1 인접
#18개의 육각형 > +24개의 육각형 : 육각 지점 *2 + 나머지*1 인접
#1+등차가 6인 수열의 합

def GoToRoom(Num):
    if Num == 1:
        return 1
    for MIN in range(1,Num):
        if (3*pow(MIN,2)+3*MIN) >= (Num-1) :
            return MIN+1  
            
    
if __name__ == "__main__":
    Num = int(input())
    print(GoToRoom(Num))

    