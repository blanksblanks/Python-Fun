# Defines a function is_palindrome() that recognizes palindromes
# (i.e. words that look the same written backwards). 

# uses slicing feature to reverse text
# seq[a:b] code makes slices froms sequence a to b
# providing third argument that determines the 'step' by which slicing is done
# default step is 1, giving negative step -1 returns text in reverse
def reverse(text):
    return text[::-1]

# if the original text and reversed are equal, it's a palindrome
def is_palindrome(text, punctuation = " .,?!:;-—)(]['\"\\/"):
    text = text.lower() #  makes text lower case
    for x in punctuation: # for loop checks text for x items from tuple
        text = text.replace(x, '') # removes x items
        # 'print text' can be used to see inefficient process of loop
    return text == reverse(text) # checks if text matches reverse text

# if text == 'Q': sys.exit() works as a way for user to quit

# raw_input() function takes string as argument and returns it to user
something = raw_input("Enter text: ")
if is_palindrome(something): # if true
    print "Yes, it is a palindrome"
else:
    print "No, it is not a palindrome"
