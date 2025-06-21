"""UI-manager file

Contains main activity loop
Prints information to the user
Uses logic file help-functions for file access
"""

import os
import random

#_swedish_or_svartiska = random.randrange(0, 2)
#_random_word_option = random.randint(2) #Later update max value to length of word_tuple_list 

def main_ui_loop(word_tuple_list):
    choice = None
    while (True):
        choice = main_menu_message()
        if (choice == "1"):
            pass
        elif (choice == "2"):
            random_word_match(word_tuple_list)
        elif (choice == "3"):
            pass
        elif (choice == "4"):
            exit()
        else:
            print("input error, please try again") 



def main_menu_message():
    print("==Main Menu==")
    print("\n")
    print("Hello and welcome to this applicaiton")
    print("Choose your option from down below")
    print("\n")
    print("1. Add word file")
    print("2. Do random word match")
    print("3. Create custom sublist(Future choice)")
    print("4. Exit application")
    return input()

"""Tests the user on a random tuple in saved words

Function which selects a random tuple from all saved
tuples and checks if the user is able to match the 
swedish or orcish word with the matching opposite.
Call either with the complete word list or a selected
sublist. The word_tuple_list should be the list of 
(svartiska, svenska, ordtyp\n) tuples.
"""
def random_word_match(word_tuple_list):
    while(True):
        selected_tuple = word_tuple_list[random.randrange(0, len(word_tuple_list))]
        swedish_or_svartiska = random.randrange(0, 2)
        print("The word you should translate is " + selected_tuple[swedish_or_svartiska])
        answer = input()
        if any(substring in answer for substring in selected_tuple[abs(swedish_or_svartiska-1)]):
            print("Correct!") 
        else:
            print("Incorrect")
        print("The translation was " +  selected_tuple[abs(swedish_or_svartiska-1)])
        print("Do you want to go continue? [yes/no]")
        answer = input()
        if (any (substring in answer for substring in "no")):
            break
        else:
            print("\n")

    



def add_word_file():
    pass