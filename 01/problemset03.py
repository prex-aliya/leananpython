#!/usr/bin/env python3
#
# This is pretty much the same as the last one just some changes
# at the bottom
#
# Questions? Try looking it up on
# https://docs.python.org/
#
# You only need to know the bottom vvv
# the top is mostly fluf to get
# good user experience


# imports sys to use sys.exit()
# uses it by default though (not neccissary)
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm
import sys;


# these define opertions that are repetitive
#
def help():
    print("[+] python problemset01.py [-f | num less 8] [num]");
    print("\t-f is to force a bigger number or a negative");
    print("\t   (which does nothing)");
    # exit with one, which tells there was an error
    sys.exit(1);

def invalid():
        print("[-] Invalid");
        help();


# gets the arguments from cmd
argument = sys.argv;
# gets the length of the arguments
length = len(argument);

# if there is an argument
if length != 1:
    # if the length of the argument is 2 so that
    # we can get a number with the flag, else
    if argument[1] == "-f":
        # https://pythonexamples.org/python-if-and/#2
        # how to use the if and
        if length >= 2 and argument[2].isnumeric():
            size = int(argument[2]);
        else:
            invalid();
    elif argument[1] == "-help" or argument[1] == "--help":
        help();

    # https://www.pythonpool.com/python-check-if-string-is-integer/
    # to detect if a string is numeric like the arguments
    # https://www.tutorialkart.com/python/python-range/python-if-in-range/
    # how to detect if a variable is in a range
    elif argument[1].isnumeric() and int(argument[1], base=16) in range(1, 9, 1):
        size = int(argument[1]);
    else:
        invalid();
else:
    size = 4;




# Really only need this vvv



# This is a key word to make a function
# https://www.geeksforgeeks.org/python-def-keyword/
def print_piramid(ammount, cart):
    print(cart * ammount + cart, end="");


for x in range(size):

    # print white space. range from x to size,
    # which inverses the range, when size increases
    # the ammount it prints gets bigger, but gradually
    # gets less and less

    print_piramid(size-x, " ");
    print_piramid(x, "#");

    print(" ", end="");
    print_piramid(x, "$");
    # This print the newline charactor
    print("\n");

# vim: textwidth=64
