from Frob import * 

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    front = start.before
    if  front == None:
        return start
    return findFront(front)
    
# **** test ****

# create a linked list
test_list = Frob('python')
aList = ['java','ruby','javaScript','masa','christine','jquery',
    'php','mySql','css','html','android']
for elem in aList:
    insert(test_list, Frob(elem))

# move the cursor at the start of the list
cursor = findFront(test_list)

# print one by one        
while True: 
    print '------',cursor.name,'-------'
    if cursor.after != None:  
        print '  next :', cursor.after.name
        cursor = cursor.after
    else:
        break