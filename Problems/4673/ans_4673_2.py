#https://www.acmicpc.net/problem/4673

#1부터 10000까지 일일이 숫자 확인하는 방식(브루트포스 알고리즘)
#1부터 시작해서 함수 적용하여 생성된 숫자를 제외시키기
#제외된 숫자를 뺀 나머지 숫자 중 가장 빠른 숫자부터 다시 함수 적용
#10000까지 확인될 때까지 반복

num_list = []
def Gen_Num(num):                
    gen_num = num
    num = str(num)        
    for k in range(len(num)):
        gen_num = gen_num+int(num[k])
    if gen_num > 100:
        return num_list        
    else:
        num_list.append(gen_num)
        return Gen_Num(gen_num)        
        
    
def solve():
    chk_num = list(range(1,101))
    for j in chk_num:
        del num_list[0:]
        list_gen = Gen_Num(j)
        for i in range(len(list_gen)):
            if list_gen[i] in chk_num:
                chk_num.remove(list_gen[i])
    return chk_num  
  
if __name__ == "__main__":    
    chk_num = solve()
    for i in chk_num:
        print(i)
        