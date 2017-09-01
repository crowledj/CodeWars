# summing the intgers from 1->n (via gauss's childhood trick!)
def f(n):
    
    try:
        #check if number is positive and an integer, otherwise return error
        if n <= 0 or (n % 1 != 0):
            return None
        else:
           return (n*(n+1)/2)
    #catch the case when a non number , i.e a string is passed in to the function     
    except TypeError as e:
        print("wrong type passed as argument to function -- error code -- ")
        return None
