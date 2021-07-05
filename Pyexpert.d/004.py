#! /usr/bin/env python

import sys

if len(sys.argv) !=2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()    

n1 = int(sys.argv[1])

result = "neither 3,7"

if n1 % 3 ==0 and n1 % 7 == 0:
    result = "3x and 7x"
elif n1 % 3 == 0:
    result = "3x"
elif n1 % 7 == 0:
    result = "7x"

print(result)
