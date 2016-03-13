# Let's use an approximation algorithm to estimate the area under this curve!
# first splitting up the area into equally-sized rectangles 
# (in this case, six of them, one rectangle per year):

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    
    # point of time (initialize to start)
    year = start

    # total exposure
    exposure = 0
    
    while year < stop:
        # area of single rectangle (height: f(year), width: step)
        exposure += f(year) * step
        year += step
    
    return exposure       
               
# calculate activity of Cobalt-60 at a given point of time
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

# test
(start, stop, step) = (40, 100, 1.5)
print 'start:', start, 'stop:', stop, 'step:', step, 'radiationExposure:', radiationExposure(start, stop, step)