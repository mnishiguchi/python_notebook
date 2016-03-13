#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    lenCtr = 0
    this = []
    
    # convert entire text to a list of words
    words = text.split()
    
    # get a length of all the word
    for each in words[:]:
        lenCtr += len(each) + 1  # word length + whitespace
        this.append(each)  # add word to this line
        words.remove(each)  # remove word from remaining text
        print this,
        print words,
        print lenCtr
        if  lenCtr >= lineLength:
             # insert \n when lineLength is reached
            this.append('\n')
            break
    # if itarable is exhausted, just return entire text
    else:
        return ' '.join(words)
    # remaining text
    text = ' '.join(words)
    return ' '.join(this) +  insertNewlines(text, lineLength)
   
## -------test  insertNewlines(text, lineLength) ----------
text = 'I really enjoy coding. I want to learn python, Java, JavaScript, Ruby, etc too many things'
print insertNewlines(text, 12)