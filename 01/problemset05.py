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
    input = int(input("Card Number: "));
except:
    error("possible input violation");

# Is the card number 13 or 16 digits long?
length = length(input);
if length not in [13, 16]:
    error("invalid card number format");
print(f"[+] length is: {length}");

numbers = [0] * 16;
#for x in range(15, 0, -1):
#    #print(input - round(input, -1));
#    numbers[x] = input - round(input, -1);
#    print(round(input, -1))
#    print(input)
#    input = floor(input*0.1)#round(input, shift)

if numbers[0] not in [6, 5, 4] and length == 13:
    if numbers[3] not in [6, 5, 4]:
        print("[+] not a credit card number");



print(numbers);

print("[+] Valid card number format");





# vim: textwidth=64
