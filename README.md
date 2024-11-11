Random wordsearch generator and solver.

Takes an input list of words and a grid size, selects words that would fit in that grid, lays the chosen words out in the grid, before filling in the blanks.

First function
create a list of every word that could fit within the grid, base the number of words off the size of the grid.
Grid would be a list of rows, which are each a list of columns. Empty spaces could be represented by '0'
Iterate over each letter in each word, and position them in a line using one direction, either up, down, left or right.
Once every word has been placed into its spot on the grid. Use the second function to fill in the rest of the spots.
Once the grid has been filled up, call the first solving function at position 0,0

Second function
Iterates over every space in the grid, left to right, top to bottom. If a spot contains '0', use rand to choose a random letter from a random word, and fill in the spot. Once it makes one final pass with no zeroes remaining, return.

Iterate over each letter, see if it corresponds to the first letter in a word, checks every direction for the next letter in that word.

Goes across the grid, left to right, top to bottom, and checks each letter using the two functions below.

Two seperate functions
First function
Takes a letter as input
Create a list of all words with that first letter
If there are no words starting with that letter, exit and move on
Pass each word and each direction combination into the second function, starting at position '0' in the word, and the full word passed in

Second function
Takes a letter, word and direction as input.
Check if the next letter in the word is in that direction.
If it is, recursively call on the next letter and splice the current letter from the word, ie function(a, apple, down) becomes (p, pple, down) and return True
If it is not, return False

Once it has iterated over the entire grid, and found every possible word, exit the program.



Difficulty could be done by using different, more complicated lists of words, or purely through the grid size.