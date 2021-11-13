import math

list = input()
inputval=list.split()
H = int(inputval[0])
M = int(inputval[1])

Time_min = H*60 + M
Time_min_2 = Time_min -45

H2 = math.floor(Time_min_2/60)
M2 = Time_min_2%60

if H2<0:
    H2 = H2+24

print(H2, M2)