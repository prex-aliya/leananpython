#!/usr/bin/env python3
#
# This time we shall implement Coleman-Liau formula for
# dictating readability of a text
#
# https://readabilityformulas.com/coleman-liau-readability-formula.php
# This is how the formula works.

import sys;
import re;

arguments = sys.argv;
length = len(arguments);

def help():
    print("[+] usage: python problemset06.py [-v][-n][sentance]");
    print("\t -v verbose output");
    print("\t -n sentance input from terminal everything\n");
    print("\t\t after this command no matter what.");
    print("To get a actually good output you will need to")
    print("\tprovide at least a paragraph of text, prefably 500 words")
    sys.exit(1);
def warning(err):
    if verbose == True: print("[-] An Error Occurred: " + err);
def error(err):
    warning(err);
    help();
def positive(mes, pos): print(f"[+] {mes}{pos}");
def verbose(mes, pos):
    if to_verbose == True:
        positive(mes, pos);

to_verbose = False;
prompt_user = True;
# lotta fluff here
if length != 1:
    for x in range(1, length):
        if arguments[x] == "-v":
            to_verbose = True;
            positive("Verbose Enabled", "");
        if arguments[x] == ("-help" or "--help"):
            help();
        if arguments[x] == "-n":
            try:
                findit = x+1;
            except: error("Argument input has failed");
            prompt_user = False;
            positive("CMD Arguments Enabled", "");
            break;

if prompt_user == True:
    try:
        input = input("Sentance Input: ");
    except:
        error("Possible input violation");



# Where The Real Brains Are vvv



# Defining inital variables
letters = 0;
words = 0;
sentances = 0;

# peice together the arguments from cmd
input = arguments[findit];
for x in range(findit+1, length):
    input += arguments[x];
    words += 1;

# count how many letters are in the peiced together input
for x in input:
    if x.isalpha(): letters += 1;
    if x == "." or x == "!" or x == "?":
        sentances += 1;

verbose("Letter Count:\t", letters);
verbose("words Count:\t", words);
verbose("Sentances Count:\t", sentances);

letters_ph   = letters/words*100;
sentances_ph = sentances/words*100;

print(); # prints new line
verbose("Letter Count per 100 Words:\t\t", round(letters_ph));
verbose("Sentances Count per 100 Words:\t", round(sentances_ph));

# CLI = 0.0588L - 0.296S - 15.8
# This is the Equation ^ its horable for small ammounts of text
reading_level = round((0.0588 * letters_ph) - (0.296 *
                            sentances_ph) - 15.8);

# Just Quality of Life, this makes it so if you provide a very
# small inserpt of text it tells the user that more may be
# needed
if reading_level <= 0:
    reading_level = 1;
    verbose("More input may be needed", "");

print();
positive("The Text You Provided is Grade: ", reading_level);



# vim: textwidth=64
