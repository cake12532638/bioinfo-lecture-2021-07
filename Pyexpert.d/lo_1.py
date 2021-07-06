#! /usr/bin/env python
"""
nucl = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCT\
GTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


print("A:", nucl.count("A"), ("\nT:"), nucl.count("T"),\
 "\nG:", nucl.count("G"), "\nC:", nucl.count("C"))

"""

#for문 input 사용해서 하기

nucl =input("input your DNA")

l_nuc = ["A", "C", "G", "T"]

nucl_u = nucl.upper()

for i in l_nuc :
    print(i,":", nucl_u.count(i))

