import random
def  number(n):
    #n=int(input("No of digits in number:- "))

    typestr = ""

    y=random.randint(1,9)

    typestr += str(y)
    for i in range(0,n-1):

        x=random.randint(0,9)
        typestr += str(x)

    print(typestr)

number(7)

