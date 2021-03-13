lst=[10,20,30]
pos=int(input("enter pos"))
num1=int(input("num1 : "))
num2=int(input("num2 : "))

try:
    print(num1/num2)
    print(lst[pos])
except Exception as e:
    print("Exception occured",e.args)
finally:
    print("finally code here")