"""Main file
The main file, initiates the overall logic including reading the initial 
file that is provided with the program. When setup is done, calls the 
UI-manager which handels the main loop.
"""
import logic
import ui

EXAMPLE_FILE_NAME = 'word-files/Example_2.csv'


def main():
    print("Välkommen till denna app")
    print("Påbörjar setup:\n")
    with open(EXAMPLE_FILE_NAME) as word_file:
        print(word_file.read())
    print("\n===Testing logic===\n")
    word_tuple_list = logic.read_file(EXAMPLE_FILE_NAME)
    print(word_tuple_list)
    ui.main_ui_loop(word_tuple_list)




if __name__ == "__main__":
    main()
    