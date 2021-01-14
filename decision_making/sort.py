num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

for i in range(1,4):
    if (num1<=num2 & num1<=num3):
        print(num1)
        num1=num2

    elif num2<=num1 & num2<=num3:
        print(num2)
        num2=num3

    elif num3<=num1 & num3<=num1:
        print(num3)
        num3=num2


