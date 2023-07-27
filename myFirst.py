#자료형
####숫자############################
#1)정수(int)
#2)실수(float)
#3)복소수(complex)
###ex) 
# a = 1 + 2j
# print(type(a)) #complex. a변수의 자료형은 무엇인지 출력해

# a = 1 
# print(type(a)) #int
# a='파이썬 드디어 시작'
# print(type(a)) #str 문자열
# print(a) #a의 내용을 출력
# a = 100
# print(type(a))
# print(len(a)) #a는 길이가 얼마야?오류. 숫자는 길이가 없다.
#int(정수)는 길이를 잴 수 없다.
# a='파이썬 드디어 시작' #문자열: "", ''로 표현
# print(len(a)) 
# print(type(a))#str : 문자열은 길이를 잴 수 있다.
# b="큰따옴표도 문자열" 
# print(type(b))
# print(b) #문자열은 인덱스 값을 가짐. 배열
# b[0],b[1],b[2]... 형태로 저장됨.

# a = 1.1
# print(type(a)) #float
# x = 3
# print(id(x)) #140707281101672 객체의 주소값 반환.
# #변수에 저장되는 것은 실제값이 아니고 객체의 주소이다.
# a = "안녕하세요"
# print(a[0]) #안
# print(a[3]) #세
# print(a[-1]) #요
# print(a[-2]) #세
# print(a[-4]) #녕
# print(a[5]) #a변수에 저장된 문자열은 인덱스값이 0부터 4까지 존재하므로 오류
# print(a[0:3]) #안녕하  인덱스 0:3은 0~2까지만 출력됨.
# print(a[::]) #안녕하세요 .처음부터 끝까지 출력
# print(a[::2]) #안하요 . 처음부터 끝까지 2자리씩 건너띄고 출력

# a = "1,2,3,4,5,6,7,8,9"  #""는 문자열
# print(len(a)) #쉼표도 문자열의 길이에 포함되므로 17이 나온다.
# print(a[::2])
# b="987654321"
# print(b) #987654321
# print(b[::-1]) #123456789  역순출력

############문자열의 함수#######################

# a="abcd"
# print(type(a)) #str
# print(a.find('b')) #인덱스값 1을 반환함. a[1]
# print(a.replace('b','!!')) #a!!cd
# print(a[::-1]) #dcba 
# print(a) #replace()함수를 수행 후 a변수에 저장되지는 않음
# print(a.split('b')) #['a', 'cd'] b는 제외됨.
#ctrl+함수클릭 --> 해당 문법확인
#help(a.find)  #문법 확인 --more부분 클릭 후 엔터... 다음페이지보임.
# a = "abc"
# print(a.replace('b','~')) #a~c
# print(a) #abc
# a = a.replace('b','~') #  replace()함수를 적용한 후 다시 변수에 저장
# print(a)  #a~c

# c = 12345  #int
# # print(type(c)) #int
# # print(str(c)) 
# c = str(c)  #int --> str변환하고 c변수에 저장
# print(type(c))  #str

# a = "안녕하세요 \n제 이름은 이선희입니다. \n잘 부탁드립니다."
# print(a)  #출력결과: \n 엔터키에 해당
# 안녕하세요 
# 제 이름은 이선희입니다.
# 잘 부탁드립니다.
#연산자: +, -, *, /, //, %(나머지연산자), **(제곱연산자)
#대입연산자: (+=, -=, *=, /=, %=, **=)

# print(5+3)
# print(3-2)
# b = 5+3
# print(b)

# c=3-2
# print(c)

# print(4*3)
# print(type(9/3)) #float 3.0  나누기의 결과 값은 실수
# print(5/3)
# print(type(5/3)) #float
# b = int(5/3) #기존의 데이터 타입을 정수형으로 변환
# print(type(b)) #int
# print(5//3) #1  5나누기 3을 한 후 소수점이하 버림.
# print(5%3) #2 나머지연산자. 5를 3으로 나눈 나머지 값만 출력.
# print(5**3) #125   5의 3승

# ##대입연산자 
# a = 5
# a += 3  # a를 3증가해라. a = a+3
# print(a)
# a -= 2  # a에서 2를 빼기. a = a-2
# print(a) #6

# b = 5
# b **= 3 #   b= b**3
# print(b) #125
# #divmod()함수
# print(divmod(5,3)) #5를 3으로 나누어라 결과값: (1, 2) 몫은 1, 나머지 2
# #pow()함수 : 제곱근
# print(pow(5,3)) #5의 3승 125

#그 외의 cos,sin,tan 등 계산시 제공되는 모듈: math

# import math #math모듈(math.py) 불러들임. 
#모듈 속에는 여러개의 함수가 선언되어 있고 필요한 함수들을 호출해서 사용함.

# print(math.sqrt(8))  #2.8284271247461903 sqrt():제곱근

############리스트(list): 대괄호[]로 표현,콤마로 구분. 값 변경가능
#임의의 객체(아무값이나)를 순서대로 저장하는 집합형태의 자료형
# a = [1,2,3,4]  
# print(type(a)) #list
# print(a)

# a = [1,2,[1.1,2],'a'] #리스트
# print(a[2]) #[1.1, 2]
# b = a[2]###############################
# print(b)
# b.remove(2) #2라는 숫자값을 삭제
# print(b)
# a[2]=b
# print(a)###############################
# print(a[0]) #1
# print(a[0:4]) #[1, 2, [1.1, 2], 'a'] a[0]~a[3]출력
#####리스트의 여러가지 함수
####append(),remove(),reverse(),sort()
# a = [4,1,3,2] #리스트 데이터
# a.append(5) #끝에 5를 추가
##print(a.append(5)) #오류: None 즉, 리턴값이 아무것도 없다.
# print(a) #[4, 1, 3, 2, 5]
# a.remove(2) #리스트 중 2를 삭제
# print(a) #[4, 1, 3, 5]
# a.sort() #숫자 정렬(작은수->큰수)
# print(a) #[1, 3, 4, 5]
# print(a)  #[4, 1, 3, 2]
# a = a.append(5) #append()함수의 결과는 변수에 저장할 수 없다. 
# print(a) #None
# print(a[::-1]) #역순출력 [2, 3, 1, 4]
# print(a) #[4, 1, 3, 2] 즉, 역순출력은 리스트값을 변환하지 않는다.
# a.reverse() #리스트 값을 변화시킨다.
# print(a.reverse())  #오류: 리턴값이 None이므로 직접출력할 수 없다. 
# print(a) # [2, 3, 1, 4]

# b = 0b11 #접두어 0b는 이진수
# print(type(b))  #int
# print(b)  #3 즉,2진수 11은 3(00,01,10,11,100,101,110,111,1000)
# c = 0o12
# print(type(c)) #int
# print(c) #10  
# d=0X23  #접두어 0X 16진수
# print(type(d))
# print(d)  #35

# a = "123"
# print(type(a))
# print(a)
# print(int(a))
# a = 3403490885623840380507830850034
# print(type(a)) #int
# print(a)
# b = 2e-4 #e-4:소수자리가 4자리 늘어남
# print(type(b))
# print(b) #0.0002
# c =3e3 #e3: 정수부에서 3자리를 이동
# print(type(c))
# print(c) #3000.0

####문자열 자료형. 문자열 연산############
# a='1'
# print(type(a)) #str
# b = "Hello, World!"
# print(type(b))
# print('1'+'2') #12
# print(1+2) #3
# a='Hello! '
# b="World"
# print(a+b) #a와 b가 문자열이므로 +는 문자열 연결연산자로 작용한다

# print('2'*3) # 222 *:반복연산자
# print(2*3) #6
# print('안녕하세요 '*3)

# a = '안녕하세요'
# print(a[::-1]) #:: - 전체출력, -1역순 '요세하녕안'

# a='12345'
# b='34567'
# c = a[0:3] + b[1:] #a는 a[0]~a[2]까지, b[1:]-b[1]~끝까지
# print(c)
# a = 'abcdefghi'
# print(a.upper()) #대문자로 변환 ABCDEFGHI
# a='ABCDEFGHI'
# print(a.lower()) #소문자로 출력
# a = 'abCDefgHi'
# print(a.swapcase()) #대소문자가 바뀜
# a = 'abcde'
# print(a.replace('cd','1'))  #문자열 대체 함수
# a = ['a','b','c']
# print(a) # ['a', 'b', 'c']
# print('#'.join(a)) #   a#b#c

# a = 'abcd abcd'
# print(a.capitalize()) #맨앞자가 대문자
# print(a.title()) #단어별로 첫번짹 글자가 대문자가 됨
# a = '  abcd efg    '
# print(a) #  abcd efg
# print(a.strip()) #앞뒤(좌우) 공백제거
# print(a)
# print(a.lstrip()) #좌측 공백제거
# print(a.rstrip()) #우측 공백제거

# a = 'abcdef'
# print(a.index('e')) #4 id()참조
# print(a.index('g')) #ValueError
# print(a.find('e')) #find()도 인덱스 값을 반환한다. 4
# print(a.find('g')) #-1 a에 해당 데이터가 없음.

# li = list() #[]
# print(li, type(li)) #[] <class 'list'>  두개의 출력값을 한꺼번에 지정

# li = [1,2,3,4,5,6,7,8,9]
# print(li[0]) #1
# print(li[len(li)-1]) #li[8] len(li)-1 --> 8

# li = [1,2,3,4,5,6,7,8,9]
# li[0] = 99 
# print(li)
# li[1] = [1,2,3]
# print(li)
# li[2] ='문자'
# print(li)  #리스트 값은 문자, 숫자, 군집자료형 모두 들어갈 수 있음.

#########군집자료형: 튜플 ########################
#튜플: 자료 값의 변경 불가
#괄호()
# t = (1,2,3) #튜플
# print(t,type(t)) #(1, 2, 3) <class 'tuple'>

# a = [1,2,3]
# a[0] = 4
# print(a)
# a=(1,2,3)
# a[0]=4
# print(a) #TypeError 튜플은 데이터를 변경할 수 없다.

# a =1,2,3,4 #튜플
# print(type(a)) #<class 'tuple'>

# li = [1,2,3] #리스트
# tu = (1,2,3) #튜플
# print(li, type(li))
# print(tu, type(tu))
# print(li[0],li[0:2]) #1 [1, 2]
# print(li + li) #[1, 2, 3, 1, 2, 3]
# print(tu + tu) #(1, 2, 3, 1, 2, 3) 일시적으로 이렇게 나옴
# print(tu) #(1, 2, 3)
# print(li) #[1, 2, 3]

###########군집자료형: 딕셔너리 ##################
#중괄호{} ex){키1:값1, 키2:값2.... }  key:value쌍
#키는 변경 불가한 객체
# a = {'key':'value', 1:[1,2,3], (1,2):'a'}
# print(a[1]) #a[1]:1은 키값. [1, 2, 3]
# print(a['key']) #value 키값 입력-> value값이 나옴
# print(a[(1,2)]) #a
# print(type(a)) #<class 'dict'>

# d ={1:1,
#     'a':[1,2,3],
#     (1,2):"aaa"
#     }
# print(d) #{1: 1, 'a': [1, 2, 3], (1, 2): 'aaa'}
# print(d['a']) #[1, 2, 3]
# print(d[(1,2)]) #aaa

######군집데이터 - set(집합)########################
# 중괄호{}, 중복제거, 인덱스를 지원하지 않는다.
# a={1,2,3,4}  #set(집합) 
#딕셔너리랑 다른 점: 키:값의 쌍으로 이루어져 있지 않다.
# print(type(a)) #<class 'set'>
# a = {1,1,1,1,1,2,3,4}
# print(type(a)) #{1, 2, 3, 4}  집합은 중복이 제거된다.
# print(a) 

#미션: 리스트에 중복을 제거(set()) --> 리스트타입으로 변환(list())
# a=[1,2,1,1,1,2,3,4,2,2,3,4,5,6,7,8,0,0,2]
# a.sort()
# print(a)
# # print(set(a)) #리스트타입의 중복은 set()함수를 이용하여 제거
# # print(a)
# print(type(a))
# a = set(a)
# print(a)
# a = list(a)
# print(a) 

# s = "hello"
# s = set(s) 
# print(s)#{'l', 'o', 'e', 'h'}
# print(type(s))
# print(s[0]) #TypeError : set데이터는 순서가 없다. 그래서 인덱스를 지원하지 않는다.

# s1 = set([1,2,3,4,5,6])
# print(type(s1))
# s2 = set([4,5,6,7,8,9])
# print(s1)
# print(s2)

# print(s1&s2) #교집합 {4, 5, 6}
# print(s1|s2) #합집합 {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(s1.union(s2)) #합집합 {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(s1-s2) #차집합 {1, 2, 3}
# print(s1.difference(s2)) #차집합 {1, 2, 3} 

##집합에서의 값 추가
# add()

# s = {1,2,3}
# s.add(4) #집합은 자료추가 가능
# print(s) #{1, 2, 3, 4}
# s.remove(2) # 2라는 값을 제거
# print(s) #{1, 3, 4}
# s.update([5])
# ##s.update(5) # 오류 
# print(s)
# s.update([6,7])
# print(s) #{1, 3, 4, 5, 6, 7}

# ###ppt 40페이지 연습문제
# T =(1,2,3,4,5,6,7,8)
# T = list(T)
# print(T) #[1, 2, 3, 4, 5, 6, 7, 8]
# T[0]=0
# print(T)
# T.append(9)
# print(T)
# T.remove(8)
# print(T)
# T = tuple(T)
# print(T)

# ## ppt 48페이지
# a = [4,6,2,1,8,5,3,2,8,9,6]
# # a.sort()
# a.sort(reverse=False)
# print(a) #[1, 2, 2, 3, 4, 5, 6, 6, 8, 8, 9]
# #a.sort(reverse=True)
# a = list(set(a)) #set()중복제거 --> list() 타입으로 변환 
# print(a)
# a.reverse()
# print(a)

# print(5+3)
# print(5//3)
# print(5**3)
# print(pow(5,3))
# print(5%3)
# print(5/3)
# print(divmod(5,3)) #(1, 2) 몫:1 나머지:2
# a = 3
# a += 3 # a = a+3
# print(a)

# a = "안녕하세요\n이선희입니다.\n잘 부탁드립니다."
# print(a)
# a = """안녕하세요   
# 잘 부탁드립니다.
# 홍길동입니다."""
# print(a)

#"""원하는 형태로 출력하기 위한 내용 추가"""
# print('오'*5)
# print('오예~'*3)

# d = {'이름':'홍길동', '주소':'파주시', '전화':'010-0000-0000'}
# print(d['이름'])
# print(d['주소'])
# print(d['전화'])
# print(d.keys()) #dict_keys(['이름', '주소', '전화']) dict_keys()는 자료형이다.
# print(d.values()) #dict_values(['홍길동', '파주시', '010-0000-0000'])
# print(d.items()) #dict_items([('이름', '홍길동'), ('주소', '파주시'), ('전화', '010-0000-0000')])

# #############조건문 #############################
# # if(조건), while(조건->참 일때)  while(1):수행
# #불(bool)자료형? 참(1 - True)/거짓(0 - False)

# a = True
# print(type(a)) #<class 'bool'>
# b = False
# print(type(b)) #<class 'bool'>

# print(bool([1,2,3])) #True
# print(bool('abcd')) #True
# ###
# 1 x 1 = 1 (참)
# 1 x 0 = 0 (거짓) 
# 0 x 1 = 0
# 0 x 0 = 0
# print(bool("")) #False
# print(bool({'a':1,'b':2})) #True
# print(bool([1,2,3])) #True
# print(bool([])) #False
# print(bool((1,2,3))) #True
# print(bool(1))  #T
# print(bool(0)) #F
# print(bool(())) #F
# print(1 == 1) # 1을 리턴 -->T  ~와 같다
# print(1 == 2) # 0을 리턴 -->F
# print(1>0) # T 리턴 값 1을 반환
# print(2<1) #F 리턴 값 0을 반환
# print(1 >= 1) #T
# print(1 != 0) #T ~와 같지 않다.
#논리연산자: and/or/not
# a = True
# b = True
# # print(a and b) #T  a=1 b=1 1*1=1(참)
# a = False # a = 0
# print(a and b)  #곱하기 0 x 1 = 0
# print(not a)  #True
# print(not b) #False
# print(a or b) #더하기 0 + 1 = 1 둘중 하나가 참이면 참이 된다.

# a = 1
# b = 2
# print(a>0 and b>1) #True
# print(a == 0 or b!=1) # 0 + 1 = 1 --> T
# print("a" and "b") #둘 다 만족하면 뒤 출력(b)
# print("a" or "b")  #둘 중 하나 만족하면 앞 출력(a)

#if(조건문) :조건문이 참(T/1) 일 때 내용 수행
# if(True): #:은 if문의 시작을 알림
#     print(1) #1

# print(2) #if문과 무관한 출력 2

# if(True):
# print(1) #IndentationError: 
# print(2)
#
############if문#############################
# score = 93

# if score > 90:
#     print('A')  #A
# if score > 80:
#     print('B')  #B
# if score > 70:
#     print('C') #C

# score = 73
# if 100 >= score >= 90:  # F --> 0
#     print('A')
# if score >=80 and score < 90:
#     print('B')
# if score >=70 and score < 80:
#     print('C') #C

##if 조건1 elif 조건2 else ....
## if elif else
# score = 95
# if score >=90:
#     print('A')
# elif score >=80:
#     print('B')
# else:  # 나머지 조건을 모두 포함
#     print('C')

# a = 2
# if(a==2): #참 먼저나온 참이 출력
#     print(1) #1
# elif(a==2): #참 두번째 나온 참은 무시됨.
#     print(2)
# else:
#     print(4)
#if의 if문
# a = 3
# b = 2
# if(a == 1): #참 1
#     if(b == 3): #거짓 0
#         print(1)
#     else:
#         print(2) #a==1일 때 2
# else:
#     print(3) #a=3일 때 3출력

#if~elif~else  if~else  if~if~if...
# a=1
# b=3
# if(a == 1):
#     if(b == 3):
#         if(a<b): 
#             print(0)
#         print(1) #위의 if문과 무관
#     else:
#         print(2)
# else:
#     print(3)

# a = 2
# if(a == 1):
#     msg='a is 1'
# else:
#     msg='a is not 1'
# print(msg)

############if문 응용: 리스트와 함께 사용 ##########
# fruit = ['사과','배','딸기', '포도']
# fruit.append('귤')
# print(fruit)

# if '딸기' in fruit:   #fruit리스트 속에 아이템 '딸기'가 있으면
#     print("딸기가 있네요.^^")

############ continue ################
# :continue문을 만나면 블럭의 남은 부분은 건너띄고 반복문 처음으로 돌아감.
##ex) 1~100까지의 합(3의 배수 제외)
# hap, i = 0, 0

# for i in range(1,101):
#     if i % 3 == 0:
#         continue  # i가 3의 배수이면 아래블럭을 건너 띄고 for문으로 돌아간다.

#     hap += i # hap = hap + i  hap = 0 + 1  hap = 1 + 2 hap = ....
# print("1~100까지의 합(3의 배수 제외): %d" % hap)
#1~100까지의 합(3의 배수 제외): 3367

########### 포멧팅 - print() ##################
# print("....%d %f %s %x...." % 변수1, 변수2, 변수3, 변수4)
## %는 좌우를 구분하는 용도(빼먹지 않게 주의!)
## 서식:
## 1) 정수: %d(정수), %x (16진수), %o (8진수)
## 2) 실수: %f (소수점이 붙은 수)
## 3) %c (한글자), %s (두 글자 이상의 문자열)  

##ex1) (포멧팅) 1부터 10까지 더하는 예제(for문)
# i, hap = 1, 0

# for i in range(1,11,1):
#     hap = hap + i  #hap = 0 + 1  hap = 1 + 2....

# print("1부터 10까지의 합: %d" % hap)  #1부터 10까지의 합: 55

##ex2) (포멧팅) 중첩문(2중 for문)의 예
# for i in range(0,3,1): #0~2
#     for j in range(0,2,1): #0~1
#         print("중첩 for문입니다. i값: %d, j값: %d" % (i, j))

##ex3) (포멧팅) 100을 찍는 print()
# print(100)
# print('%d' % 100)

##ex4) (포멧팅) 변수대신 숫자
# print("%d" % (100+100)) 
# print("%d / %d = %5.1f" % (100, 200, 0.5)) #100 / 200 =   0.5

##ex5) (포멧팅) 정수
# print("%d" % 123) #123   
# print("%5d" % 123)#  123  정수 5자리 확보
# print("%05d" % 123) #00123  정수 5자리 확보 --> 공백을 0으로 채움

##ex6) (포멧팅) float
# print("%f" % 123.45) #123.450000 (소수점이하가 6자리로 출력)
# print("%7.1f" % 123.45) #  123.5 
# print("%7.3f" % 123.45) #123.450 #총 일곱자리이고 소수점이하 3자리

##ex7) (포멧팅) 문자열(str)
# print("%s" % "Python") #Python
# print("%10s" % "Python") #    Python  문자열 열자리 확보

##ex8) (포멧팅) format()함수사용 -- 출력순서 지정해 주는 역할
# print("{0:d} {1:5d} {2:05d}".format(123, 456,789)) #123   456 00789

##########이스케이프 문자(\) ###############
# \n : 엔터키
# \t : 탭키
# \b : Backspace
# \\ : \출력
# \' : '출력
# \" : "출력

##ex)
# print("\n줄바꿈\n연습")
# print("\t탭키\t연습")
# print("글자가 \"강조\"되는 효과1")
# print("글자가 \'강조\'되는 효과2")
# print("\\\\\\역슬래시 세 개 출력")
# print(r"\n \t \" \\를 그대로 출력")
      

###########위의 문장을 '조건부 표현식'으로 만들기
##문장을 짧게 만듬
# msg2 = 'a is 1' if(a == 1) else 'a is not 1'
# print(msg2)

########## for문 ###################
#반복문 반복적 객체: 리스트, 튜플, 집합, 범위 데이터
# for i in '1234': #for문 시작. '1234'이 자리에 들어 갈 데이터 반복적 객체!
#     print(i)   #'1234'의 데이터의 인덱스값을 증가시키며 i를 출력
#                #1
#                #2
#                #3
#                #4

# for i in 1000: #TypeError: 'int' object is not iterable 
#     print(i)

# a = [1,2,3]
# print(a[0])
# print(a[0:2])

##range(0,10,2)  range(시작값,10미만,2칸씩 가져옴)
# range(10) #0부터 9까지의 값

# for i in range(10):  #0~9까지 10개 range(0(이상), 10(미만))
#     print(i)

# for i in range(0,10,2):
#     print(i)   #세로로 2 4 6 8이 출력됨

# for i in range(1,101,2):
#     print(i) #1 3 5..... 99(세로로 출력)

# for i in range(1,101,2):
    #print(i,end=',') #출력 끝에 연결해서 찍음(옆으로 출력)
    #print(i,end=' ')
    #print(i,end='')

# for i in range(1,51): #1일 때 2*1-1 =1, 2일 때 2*2-1=3 50번 루프돔.
#     print(2*i-1,end=' ')  #1부터 50까지의 홀수

# for i in {1,2,3}:
#     print(i)
# for i in [1,2,3]:
#     print(i)
# a = 'apple'
# for i in a:
#     print(i,end=' ') #a p p l e

# for i in (4,5,6): 
#     print(i)
# for i in {'이름':'홍길동','주소':'파주시','전번':'01000000000'}:
#     print(i) #이름 주소 전번 (key만 출력)

# d = {'이름':'홍길동','주소':'파주시','전번':'01000000000'}
# print(d['주소'])
# print(d['이름'])
# print(d.keys()) #dict_keys(['이름', '주소', '전번'])
# print(d.values()) #dict_values(['홍길동', '파주시', '01000000000'])
# print(d.items())
#dict_values(['홍길동', '파주시', '01000000000'])

# d2 = {'a':'뭐지?','b':'몰라'}
# print(d2['b'])

#for문에 반복가능한 객체들: 
# 문자열(str),튜플(tuple),리스트(list), 집합(set), 딕셔너리(dict), range() 등

# import collections.abc

# obj = [1,2,3,4]
# obj2 = {1,2,3,4}
# obj3 = "abcdef"
# obj4 = {'a':1,'b':'aa','c':3}
# obj5 = (1,2,3,4)
# obj6 = range(10)
# obj7 = range(1,10)

# print(isinstance(obj7,collections.abc.Iterable))
# # isinstance()메소드를 통해서 해당 객체가 반복가능한 객체인지 아닌지를 판단 True/False반환
# isinstance() -> bool
#range(10) range(0,10)
# ld = list(range(10))  
# print(ld) 
# ld2 = ['a',9,[1,2,3],('a','b')]
# print(range(len(ld2)))  

# for i in ld2:
#     print(i)

# for i in (range(len(ld2))):
#     print(ld2[i])  #ld2의 각각의 요소값을 출력

# for j in (1,2,3,4):
#     print(j,end=',')    

# for i in [1,2,3,4]:
#     print(i,end='-')

# for i in [1,2,3,4]:  #이중for문
#     for j in (1,2,3,4):
#         print(j,end=',')  #1,2,3,4
#     print(i,end='-')

################# while문 #########################
###무한루프 주의!!
##  while(조건-참):  #조건이 참일 때 아래 구문 수행
#초기값,조건,증감이 존재
# num = 5  #초기값
# while (num>0):  #조건
#     print(num) 
#     num -= 1  # num = num - 1  감소

# num = 1
# while (num <10):
#     print(num)
#     num += 1 # num = num + 1
#     if num == 3:
#         continue  
#     if num == 5:
#         break   #while문 종료

####input()#####################
#사용자로 부터 데이터 값을 입력 받는 메소드
# 리턴 값 --> str      1 --> '1' --> int()
# a = input("정수를 입력하세요!:")
# a = int(a)
# print(a+a)

############
# a = input()   #사용자 입력 받기1 엔터 후
# b = input()   #사용자 입력 받기2 엔터
# a = int(a)  
# b = int(b)
# result = a + b
# print(a, "+", b, "=", result) 
# print(type(a), type(b))

###########
# a = int(input('첫번째 정수값:'))
# b = int(input('두번째 정수값:'))
# result = a + b
# print(a,"+",b,"=",result)
# result = a - b
# print(a,"-",b,"=",result)
# result = a * b
# print(a,"x",b,"=",result)
# result = a / b
# print(a,"/",b,"=",result)
# ############
###파이썬의 파일 입출력
# open(파일경로,모드) - 모드: 읽기, 쓰기, 수정
# close()

# f = open("a.txt",'w')
# f.write("1234")
# f.close()

# f = open("a.txt",'a')
# f.write("5670")
# f.close()

# import os

# print(os.getcwd()) #C:\pythonProject

# f = open("C:\\pythonProject\\test\\a.txt",'w') ##쓰기 모드
# f.write("진짜로 잘되지....") #write()
# f.close()

# f = open("C:\\pythonProject\\test\\a.txt",'r')  ##읽기 모드
# print(f.read())  #read()
# f.close()

############파이썬 함수 ##################
## 함수: 입력 --> 처리(실행) --> 출력
#def 함수명():
#   실행할 코드 

###### 매개변수가 없는 함수 ###################
# def func():  ##func()이라는 함수 (선언부)
#     print(1)

# func()  ##(실행부) 1 출력

# def func(): 
#     "숫자를 출력해주는 함수입니다."  #함수의 기능정의 가능. help(func)을 부르면 나타남
#     print(1)

# func()  # 함수 호출부
# help(func)  # 기능 정의된 내용이 출력됨.

# def gugu():
#     "구구단 2단을 출력하는 함수입니다."
#     for i in range(1,10):
#         print(f"{2} x {i} = {2*i}")   #formatting 방법: f"{} {} "

# help(gugu)
# gugu() 

# def gugu2():
#     "구구단 3단을 출력하는 함수입니다."
#     for i in range(1,10):
#         print(f"{3} x {i} = {3*i}")

# help(gugu2)
# gugu2()

########함수의 매개변수 #########
#def func(x):  #x는 매개변수(파라미터) 
#함수를 호출할 때 아규먼트의 갯수는 반드시 파라미터의 개수와 일치하여야 한다.
# def gugu(x):  #매개변수는 함수속에 선언되어 있음.
#     for i in range(1,10):
#         print(f"{x} x {i} = {x*i}")

# gugu()     #매개변수로 넘겨줄 아규먼트 값이 없으므로 오류.
# # gugu(3)  #3은 인자값(아규먼트)
# # gugu(4)
# # gugu(5)

# def gugu(x=2): #기본값 세팅
#     for i in range(1,10):
#         print(f"{x} x {i} = {x*i}")

# gugu(5)  #아규먼트가 있을 때는 해당 단수를 출력
# gugu()   #아규먼트가 없을 때는 기본설정값의 단수로 출력

# def func(x,y,z,a,b=0,c=1):
#     print(f"{x} = x,{y} = y, {z} = z,{a} = a, {b} = b, {c} = c")

# func(1,2,3,4,5)

# def func(x,y,z,a):
#     print(x, y, z, a)

# func(1,2,3) #아규먼트 1개 a부족 --> 오류

# def func():
#     a = 2  #함수 속에 선언된 변수 a -- local(지역)변수. 함수 내부에서만 통용되는 변수
#     print(a)
# a = 1   #global(전역)변수. 프로그램 전체에 통용되는 변수
# print(a)  #1
# # func()

############# return 값이 있는 함수 ##################

# def sum_num(x,y):
#     result = x + y
#     print(result)
#     return result

# a = sum_num(3,5)  #리턴 값: 8
# print(a)

# a = 1
# def func1():
#     a=2
#     return a

# a = func1()
# print(a) #2

# b = [1,2,3]
# def func2():
#     b = [4,2,3]
#     b[0] = 4
#     print(b)

# func2()  #[4, 2, 3]
# print(b) #[1, 2, 3]

##함수 선언부###
# def func1():
#     result = 100
#     return result

# def func2():
#     print("반환값이 없는 함수 실행")

# hap = 0 #전역변수

#####메인 코드 부분#########
# hap = func1()
# print("func1()에서 돌려준 값: %d" % hap) #func1()에서 돌려준 값: 100
# func2()   #반환값이 없는 함수 실행

#군집자료형을 쓰는 이유 중 하나는 반환값이 여러개인 함수인 경우에 사용
# 함수는 문법상 리턴 값이 두개 이상 일 수가 없음. 2개 이상을 반환받아야 할 때 리스트를 사용할 수 있다.
# 리스트에 반환할 값을 넣은 후 리스트 변수를 리턴하면 문법상 오류가 없어짐.
# 
# def sum():
#     pass #예약어이고, 아무기능도 하지 않지만 실행코드 대신 써서 오류방지

# def sub():
#     pass

##########################################
# a = 1
# def func1():
#     a = 2

# func1()  #아무 동작도 안 일어남.? 함수내부에 출력값이나 리턴 값이 없기 때문
# print(a)  #1

# def func1():
#     a = 2
#     return a
# print(func1()) #2  리턴 값이 있으므로 바로 출력 가능
# b = func1()  #리턴 값을 변수에 저장 후
# print(b)   #2
    
# b = [1,2,3]
# def func2():
#     b = [4,2,3]
#     b[0] = 4
#     print(b)

# func2()  #[4, 2, 3]
# print(b) #[1, 2, 3]

# def func(a, *b):  #*는 매개변수가 몇 개이어도 상관없음
#     print(a)
#     print(b)

# func(1,2,3,4,5,6,7)
 
# def func(a,b,c,d,e): #5개의 파라미터(=매개변수)
#     print(a)
#     print(b)

# func(1,3,5,7,9)  #5개 아규먼트(=인자값)

##########모듈 #####################
#1) 표준모듈
#2) 사용자모듈
#3) 외부모듈 

# import turtle  ##파이썬의 표준모듈(내장) - Turtle graphic
# t = turtle.Turtle() #turtle.Turtle(): 거북이 인스턴스생성(객체).인스턴스명 t. 캔버스생성
# t.shape('turtle') #거북이 모양 생성
# t.forward(100) #전진 100
# turtle.exitonclick()  #프로그램 종료를 위해서 클릭시 캔버스 닫힘.

#파일명은 모듈명과 같지 않도록 주의!!

# t = turtle.Turtle()
# t.shape('turtle')
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# turtle.exitonclick()

# import turtle

# t = turtle.Turtle()
# t.speed(10)
# t.shape('turtle')
# t.color('pink')
# t.begin_fill()
# for i in range(5):
#     t.forward(200)
#     t.right(144)
# t.end_fill()
# turtle.exitonclick()

# import sys
# print(sys.builtin_module_names)  #표준 모듈 리스트

# import math
# print(dir(math))

# import turtle
# print(dir(turtle)) #turtle모듈이 제공하는 함수 목록

##########calendar 모듈 #####################
# import calendar
# print(calendar.calendar(2002))

########## time 모듈 ################
# import time
# print(time.ctime())  #Fri Jul 14 14:47:15 2023
# print(time.time())   #1689313635.6972299
# print(1)
# time.sleep(5)  #5초동안 멈춤
# print(2)
########1부터 9까지 출력하는 프로그램###############
# for i in range(1,10): #1~9까지 출력
#     print(i)
#     time.sleep(1) #1초 동안 멈춤

######## 시간내에 단어 입력하는 프로그램 ##########
# word ='cookie'
# start_time = time.time()  #현재의 시간을 시작시간으로 세팅
# answer = input('cookie를 입력해주세요:')
# end_time = time.time() #입력완료 시간을 끝시간으로 세팅
# if word == answer and (end_time-start_time) < 5: #입력시간이 5초미만인가?
#     print('정답')
# else:
#     print('오답')

# import random #무작위 숫자를 뽑아줌 즉, 0~1까지의 숫자

# words = ['cookie', 'apple', 'banana']  # 인덱스 값 words[0]~[2]
# print(random.choice(words))  #랜덤하게 선택해서 출력해줌
# print(random.choice(words))
# print(random.choice(words))

# a = range(1,10) #1부터 9가지 무작위 숫자를 3번 추출
# print(random.choice(a))
# print(random.choice(a))
# print(random.choice(a))

############### random()함수를 이용해서 3개의 단어중 하나를 선택###
# words = ['cookie', 'apple', 'banana']  # 인덱스 값 words[0]~[2]

# print(words[0]) #cookie
# print(random.random())  #0~1 사이의 값을 선택하여 반환함. 0.26512977087979583
# # 0.1 x 3 = 0.3  0.4 x 3 = 1.2   0.9 x 3 = 2.7  
# # 각각의 값을 정수로 변환하면 0,1,2의 값을 반환함.
# print(int(random.random()*3)) # 인덱스 값의 범주인 0~2까지 출력됨
# print(words[int(random.random()*3)]) # 인덱스 값의 범주인 0~2까지 출력됨

# words = ['cookie','apple','banana','melon','blueberry']
# print(words[int(random.random()*5)]) #0.9*5=int(4.5)=>4 0~4까지의 값을 발생
# print(words[random.randint(0,4)])

########클래스 ###########################
# class Car:   #Car클래스 선언부
#     color = ""  #필드1 #자동차의 필드 = 클래스 속의 변수
#     speed = 0   #필드2

#     def upSpeed(self, value):  #메서드1. self:클래스 자기자신.
#     # self는 클래스의 변수(color, speed)를 참조 하기 위하여 사용되는 매개변수.    
#         self.speed += value   # self.speed = self.speed + value
#         # 매개변수 value로 전달 받은 값을 기존의 speed에 추가해라.
    
#     def downSpeed(self, value): #메서드2
#         self.speed -= value

#     #메인코드 부분 : 인스턴스 생성, 메서드 호출.....
# myCar1 = Car()
#     #클래스 객체(인스턴스)를 생성하고 myCar1이라는 이름을 붙임.
# myCar1.color = "빨강"  #인스턴스 생성하고 나면 
# myCar1.speed = 0       #생성된 인스턴스의 필드(변수) 영역이 만들어짐. 

# myCar2 = Car() # 인스턴스 생성
# myCar2.color = "파랑"
# myCar2.speed = 0

# myCar3 = Car() #인스턴스 생성
# myCar3.color ="노랑"
# myCar3.speed = 0

# myCar1.upSpeed(30) 
# print("자동차1의 색상은 %s이며, 현재속도는 %d km입니다" % (myCar1.color, myCar1.speed))

# myCar2.upSpeed(60)
# print("자동차2의 색상은 %s이며, 현재속도는 %d km입니다." % (myCar2.color, myCar2.speed))

# myCar3.upSpeed(0)
# print("자동차3의 색상은 %s이며, 현재의 속도는 %d km입니다." % (myCar3.color, myCar3.speed))

###### 매개 변수가 없는 생성자:기본생성자(메서드) ###########
#클래스 선언부
# class Car:
#     color = ""
#     speed = 0

#     def __init__(self):   #기본생성자 메서드: 매개변수 없음
#         self.color = "빨강"
#         self.speed = 0
    
#     def upSpeed(self,value): #메서드 1
#         self.speed += value
    
#     def downSpeed(self,value): #메서드 2
#         self.speed -= value

# #메인 코드 부분
# myCar1 = Car() #인스턴스 생성과 동시에 생성자메소드를 호출->필드들의 값 세팅
# myCar2 = Car()

# print("자동차1의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
# print("자동차2의 색상은 %s이며, 현재속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

######매개변수가 있는 생성자메서드 ###############
# class Car:
#     color = ""  # 인스턴스변수. 각각의 인스턴스가 생성될 때 그 인스턴스 소속 필드로 세팅.
#     speed = 0   # 인스턴스변수 

#     def __init__(self, value1, value2): #두 개의 매개변수(파라미터)
#         self.color = value1
#         self.speed = value2

#     def upSpeed(self,value):
#         self.speed += value

#     def downSpeed(self,value):
#         self.speed -= value

#     ##메인코드 부분
# myCar1 = Car("빨강", 30)  #인스턴스 생성과 동시에 두개의 아규먼트를 생성자메서드에게 넘겨줌
# myCar2 = Car("파랑", 60)

# print("자동차1의 색상은 %s이며, 현재의 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
# print("자동차2의 색상은 %s이며, 현재의 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

#### 클래스 변수 ###############
#: 여러 개의 인스턴스들이 하나의 변수를 공유. 클래스 내의 전역변수 
# class Car:
#     color =""  #인스턴스변수1. 메서드 안의 지역변수
#     speed =0   #인스턴스변수2
#     count =0   #클래스변수. 클래스 전체에서 전역변수 같은 존재

#     def __init__(self): #기본생성자 :매개변수가 없는 생성자
#         self.speed = 0 #(인스턴스변수)self.으로 부르면 인스턴스 변수이고
#         Car.count += 1 #(클래스변수)Car.으로 변수를 부르면 클래스변수인 것을 알 수 있다.

# #변수 선언 부분
# myCar1, myCar2 = None, None  #변수 선언부는 생략가능.

# #메인코드 부분
# myCar1 = Car() #기본 생성자이므로 아규먼트 필요없음.
# myCar1.speed = 30 
# print("자동차1의 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다." % (myCar1.speed, Car.count))

# myCar2 = Car() #기본 생성자이므로 아규먼트 필요없음.
# myCar2.speed = 60
# print("자동차2의 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다." % (myCar2.speed, Car.count))

class Car:
    pass  #빈클래스 선언 --> 문법 오류 방지


