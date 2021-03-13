f=open("covid_19_india.csv","r")
i=0
dict={}

for line in f.readlines()[1:]:
    list1=line.split(",")
    state=list1[3].rstrip("***")
    confirmed_cases=int(list1[8])
    if state not in dict:
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,"=>",v,end="\n")

