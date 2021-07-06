#! /usr/bin/env python
"""
val = 0

for i in range(1,11):
    val += i

print(val)
"""
"""
#곱으로 바꾸기 

val = 1

for i in range(1,11):
    val *= i

print(val)
"""
"""
import sys

n= int(sys.argv[1])
val=1

while n>0 :
    val *= n
    n -= 1
print(val)
"""
#While 문을 사용해서 Factorial 값 구하기
#sys.argv로 인수 받기
# 3! 이면 3*2*1이 되어야함
#7! 이면 7*6*5*4*3*2*1 이런식
#모듈 불러오기
import sys
#변수 하나
val =1

#예외처리
if len(sys.argv) !=2:
    print(f"#usage {sys.argv[0]} [num]")
    sys.exit()
elif sys.argv[1].isdigit():
    i=int(sys.argv[1])
    while i > 0:
        val *= i
        i -= 1
else :
    print(f"#usage {sys.argv[0]} [num]")
    sys.exit()
print(sys.argv[1],"!:",val)
