from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#

# helper function to check if word is entirely composed of letters in the hand
def isConstructableWord(word, hand):
    """
    Returns True if word can be constructed entirely with letters in the hand.
    Otherwise, returns False.

    Does not mutate hand
   
    word: string, a word listed in words.txt
    hand: dictionary (string -> int)
    """
    # copy of dictionary
    hand_copy = hand.copy()
    
    # check if word is entirely composed of letters in the hand
    for letter in word:
        # ensure letter exsists in hand
        if letter not in hand_copy.keys():
            return False

        # ensure letter is not consumed
        if hand_copy[letter] > 0:
            # decrement counter
            hand_copy[letter] -= 1
        else: 
            return False
    return True


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
      
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None

    # For each word in the wordList
    for word in wordList:
        score = 0
        # If you can construct the word from your hand
        if isConstructableWord(word, hand):
            
            # Find out how much making that word is worth
            score = getWordScore(word, n)
              
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word

    # return the best word you found.
    return best_word
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# test
#

wordList = loadWords()
print

# test suit format [(hand, wordList, n), expected result]
testLists = [
    [ ( { 'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1 }, wordList, 6 ), 'appels' ],
    [ ( { 'a': 2, 'c': 1, 'b': 1, 't': 1 }, wordList, 5 ), 'acta' ],
    [ ( { 'a': 1, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2 }, wordList, 12 ), 'immanent' ],
    [ ( { 'e': 1, 'z': 2, 'q': 2, 'n': 2, 't': 2 }, wordList, 12 ), None ]
]

def test_compChooseWord(testLists):
    for alist in testLists:
        hand = alist[0][0]
        wordList = alist[0][1]
        n = alist[0][2]
        word = compChooseWord(hand, wordList, n)
        
        if word == alist[1]:
            print '\tSUCCESS:', word
        else:
            print '\tFAILURE:', word, '\texpected:', alist[1]

# execute test
test_compChooseWord(testLists)