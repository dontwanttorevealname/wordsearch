from main import *

with open('Words.txt', 'r') as file:
    file_contents = file.read()

wordlist= file_contents.split(', ')


'''grid = MakeGrid(15, 15)
print("Empty : \n")
for row in grid:
    print(row)
print("\n \n \n Words : \n")
words = SelectWords(wordlist, 10, 15)
grid = InsertWords(grid, words)
for row in grid:
    print(row)
print("\n \n \n Filled : \n")
grid = FillGrid(grid, words)
for row in grid:
    print(row)'''

def StartCanvas(wordlist, seed=None):
    running = True
    BLACK = pygame.Color('black')
    if seed is not None:
        pygame.display.set_caption("Grid :" + str(seed))
    selected_letters = []
    selected_cells = []
    located_words = []
    last_cell = ""
    while running:
        # Generate the grid for the current loop
        grid = BuildGrid(wordlist, 10, 6, seed)
        found_words = fill_grid(grid, wordlist)

        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = grid[i][j].lower()  
        canvas.fill(BLACK)
        draw_grid(grid)
        draw_found_words(found_words, grid)
        for row in grid:
            print(row)
        pygame.display.flip()

        # Wait here until the space key is pressed
        waiting_for_space = True
        while waiting_for_space:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle quitting
                    running = False
                    waiting_for_space = False  # Exit the inner loop if quitting

                # Check for the space key press
                if set(word.lower() for word in located_words) == set(word.lower() for word in found_words):
                    waiting_for_space = False  # Exit the inner loop on space press
                    located_words = []

                # Check for mouse click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos  # Get mouse position
                    # Determine which grid cell was clicked
                    cell_row = (mouse_y - (height - len(grid) * 30) // 2) // 30
                    cell_col = (mouse_x - (width - len(grid[0]) * 30) // 2) // 30
                    # Make sure the clicked cell is within the grid bounds
                    if 0 <= cell_row < len(grid) and 0 <= cell_col < len(grid[0]):
                        letter = grid[cell_row][cell_col]

                        # If the letter is lowercase, transform it to uppercase
                        if letter.islower():
                            selected_cells.append((cell_row, cell_col))
                            selected_letters.append(letter)
                            filtered_words = found_words if not selected_letters else [
                                word for word in found_words 
                                if word.lower().startswith(''.join(selected_letters))
                            ]

                                            

                            grid[cell_row][cell_col] = letter.upper()

                            if not filtered_words:
                                for cell in selected_cells:
                                    uprow, upcol = cell
                                    grid[uprow][upcol] = grid[uprow][upcol].lower()
                                selected_letters = []


                            if selected_cells:
                                last_cell = selected_cells[-1:]
                                if len(selected_cells) >= 2:
                                    second_last_cell = selected_cells[-2]
                                    last_cell = selected_cells[-1]
                                    # Calculate current differences
                                    row_diff = last_cell[0] - second_last_cell[0]
                                    col_diff = last_cell[1] - second_last_cell[1]
                                        
                                        # If we have 3 or more cells, compare directions
                                    if len(selected_cells) >= 3:
                                        third_last_cell = selected_cells[-3]
                                        prev_row_diff = second_last_cell[0] - third_last_cell[0]
                                        prev_col_diff = second_last_cell[1] - third_last_cell[1]
                                            
                                            # If direction changed, store the new direction
                                        if (row_diff != prev_row_diff or col_diff != prev_col_diff):
                                            for cell in selected_cells:
                                                uprow, upcol = cell
                                                grid[uprow][upcol] = grid[uprow][upcol].lower()
                                            grid[cell_row][cell_col] = grid[cell_row][cell_col].lower()
                                            selected_letters = []
                                            selected_cells = []
                            if filtered_words:  # Check if there are any filtered words
                                if len(filtered_words) == 1:  # Check if there's exactly one word
                                    current_word = filtered_words[0].upper()  # Get the single word and make it uppercase
                                    selected_string = ''.join(selected_letters).upper()  # Join selected letters into string

                                    if current_word == selected_string:
                                        located_words.append(current_word)
                                        selected_letters = []
                                        if selected_cells:
                                            selected_cells = []

            # Redraw the grid after a click
            canvas.fill(BLACK)
            draw_grid(grid)
            draw_found_words(found_words, grid)
            pygame.display.flip()

        # Now we'll reveal the answer
        words = fill_grid(grid, wordlist)  # Fill the grid with answers
        canvas.fill(BLACK)
        draw_grid(grid)
        draw_found_words(found_words, grid)
        for row in grid:
            print(row)
        pygame.display.flip()
        pygame.time.delay(3000)


def MakeHTML(wordlist, seed=None):
    grid = BuildGrid(wordlist, 10, 6, seed)
    
    emptygrid = []
    for row in grid:
        emptyrow = []
        for item in row:
            emptyrow.append(item)
        emptygrid.append(emptyrow)
            
    words = fill_grid(grid, wordlist)
    for row in grid:
        print(row)
    for row in emptygrid:
        print(row)
    if not seed == None:
        generate_html_grids(emptygrid, grid, words, seed)
    else:
        generate_html_grids(emptygrid, grid, words)
             


StartCanvas(wordlist)

#MakeHTML(wordlist, 6)

