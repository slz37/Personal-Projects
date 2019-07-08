'''
Condenses all files in folders within the current working directory
to a single folder.
'''

import os, shutil

#Grab list of folders containing key, ignore zip and folder if it's the same as key
key = "Shiki"
folder_to_move_to = r"C:\Users\Luke\Downloads\Shiki"
folders = [f for f in sorted(os.listdir(os.getcwd())) if (key in f and ".zip" not in f and f != key)]

#Now move all files to specified folder
for folder in folders:
    for r, d, f in os.walk(folder):
       for file in f:
           if ".mkv" in file:
               file_origin = r + "\\" + file
               move_dest = folder_to_move_to + "\\" + file
               shutil.move(file_origin, move_dest)

    #Cleanup
    shutil.rmtree(folder)
