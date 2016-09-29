"""
## Project Objective 
3) An index file contains a list of text file paths to be considered ( one per line ). Build a file list that
contains respective dictionary of words which are grouped by the starting alphabet. If we enter a word,
the program should be able to display all the files where this word is found. 

## Team Members 
1. Aswin Kumar (S6)     U101113FBT003
2. E.Gurubaran (S6)     U101113FEC024
3. S.Karthikeyan (S5)   U101113FCS088
4. Vaddela Jaideep (S5) U101113FCS160
5. Pranith Kumar (S6)   U101113FEC225

## Instructions
1. Please run the "main.py" by using the following command in your command promt.  `python3 main.py`
2. The file containing the list of text files to be indexed needs to have one file name per line. 
"""

import os,re
from getchar import getch

dict = {}

def clscr():  # clears the screen
    if os.name == "posix":
        os.system('clear')  # on linux / os x
    elif os.name == "nt":
        os.system('cls')  # Windows

def init_dict():  # initilises the dictionary with all the alphabets
    for i in range(ord('a'),ord('z')+1):
        dict[chr(i)] = {}

def find_word(search_word,dictionary):  # finds the given word from the dictionary.
    return dictionary[search_word.lower()[0:1]].get(search_word.lower())

def main_menu():  # displays main menu and takes care of user menu selections
    clscr()
    print("Main Menu\n".center(100))
    print("Hi, there!!!!".center(100))
    print("This Program helps you index the words in a list of text files and search through them.".center(100))
    print("1. Build the dictionary\n2. Search word\n3. Exit\n\nPress the respective number to choose your option:")
    while True:
        input = getch()
        if input == '1':
            build_dict_menu()
        elif input == '2':
            search_menu()
        elif input == '3':
            print("are you sure you want to exit? ('y' to exit')")
            input = getch()
            if input.lower() == 'y':
                print("\n")
                print("Hope you enjoyed using this program !!! Bye :)\n\n".center(100))
                exit()
            main_menu()

def build_dict_menu():  # displays built dictionary menu
    clscr()
    print("Build Dictionary".center(100))
    while True:
        print("\n\nYour Current Directory is: "+ os.getcwd())
        print("\nPlease enter the < path/filename > containing the list of text file to be indexed: - (type `back()` to go to main menu)")
        file = input()
        if file == "back()":
        	main_menu()
        try:
            with open(file, 'r', encoding="ascii", errors="surrogateescape") as f:
                if(os.stat(file).st_size == 0):
                    print("The file is empty. please try again.")
                else:
                    process_filelist(f)
        except OSError:
            print("File not Found. Please try again.")

regex = re.compile("([A-Za-z]+)")  # regular expression that returns words from line
def file_processing(fname,fp,dict):  # this adds words to the dictionary from single text file passed to it.
    L=[]
    for line in fp:
        for word in regex.findall(line):
            word = word.lower()
            if word not in L:
                L.append(word)
                filenames_list = find_word(word,dict)
                if filenames_list == None:
                    dict[word[0:1]][word] = [fname]
                else:
                    if fname not in filenames_list:
                        filenames_list.append(fname)

def process_filelist(f):  # this function processes the list of files to index
    file_success = file_empty = file_missing = 0
    print("processing files now...")
    for line in f:
        line = line.strip()
        try:
            with open(line, "r", encoding="ascii", errors="surrogateescape") as fobj:
                if(os.stat(line).st_size == 0):
                    print(line, " is empty.")
                    file_empty += 1
                else:
                    file_processing(line,fobj,dict)
                    file_success += 1
        except OSError:
            print(line, "is not Found")
            file_missing += 1
    print("\nfiles indexing Complete...")
    print(file_success , " of " , (file_empty+file_missing+file_success) , " files processed successfully.")
    print(file_empty , "files were empty.")
    print(file_missing , "files were not found.")
    print("\n press any key...")
    getch()
    main_menu()

def search_menu():  # displays the search menu
    clscr()
    print("Word Search".center(100))
    print("Enter the word you want to search: ")
    word = input()
    file_list = find_word(word.lower(),dict)
    if file_list == None:
        print("'"+ word + "'is not found in any file")
    else:
        print("'"+ word + "' is found in the following files:")
        for fname in file_list:
            print(fname)
    print("\nPress any key to return to main menu...")
    getch()
    main_menu()

init_dict()
if __name__ == '__main__':
    main_menu()