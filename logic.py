"""This file contains the overall logic of the program, including support functions
such as the file reading, word processing and similar.
"""

import constants

"""Reads the .csv file to split and order the strings
(Consider having this only read a file and 
have a string handler split the string itself)
NOTE: Assumes sanity check has been performed and that
file_name is a valid file.

file_name is the name of the .csv file that is to be read,
located in the local directory. File should be ordered with
"[svartiska], [svenska], [ordtyp]^M" 
Returns a list of ([svartiska], [svenska], [ordtyp]) tuples, 
with each variable being a string.
"""
def read_file(file_name):
    tuple_list = []
    with open(file_name) as open_file:
        n = 0
        while(n < 100):
            try:
                temp_list = open_file.readline().split(",")
                if (not temp_list == [""]):
                    tuple_list.append(tuple(temp_list))
                else:
                    break
            except:
                break
            n+=1
            print(n)
        return tuple_list





"""Saves a glossary/lesson to file_name

If no file with the name exists, creates a new file with 
that name.
If a file with that name exists, overwrites the existing
contents of the file.
No checks are done to see if a file exists or not, that 
is done in another function.
"""
def write_glossary(file_name):
    pass


"""Checks if a file exists and is a saved glossary

Sanity check that first checks if a file 
with name file_name exists in the current
folder, second if it is a glossary file. 

If the file is not in the current folder
(or in the saved glossary folder, not yet
decided but probably a good idea) or , return 
an error.

If the file is an existing glossary file, 
return [name of existing file constant].

If the file does not exist, return
[name of file does not exist constant].
"""
def is_glossary_file(file_name):
    if any(substring in file_name for substring in ["..", "/", "~"]):
        return constants.FILE_ERROR
    else:
        return constants.FILE_DOES_NOT_EXIST