class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
     
    def __eq__(self, other):
        '''returns True if coordinates refer to same point in the plane
            (i.e., have the same x and y coordinate)
        '''
        return self.x == other.x and self.y == other.y

    # In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.
    def __repr__(self):
        ''' returns a string that looks like a valid Python expression
            that could be used to recreate an object with the same value.
        '''
        # return 'Coordinate(%r, %r)' % (self.x, self.y)
        return 'Coordinate(' + str( self.getX() ) + ', ' + str( self.getY() ) + ')'
        
        
## test
##----------------------------------

c = Coordinate(5, 1)
d = c
print c == d # compare based on definition of __eq__
print c
print repr(c)
print eval( repr(c) ) == c
print c.__class__, c.__dict__