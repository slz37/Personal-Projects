'''
Sets up the main gui window and functionality for
Sudoku Solver.
'''

import tkinter
import sys
from solver import *
from tkinter import filedialog
import pathlib

def generate_subgrid(subframe, number_grid):
    '''
    Generates the subgrid that contains each
    text box.
    '''
    
    #Add grid to subframe
    for i in range(0, 3):
        for j in range(0, 3):
            number_grid.append(tkinter.Text(subframe, width = 3, height = 2))
            number_grid[-1].grid(row = i, column = j)

def generate_grid():
    '''
    Generates a 9x9 sudoku grid
    with separating lines.
    '''

    number_grid = []

    #Master frame for grid
    frame = tkinter.Frame(WINDOW)
    frame.pack(side = "top")

    #Grid of text boxes
    for i in range(0, 5):
        #Horizontal line
        if (i % 2) == 1:
            line = tkinter.Frame(frame, height = 3, width = 255, bg = "black")
            line.grid(row = i, columnspan = 300)
        else:
            for j in range(0, 5):
                #Vertical line
                if (j % 2) == 1:
                    line = tkinter.Frame(frame, height = 105, width = 3, bg = "black")
                    line.grid(row = i, column = j)
                else:
                    #Subframe for text boxes
                    subframe = tkinter.Frame(frame)
                    subframe.grid(row = i, column = j)

                    generate_subgrid(subframe, number_grid)
            
    return number_grid

def generate_info():
    '''
    Generates the info and solve
    button.
    '''

    #Frame
    frame = tkinter.Frame(WINDOW)
    frame.pack(side = "bottom")

    #Instructions
    tkinter.Label(frame, text =
                  'Fill in values and then click solve!').grid(row = 4, column = 2)

    #Solve Button
    solve_button = tkinter.Button(frame, text = 'Solve', width =
                            20, command = lambda: solution(number_grid))
    solve_button.grid(row = 5, column = 3)

    #Load/Save Button
    save_button = tkinter.Button(frame, text = 'Save', width =
                            20, command = lambda: save_puzzle(number_grid))
    save_button.grid(row = 5, column = 1)
    load_button = tkinter.Button(frame, text = 'Load', width =
                            20, command = lambda: load_puzzle(number_grid))
    load_button.grid(row = 5, column = 2)

def save_puzzle(number_grid):
    '''
    Saves the current state of the puzzle
    to a file, such that it can be loaded
    in the future.
    '''

    #Open directory and let user save
    current_dir = pathlib.Path(__file__).parent
    file_out = filedialog.asksaveasfile(initialdir = current_dir, title = "Select file",
                                                     filetypes = (("text files", "*.txt"), ("all files", "*.*")),
                                                     mode = "w", defaultextension = ".txt")

    #Get rows
    rows, _, _ = split_tiles(number_grid)

    #Add rows to file
    for row in rows:
        string = ""
        for tile in row:
            #Format text
            text = tile.get("1.0", tkinter.END)
            text = text.strip("\n")

            #Fill empty with 0's
            if text == "":
                text = "0"

            string += text + " "

        #Write
        file_out.write(string + "\n")

    #Close file
    file_out.close()

def load_puzzle(number_grid):
    '''
    Loads a previously saved puzzle
    into the grid to be solved.
    '''

    try:
        #Open directory and let user select file to open
        current_dir = pathlib.Path(__file__).parent
        file_in = filedialog.askopenfile(initialdir = current_dir, title = "Select file",
                                                    filetypes = (("text files", "*.txt"), ("all files", "*.*")),
                                                    mode = "r", defaultextension = ".txt")

        #Read in puzzle and format
        text = file_in.read()
        text = text.replace("\n", "")
        text = text.split(" ")

        #Get rows
        rows, _, _ = split_tiles(number_grid)
        rows = rows.flatten()
        
        #Now replace all tiles with data loaded from file
        update_grid(rows, text)
    except:
        raise(Exception("Invalid puzzle file!"))

def update_grid(rows, text):
    '''
    Replaces all values currently in the grid
    with the new values specified in rows.
    '''

    #Iterate over every tile
    for i, tile in enumerate(rows):
            #Remove 0's
            if text[i] == "0":
                new_val = ""
            else:
                new_val = text[i]

            #Replace current value with new value
            tile.delete("1.0", tkinter.END)
            tile.insert(tkinter.END, new_val)

def on_closing():
    '''
    Closes the tkinter window
    and exits the program.
    '''
    
    WINDOW.destroy()
    sys.exit()

if __name__ == "__main__":
    #Initiate Setup
    WINDOW = tkinter.Tk()
    WIDTH = 500  
    HEIGHT = 400  
    X = 100
    Y = 100

    #Update Window and Run
    WINDOW.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, X, Y))
    WINDOW.title("Sudoku Solver")
    WINDOW.protocol("WM_DELETE_WINDOW", on_closing)

    number_grid = generate_grid()
    generate_info()
    WINDOW.mainloop()
