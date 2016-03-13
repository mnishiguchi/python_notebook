from Frob import * 

test_list = Frob('zsa zsa')
a = Frob('ashley')
m = Frob('marcella')
v = Frob('victor')

insert(test_list, m)
insert(m, a)
insert(a, v)

for e in [test_list, a, m, v]:
    print '------------',e.name,'------------'
    print 'before: ',
    if e.before == None:
        print 'None',
    else:
        print e.before.name,
    print '  after:',
    if e.after == None:
        print 'None'
    else:
        print e.after.name