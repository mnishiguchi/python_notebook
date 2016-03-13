import math

def sq(x):
    return x * x


class Coordinate(object):
    # this method is called when an object is created
    def __init__(self, x, y):  
        self.x = x
        self.y = y
    def __str__(self):
        return "<" + str(self.x) + ","+str(self.y) + ">"
    def distance(self, other):
        return math.sqrt( sq(self.x - other.x)
                         + sq(self.y - other.y) )

c = Coordinate(3,4)
Origin = Coordinate(0,0)
print 'distance:', c.distance(Origin)
print c
print Coordinate
print Coordinate.distance
print Coordinate.__init__
print isinstance(c, Coordinate)

