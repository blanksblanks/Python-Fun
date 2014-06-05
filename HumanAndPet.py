from random import randint

class Human(object):
	'''Represents a human, with a name and pet.'''
	# A class variable, counting the number of humans
	population = 0

	def __init__(self, name, pet):
		pass
		self.name = name
		self.pet = pet
		# When the person is initialized, he/she is added to the population
		Human.population += 1

	# Calls makeNoise on pet and passes a random int as a parameter
	def makePetMakeNoise(self):
		number = randint(1, 10)
		self.pet.makeNoise(number)

	# Calls the eat() method of the pet
	def feedPet(self):
		self.pet.eat()

	# Prints the current population.
	@classmethod
	def populationCount(cls):
		print "The total number of humans is: %d." %(cls.population)

class Pet(object):
	'''Represents a pet, with a name and noise.'''
	def __init__(self, name, noise, canMakeNoise):
		self.name = name
		self.noise = noise
		self.canMakeNoise = canMakeNoise

	def makeNoise(self, number):
		self.number = number
		if self.canMakeNoise == True:
			print self.name , ( (self.noise + ' ') * self.number)
		else:
			print "%s *remains silent*" % (self.name)

	def eat(self):
		print "%s is eating..." % (self.name)

class Cat(Pet):
	'''Represents a cat of the Pet class'''
	# Cat will complain it's still hungry after eating
	def eat(self):
		print "%s is eating..." % (self.name)
		print "I'm still hungry, meow"

class Dog(Pet):
	'''Represents a dog of the Pet class'''
	pass

molly = Cat("Molly", "mrow", True)
karuz = Dog("Karuz", "", False)
summer = Dog("Summer", "ARF!", True)
spicy = Dog("Spicy", "meee-oww", True)
sriracha = Dog("Sriracha", "roof", True)
byte = Cat("Byte", "mew", True)

b = Human("Rob", molly)
l = Human("Liyana", karuz)
a = Human("Alex", summer)
n = Human("Nina", spicy)
k = Human("Karla", sriracha)
s = Human("Sam", byte)

people = [b, l, a, n, k, s]

for person in people:
	person.makePetMakeNoise()
	person.feedPet()
	
Human.populationCount()