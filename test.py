from main import *

with open('Words.txt', 'r') as file:
    file_contents = file.read()

wordlist= file_contents.split(', ')


#words = SelectWords(wordlist, 5)
grid = MakeGrid(15, 15)
print("Empty : \n")
for row in grid:
    print(row)
print("\n \n \n Filled : \n")
words = SelectWords(wordlist, 1, 3)
FillGrid(grid, words)