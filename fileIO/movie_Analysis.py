f=open("movies.csv","r")
dict={}

for line in f:
    data=line.rstrip().split(",")
    year=data[2]
    id=data[0]
    if year not in dict:
        dict[year]={ id:{"movie":data[1],"rating":data[3],"time":data[4]}}
    else:
        dict[year] ={ id:{"movie":data[1],"rating":data[3],"time":data[4]}}
print(dict,end="\n")