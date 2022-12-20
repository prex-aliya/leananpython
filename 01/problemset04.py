#!/usr/bin/env python3

import sys;


def help():
    print("[+] python problemset03.py [+float | +num]");
    #print("\t-f is to force a bigger number or a negative");
    sys.exit();

def invalid():
        print("[-] Invalid");
        help();


argument = sys.argv;
length = len(argument);

if length != 1:
    if argument[1] == "-help" or argument[1] == "--help":
        help();
    # https://www.geeksforgeeks.org/python-check-for-float-string/
    # to check if it is a float, by replacing . with nothing to see if its an
    # intager
    elif argument[1].replace('.', '', 1).isnumeric() and float(argument[1]) > 0:
        size = float(argument[1]);
    else:
        invalid();
else:
    help();


# Heres the brains vvv
# https://datagy.io/python-round-2-decimals/
# how to use the round keyword ^
print(round(size - round(size), 2));






# vim: textwidth=64
