from re import *
rule='(\+\d{2}\s)?\d{10}'
var=input("Enter phnnum\n")
match=fullmatch(rule,var)
if match!=None:
    print("valid")
else:
    print("invalid")