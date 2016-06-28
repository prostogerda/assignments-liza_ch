#! /usr/bin/env python3


"""
Game offers to user to guess integer number from 0 to `max_rand_num`.
User has limited efforts.
After win or loss user can play again or finish the game.
"""


import random
import time
import sys


def main():
    """
    Defines maximum number to guess and amount of lives, and starts the game.
    :return:
    """
    max_rand_num = 100
    lives = 10
    play(max_rand_num, lives)


def play(max_rand_num: int, lives: int):
    """
    Generates random number from 0 to `max_rand_num` and offers user to guess it.
    Number of lives decreases with every failure.
    When lives end or user guesses the number, game offers to play again.
    :param max_rand_num:
    :param lives: lives < max_rand_num
    :return:
    """
    unknown_num = random.randint(0, max_rand_num)
    win = False
    curr_lives = lives
    while curr_lives > 0 and not win:
        # In this cycle user tries to guess the number
        guess = input("Guess a number from 0 to {}! ".format(max_rand_num))
        try:
            # Checks if input is correct (input string may be converted to int)
            guess_int = int(guess)
            curr_lives, win = compare(guess_int, unknown_num, curr_lives,
                                      max_rand_num)
        except ValueError:
            print("{} is not integer".format(guess))
    if win:
        print("You win!")
    else:
        print("You lose!")
    time.sleep(1)
    replay = input("Would you like to play again? Y/N ")
    # Replay or not in dependence of input
    return play(max_rand_num, lives) if repeat(replay) else sys.exit()


def compare(guess: int, unknown_num: int, curr_lives: int, max_rand_num: int):
    """
    Compares unknown number and guessed number.
    In case of fail number of lives decreases.
    :param guess:
    :param unknown_num:
    :param curr_lives: > 0
    :return:
    """
    win = False
    if guess > max_rand_num or guess < 0:
        print("{} is out of [0, {}] interval. "
              "Please try again".format(guess, max_rand_num))
    elif guess == unknown_num:
        win = True
    elif guess > unknown_num:
        print("Guess lower!")
        curr_lives -= 1
    else:
        print("Guess higher!")
        curr_lives -= 1
    return curr_lives, win


def repeat(replay: str):
    """
    Checks if user wants to replay
    :param replay:
    :return:
    """
    if replay == "Y":
        print("Enjoy!")
        return True
    if replay == "N":
        print("Goodbye!")
        return False
    return repeat(input("Please enter Y or N: "))

if __name__ == '__main__':
    main()
