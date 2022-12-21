#!/usr/bin/env python3
#
# This time we shall implement Coleman-Liau formula for
# dictating readability of a text
#
# https://readabilityformulas.com/coleman-liau-readability-formula.php
# This is how the formula works.

import sys;

arguments = sys.argv;
length = len(arguments);

def help():
    print("[+] usage: python problemset05.py [credit card num]");
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

if prompt_user == True: error("No use of -n argument");



# Where The Real Brains Are vvv



letters = 0;
words = 0;
sentances = len(re.findall(r"[^?!.][?!.]", paragraph));

input = arguments[findit];
for x in range(findit+1, length):
    input += arguments[x];
    words += 1;

for x in input:
    if x.isalpha(): letters += 1;
    print(x);

print(letters);
print(words);
print(sentances);



# vim: textwidth=64
