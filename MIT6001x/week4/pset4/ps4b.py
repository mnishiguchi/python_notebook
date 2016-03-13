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
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n): 
    """
    [Computer mode]
    Allows the user to automatically play the given hand, as follows:

    * The hand is displayed.
    * After computing every turn: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    assert n >= len(hand), 'length of hand must be equal to or lesser than n'
    
    # Keep track of the total score
    totalScore = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        
        # Display the hand
        print
        print 'Current Hand:',
        displayHand(hand)
        
        # compute best word possible
        word = compChooseWord(hand, wordList, n)
        
        # If the input is a single period:
        if word == None:   
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # Tell the user how many points the word earned, 
            # and the updated total score, in one line followed by a blank line
            earnedScore = getWordScore(word, n)
            totalScore += earnedScore
            print '\"%s\" earned %d points. Total: %d points' % (word, earnedScore,totalScore)
                
            # Update the hand 
            hand = updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print
    print 'Total score:', totalScore, 'points.'
    
    
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
    
    # remember hand
    hand = {}
    
    while True:
        # user prompt #0
        while True:
            # Asks the user to input 'n' or 'r' or 'e'.
            print
            userInput0 = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            
            # If the user inputs 'e', exit the game.
            if userInput0 == 'e':
                return
                
            # If the user inputs 'n', let the user play a new (random) hand.
            elif userInput0 == 'n':
                # get a new hand
                hand = dealHand(HAND_SIZE)  
                break 
                
            # If the user inputs 'r', let the user play the last hand again.
            elif userInput0 == 'r':
                if hand == {}:
                    print
                    print 'You have not played a hand yet. Please play a new hand first!'
                else:
                    break
                        
            # If the user inputs anything else, tell them their input was invalid.    
            else:
                print
                print 'Invalid command.'
        
        # user prompt #1
        while True:
            # Asks the user to input a 'u' or a 'c'.
            print
            userInput1 = raw_input('Enter u to have yourself play, c to have the computer play: ')
            
            # If the user inputs anything that's not 'c' or 'u', keep asking them again.
            if userInput1 == 'u':
                playHand(hand, wordList, HAND_SIZE)
                break
            # If the user inputs 'n', let the user play a new (random) hand.
            elif userInput1 == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
                break
            # If the user inputs anything else, tell them their input was invalid.    
            else:
                print
                print 'Invalid command.'

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


