# src/root_finder.py is the logic. It contains just 1 function, find_related_words

from data.german_roots_database import german_roots_database

def find_related_words(word:str): #this function is an auxiliary (or element) of main. It'll be called by main
    word = word.lower()
    if word in german_roots_database:
        return german_roots_database[word]
    for root in german_roots_database:
        if root in word or word in root:
            return german_roots_database[root]
    return None


