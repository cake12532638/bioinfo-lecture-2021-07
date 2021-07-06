#! /usr/bin/env python
"""
if len(sys.argv) !=3 :


num1 =3
num2 =5

print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1*num2)

print(num1%)
print(num2%)

print(num1**2)
print(num2**2)
"""
#두 변수의 사칙연산, 나머지 , 제곱이 나오도록 하기
#sys 사용해서 인수를 바로 입력할수 있게 만들기
#모듈 불러오기
import sys
#편하게 할수있는 리스트 작성
#리스트 안씀, 스트링으로 들어가서 쓸 이유가 없었다
l_op=["+","-","*","/","%"]
#예외 처리

if len(sys.argv) !=3 :
    print(f"#usage : python ./{sys.argv[0]} [num1] [num2]")
    sys.exit()
#인수를 세개 이상 했을경우 사용법 알려주고 끝
#문자열 포맷팅 사용
elif sys.argv[1].isdigit() and sys.argv[2].isdigit():
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    print(n1,"+",n2,":", n1 + n2)
    print(n1,"-",n2,":", n1 - n2)
    print(n1,"*",n2,":", n1 * n2)
    print(n1,"/",n2,":", n1 / n2)
    print(n1,"%",n2,":", n1 % n2)
    for i in sys.argv[1:]:
        print(i,"squre:",int(i)**2)
#for 문 써서 프린트를 한줄 줄여봄
#ilst 속 인자는 string 이라서 int를 따로 해줘야 했다
else :
    print(f"please input intiger\n\
#usage : python {sys.argv[0]} [num1] [num2]")
