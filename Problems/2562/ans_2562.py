"""9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다."""
num_list = []
num_max = 0
max_order = 0
i = 0
while i < 9:
    num_val = int(input())
    num_list.append(num_val) 
    num_max = max(num_max, num_list[i])
    if num_max == num_list[i]:
        max_order = i+1
    i+=1
print("%d\n%d"%(num_max, max_order))    
    
    