'''
Solves the provided state of
a sudoku puzzle using knuth's
algorithm x.
'''
from solver_setup import *
from random import randint
from gui import update_grid

def exact_cover(X, Y):
    '''
    Formulates an exact cover problem
    given two inputs X and Y.
    '''
    return

def algorithm_x(number_grid):
    '''
    Uses Knuth's algorith X to
    solve a sudoku puzzle.
    '''

    #Constraints -> row-col, row-num, col-num, cell-num
    #https://en.wikipedia.org/wiki/Exact_cover#Sudoku
    
    row_col = []

def solution(number_grid):
    '''
    Attempts to solve the current
    state of the puzzle.
    '''
    rows, _, _ = split_tiles(number_grid, return_values = True)
    initial_state = rows.flatten()
    immutable_tiles = get_immutable_tiles(number_grid)

    #Don't want user messing with solver
    freeze_tiles(number_grid)

    #Check validity and get tile groupings
    check_valid(number_grid)

    #Solver
    sol = algorithm_x(number_grid)

    #Update grid to reflect solution
    update_grid(rows, sol)

    #Now user can interact again
    unfreeze_tiles(number_grid)
    
def place_numbers(number_grid, immutable_tiles):
    '''
    Places numbers randomly selected
    from 1-9 in empty spots on the
    grid.
    '''
    
    #Add new values to mutable tiles
    for tile in number_grid:
        if tile not in immutable_tiles:
            new_val = randint(1, 9)

            #Need to reenable to update
            tile.config(state = tkinter.NORMAL)
            tile.insert(tkinter.END, new_val)
            tile.config(state = tkinter.DISABLED)

    return number_grid

def check_rules(number_grid):
    '''
    Checks whether the current state
    of the grid follows the rules of
    sudoku and returns the number
    of errors.
    '''
    errors = 0
    rows, cols, cells = split_tiles(number_grid, return_values = False)

    #Check rows
    for row in rows:
        unique_vals = len(np.unique(row))
        
        if unique_vals != 9:
            errors += (9 - unique_vals)

    #Check columns
    for col in cols:
        unique_vals = len(np.unique(col))
        
        if unique_vals != 9:
            errors += (9 - unique_vals)

    #Check cells
    for cell in cells:
        unique_vals = len(np.unique(cell))

        if unique_vals != 9:
            errors += (9 - unique_vals)

    #Check against original state
    for i in range(len(number_grid)):
        if (initial_state[i] != number_grid[i]) and (initial_state[i] != 0):
            errors += 2
            
    return errors

