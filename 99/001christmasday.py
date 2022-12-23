#!/usr/bin/env python3
#
# This progrom finds out how many days till christmas


from datetime import datetime;
import sys;


prompt_user = False;
user_date = False;
day = 26;
month = 12;
year = 2020;
arguments = sys.argv;
length = len(arguments);


def verbose_true(input):
    if to_verbose == True:
        print(input)
def help():
    print("[+] usage: python 001christmasday.py");
    print("\t-v verbose output");
    print("\tThis Small Program Prints Out How");
    print("\tLong Till Christmas Day!");
    #print("\tThere is Room for Improvment im too lazy");
    sys.exit();
def warning(err):
    verbose_true("[-] WARNING: {}".format(err));
def error(err):
    verbose_true("[-] ERROR: {}!".format(err));
    help();
def verbose(input):
    verbose_true("[*] {}".format(input));
def positive(input):
    print("[+] {}".format(input));

def user_input():
    if prompt_user == true:
        while True:
            try:
                day   = int(input("Day: "));
                month = int(input("Month: "));
                year  = int(input("Year: "));
                break;
            except:
                error("Possible input violation");


to_verbose = False;
if length != 1:
    for x in range(1, length):
        if arguments[x] == "-v":
            to_verbose = True;
            positive("verbose enabled");
        if arguments[x] == ("-help" or "--help"):
            help();
        if arguments[x] == "-d":
            positive("cmd arguments enabled");
            break;



# vvv



def main():
    if prompt_user == True:
        current = datetime(day=int(day), month=int(month), year=int(year));
        year_c = datetime.now().strftime("%Y");
        verbose("Using user specified date");
    else:
        try:
            current = datetime.now();
            year_c = datetime.now().strftime("%Y");
        except: warning("Failed to Get Current Time\n\twill use defult time");

    if current.month == 12 and current.day >= 25:
        try: year_c = int(year_c);
        except: error("Failed to convert year into intager");
    try: date2 = datetime(day=25, month=12, year=int(year_c),
                          hour=8);
    # personal family tradition
    except: error("Failed to convert date into intager");


    timedelta = date2 - current;

    delta_seconds = timedelta.seconds;
    delta_minuets = delta_seconds*60;
    delta_hours   = delta_minuets*60;

    verbose("Time left in Seconds {}".format(timedelta.total_seconds()));
    verbose("Days: {}".format(timedelta.days));
    #verbose("Hours: {}".format(delta_hours));
    #verbose("Minuets: {}".format(delta_minuets));
    verbose("Seconds: {}".format(timedelta.seconds));
    verbose("MicroSeconds: {}".format(timedelta.microseconds));

    print("Only {0} Days and {1} Hours Left!".format(timedelta.days,
                    round(timedelta.seconds/60/60, 2)));



# Runs Main Function when all is loaded
if __name__ == "__main__":
    main();

# vim: textwidth=64
