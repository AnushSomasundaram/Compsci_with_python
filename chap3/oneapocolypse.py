def howmanyones(a,b):

    counta=0    
    for i in str(a):
        if i=='1':
            counta += 1
        
    countb=0    
    for i in str(b):
        if i=='1':
            countb += 1

    if counta>countb:
        print("The number of ones in A is greater.")
    
    elif countb>counta:
        print("The number of ones in B is greater.")

    elif counta==0 and countb==0:
        print("No ones in both numbers")
    
    elif counta==countb:
        print("Both numbers have equal number of ones")

howmanyones(202,200)