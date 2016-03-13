#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # copy of dictionary
    hand_copy = hand.copy()

    # check if word is entirely composed of letters in the hand
    for letter in word:
        # letter exsists in hand
        if letter in hand_copy.keys():
            # ensure letter is not consumed
            if hand_copy[letter] > 0:
                # decrement counter
                hand_copy[letter] -= 1
            else: 
                return False
        else:
            return False
    
    # Finally, check if word is in the wordList
    return word in wordList
