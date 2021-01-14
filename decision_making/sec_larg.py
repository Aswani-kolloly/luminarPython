a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if a >= b and a >= c:
    if b >= c:
        print("2nd largest number\n", b);
    else:

        print(" 2nd largest number\n", c);


elif (b >= a and b >= c):
    if (a >= c):

        print(" 2nd largest number\n", a);

    else:

        print("2nd largest number\n", c);




elif (a >= b):

    print(" 2nd largest number\n", a);
else:

    print("\n\n%.2lf is the 2nd largest number\n", b);






