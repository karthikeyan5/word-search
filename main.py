# this is the file that should be executed.
import os,sys
import process_file,find_word
from getchar import getch

dict = {}


def clscr():
    if os.name == "posix":
        os.system('clear')  # on linux / os x
    elif os.name == "nt":
        os.system('cls')  # Windows

def init_dict():
    for i in range(ord('a'),ord('z')+1):
        dict[chr(i)] = {}
    print(dict)



def main_menu():
    clscr()
    print("Main Menu\n".center(100))
    print("Hi, there!!!!".center(100))
    print("This Program helps you index the words in a list of text files and search through them.".center(100))
    print("1. Build the dictionary\n2. Search word\n3. Exit\n\nPlease choose your option:")
    input = getch()
    if input == '1':
        build_dict_menu()
    elif input == '2':
        search_menu()
    elif input == '3':
        exit() 

def build_dict_menu():
    clscr()
    print("Build Dictionary".center(100))
    print("\n\nYour Current Directory is: "+ os.getcwd())
    print("\n\nPlease enter the <path/filename> containing the list of text file to be indexed: ")
    file = input()

    try:
        with open(file, 'r', encoding="ascii", errors="surrogateescape") as f:
            if(os.stat(file).st_size == 0):
                print("The file is empty please try again.")
            else:
                process_filelist(f)
    except OSError:
        print("File not Found")
    

def process_filelist(f):
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
                    process_file.file_processing(line,fobj,dict)
                    file_success += 1
        except OSError:
            print(line, "is not Found")
            file_missing += 1
    #print(dict['a'])
    getch()
    main_menu()

def search_menu():
    clscr()
    print("Word Search".center(100))
    print("Enter the word you want to search: ")
    word = input()
    file_list = find_word.find_word(word.lower(),dict)
    if file_list == None:
        print(word ,"is not found in any file")
    else:
        print("'"+ word + "' is found in the following files:")
        for fname in file_list:
            print(fname)
    getch()
    main_menu()






init_dict()
main_menu()






#print(os.stat('./test-data/file1.txt').st_size)
fp = open("./test-data/file1.txt", "r", encoding="ascii", errors="surrogateescape")
for i in fp.readlines():
    try:
        i.encode()
        #print (i.strip())
    except UnicodeError:
        i = i[::]
        #print ("it was not a ascii-encoded unicode string!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\nn\n\n\\n\nn\n!!!!!!!!!!!!!!!!!!!!!!!!")






"""

try:
    with open('/tmp/input.txt', 'r') as f:
        ...
except OSError:
    # 'File not found' error message.
    print("Fichier non trouvé")


--------

try:
    mystring.decode('ascii')
except UnicodeDecodeError:
    print "it was not a ascii-encoded unicode string"
else:
    print "It may have been an ascii-encoded unicode string"

"""