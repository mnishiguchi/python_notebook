from Frob import * 

test_list  = Frob('eric')
a = Frob('andrew')
r = Frob('ruth')
f = Frob('fred')
m = Frob('martha')

insert(test_list, a)
insert(a, r)
insert(r, f)
insert(f, m)

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

       