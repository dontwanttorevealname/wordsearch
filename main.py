import random
import random

def SelectWords(wordlst, count, size):
    if not isinstance(wordlst, list):
        print("Error; Input is not a 'list' variable.")
        return
    if count > len(wordlst):
        print("Error; Not enough words in list.")
        return
    if len(wordlst) == 0:
        print("Error; No words in list.")
        return
    filtered_words = [word for word in wordlst if len(word) <= size]
    if len(filtered_words) < count:
        print("Error; Not enough words of the specified size.")
        return  
    chosen = []
    counter = 0
    while counter < count:
        random_int = random.randint(0, len(filtered_words) - 1)
        chosen.append(filtered_words[random_int])
        counter += 1
    return chosen

def MakeGrid(rows, columns):
    if not isinstance(rows, int) or not isinstance(columns, int):
        print("Error; Input is not a 'int' variable.")
        return
    if rows <= 0 or columns <= 0:
        print("Error; Grid size too small.")
        return
    

    column = []
    rowcounter = 0
    while rowcounter < rows:
        row = []
        itemcounter = 0
        while itemcounter < columns:
            row.append('0')
            itemcounter += 1
        rowcounter +=1
        column.append(row)
    return column


def FillGrid(grid, wordlist):
    if not isinstance(grid, list):
        print("Error; Input is not a 'list' variable.")
        return
    if len(grid) <= 0:
        print("Error; Grid size too small.")
        return
    for item in grid:
        if not isinstance(item, list):
            print("Error; Input is not a 'grid' object.")
            return
        if len(item) <= 0:
            print("Error; Grid size too small.")
            return
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '0':
                random_int = random.randint(0, len(wordlist) - 1)
                random_word = wordlist[random_int]
                random_int2 = random.randint(0, len(random_word) - 1)
                letter = random_word[random_int2]
                grid[i][j] = letter
    for row in grid:
        print(row)

