#! /usr/bin/env python

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
