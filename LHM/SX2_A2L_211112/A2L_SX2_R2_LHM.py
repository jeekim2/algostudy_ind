import string
import sys
import os
import re
import fileinput

from datetime import datetime



# 경로 설정
MAP_directory_file_txt = "C:\SX2_A2L\Filtered_Map_File.txt" #텍스트파일- conti제공
Data_Type_txt = "C:\SX2_A2L\PBC_Interface_type.txt" #텍스트파일- Mando제작
## MAP 파일 내부 변수 list
Var_List = []
Var_List_valid = []
## Data type ref
Var_List_type = []
## 내부 A2L 정보를 포함하는 TXT 파일 Open 
with open(MAP_directory_file_txt, 'r') as textfile:
    for row in textfile:
        tempList = row.split()
        if len(tempList) ==3:
            Var_List.append(tempList)

len_Var_List = len(Var_List)

for i in range(len_Var_List):
    if (str(Var_List[i][0])[0] == "p")or(str(Var_List[i][0])[0] == "C"):
        Var_List_valid.append(Var_List[i])
##
#print(Var_List_valid[0][0]) #변수명
#print(Var_List_valid[0][1]) #메모리 시작주소
#print(Var_List_valid[0][2]) #메모리 사용 사이즈

#print(len(Var_List_valid))

## 내부 Type 정보를 포함하는 TXT 파일 Open

with open(Data_Type_txt, 'r') as textfile:
    for row in textfile:
        templist2 = row.split()
        Var_List_type.append(templist2)

#print(Var_List_type) : Matlab에 선언된 변수의 type 정보
#len_type = len(Var_List_type) #269
## Mando PBC Data Type
##print(Var_List_type[0][0]) #변수명
##print(Var_List_type[0][1]) #TYPE
##print(Var_List_type[0][2]) #MIN
##print(Var_List_type[0][3]) #MAX


##
# Var_List_valid[0][0]... Var_List_type[0][0]/[1][0]...[len(Var_List_type)][0] 비교
# Var_List_valid[0][1]... Var_List_type[0][0]/[1][0]... 비교
# ...Var_List_valid[0][len(Var_List_valid]
for i1 in range(len(Var_List_valid)):
    for i2 in range(len(Var_List_type)):
        if Var_List_valid[i1][0] == Var_List_type[i2][0]:
            Var_List_valid[i1].insert(3,Var_List_type[i2][1])
            Var_List_valid[i1].insert(4,Var_List_type[i2][2])
            Var_List_valid[i1].insert(5,Var_List_type[i2][3])
        
for i in range(len(Var_List_valid)):
    if len(Var_List_valid[i]) == 3:
            Var_List_valid[i].insert(3,"N/A") ## 기존 정의 되지 않은 Var_List_valid에 N/A 추가 하기
            Var_List_valid[i].insert(4,"N/A")
            Var_List_valid[i].insert(5,"N/A")
   
   

####################


for i3 in range(len(Var_List_valid)):
    if str(Var_List_valid[i3][3])[0] == "e":
        Var_List_valid[i3].insert(6,Var_List_valid[i3][3]) ## Type이 Enum 값인 경우


##
#print(Var_List_valid[0][0]) #변수명
#print(Var_List_valid[0][1]) #메모리 시작주소
#print(Var_List_valid[0][2]) #메모리 사용 사이즈
#print(Var_List_valid[0][3]) #Type
#print(Var_List_valid[0][4]) #Min
#print(Var_List_valid[0][5]) #Max
#print(Var_List_valid[0][6]) #Enum value or NO_COMPU_METHOD


## A2L 파일 기록
## 기록 파일 경로 및 이름 설정

## Var_List_valid 의 Type A2l양식에 맞게 변경


for i1 in range(len(Var_List_valid)):
    if str(Var_List_valid[i1][3])[0] == "e":
        Var_List_valid[i1].insert(3,"SLONG")
        Var_List_valid[i1].insert(4,-2147483648)
        Var_List_valid[i1].insert(5,2147483647)

    if str(Var_List_valid[i1][3])[0] == "N":
        Var_List_valid[i1].insert(3,"SLONG")
        Var_List_valid[i1].insert(4,-2147483648)
        Var_List_valid[i1].insert(5,2147483647)
        Var_List_valid[i1].insert(6,"NO_COMPU_METHOD")
## uint8 - UBYTE/ int8 - SBYTE
    if (str(Var_List_valid[i1][3])[0] == "u")and(str(Var_List_valid[i1][3])[1] == "i")and(str(Var_List_valid[i1][3])[2] == "n")and(str(Var_List_valid[i1][3])[3] == "t")and(str(Var_List_valid[i1][3])[4] == "8"):
        Var_List_valid[i1].insert(3,"UBYTE")
        Var_List_valid[i1].insert(4,0)
        Var_List_valid[i1].insert(5,255)
        Var_List_valid[i1].insert(6,"NO_COMPU_METHOD")

    if (str(Var_List_valid[i1][3])[0] == "i")and(str(Var_List_valid[i1][3])[1] == "n")and(str(Var_List_valid[i1][3])[2] == "t")and(str(Var_List_valid[i1][3])[3] == "8"):
        Var_List_valid[i1].insert(3,"SBYTE")
        Var_List_valid[i1].insert(4,-126)
        Var_List_valid[i1].insert(5,125)
        Var_List_valid[i1].insert(6,"NO_COMPU_METHOD")

    if (str(Var_List_valid[i1][3])[0] == "u")and(str(Var_List_valid[i1][3])[1] == "i")and(str(Var_List_valid[i1][3])[2] == "n")and(str(Var_List_valid[i1][3])[3] == "t")and(str(Var_List_valid[i1][3])[4] == "1")and(str(Var_List_valid[i1][3])[5] == "6"):
        Var_List_valid[i1].insert(3,"UWORD")
        Var_List_valid[i1].insert(4,0)
        Var_List_valid[i1].insert(5,65535)
        Var_List_valid[i1].insert(6,"NO_COMPU_METHOD")

    if (str(Var_List_valid[i1][3])[0] == "i")and(str(Var_List_valid[i1][3])[1] == "n")and(str(Var_List_valid[i1][3])[2] == "t")and(str(Var_List_valid[i1][3])[3] == "1")and(str(Var_List_valid[i1][3])[4] == "6"):
        Var_List_valid[i1].insert(3,"SWORD")
        Var_List_valid[i1].insert(4,-32768)
        Var_List_valid[i1].insert(5,32767)
        Var_List_valid[i1].insert(6,"NO_COMPU_METHOD")

    if (str(Var_List_valid[i1][3])[0] == "u")and(str(Var_List_valid[i1][3])[1] == "i")and(str(Var_List_valid[i1][3])[2] == "n")and(str(Var_List_valid[i1][3])[3] == "t")and(str(Var_List_valid[i1][3])[4] == "3")and(str(Var_List_valid[i1][3])[5] == "2"):
        Var_List_valid[i1].insert(3,"ULONG")
        Var_List_valid[i1].insert(4,0)
        Var_List_valid[i1].insert(5,4294967295)
        Var_List_valid[i1].insert(6,"NO_COMPU_METHOD")

    if (str(Var_List_valid[i1][3])[0] == "i")and(str(Var_List_valid[i1][3])[1] == "n")and(str(Var_List_valid[i1][3])[2] == "t")and(str(Var_List_valid[i1][3])[3] == "3")and(str(Var_List_valid[i1][3])[4] == "2"):
        Var_List_valid[i1].insert(3,"SLONG")
        Var_List_valid[i1].insert(4,-2147483648)
        Var_List_valid[i1].insert(5,2147483647)
        Var_List_valid[i1].insert(6,"NO_COMPU_METHOD")

    #Var_List_valid[i1].delete(Var_List_valid[i1][7])
   #Var_List_valid[i1].delete(Var_List_valid[i1][8])
    #Var_List_valid[i1].delete(Var_List_valid[i1][9])
#####################   

#for i1 in range(len(Var_List_valid)):
#    print(Var_List_valid[i1])




## 메모장 입력
####################################
with open("C:\SX2_A2L\SX2_PbcInternal_A2L_"+datetime.today().strftime("%Y%m%d")+".a2l", 'w') as data:
    for i in range(1,len(Var_List_valid)):
        if str(Var_List_valid[i][0])[0] == "p":
            data.write("    /begin MEASUREMENT " + str(Var_List_valid[i][0]) +" \"\""+  "\n"  )
            data.write("    "+  str(Var_List_valid[i][3]) +" "+ str(Var_List_valid[i][6]) + " " +"0 0 "+ str(Var_List_valid[i][4]) +" "+ str(Var_List_valid[i][5]))
            data.write("\n    ECU_ADDRESS 0x"+str(Var_List_valid[i][1])+"\n")
            data.write("    ECU_ADDRESS_EXTENSION 0x0\n")
            data.write("    FORMAT \"%.15\"\n")
            data.write("    /begin IF_DATA CANAPE_EXT\n")
            data.write("     100\n")
            data.write("     LINK_MAP \""+" "+str(Var_List_valid[i][0])+" "+"\" 0x"+str(Var_List_valid[i][1])+" "+" 0x0 0 0x0 1 0x9F 0x0\n")  ##0x9F 의미를 모르겠음
            data.write("     DISPLAY 0 "+str(Var_List_valid[i][4]) +" "+ str(Var_List_valid[i][5])+"\n" )
            data.write("    /end IF_DATA\n")
            data.write("      SYMBOL_LINK \""+str(Var_List_valid[i][0])+"\" 0\n")  
            data.write("    /end MEASUREMENT\n\n\n")

        if str(Var_List_valid[i][0])[0] == "C":
            data.write("    /begin CHARACTERISTIC " + str(Var_List_valid[i][0]) +" \"\""+  "\n"  )
            data.write("    VALUE 0x"+  str(Var_List_valid[i][1]) +" __UWORD_S 0"+ " NO_COMPU_METHOD " +" "+ str(Var_List_valid[i][4]) +" "+ str(Var_List_valid[i][5]))
            data.write("\n    ECU_ADDRESS_EXTENSION  0x0"+"\n")
            data.write("    EXTENDED_LIMITS " + str(Var_List_valid[i][4]) +" "+ str(Var_List_valid[i][5]) +"  \n")
            data.write("    FORMAT \"%.15\"\n")
            data.write("    /begin IF_DATA CANAPE_EXT\n")
            data.write("     100\n")
            data.write("     LINK_MAP \""+" "+str(Var_List_valid[i][0])+" "+"\" 0x"+str(Var_List_valid[i][1])+" "+" 0x0 0 0x0 1 0x9F 0x0\n")  ##0x9F 의미를 모르겠음
            data.write("     DISPLAY 0 "+str(Var_List_valid[i][4]) +" "+ str(Var_List_valid[i][5])+"\n" )
            data.write("    /end IF_DATA\n")
            data.write("      SYMBOL_LINK \""+str(Var_List_valid[i][0])+"\" 0\n")  
            data.write("    /end CHARACTERISTIC\n\n\n")

print("A2L done")


