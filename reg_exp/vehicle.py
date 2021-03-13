from re import *
rule='[a-zA-Z]{2}\s?\d{2}\s?[a-zA-Z]{2}\s?\d{4}'

variable=input("enter veh num\n")
matcher=fullmatch(rule,variable)
if matcher!=None:
    print("ok")
else:
    print("not ok")
