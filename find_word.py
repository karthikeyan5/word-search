# finds the given word from the dictionary.
def find_word(search_word,dictionary):
    #dictionary = {'a':{'aband':['file1.txt','file3.txt'],'apple':['file1.txt']},'b':{'ball':['file5.txt','file8.txt','file1.txt'],'baby':['file5.txt','file2.txt','file3.txt'],'boy':['file5.txt','file8.txt','file1.txt']},'c':{'car':['file45.txt','file28.txt','file12.txt'],'coil':['file5.txt','file1.txt'],'cruze':['file15.txt','file18.txt','file1.txt']}}

    first_alphabet = (search_word.lower()[0:1])
    result = dictionary[first_alphabet].get(search_word.lower())
    return result
    