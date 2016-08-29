# this is the file that should be executed.
import os,sys
import process_file,find_word
from getchar import getch


def clscr():
    if os.name == "posix":
        os.system('clear')  # on linux / os x
        os.system('clear')  # on linux / os x
    elif os.name == "nt":
        os.system('cls')
        os.system('cls')  # Windows




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
            
    except OSError:
        # 'File not found' error message.
        print("Fichier non trouvé")
    



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