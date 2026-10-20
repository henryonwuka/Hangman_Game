"""A Basic Hangman Game"""

import random
from os import strerror
import ascii_hangmane_art


class Hangman:
    def __init__(self):
        self.__player_score = 0
        self.__player_attempts = 0
        # self.player_word_attempt = []
        self.player_max_attempts = 6
        self.__word_list = []
        print("Loading Game...")
        self.get_words()
        

    # def start_game(self):
    #     pass


    def player_state(self):
        """
        Returns True if player has more attempt, else False.
        """
        return self.__player_attempts < self.player_max_attempts


    def get_words(self):
        #Opening file
        try:
            word_file = open("word_list", mode="r") #Inputs a file containing comma separated words to be used in the game
        except IOError as exc:
            print(strerror(exc.errno))

        #Loading words into game instance wordlist
        self.__word_list += word_file.readlines()

        #Closing file
        word_file.close()


    def random_word_pick(self):
        """Returns a random word from the word list in lower case"""
        return (random.choice(self.__word_list)).upper().strip()


    def ascii_display(self):
        print(ascii_hangmane_art.hangman_stages[self.__player_attempts])


    def player_input(self):
        """Gets and returns a valid lower case letter from player"""

        while True:
            player_input = input("Enter a Letter: ")
            if len(player_input) == 1 and player_input.isalpha():
                return player_input.upper().strip()
            else:
                print("Enter a valid letter!!!")


    def play_game(self):
        hidden_word = self.random_word_pick()
        display_word = "_" * len(hidden_word)
        print("Guess the word correctly, and save the man")
        self.ascii_display()

        while self.player_state() and display_word != hidden_word:
            print(f"{display_word}")
            player_word = self.player_input()

            if player_word in hidden_word and player_word not in display_word:
                print(f"Correct")
                for i in range(len(hidden_word)):   #Replace a correct word in the display
                    if hidden_word[i] == player_word:
                            display_word = display_word[:i] + player_word + display_word[i + 1:]
                
                if display_word == hidden_word:
                    self.__player_score += 1
                    print(f"Full word: {display_word}\nScore: {self.__player_score}")
                    return

            else:
                if player_word in display_word:
                    print(f"You already entered that letter!!!")

                else:
                    self.__player_attempts += 1
                    self.ascii_display()
                    print(f"Opps, wrong letter. Attempts left: {self.__player_attempts}/{self.player_max_attempts}")


    def end_game(self):
        """Ends the game and displays player results"""
        print(f"Game Over\nFinal Score: {self.__player_score}")

        #Resets game parameters
        self.__player_score = 0
        self.__player_attempts = 0



def main():
    game_instance = Hangman()
    while game_instance.player_state():
        game_instance.play_game()

    else:
        game_instance.end_game()

main()