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

def handle_cell_selection(grid, cell_row, cell_col, selected_cells, selected_letters, found_words):
    letter = grid[cell_row][cell_col]
    
    if not letter.islower():
        return selected_cells, selected_letters
        
    selected_cells.append((cell_row, cell_col))
    selected_letters.append(letter)
    grid[cell_row][cell_col] = letter.upper()
    
    filtered_words = [word for word in found_words 
                     if word.lower().startswith(''.join(selected_letters))]
    
    if not filtered_words:
        reset_selected_cells(grid, selected_cells)
        return [], []
        
    return selected_cells, selected_letters

def check_direction_change(selected_cells, grid):
    if len(selected_cells) >= 3:
        last_cell = selected_cells[-1]
        second_last_cell = selected_cells[-2]
        third_last_cell = selected_cells[-3]
        
        row_diff = last_cell[0] - second_last_cell[0]
        col_diff = last_cell[1] - second_last_cell[1]
        prev_row_diff = second_last_cell[0] - third_last_cell[0]
        prev_col_diff = second_last_cell[1] - third_last_cell[1]
        
        if (row_diff != prev_row_diff or col_diff != prev_col_diff):
            reset_selected_cells(grid, selected_cells)
            return True
    return False

def reset_selected_cells(grid, selected_cells):
    for row, col in selected_cells:
        grid[row][col] = grid[row][col].lower()

def check_word_completion(filtered_words, selected_letters, selected_cells):
    if not filtered_words:
        return False, None
        
    if len(filtered_words) == 1:
        current_word = filtered_words[0].upper()
        selected_string = ''.join(selected_letters).upper()
        
        if current_word == selected_string:
            return True, current_word
    return False, None

def handle_game_display(grid, found_words, canvas, BLACK):
    canvas.fill(BLACK)
    draw_grid(grid)
    draw_found_words(found_words, grid)
    pygame.display.flip()

def StartCanvas(wordlist, seed=None):
    running = True
    BLACK = pygame.Color('black')
    if seed is not None:
        pygame.display.set_caption("Grid :" + str(seed))
        
    selected_letters = []
    selected_cells = []
    located_words = []
    
    while running:
        # Generate and initialize grid
        grid = BuildGrid(wordlist, 10, 6, seed)
        found_words = fill_grid(grid, wordlist)
        grid = [[letter.lower() for letter in row] for row in grid]
        
        # Initial draw
        handle_game_display(grid, found_words, canvas, BLACK)

        # Main game loop
        waiting_for_space = True
        while waiting_for_space:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return  # Exit the function entirely
                    
                if set(word.lower() for word in located_words) == set(word.lower() for word in found_words):
                    waiting_for_space = False
                    located_words = []
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    cell_row = (mouse_y - (height - len(grid) * 30) // 2) // 30
                    cell_col = (mouse_x - (width - len(grid[0]) * 30) // 2) // 30
                    
                    if 0 <= cell_row < len(grid) and 0 <= cell_col < len(grid[0]):
                        selected_cells, selected_letters = handle_cell_selection(
                            grid, cell_row, cell_col, selected_cells, selected_letters, found_words
                        )
                        
                        if selected_cells and check_direction_change(selected_cells, grid):
                            selected_letters = []
                            selected_cells = []
                            
                        filtered_words = [word for word in found_words 
                                        if word.lower().startswith(''.join(selected_letters))]
                        
                        word_completed, current_word = check_word_completion(
                            filtered_words, selected_letters, selected_cells
                        )
                        if word_completed:
                            located_words.append(current_word)
                            selected_letters = []
                            selected_cells = []
            
            # Update display
            handle_game_display(grid, found_words, canvas, BLACK)

        # Show answer and delay
        words = fill_grid(grid, wordlist)
        handle_game_display(grid, found_words, canvas, BLACK)
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

