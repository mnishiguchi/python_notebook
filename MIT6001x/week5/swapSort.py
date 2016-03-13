import random

def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    ctr = 0
    # iterate L[0] through L[-1]
    for i in range( len(L) ):
        
        # prove the sub-list for the smaller int
        for j in range( i+1, len(L) ):
            
            # everytime smaller int is found,
            # put it in the leftmost position of unsorted sub-list
            if L[j] < L[i]:
                
                # a short form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                ctr += 1 
                print 'ctr',ctr,L
                
    print "Final L: ", L

#### this sorting algorithm is NOT efficient ####
def modSwapSort(L): 
    """ L is a list on integers """
    ctr = 0
    print "Original L: ", L
    for i in range( len(L) ):
        for j in range( len(L) ):
            # ensure L[i] is the greatest int,
            # everytime greater int is found, swap it
            if L[j] < L[i]:
                # swap
                L[j], L[i] = L[i], L[j] 
                ctr += 1
                print 'ctr',ctr,L
    print "Final L: ", L
  
      
## test
##----------------------------------------------

# generate a list of ramdom numbers   
L = [5,4,3,2,1]  
#for i in range(5):
#    L.append( random.randint(0, 100) )
L1=L[:]
L2=L[:]

# execute functions
print
swapSort(L1)
print
modSwapSort(L2)
