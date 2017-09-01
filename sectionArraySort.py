#In this kata you are given an array to sort but you're expected to start sorting from a specific position of the array (in ascending order) and optionally you're given the number of items to sort.

#array - array to sort
#start - position to begin sorting
#length - number of items to sort (optional)
#if the length argument is not passed or is zero, you sort all items to the right of the start postiton in the array
#

def sect_sort(array, *posArgs):

    posArgs=list(posArgs)
    start=posArgs[0]
    if(len(posArgs) >=2):
        length=posArgs[1] 
    else:
        length=0    
  
    intTruth=all(isinstance(x, int) for x in array)
    floatTruth=all(isinstance(x, float) for x in array)
    
    #Check if the list contains any elements
    if not array :
        return []

    if (start+length > len(array)):
        length=len(array)
    
    if( length and  (intTruth or floatTruth) ): 
        #copy a portion of the inputted list to sort
        tmp=array[start:start+length]
        tmp.sort()

        if tmp:
            #join the unsorted pieces of the original lust with the temporary sorted piece
            array=array[:start]+tmp+array[start+length:len(array)]
            
    elif ( (intTruth or floatTruth) and length==0 ):

        tmp=array[start:len(array)]
        tmp.sort() 

        if tmp:
            array=array[0:start]+tmp

    else:
        print("not all array elements are not numeric -- please fix! \n")
        return []
    
    return array