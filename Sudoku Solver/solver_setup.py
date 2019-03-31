'''
Performs all functions to setup the system for
the solver.
'''

import tkinter
import numpy as np

def freeze_tiles(number_grid):
    '''
    Freeze inputs of all tiles
    so user cannot mess with solver.
    '''

    for tile in number_grid:
        tile.config(state = tkinter.DISABLED)

def unfreeze_tiles(number_grid):
    '''
    Unfreeze inputs so that user
    can now input a new puzzle
    to solve.
    '''

    for tile in number_grid:
        tile.config(state = tkinter.NORMAL)

def check_valid(number_grid):
    '''
    Checks the initial state of the puzzle
    for validity, not including the
    sudoku rules.
    '''

    #Grab values
    values = []
    for tile in number_grid:
        val = tile.get("1.0", tkinter.END)
        val = val.strip("\n")

        #Check that it's a number 1-9 or empty
        try:
            #Use temp value for empty tiles
            if val == "":
                temp_value = "1"
            else:
                temp_value = val
            int(temp_value)
        except:
            unfreeze_tiles(number_grid)
            raise(Exception("Value {} is not an integer.".format(val)))

        if (int(temp_value) < 1) or (int(temp_value) > 9):
            unfreeze_tiles(number_grid)
            raise(Exception("Value {} is not between 1-9.".format(temp_value)))
        
        values.append(val)

    #Check that anything was input
    if not any(values):
        unfreeze_tiles(number_grid)
        raise(Exception("Must input at least 1 given number."))


def split_tiles(number_grid, return_values = False):
    '''
    Splits the tiles into cols, rows, and cells,
    so that checking that they follow sudoku
    rules is simple.
    '''
    
    rows = np.array([])
    cols = np.array([])
    cells = np.array([number_grid[j:j + 9] for j in range(0, 81, 9)])

    #Convert from tkinter object to values
    if return_values:
        for i in range(0, len(cells)):
            for j in range(0, len(cells)):
                val = cells[i][j].get("1.0", tkinter.END)
                val = val.strip("\n")

                #Replace empty with 0 or int
                if val == "":
                    val = 0
                else:
                    val = int(val)
                    
                cells[i][j] = val

    #Rows
    for i in range(0, 9, 3):
        #Need 3 to fully parse structure
        row1 = np.array([j[0:3] for j in cells[i:i + 3]]).flatten()
        row2 = np.array([j[3:6] for j in cells[i:i + 3]]).flatten()
        row3 = np.array([j[6:9] for j in cells[i:i + 3]]).flatten()
        combined = np.vstack((row1, row2, row3))
        
        rows = np.vstack((rows, combined)) if rows.size else combined

   #Cols
    for i in range(0, 3):
        for j in range(0, 3):
            col = np.array([k[i::3] for k in cells[j::3]]).flatten()

            cols = np.vstack((cols, col)) if cols.size else col

    return rows, cols, cells

################
# Deprecated Code #
################

def grid_vals(number_grid):
    '''
    Creates a list of rows containing the value for each
    corresponding column.
    '''
    value_grid = np.array([])
    cells = np.array([number_grid[j:j + 9] for j in range(0, 81, 9)])

    #Convert from tkinter object to values
    for i in range(0, len(cells)):
        for j in range(0, len(cells)):
            val = cells[i][j].get("1.0", tkinter.END)
            val = val.strip("\n")

            #Replace empty with 0 or int
            if val == "":
                val = 0
            else:
                val = int(val)
                
            cells[i][j] = val

    #Rows
    for i in range(0, 9, 3):
        #Need 3 to fully parse structure
        row1 = np.array([j[0:3] for j in cells[i:i + 3]]).flatten()
        row2 = np.array([j[3:6] for j in cells[i:i + 3]]).flatten()
        row3 = np.array([j[6:9] for j in cells[i:i + 3]]).flatten()
        combined = np.vstack((row1, row2, row3))
        
        value_grid = np.vstack((value_grid, combined)) if value_grid.size else combined

    return value_grid

def get_immutable_tiles(number_grid):
    '''
    Takes the tiles and splits them in
    to two groups: immutable (given numbers)
    and mutable (ones to solve for).
    '''

    immutable_tiles = []

    #Check if tile contains value
    for tile in number_grid:
        val = tile.get("1.0", tkinter.END)
        val = val.strip("\n")

        if val:
            immutable_tiles.append(tile)
        else:
            continue

    return immutable_tiles
