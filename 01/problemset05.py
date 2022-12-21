#!/usr/bin/env python3
#
# This time we shall implement luhn's algorithm for validating a
# credit card number
#
# https://www.creditcardvalidator.org/articles/luhn-algorithm
# https://www.geeksforgeeks.org/program-credit-card-number-validation/
#
# easiest is to see if there not equal to 13 or 16
#
# The length of a credit card number falls between 13 and 16,
# wilst also starting with
#       6  = Discover
#       5  = Master
#       4  = Visa
#       37 = American Express

from math import floor, log10;
import sys;


arguments = sys.argv;
length = len(arguments);


def help():
    print("[+] usage: python problemset05.py [credit card num]");
    print("\t -v verbose output");
    print("\t -n specify CC number, takes the direct next");
    print("\t     argument so be careful.");
    sys.exit(1);
def error(err):
    if verbose == True:
        print("[-] An Error Occurred: " + err);
    help();
def positive(mes, pos):
    print(f"[+] {mes}{pos}");

# https://thecodingbot.com/count-the-number-of-digits-in-an-integer-python4-ways/
def lengthof(num):
    num = abs(num);
    digits = floor(log10(num)) + 1;
    return digits



# Where The Real Brains Are vvv



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
        if arguments[x] == "-n" and arguments[x+1].isnumeric():
            try:
                input = int(arguments[x+1]);
            except:
                error("Argument input has failed");
            prompt_user = False;
            positive("CMD Arguments Enabled: ", arguments[x]);

# This One is down here because a bool is not callable, this
# means that the functions can not callit, so I moved it down
# here so that is doesnt have to call it. Make Sure Names Are
# Distinct.
# https://researchdatapod.com/how-to-solve-python-typeerror-bool-object-is-not-callable/
def verbose(mes, pos):
    if to_verbose == True:
        positive(mes, pos);

if prompt_user == True:
    # This gets input from user and only accepts it if the input is
    # an intager.
    try:
        input = int(input("Card Number: ").replace('-', ''));
    except:
        error("Possible input violation");


# Is the card number 13 or 16 digits long?
length = lengthof(input);
if length not in [13, 16]:
    error("invalid card number format");
verbose("length is: ", length);


# makes the number into an array, by modulo or % the input
# number then removing the last big of the input, by multiplying
# by 0.1, which is equivilant to deviding my 10 excetpt when you
# multiply by 0 it doesnt expload.
numbers = [0] * length;
for x in range(length, 0, -1):
    numbers[x-1] = input % 10;
    input = floor(input * 0.1);


for x in range(1, length, 2):
    addin = numbers[x]*2;
    if addin > 10:
        numbers[x] = addin - 9;
    else:
        numbers[x] = addin;

luhn = sum(numbers)*9;
verbose("luhn algorithm's number: ", luhn);


# FINAL OUTPUT and decision
if (luhn % 10) == 0:
    cardven = "unknown";
    if numbers[0] in [6, 5, 4]:
        if numbers[0] == 6: cardven = "Discover";
        elif numbers[0] == 5: cardven = "Master";
        elif numbers[0] == 4: cardven = "Visa";
        elif numbers[0] == 3 and numbers[1] == 7: cardven = "American Express";
    positive("Valid card number", "");

    # The CC Vender
    positive("Card Vender(", cardven + ")");

    # https://dnschecker.org/credit-card-validator.php?ccn=6231231231234
    # Witch Major industry the credit card is used in.
    MII = ["ISO / TC", "Airlines", "Future industry", "Travel and leisure", "Banking and finance", "Finance and banking", "Sales and bankind/finance", "Petroleum", "Healthcare/telecommunications", "national standard bodies"];
    positive("Major industry identifier: ", MII[numbers[0]]);
else:
    print("[-] Invalid card number");



# vim: textwidth=64
