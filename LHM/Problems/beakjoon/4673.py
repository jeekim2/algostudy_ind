#https://www.acmicpc.net/problem/4673

#1~10 self number

#1: 1 + 1 =2
#2 :2 + 2 =4
#3
import math
'''
for i in range(10):
    i = i + math.floor(i/10)+math.floor(i%10)
'''
def DN(i):
    return i + math.floor(i/10)+math.floor(i%10)


# DN(i)
# DN(DN(i))
# DN(DN(DN(i)))
# DN(DN(DN(DN(i))))
# DN(DN(DN(DN(DN(i)))))
# DN(DN(DN(DN(DN(DN(i))))))
# DN(DN(DN(DN(DN(DN(DN(i)))))))
# DN(DN(DN(DN(DN(DN(DN(DN(i))))))))  
# DN(DN(DN(DN(DN(DN(DN(DN(DN(i)))))))))
a = []
# 1~100까지 수 배열
for i in range(1,101):
    a.append(i)


for i in range (1,101):
    for j in range(1,101):
        if int(a[j]) == int(DN[i]):
            a.remove[j]
        
    
print(a)
