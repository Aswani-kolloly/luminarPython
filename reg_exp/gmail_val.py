from re import *

rule='^[a-z]+\d*@[a-z]+\.[a-z]{2,3}'
id=input("Enter id\n")
matcher=fullmatch(rule,id)
if matcher!=None:
    print("valid")
else:
    print("invalid")