#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    assert type(word) == str and word.islower() or word == '', 'Invalid input'
    
    # create a copy of hand
    hand_updated = hand.copy()  # Has no side effects: does not modify hand
    
    # Assumes that 'hand' has all the letters in word.
    if word == '':
        return hand
    
    try:
        for letter in word:
            if hand_updated[letter] > 0:    # if letter exists in hand
                hand_updated[letter] -= 1   # decrement quantity by 1
            else:
                raise ValueError('Invalid word: number of letter is insufficient')
        
    except KeyError as e:
        print e,
        print ': can\'t find this letter in hand'
    
    except ValueError as e:
        print e
        
    else:
        return hand_updated

# test
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = 'quail'   
print updateHand(hand, word)
