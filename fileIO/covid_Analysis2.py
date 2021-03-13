f=open("covid_19_india.csv","r")
i=0
lst=[]
dict={}
for line in f.readlines()[1:]:
    data=line.rstrip("\n").split(",")
    state=data[3]
    if state not in dict:
        dict[state]={"Date":data[1],"Time":data[2],"ConfirmedIndianNational":data[4],"ConfirmedForeignNational":data[5],"Cured":data[6],"Deaths":data[7],"Confirmed":data[8]}
    else:
        dict[state] = {"Date": data[1], "Time": data[2], "ConfirmedIndianNational": data[4],"ConfirmedForeignNational": data[5], "Cured": data[6], "Deaths": data[7], "Confirmed": data[8]}
for k,v in dict.items():
    print(k,"=>",v,end="\n")
def print_covid_info(**kwargs):
    state=kwargs["state"]
    prop=kwargs["prop"]
    if state in dict:
        print(prop," in ",state," ",dict[state][prop])
    else:
        print("Not foud")
print_covid_info(state="Kerala",prop="Cured")
