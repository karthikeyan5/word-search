# this adds words to the dictionary from single text file passed to it.
import find_word as fw
def file_processing(fname,fp):
    L=[]
    for line in fp:
        for word in line.split():
            if word not in L:
                filenames_list = fw.find_word()
                if filenames_list == "None":
                    dict[word[0:1]] = word
                    dict[word[0:1]][word] = fname
                else:
                    filenames_list.append(fname)
                    dict[word[0:1]][word] = filenames_list.append(fname)
                    L.append(word)

