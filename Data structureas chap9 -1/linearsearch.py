def linearsearch():

    noe = int(input("Enter the number of elements in the data set:-"))

    i=0
   
    values = []

    while i < noe :
        values.append(int(input("Enter the element:-")))
        i = i+1

    """print("The dataset is :-")
    
    item = 0
    while item < noe :
        print(values[item])
        item = item +1"""

    ele = int(input("Enter the value to be found:- ")) 

    x =0
    
    if x<noe:
        while x < noe:
            if ele == values[x]:
                print("The value you are looking for is in the ",x+1,"position." )
                return()
            else:
                x = x+1
    else:
        "The value you are searching for does not exist "

linearsearch()
