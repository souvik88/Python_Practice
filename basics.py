'''
import random
verbs = ['Leverage', 'Sync', 'Target']
adjectives = ['Freemium', 'Cloud-based', 'API-based']
nouns = ['Early Adopter', 'Low-hanging Fruit', 'Process']
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)
phrase = verb + ' ' + adjective + ' ' + noun
print(phrase)
'''
"""
sum = 50 + 50
print(sum)
"""

# open and read a text file from a location
'''
my_file = open("test.txt")
my_file_read = my_file.read()
my_file.close()
print(my_file_read)
print(my_file_read)
'''
# open and read a text file from any location
'''
myfile = open("Z:\\test.txt")
myfile_read = myfile.read()
myfile.close()
print(myfile_read)
'''
# try ~ except to check if file exist
'''
try:
	with open("text.txt") as f:
		text = f.read()
except FileNotFoundError:
	text = None

print(text)
'''
'''
words = ["Writing a file using Python code"]
with open("sentence.txt", "w") as f:
    for w in words:
        f.write(w)
with open("sentence.txt", "a") as f:
    print(30*"=", file=f)
    print("End of text file.", file=f)
print(words)
'''
print('testing')