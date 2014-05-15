import re

def make_3sg_form(verb):
    ''' (str) -> str
    Defines a function  make_3sg_form() which given a verb in infinitive form returns its
    third person singular form. The third person singular verb form in English is d
    distinguished by the suffix -s, which is added to the stem of the infinitive form:
    run -> runs. A simple set of rules can be given as follows:
        1. If the verb ends in y, remove it and add ies
        2. If the verb ends in o, ch, s, sh, x or z, add es
        3. By default just add s
    Note rules must be regarded as heuristic, and won't work for all cases.
    '''
    ruletwo = 'o', 'ch', 's', 'sh', 'x', 'z'
    if verb.endswith('y'): # Use string method endswith() for Rule 1
        return re.sub('y$', 'ies', verb)
    elif verb.endswith(ruletwo): # Uses a var because endswith() takes 3 args max
        return verb + 'es'
    else: # Rule 3
        return verb + 's'

print make_3sg_form('try')
print make_3sg_form('brush')
print make_3sg_form('run')
print make_3sg_form('fix')
print make_3sg_form('salivate')
print make_3sg_form('gallivant')
print make_3sg_form('relish')
print make_3sg_form('see')