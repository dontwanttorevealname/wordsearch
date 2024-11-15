import random
import random
import pygame
import sys
import time

pygame.init()

width, height = 1000, 1000
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Canvas")


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
    return grid

def InsertWords(grid, wordlist):
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
    for word in wordlist:
        flip = random.randint(0, 1)
        if flip == 1:
            grid = InsertWordVertically(grid, word)
        else:
            grid = InsertWordHorizontally(grid, word)

    return grid

def InsertWordHorizontally(grid, word):
    # word = word.upper()
    flip = random.randint(0, 4)
    if flip == 1:
        word = word[::-1]
    length = len(word)
    lengthX = len(grid[0])
    if length > lengthX:
        print("Error; Word too big.")
        return
    current_row = random.randint(0, len(grid) - 1)
    start_position = random.randint(0, lengthX - length)
    for i in range(length):
        if grid[current_row][start_position + i] != '0':
            return grid
    current_position = start_position
    for letter in word:
        grid[current_row][current_position] = letter
        current_position += 1
        
    return grid


def InsertWordVertically(grid, word):
   # word = word.upper()
    flip = random.randint(0, 4)
    if flip == 1:
        word = word[::-1]
    length = len(word)
    lengthY = len(grid)
    if length > lengthY:
        print("Error; Word too big.")
        return grid
    current_column = random.randint(0, len(grid[0]) - 1)
    start_position = random.randint(0, lengthY - length)
    for i in range(length):
        if grid[start_position + i][current_column] != '0':
            return grid
        
    current_position = start_position
    for letter in word:
        grid[current_position][current_column] = letter
        current_position += 1
        
    return grid


def BuildGrid(wordlist, size, count, seed=None):
    random.seed(seed)
    grid = MakeGrid(size, size)
    words = SelectWords(wordlist, count, size)
    print(words)
    grid = InsertWords(grid, words)
    grid = FillGrid(grid, words)
    return grid



def draw_grid(grid):
    font = pygame.font.Font(None, 20)  # Smaller font size
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Setting the size of the grid
    grid_width = cols * 30  # Cell width (30 pixels)
    grid_height = rows * 30  # Cell height (30 pixels)

    # Calculate top-left position to center the grid
    start_x = (width - grid_width) // 2
    start_y = (height - grid_height) // 2

    # Draw the outline of the grid
    pygame.draw.rect(canvas, (255, 255, 255), (start_x, start_y, grid_width, grid_height), 2)  # White outline

    # Draw letters in the grid
    for row in range(rows):
        for col in range(cols):
            letter = grid[row][col]
            
            # Set the color based on uppercase or lowercase
            if letter.isupper():
                color = (0, 255, 0)  # Green for uppercase
            else:
                color = (255, 255, 255)  # White for lowercase
            
            text_surface = font.render(letter, True, color)  # Render with the selected color
            
            # Adjusting position for the text to be center-aligned with minimal padding
            text_rect = text_surface.get_rect(center=(start_x + col * 30 + 15, start_y + row * 30 + 15))  # Centered with 15px padding
            canvas.blit(text_surface, text_rect)


def generate_html_grids(grid1, grid2, word_list, output_file=0):
    output_file = "grids" + str(output_file) + ".html"
    solved_file = str(output_file) + "_solved.html"

    # Define CSS style for the grids
    styles = """
    <style>
        .grid {
            display: inline-block;
            border: 2px solid black;
            margin: 20px;
        }
        .cell {
            display: inline-block;
            width: 30px;
            height: 30px;
            text-align: center;
            border: 1px solid lightgray;
            line-height: 30px; /* Center text vertically */
            font-size: 20px;  /* Adjust font size */
        }
        .capital {
            color: green;     /* Color for capital letters */
        }
        .word-list {
            margin: 20px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
    """

    # Start the HTML document for the first grid
    html_content = f"<!DOCTYPE html>\n<html>\n<head>\n<title>Grid Display</title>\n{styles}\n</head>\n<body>\n"
    
    # Function to create a grid's HTML representation
    def create_grid_html(grid):
        grid_html = '<div class="grid">'
        for row in grid:
            grid_html += '<div>'
            for cell in row:
                cell_class = 'capital' if cell.isupper() else ''
                grid_html += f'<div class="cell {cell_class}">{cell}</div>'
            grid_html += '</div>'
        grid_html += '</div>'
        return grid_html

    # Add the first grid to the HTML content
    html_content += "<h2>Grid 1</h2>\n"
    html_content += create_grid_html(grid1)

    # Add the word list to the HTML content
    html_content += "<div class='word-list'>Word List:<br>" + "<br>".join(word_list) + "</div>"

    # Link to the second grid
    html_content += f"<a href='{solved_file}'>View Answer Grid</a>"

    # Close the HTML document for the first grid
    html_content += "</body>\n</html>"

    # Write the content to the output HTML file
    with open(output_file, "w") as file:
        file.write(html_content)

    # Start the HTML document for the second grid
    solved_html_content = f"<!DOCTYPE html>\n<html>\n<head>\n<title>Solved Grid Display</title>\n{styles}\n</head>\n<body>\n"

    # Add the second grid to the solved HTML content
    solved_html_content += "<h2>Grid 2</h2>\n"
    solved_html_content += create_grid_html(grid2)

    # Close the HTML document for the solved grid
    solved_html_content += "</body>\n</html>"

    # Write the content to the second output HTML file
    with open(solved_file, "w") as file:
        file.write(solved_html_content)

    print(f"HTML files '{output_file}' and '{solved_file}' have been generated.")


def mark_word(grid, word, start_row, start_col, direction):
    """Check if a word can be marked from the start position in a specific direction."""
    delta_row, delta_col = direction
    word_length = len(word)
    positions = []

    for i in range(word_length):
        row = start_row + delta_row * i
        col = start_col + delta_col * i
        
        # Check if the current position is within the grid boundaries
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != word[i]:
            return False, []

        positions.append((row, col))

    return True, positions

def fill_grid(grid, wordlist):
    """Fill the grid with capitalized words found from the wordlist and return a list of found words."""
    if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid) or len(grid) == 0:
        return "Error; Input is not a valid grid."
    
    found_words = []  # List to store found words
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].islower():  # Only check lowercase letters
                for word in wordlist:
                    if grid[i][j] == word[0]:  # Check if the first character matches
                        # Attempt to mark the word without changing the grid yet.
                        success = False
                        for direction in directions:
                            found, positions = mark_word(grid, word, i, j, direction)
                            if found:
                                # If the word is found, capitalize the letters and add word to the list.
                                for pos in positions:
                                    grid[pos[0]][pos[1]] = grid[pos[0]][pos[1]].upper()
                                found_words.append(word)  # Add the found word to the list
                                success = True
                                break
                        
                        if not success:
                            # If we failed to find the word, we revert the first letter back to lowercase.
                            grid[i][j] = grid[i][j].lower()
                            
    return found_words


def draw_found_words(found_words, grid):
    font = pygame.font.Font(None, 25)  # Larger font size for found words
    # Create and render the found words text
    found_words_text = "Found Words: " + ", ".join(found_words)
    text_surface = font.render(found_words_text, True, (255, 255, 255))

    # Calculate position for the text to be just below the grid
    rows = len(grid)
    grid_height = rows * 30  # Cell height (30 pixels)
    text_y_position = (height - grid_height) // 2 + grid_height + 10  # 10 pixels below the grid

    # Center the text below the grid
    text_rect = text_surface.get_rect(center=(width // 2, text_y_position))
    canvas.blit(text_surface, text_rect)