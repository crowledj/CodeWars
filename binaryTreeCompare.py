## Binary Tree compare :

def compare(a, b):

    if(a!= None and b!= None):        
        if(a.val == b.val):   
            #general case requires all child nodes to be non null pointers 
            if(a.left != None and b.left != None and a.right != None and b.right != None):
                if(a.left.val == b.left.val and a.right.val == b.right.val):
                    if not compare(a.left,b.left):
                        return False    
                    if not  compare(a.right,b.right):
                        return False    
                else:
                    return False     
            #Case when all child nodes are None pointers - then trees are identical        
            elif(a.left == None and b.left == None and a.right == None and b.right == None):
                #return True 
                pass                
            #Case where same oriented children are null pointers on both trees
            elif( (a.left == None and b.left == None) or (a.right == None and b.right == None) ):
                if not compare(a.left,b.left):
                    return False
                if not compare(a.right,b.right):
                    return False
            #any other combo means trees differ:    
            else:
                return False 
        #parent values differ        
        else:
            return False                     
    else:       
        if(a== None and b== None):
            pass
        else:
            return False               
            
    return True  