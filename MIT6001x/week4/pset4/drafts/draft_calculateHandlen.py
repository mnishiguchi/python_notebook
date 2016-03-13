def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # get list of counters
    letterCounters = hand.values()

    # get sum of counters
    handLength = 0
    for each in letterCounters:
        handLength += each
        
    return handLength

# test
hand = { 'a': 2, 'b':3, 'c': 1 }
print calculateHandlen(hand)
