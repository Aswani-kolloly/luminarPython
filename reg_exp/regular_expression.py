from re import *
p="ab"
str="abswabqwab"
matcher=finditer(p,str)
c=0
for match in matcher:
    print(match.start())
    print(match.group())
