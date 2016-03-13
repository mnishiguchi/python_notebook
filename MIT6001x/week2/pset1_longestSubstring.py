'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
'''

s = raw_input('Type a string of lower case characters: ')

longest = ''

for i in range(len(s)) :
    probe = s[i:]
    prev = ''
    candidate = ''
    
    for char in probe :
        if char >= prev :
            candidate = candidate + char
            prev = char
        else :
            break
         
    if len(candidate) > len(longest) :
        longest = candidate
        
print longest    
                
    
