# Hangman Game

import random
import string

WORDLIST_FILENAME = "/Users/arthurwilliams/Desktop/hangman_game/Hangman/practise/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word,letters_guessed):

        """"This function takes in two parameters, one that is a string 
            and another that is a list that contains letters. 
            The string is compared with the list of letters and if they
            consist of the same type and amount of letters then the function will return 
            a True boolean if not a False boolean will be returned
        """

        # compares the size of both arguments
        if (letters_guessed) != 0:
            #when the element is in both arguments it is removed from the list
            word = [x for x in secret_word if x in letters_guessed] 
            #if the list is empty return True and if not return False
            if len(word) == len(secret_word):
                return True
            else:
                return False
        return False



def get_guessed_word(secret_word,letters_guessed,results=""):

        """"This function takes in two parameters, one that is a string 
            and another that is a list that contains letters. 
            The string is compared with the list of letters and function returns the letters
            that are in both variables and an "_ " for missing letters"""

        #create an empty string
        ans = results
        if ans == "":
            #loop over string and if letter is in list of letters append it to the string "ans" if not append "_ "
            for x,y in enumerate(secret_word):
                if y in letters_guessed:
                    ans += y+" "
                else:
                    ans += "_ "
            #replace the whitespace after the last string element with a fullstop
            ans = ans[:-1] #+"."
            #return the string ans 
            return ans



def get_available_letters(letters_guessed):

        """"Function takes in one input that is a list of letters and returns a string 
            of all the letters in the alaphabet that are not found in this list. """

        #create a list of all the letters that are not in the input list
        results = [x for x in string.ascii_lowercase if x not in letters_guessed]
        #create an empty string
        ans = ""
        #add all the elements in the list results to the string ans 
        for x in results:
            ans += x
        #return the string ans 
        return ans
    
    

def hangman(secret_word):


        """"This function takes as input a random 'secret word' from the words.txt word bank and initializes a game of 
            hangman by welcoming the palyer and presenting the numbe rof guesses they have available"""
        terminate = False
        guesses = 6 
        warning = 3
        letters_guessed = []
        w_letters_guessed = []

        print("\nWelcome To The Game Hangman !")
        print("I am thinking of a word that is", len(secret_word), "letters long")
        print("_ _ _ _ _ _ _ _ _ _")
        print("\nYou have", warning, "warnings left.")
        
        while guesses > 0:

            print("\nYou have", guesses, "guesses left.")
            print("Available letters: ", get_available_letters(letters_guessed))
            lg = input("Please guess a letter: ")
            if str.isalpha(lg): 
                lg = lg.lower()
                if lg not in get_available_letters(letters_guessed) or lg in w_letters_guessed:
                    results = get_guessed_word(secret_word, letters_guessed)
                    if warning > 0:
                        warning -= 1
                    else: 
                        guesses -= 1
                    print("Opps! That letter has already been choosen:", "You have", warning, "warnings left:", results)
                else:
                    if lg in secret_word:
                        letters_guessed.append(lg)
                        results = get_guessed_word(secret_word, letters_guessed)
                        print("Good guess:", results)
                        terminate = is_word_guessed(secret_word,letters_guessed)
                        if terminate == True:
                            print("\nCongratulations You Have Guessed The Right Word, Your Final Score Is:", len(secret_word)*guesses, ".")
                            break
                    else:
                        w_letters_guessed.append(lg)
                        results = get_guessed_word(secret_word, letters_guessed)
                        print("Opps! That letter is not in my word:", results)
                        if lg in ["a","e","i","o","u"]:
                            guesses -= 2
                        else:
                            guesses -= 1
                print("_ _ _ _ _ _ _ _ _ _")
            else:
                lg = lg.lower()
                if warning > 0:
                        warning -= 1
                else: 
                    guesses -= 1
                results = get_guessed_word(secret_word, letters_guessed)
                print("You can only input alphaets", "You have", warning, "warnings left:",results )
                print("_ _ _ _ _ _ _ _ _ _")

        if terminate != True:
            print("\nUnfortunately You Have Not Been Able to Complete This Game\nThe Right Word Was:", secret_word + ".")
        



# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word.replace(" ","")) == len(other_word):
        for x,y in enumerate(my_word.replace(" ","")): 
            if y.lower() in string.ascii_lowercase and my_word.count(y) == other_word.count(y):
                if y.lower() == other_word[x]:
                    ans = True
                else: 
                    ans = False
                if ans == False:
                    return False
            elif y != "_": 
                return False
    else:
        ans = False
    return ans



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    ls = []
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()

    for word in wordlist:
        if match_with_gaps(my_word.strip(),word) == True:
            ls.append(word)
    if len(ls) == 0: 
        print("No Matches Found")
    else:
        print(ls)



def hangman_with_hints(secret_word):


        """"This function takes as input a random 'secret word' from the words.txt word bank and initializes a game of 
            hangman by welcoming the palyer and presenting the numbe rof guesses they have available"""
        terminate = False
        guesses = 6 
        warning = 3
        letters_guessed = []
        w_letters_guessed = []

        print("\nWelcome To The Game Hangman !")
        print("I am thinking of a word that is", len(secret_word), "letters long")
        print("_ _ _ _ _ _ _ _ _ _")
        print("\nYou have", warning, "warnings left.")
        
        while guesses > 0:

            print("\nYou have", guesses, "guesses left.")
            print("Available letters: ", get_available_letters(letters_guessed))
            lg = input("Please guess a letter: ")
            if str.isalpha(lg): 
                lg = lg.lower()
                if lg not in get_available_letters(letters_guessed) or lg in w_letters_guessed:
                    results = get_guessed_word(secret_word, letters_guessed)
                    if warning > 0:
                        warning -= 1
                    else: 
                        guesses -= 1
                    print("Opps! That letter has already been choosen:", "You have", warning, "warnings left:", results)
                else:
                    if lg in secret_word:
                        letters_guessed.append(lg)
                        results = get_guessed_word(secret_word, letters_guessed)
                        print("Good guess:", results)
                        terminate = is_word_guessed(secret_word,letters_guessed)
                        if terminate == True:
                            print("\nCongratulations You Have Guessed The Right Word, Your Final Score Is:", len(secret_word)*guesses, ".")
                            break
                    else:
                        w_letters_guessed.append(lg)
                        results = get_guessed_word(secret_word, letters_guessed)
                        print("Opps! That letter is not in my word:", results)
                        if lg in ["a","e","i","o","u"]:
                            guesses -= 2
                        else:
                            guesses -= 1
                print("_ _ _ _ _ _ _ _ _ _")
            else:
                if lg == "*":
                    results = get_guessed_word(secret_word, letters_guessed)
                    show_possible_matches(results)
                else: 
                    if warning > 0:
                            warning -= 1
                    else: 
                        guesses -= 1
                    results = get_guessed_word(secret_word, letters_guessed)
                    print("You can only input alphabets", "You have", warning, "warnings left:",results )
                    print("_ _ _ _ _ _ _ _ _ _")

        if terminate != True:
            print("\nUnfortunately You Have Not Been Able to Complete This Game\nThe Right Word Was:", secret_word + ".")
        


if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word)
