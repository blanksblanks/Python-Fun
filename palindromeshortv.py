text = raw_input("Enter text: ")
punctuation = " .,?!:;-—)(]['\"\\/"
for x in punctuation:
    text = text.lower().replace(x, '')
if text == text[::-1]: print "Yes, it is a palindrome"
else: print "No, it is not a palindrome"csrrrrrrrrrr