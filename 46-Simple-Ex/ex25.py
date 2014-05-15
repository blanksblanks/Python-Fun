import re

def make_ing_form(verb):
	''' (str) -> str
	Defines function make_ing_form, which given an infinitive verb returns present
	participle form. In English, the present participle is formed by adding the suffix
	-ing to the infinite form: go -> going. A simple set of heuristic rules can be
	given as follows:
		1. If the verb ends in e, drop the e and add ing
		(if not exception: be, see, flee, knee, etc.)
		2. If the verb ends in ie, change ie to y and add ing
		3. For words consisting of consonant-vowel-consonant, double the final letter
		before adding ing
		Test your function with words such as lie, see, move and hug.
	'''
	exceptions = ['be', 'see', 'flee', 'knee']
	if verb in exceptions: # Address exceptions first
		return verb + 'ing'
	else:
		if verb.endswith('ie'): # Rule 2 because we must address ie before e
			return re.sub('ie$', 'ying', verb)
		elif verb.endswith('e'): # Rule 1 because it applies to non-ie verbs
			return re.sub('e$', 'ing', verb)
		elif not verb.endswith(r'([bcdfghjklmnpqrstvwxz][aeiou][bcdfghjklmnpqrstvwxz])'):
			return verb + verb[-1] + 'ing' # Rule 3, consonant, vowel, consonant
		else: # Regular verbs
			return verb + 'ing'

print make_ing_form('lie')
print make_ing_form('see')
print make_ing_form('move')
print make_ing_form('hug')
print make_ing_form('create')
print make_ing_form('snap')