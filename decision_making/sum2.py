a=input("Enter number")
s=int(a)
sum=0
t=0
str=""
for i in range(0,int(a)):
    sum=sum+s*(10**int(i))
    t=t+sum
print(t)