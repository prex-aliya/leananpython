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


def help():
    print("[+] python problemset05.py [credit card num]");
    #print("\t-f is to force a bigger number or a negative");
    sys.exit(1);
def error(err):
    print("[-] An Error Occurred: " + err);
    help();
# https://thecodingbot.com/count-the-number-of-digits-in-an-integer-python4-ways/
def length(num):
    num = abs(num);
    digits = floor(log10(num)) + 1;
    return digits



# This gets input from user and only accepts it if the input is
# an intager.
try:
    input = int(input("Card Number: ").replace('-', ''));
except:
    error("possible input violation");

# Is the card number 13 or 16 digits long?
length = length(input);
if length not in [13, 16]:
    error("invalid card number format");
print(f"[+] length is: {length}");

# makes the number into an array
numbers = [0] * length;
for x in range(length, 0, -1):
    numbers[x-1] = input % 10;
    input = floor(input * 0.1);

# checks if the first numbers are valid for a card company
# stated above ^^^
cardven = "unknown";
if numbers[0] in [6, 5, 4]:
    if numbers[0] == 6:
        cardven = "Discover";
    elif numbers[0] == 5:
        cardven = "Master";
    elif numbers[0] == 4:
        cardven = "Visa";


for x in range(1, length, 2):
    addin = numbers[x]*2;
    if addin > 10:
        numbers[x] = addin - 9;
    else:
        numbers[x] = addin;

print(sum(numbers));

#print("[+] Valid card number format");





# vim: textwidth=64
