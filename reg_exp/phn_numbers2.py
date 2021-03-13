from re import *
print("email validation\n***************\n\nemail lists:\n................")
f=open("email_id","r")
lst_email_id=[email.rstrip("\n")  for email in f]
print(lst_email_id)

#email validation
rule='^[a-z]+\d*@[a-z]+\.[a-z]{2,3}'

lst_valid_emails=[]
for email_id in lst_email_id:
    if fullmatch(rule,email_id):
        lst_valid_emails.append(email_id)
print("\nvalid email lists\n-------------------------")
print(lst_valid_emails)

#phone number validation
print("\nphn number validation\n***************\n\nphn num lists:\n................")
f=open("phn_num_list","r")
lst_phnum=[phno.rstrip("\n")  for phno in f]
print(lst_phnum)

rule2='(\+\d{2}\s)?\d{10}'

lst_valid_phn=[]
for phno in lst_phnum:
    if fullmatch(rule2,phno):
        lst_valid_phn.append(phno)
print("\nvalid phn num\n-------------------------")
print(lst_valid_phn)

#vehicle number validation

print("\nveh number validation\n***************\n\nveh num lists:\n................")
f=open("veh_reg_num","r")
lst_veh_regno=[num.rstrip("\n")  for num in f]
print(lst_veh_regno)

rule3='[a-zA-Z]{2}\s?\d{2}\s?[a-zA-Z]{2}\s?\d{4}'

lst_valid_vehnum=[]
for num in lst_veh_regno:
    if fullmatch(rule3,num):
        lst_valid_vehnum.append(num)
print("\nvalid veh num\n-------------------------")
print(lst_valid_vehnum)