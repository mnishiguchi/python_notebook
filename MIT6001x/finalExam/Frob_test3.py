from Frob_2 import * 

test_list = Frob('mark')
c = Frob('craig')
insert(test_list, Frob("sam"))
insert(test_list, Frob("nick"))
insert(test_list, c)
insert(c, Frob("xanthi"))
insert(test_list, Frob("jayne"))
insert(c, Frob("martha"))

# move the cursor at the start of the list
cursor = test_list.before
while True:
    if cursor.before != None:
        cursor = cursor.before
    else:
        break

# print one by one        
while True: 
    print '------',cursor.name,'-------'
    if cursor.after != None:  
        print '  next :', cursor.after.name
        cursor = cursor.after
    else:
        break