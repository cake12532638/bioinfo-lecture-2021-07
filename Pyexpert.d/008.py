#! /usr/bin/env python
"""
def greet():
    print("Hello, Boinformatics")

def greet1(name):
    print(f"Hello, {name}") #반환이 되는건 return이 있어야함

def greet2(num):
    return(num*2)

greet()
ret1 =  greet1("Ken")
print(ret1)

ret2 = greet2(3)
print(ret2)

"""
#구구단 짝수단 홀수단만 출력하도록 하기
#중첩 for문 사용
#sys로 받기

#모듈 불러오기
import sys

#예외처리
if len(sys.argv) !=2 :
    print(f"#usage : python {sys.argv[0]} 'even' or 'odd'")
    sys.exit()
elif sys.argv[1] == 'even':
    for i in range(2,9,2):
        for a in range(1,10,1): 
            print(i,"*",a,"=",i*a)
elif sys.argv[1] == 'odd':
    for i in range(1,10,2):
        for a in range(1,10,1): 
            print(i,"*",a,"=",i*a)
else:
    print(f"#usage : python {sys.argv[0]} 'even' or 'odd'")
