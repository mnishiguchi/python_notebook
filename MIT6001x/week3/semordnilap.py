# recursive function that the wrapper function calls. 
def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) == 1 or len(str2) == 1:
        return False
        
    # 0th letter of str1 equals to last letter of str2
    if str1[0] == str2[-1]:
        # if length is 2, done
        if len(str1) == 2 and len(str2) == 2:
            return True
        #else check substrings
        else:
            return semordnilap(str1[1:], str2[:-1])
    else:
        return False
 
      
# wrapper function to check base case
# base case : length 1
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False
    return semordnilap(str1, str2)  


# test
print semordnilapWrapper('tact', 'cat')