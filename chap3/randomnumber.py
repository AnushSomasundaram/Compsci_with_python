import random

def rando(a,b):
    
    print("Three random numbers are:-")
    
    for i in range (0,3):
        t=random.randint(a,b)
        print(t)

x=int(input("Enter the starting of range "))

y=int(input("Enter the ending of range:-")) 

rando(x,y)


