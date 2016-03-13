def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom) for item in list_of_numbers]

# change the definition of SimpleDivide so that the call does not raise an exception.
# When dividing by 0, FancyDivide should return a list with all 0 elements.
# Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.

def SimpleDivide(item, denom):
    result = 0
    try:
        result = item / denom
    except ZeroDivisionError as e:
        print e
        return 0
    else:
        print 'success'
        return result

#### test ####

aList = [0, 2, 4]

def test(aList):
    for index in range( len(aList) ):        
        print FancyDivide(aList, index) 

test(aList) 