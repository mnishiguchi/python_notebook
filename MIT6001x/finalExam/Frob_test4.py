from Frob import * 

test_list = Frob('leonid')
a = Frob('amara')
j1 = Frob('jennifer')
j2 = Frob('jennifer')
s = Frob('scott')

insert(test_list, s)
insert(s, j1)
insert(s, j2)
insert(j1, a)

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