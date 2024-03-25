import re
import os
import sys

def terminal():     #Function that handles the given terminal arguments

    size = os.get_terminal_size()
    width = size.columns
    if width % 2 == 1:
        left= right = width // 2 - 5
    else:
        left = width // 2 - 6
        right = left + 1

    try:
        if '-h' in sys.argv or '-help' in sys.argv:
            print(left*'=','help page',right*'='+"""
    
NAME 
        Microprocessor
        
SYNOPSIS
         python -u | python3  "Script path" "Path of the assembly file to compile" "Path of the generated source files directory" | [-h | -help]
""")
            quit()

        else :
            file = sys.argv[1]
            generated_file_path = sys.argv[2]
            
    except IndexError :
        return [None, None]
    else:
        return [file, generated_file_path]