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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting_for_space = False  # Exit the inner loop on space press

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
                            grid[cell_row][cell_col] = letter.upper()

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
             


StartCanvas(wordlist, 6)

#MakeHTML(wordlist, 6)

