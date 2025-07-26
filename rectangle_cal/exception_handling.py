
try:
    print(x)
except NameError:
    print("variable x is not defined.")
else:
    print("Everything went wrong.")
    
    x=-1
    
    if x < 0:
        raise ValueError("Sorry, no numbers below zero")