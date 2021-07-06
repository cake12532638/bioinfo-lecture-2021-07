#! /usr/bin/env python
"""
import math
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

r = int(sys.argv[1])
pi = math.pi

result = round(r**2 * pi, 2)

print(result)

"""
"""
import math
import sys

if len(sys.argv) !=2 :
    print(f"#usage: python{sys.argv[0]} [num]")
    sys.exit()
elif sys.argv[1].isdigit():
    r = int(sys.argv[1])
    pi = math.pi
    result = round(r**2*pi, 2)
    print(result)
else:
    print("Sorry!")
    sys.exit() 

"""
"""
sys.argv를 사용하면 스크립트 뒤 인수를 입력하는것으로
인수를 직접 줘서 프로그램을 실행시키는 방식이 가능
도스에서 프로그램을 굴리는 방식
sys.arvg 자체는 스크립트 이름을 0번으로 하는 리스트를 작성
"""

#필요한 모듈 로드
import math
import sys
#필요한 변수 먼저 선언
pi= math.pi

#함수는 굳이 쓸필요 없지만, 연습을 위해 사용해봄
def cirarea(a):
#인수 하나를 가진 함수를만드는데
    result = a**2*pi
#결과는 a의 제곱에 원주율을 곱함(원의넓이)
    return result
#결과 반환

#예외처리(스트링일 경우? 인자를 여러개 줬을 경우?)
if len(sys.argv) !=2:
#만약 리스트 인자가 2개가 아닐 경우
    print(f"#usage : python {sys.argv[0]} [num]")    
#사용법에 대한 메세지 출력
#중괄호를 이용한 포멧팅 기법 사용
#sys.argv[0]은 스크립트 이름을 이야기함
#인자 여러개일경우는 여기서 컷
    sys.exit()
#종료
elif sys.argv[1].isdigit():
    r= int(sys.argv[1])
    print(cirarea(r))
#그게 아닌경우 숫자인지 확인한 뒤  원의 넓이구하는 함수로
else :
    print(f"please input intiger\n\
#usage : python {sys.argv[0]} [num]")
    sys.exit()
#사용방법 일러주고 끝(스트링일경우 여기서 컷)


