#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program guesses random numbers


import random


def main():
    # this function guesses random numbers

    # input
    user_number = int(input("Enter the number(1 ~ 10): "))

    # process
    some_variable = random.randint(1, 10+1) # a number between 1 and 10
    if some_variable ==  user_number:
        # output
        print("It is correct!")
    else:
        print("It is wrong")
        print("The number is {}".format(some_variable))

if __name__ == "__main__":
    main()
