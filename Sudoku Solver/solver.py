'''
Solves the provided state of
a sudoku puzzle using knuth's
algorithm x.
'''
from solver_setup import *
from random import randint
from gui import update_grid
from itertools import product
from math import *
from collections import Counter
import numpy as np
import sys, os

def select(constraints, possibilities, r):
    '''
    Selects the respective columns of a
    given row from potenti
    '''
    cols = []

    #Remove possibilities that do not satisfy the constraints
    for j in possibilities[r]:
        for i in constraints[j]:
            for k in possibilities[i]:
                if k != j:
                    constraints[k].remove(i)
                    
        cols.append(constraints.pop(j))
    return cols

def deselect(constraints, possibilities, r, cols):
    '''
    Returns the columns for the row back
    to the constraints.
    '''

    #Need to add them back in reverse
    for j in reversed(possibilities[r]):
        constraints[j] = cols.pop()

        #Return the possibility if it satisfies the constraints
        for i in constraints[j]:
            for k in possibilities[i]:
                if k != j:
                    constraints[k].add(i)

def solve(constraints, possibilities, solution):
    '''
    Solve the exact cover problem for sudoku using
    algorithm x.
    '''

    #If no more constraints, we're done
    if not constraints:
        yield list(solution)
    else: 
        c = min(constraints, key = lambda c: len(constraints[c]))

        #Loop over potential solutions
        for r in list(constraints[c]):
            #Add row to solution and get respective columns
            solution.append(r)
            cols = select(constraints, possibilities, r)

            #Try to solve
            for s in solve(constraints, possibilities, solution):
                yield s

            #Get rid of solution
            deselect(constraints, possibilities, r, cols)
            solution.pop()

def exact_cover(constraints, possibilities):
    '''
    Formulates an exact cover problem
    given the constraints and possible
    solutions.
    '''

    #Initiate dictionary
    constraints = {x: set() for x in constraints}

    #Add potential value (row, col, num) to each constraint
    for value, row in possibilities.items():
        for combination in row:
            constraints[combination].add(value)
    
    return constraints, possibilities

def solver(number_grid):
    '''
    Setup the initial exact cover problem
    and solve the sudoku puzzle.
    '''

    #Constraints -> row-col, row-num, col-num, cell-num
    #https://en.wikipedia.org/wiki/Exact_cover#Sudoku
    #https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html
    #row,col,cell 0 to 8, nums must be 1 to 9
    row_col = [("rowcol", x) for x in product(range(9), range(9))]
    row_num = [("rownum", x) for x in product(range(9), range(1, 10))]
    col_num = [("colnum", x) for x in product(range(9), range(1, 10))]
    cell_num = [("cellnum", x) for x in product(range(9), range(1, 10))]
    constraints = row_col + row_num + col_num + cell_num

    #Possiblities
    possibilities = dict()

    #Iterate over every row, col, num
    for (row, col, num) in product(range(9), range(9), range(1, 10)):
        #Get the cell number
        cell = 3 * floor(col / 3) + floor(row / 3)

        #Now add to list of possibilities
        possibilities[(row, col, num)] = [("rowcol", (row, col)), ("rownum", (row, num)),
                                         ("colnum", (col, num)), ("cellnum", (cell, num))]

    #Setup done -> create exact_cover
    constraints, possibilities = exact_cover(constraints, possibilities)

    #Now loop through grid and solve
    for i, row in enumerate(number_grid):
        for j, num in enumerate(row):
            if num:
                select(constraints, possibilities, (i, j, num))

    #Now finally solve
    for solution in solve(constraints, possibilities, []):
        for (row, col, num) in solution:
            number_grid[row][col] = num
        yield number_grid

def setup_solver(number_grid):
    '''
    Attempts to solve the current
    state of the puzzle.
    '''
    rows, _, _ = split_tiles(number_grid, return_values = True)
    initial_state = rows.flatten()

    #Don't want user messing with solver
    freeze_tiles(number_grid)

    try:
        #Check validity
        check_valid(number_grid)
        check_solvable(number_grid)

        if check_rules(number_grid):
            #Solve
            sol = np.array([])
            for solution in solver(rows):
                sol = solution

            if not sol.any():
                raise(Exception("Puzzle does not have a solution!"))

            #Convert solution to text
            text = []
            for row in sol:
                for value in row:
                    text.append(str(value))

            #Now user can interact again
            unfreeze_tiles(number_grid)

            #Update grid to reflect solution
            rows, _, _ = split_tiles(number_grid)
            rows = rows.flatten()
            update_grid(rows, text)
        else:
            unfreeze_tiles(number_grid)
            raise(Exception("Input does not follow sudoku rules."))
    except Exception as e:
        #Debugging - prints line # and other info
        #exc_type, exc_obj, exc_tb = sys.exc_info()
        #fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #print(e, exc_type, fname, exc_tb.tb_lineno)
        
        print(e)
        unfreeze_tiles(number_grid)

def check_solvable(number_grid):
    '''
    Checks that at least 16 values have
    been entered in the grid to ensure that
    the solver is capable of finding a solution.
    '''

    num = 0
    rows, _, _ = split_tiles(number_grid, return_values = True)

    #Count number of non-zero valuse
    for row in rows:
        for value in row:
            if value > 0:
                num += 1

    #Need at least 16 to solve
    if num >= 16:
        return True
    else:
        return False

def check_rules(number_grid):
    '''
    Checks whether the current state
    of the grid follows the rules of
    sudoku and returns the number
    of errors.
    '''
    errors = 0
    rows, cols, cells = split_tiles(number_grid, return_values = True)

    #Check rows
    for row in rows:
        counts = Counter(row)

        for num in counts:
            if num != 0 and counts[num] > 1:
                return False

    #Check columns
    for col in cols:
        counts = Counter(col)
        
        for num in counts:
            if num != 0 and counts[num] > 1:
                return False

    #Check cells
    for cell in cells:
        counts = Counter(cell)
        
        for num in counts:
            if num != 0 and counts[num] > 1:
                return False
    return True

