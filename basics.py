import random
verbs = ['Leverage', 'Sync', 'Target']
adjectives = ['Freemium', 'Cloud-based', 'API-based']
nouns = ['Early Adopter', 'Low-hanging Fruit', 'Process']
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)
phrase = verb + ' ' + adjective + ' ' + noun
print(phrase)