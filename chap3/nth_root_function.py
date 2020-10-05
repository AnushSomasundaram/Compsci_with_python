#when an value is assigned to the parameterss in a function if a value is not assigned during function call 
#it will automatically consider the original value

def nth_root(x,n=2):
    nthroot=x**(1/n)
    print("The",n,"th/rd/nd root of",x,"is",nthroot,".")

print("Calling function with x=4 and n=2")

nth_root(4,2)

print("calling function with x=4 and not specifying n value")

nth_root(4)


