"""""""""""""""
정규 표현식(regex)
텍스트를 찾고 조작 하는 데 쓰는 문자열 (검색, 치환) -> 패턴

표현식에는 특별한 구문, 명령어가 필요, 완전한 프로그래밍 언어는 아님.
프로그래밍 언어, 도구에서 대부분 지원(정규표현식이 실행될 뿐)하나 직관적이지는 않음

구현 방법이 다양하고 검색강도에 따라 표현이 다르기 때문에 답이 없어

정규 문자: 리터럴 문자
메타 문자: 특별한 의미

https://wikidocs.net/1642
https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D
https://regexone.com/lesson/introduction_abcs
"""""""""""""""
import re

###################숫자 검색####################    sales형태 검색
# data= """
# sales1.xls
# orders3.xls
# sales2.xls
# sales3.xls
# europe2.xls
# """
# pattern = re.compile('sales\d')       #sales, sales1, sales[123], sales[1-3],sales\d
# result = pattern.findall(data)
# print(result)



###################문자 검색,이스케이프#################### na형태 검색, na[4]검색
# data= """
# na.
# na1.xls
# na25.xls
# Na3.xls
# Na[4].xls
# sa1.xls
# sa[1].xls
# """
# pattern = re.compile('[nN]a\d*')       #[nN]a, [nN]a., [nN]a.*, [nN]a.+,     [nN]a[.],[nN]a\[.\], [nN]a\[.\]\.\w*
# result = pattern.findall(data)
# print(result)


###################반복, 시작/종료#################### c a t 검색, 시작과 끝
# data = []
# result = []

# data = ['cat', 'dat', 'caat', 'caaat', 'ct', 'scattering', 'pinkcat', 'ta', 'ca1t']

# pattern = re.compile('ca*t$')       #cat, ca*t, ca+t, ca{1,2}t, ca?t     ^cat, cat$

# for i in data:
#     result.append(pattern.findall(i))
# print(result)


###################Greedy, Lazy 수량자####################  <b> <b> 검색
# data= """
# This offer is not available to customers
# living in <b>AK</b> and <b>HI</B>.
# """
# pattern = re.compile('<[Bb]>.*<\/[Bb]>')       #<[Bb]>.*<\/[Bb]>, <[Bb]>.*?<\/[Bb]>
# result = pattern.findall(data)
# print(result)


###################캡처, 하위표현식###################    http,https 형식의 주소만 가져오자
# data= """
# Hello, my name is Ben. Please visit
# my website at thttp://www.forta.com/.
# My website at http://www.forta.com/.
# http://www.forta.com/
# https://www.forta.com/

# httpshttps://www.forta2.com/
# """
# pattern = re.compile('(?:https){2,}\:\/\/(.*)\/')       #http\:\/\/, https?\:\/\/, https?\:\/\/.*\/, https?\:\/\/(.*)\/,       https{2,}\:\/\/(.*)\/ (X), (https){2,} (하위표현), (?:https){2,} (비캡처링)
# result = pattern.findall(data)
# print(result)


# ###################치환-sub함수###################
# data= """
# Hello, my name is Ben. Please visit
# my website at thttp://www.forta.com/.
# My website at http://www.forta.com/.
# http://www.forta.com/
# https://www.forta.com/

# httpshttps://www.forta2.com/
# """s

# redata = []
# pa1 = 'www'
# pa2 = 'ttt'

# pattern = re.compile('https?\:\/\/(.*)\/')
# result = pattern.findall(data)

# for i in result:
#     redata.append(re.sub(pa1, pa2,i))
# print(redata)