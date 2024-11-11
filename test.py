from main import *

with open('Words.txt', 'r') as file:
    file_contents = file.read()

wordlist= file_contents.split(', ')


words = SelectWords(wordlist, 5)
print(words)