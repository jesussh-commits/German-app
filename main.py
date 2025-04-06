# main.py This is the central program, though. It's the one that manages the others

from src.root_finder_logic import find_related_words #takes or calls find_r_w from the folder where it's stored, src

def main(): #definition of the main fu or program
    print("Willkommen zum deutschen Wortstamm-Finder!")
    word = input("Gib ein deutsches Wort ein: ").strip().lower() #in var word an input is stored 


    related = find_related_words(word) #uses the only fu we've written. But it extends it, it interacts w the user giving asking for a word and giving an answer based on what it finds in data using the f
    if related:
        print(f"Wörter, die mit dem Stamm «{word}» verwandt sind:")
        for w in related:
            print(f"- {w}")
    else:
        print("Keine verwandten Wörter gefunden. Versuch ein anderes Wort.")


if  __name__ == "__main__":
    main()

print("This is my first Git-powered language learning app!")
        
