#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 17, 11, 2026
# This program generates a random number.
# It gets the user to try to guess
# the number and it uses a loop to get the user's guess.
# It breaks out of the loop if they guess correctly.

import random


def main():
    # generate a random number
    random_num = random.randint(0, 9)

    while True:
        # get user number guess
        user_num = input("Guess a number from 0-9: ")

        # check if the user input is correct data type
        try:
            user_int = int(user_num)

            if user_int != random_num:
                print("Incorrect guess, try again")
            if user_int == random_num:
                print(
                    "You guessed correctly! The correct answer is {}".format(random_num)
                )
                break

        except:
            print("{} is not a valid integer".format(user_num))


if __name__ == "__main__":
    main()
