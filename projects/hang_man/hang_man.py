import random
import turtle
import requests as r


class utility:
    def titel(self):
        
        print("""
         _   _                                         
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                           |___/                      
        """)
    
    def hang_man(self):
        pass
        



class Main(utility):
    

    
    def __init__(self) -> None:
        self.file_name = "hang_words.txt" 
        self.played_letters_list = set()
        self.hang_counter = 0
        
    
    # This tries to get a word from a word API. If it fails, it defaults to a file with words.
    def pick_word(self):
        
        print("Error fetching from API, defaulting to file-based word list.")
        word_list = open("hang_words.txt","r").read().split("\n")
        word = random.choice(word_list).lower()    
        
        return word
            
            
            
    
    def genrate_word_list(self, word):
        letter_placeholder = ["_"] * len(word)
        return letter_placeholder
    
    

    def REPL(self):
        word = self.pick_word()
        letter_string = self.genrate_word_list(word)
        while self.hang_counter <= 20:
            
            guess = input("guess a letter or guess a word to see if your correct!: ").lower()
            if len(guess) > 1:
                self.check_word(guess, word)
            else:
                self.check_letter(guess, word, letter_string)
            
        self.end_messge(word)
    
            
    def check_letter(self, guess, word, letter_string):
        if self.played_words(guess):
            if guess in word:
                for i in range(len(word)):
                    if guess == word[i]:
                        letter_string[i] = guess
                self.make_word_check(letter_string, word)
                print(f"\nyour letter {guess} was in the word,\n\ncurrent string {letter_string}\nplayed words: {self.played_letters_list}\nyou have {21 - self.hang_counter} guesses left!\n")
                
            else:
                print(f"\nyour letter is not in the word.\ncurrent string: {letter_string}\nplayed words: {self.played_letters_list}\nyou have {21 - self.hang_counter} guesses left!\n")
        
       

                
            
    def make_word_check(self, letter_string, word):
        string = ""
        for i in letter_string:
            string += i
        if string == word:
            self.end_messge(word, "win")
    

            
    def check_word(self, guess, word):
        if guess == word:
            self.end_messge(word, "win")
        print("\nnot the right word\n")
        self.hang_counter += 1
    
    
    
    def played_words(self, guess):
        if guess in self.played_letters_list:
            print("\nyou have already used this word!\n")
            return False
        else:
            self.played_letters_list.add(guess)
            self.hang_counter += 1
            return True

        
    
        
        
            
            
    

        
        
        
    def end_messge(self, word, end = "lose", ):
        print(f"you {end}! the word was {word}!")
        exit()
   

    


x = Main()
x.hang_man()
x.titel()
x.REPL()
