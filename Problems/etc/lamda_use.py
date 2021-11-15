# lamda 매개변수 : 리턴값
# map = 함수, list 요소를 함수에 넣고 반환된 값으로 새로운 리스트 구성
# filter = 함수, list 요소를 함수에 넣고 반환된 값이 True일 경우에만 새로운 리스트 생성

# 예시(1)
power = lambda x:x*x
under_3 = lambda x:x<3

list_input_a = [1,2,3,4,5]
output_a = map(power, list_input_a)
output_b = filter(under_3, list_input_a)

print(type(output_a)) # class map
print(type(output_b)) # class filter

print(list(output_a))
print(list(output_b))
