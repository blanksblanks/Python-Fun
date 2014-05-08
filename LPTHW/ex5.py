name = 'Molly'
age = 2 # estimation cause she's a stray kitty
height = 22.5*2.54 # in to cm
weight = 10.0*0.453592 # lb to kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "She's %d years old." % age
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on if she's had chocolate." % teeth

# This next command shows how you input multiple fields.
# NOTE: use %s for strings, and %d for numbers.
# %r will let you input anything, but is usually used for debugging purposes.
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)

# Besides using %s, %d, and %r, there is another way of doing this by using format.
# You won't have to differentiate between strings and numbers for this. 
print "If I add {0}, {1}, and {2} I get {3}." .format(
age, height, weight, age + height + weight)

# If you use format, the numbers within the curly brackets are also optional.
# You will get the same output as the above if you type:
print "{}'s eyes are {} and her height is {}" .format(name, eyes, height)

# If you haven't defined the variables, you can just define them within format also:
print "{} is a {}." .format("Spicy", "pregnant leopard gecko")
## This will print "Spicy is a pregnant leopard gecko."
print "{name} is a {thing}." .format(name="Spicy", thing="pregnant leopard gecko") 
## This will also print "Spicy is a pregnant leopard gecko."