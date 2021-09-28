#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program will add up all positive integers up to the entered integer.


def main():
    # this function adds the integers
    loop_counter = 0
    the_sum = 0

    # input
    user_input = input("Enter a positive integer: ")

    # process & output
    try:
        positive_integer = int(user_input)
        while loop_counter <= positive_integer:
            the_sum = the_sum + loop_counter
            loop_counter = loop_counter + 1
        print(
            "The sum of all the numbers from 1 to {0} is {1}.".format(
                positive_integer, the_sum
            )
        )
    except Exception:
        print("Invalid input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
