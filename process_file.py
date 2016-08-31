# this adds words to the dictionary from single text file passed to it.
import find_word as fw
import re
regex = re.compile("([A-Za-z]+)")
def file_processing(fname,fp,dict):
    print("fname>>",fname)
    L=[]
    for line in fp:
        for word in regex.findall(line):
            if not word.isalpha():
                continue
            word = word.lower()
            if word not in L:
                L.append(word)
                filenames_list = fw.find_word(word,dict)
                if filenames_list == None:
                    dict[word[0:1]][word] = [fname]
                else:
                    filenames_list.append(fname)