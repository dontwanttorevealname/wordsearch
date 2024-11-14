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
    if not seed == None:
        pygame.display.set_caption("Grid :" + str(seed))

    while running:
        # Generate the grid for the current loop
        grid = BuildGrid(wordlist, 10, 6, seed)  
        canvas.fill(BLACK)
        draw_grid(grid)
        for row in grid:
            print(row)
        pygame.display.flip()

        # Wait here until the space key is pressed
        waiting_for_space = True
        while waiting_for_space:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Check for the QUIT event
                    running = False
                    waiting_for_space = False  # Exit the inner loop if quitting

                # Check for the space key press
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting_for_space = False  # Exit the inner loop on space press

        # Now we'll reveal the answer
        words = fill_grid(grid, wordlist)  # Fill the grid with answers
        canvas.fill(BLACK)
        draw_grid(grid)
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
             


#StartCanvas(wordlist)

MakeHTML(wordlist, 5)

