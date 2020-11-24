import string
READ_FILENAME = "book.txt"
READ_MODE = 'r'
WRITE_FILENAME = 'summary.txt'
FILE_MODE = 'w'

book = open(READ_FILENAME , 'r')
with book:
    data = book.read().upper()
character_dictionary = {} 
for char in data:
    if char.isalpha(): 
        character_dictionary[char] = data.count(char)
  
summary = open(WRITE_FILENAME, 'w')
with summary:
    for letter in sorted(character_dictionary.keys()): 
        summary.write(f'{letter} {character_dictionary[letter]}\n')
    if len(character_dictionary) == 26:
         summary.write("\nIt has all letters.")
    else:
         summary.write("\nIt doesn't have all letters.")
