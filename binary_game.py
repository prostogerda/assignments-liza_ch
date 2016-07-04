#! /usr/bin/env python3


"""
Game offers to user to guess integer number from 0 to `max_rand_num`.
User has limited efforts.
After win or loss user can play again or finish the game.
"""


import random
import time


REPLAY = ("Y", "y")


def play(max_rand_num: int, curr_lives: int, unknown_num):
    """
    Generates random number from 0 to `max_rand_num` and offers user to guess it.
    Number of curr_lives decreases with every failure.
    When curr_lives end or user guesses the number, game offers to play again.
    :param max_rand_num:
    :param curr_lives: curr_lives < max_rand_num
    :param unknown_num: number to guess
    :return:
    """
    win = False
    while curr_lives > 0 and not win:
        # In this cycle user tries to guess the number
        guess = input("Guess a number from 0 to {}: ".format(max_rand_num))
        try:
            # Checks if input is correct (input string may be converted to int)
            guess_int = int(guess)
            curr_lives, win = compare(guess_int, unknown_num, curr_lives,
                                      max_rand_num)
        except ValueError:
            print("{} is not integer".format(guess))
    print("You win!") if win else print("You lose!")
    time.sleep(1)
    return (True if input("Would you like to play again? Y/N ") in REPLAY
            else False)


def compare(guess: int, unknown_num: int, curr_lives: int,
            max_rand_num: int) -> (int, bool):
    """
    Compares unknown number and guessed number.
    In case of fail number of lives decreases.
    :param guess:
    :param unknown_num:
    :param curr_lives: > 0
    :param max_rand_num
    :return: number of remain lives, victory status (True or False)
    """
    if guess > max_rand_num or guess < 0:
        print("{} is out of [0, {}] interval. "
              "Please try again".format(guess, max_rand_num))
        return curr_lives, False
    if guess == unknown_num:
        return curr_lives, True
    if guess > unknown_num:
        print("Guess lower!")
        return curr_lives - 1, False
    print("Guess higher!")
    return curr_lives - 1, False


def main():
    """
    Defines maximum number to guess and amount of lives, and starts the game.
    :return:
    """
    max_rand_num = 100
    lives = 10
    replay = True
    while replay:
        print("Enjoy!")
        replay = play(max_rand_num, lives, random.randint(0, max_rand_num))
    print("Goodbye!")


def main_():
    """
    "Functional" main
    """
    max_rand_num = 100
    lives = 10
    print("Enjoy!")
    main_() if play(max_rand_num, lives,
                    random.randint(0, max_rand_num)) else print("Goodbye!")

if __name__ == '__main__':
    main()
