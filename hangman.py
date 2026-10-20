"""A Basic Hangman Game"""

import random
from os import strerror


class Hangman:
    def __init__(self):
        self.player_score = 0
        self.player_attempts = 0
        # self.player_word_attempt = []
        self.player_max_attempts = 6
        self.word_list = []
        print("Loading Game...")
        self.get_words()
        

    # def start_game(self):
    #     pass

    def get_words(self):
        #Opening file
        try:
            word_file = open("word_list", mode="r") #Inputs a file containing comma separated words to be used in the game
        except IOError as exc:
            print(strerror(exc.errno))

        #Loading words into game instance wordlist
        self.word_list += word_file.readlines()

        #Closing file
        word_file.close()
        
    def random_word_pick(self):
        """Returns a random word from the word list in lower case"""
        return (random.choice(self.word_list)).upper().strip()

    def ascii_display(self):
        pass

    def player_input(self):
        """Gets and returns a valid lower case letter from player"""

        while True:
            player_input = input("Enter a Letter: ")
            if len(player_input) == 1 and player_input.isalpha():
                return player_input.upper().strip()
            else:
                print("Enter a valid letter!!!")

    def play_game(self):
        
        while self.player_attempts < self.player_max_attempts:
            hidden_word = self.random_word_pick()
            display_word = "_"*len(hidden_word)

            while display_word != hidden_word:
                print(display_word)
                player_word = self.player_input()

                if player_word in hidden_word:
                    for i in range(len(hidden_word)):   #Replace a correct word in the display
                        if hidden_word[i] == player_word:
                            display_word = display_word[:i] + player_word + display_word[i + 1:]

                else:
                    print("Wrong word")
                    self.player_attempts += 1

        else:
            self.end_game()

    def end_game(self):
        """Ends the game and displays player results"""
        print(f"Game Over\nFinal Score: {self.player_score}")

        #Resets game parameters
        self.player_score = 0
        self.player_attempts = 0



def main():
    game_instance = Hangman()
    game_instance.play_game()


main()