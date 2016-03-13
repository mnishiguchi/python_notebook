# towersOfHanoi.py	

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    
    #base case
    if n == 1:
        printMove(fr, to)
        
    else:
        # move to spare all except for the largest one
        Towers(n-1, fr, spare, to)        
        # move the largest one to Target
        Towers(1, fr, to, spare)        
        # move the rest to Target
        Towers(n-1, spare, to, fr)
        
#test
Towers(6, '--A--', '--B--', 'spare')