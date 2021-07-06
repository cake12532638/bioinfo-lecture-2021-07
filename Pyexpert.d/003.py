#! /usr/bin/env python
"""
import sys

if len(sys.argv) !=2: #2와 다르면
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])

result = "odd"


if num % 2 ==0:
    result = "even"

print(result)
"""
"""
if-else 홀짝 판별
sys.argv로 인수를 받을 예정
"""
#필요한 모듈 로드
import sys
#편하게 코드짤래
arg0 = sys.argv[0]
arg1 = sys.argv[1]
#예외처리

if len(sys.argv) !=2:
    print(f"#usage : python {arg0} [num]")
    sys.exit()
elif arg1.isdigit() :
    num = int(arg1)
    if num % 2 ==0:
        result = 'even'
    elif num % 2 ==1:
        result = 'odd'
else :
    print(f"input intiger\n\
#usage : python {arg0} [num]")
    sys.exit()
print(result)





