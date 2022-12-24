#!/usr/bin/env python3
#
# This progrom finds out how many days till christmas


from datetime import datetime;
import time;
import sys;


prompt_user = False;
user_date   = False;
# family tradition christmas starts at 8
hour_c  = 8;
day     = 26;
month   = 12;
year    = 2020;
count_intraval  = 0.1;
arguments   = sys.argv;
length      = len(arguments);


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


def find_current():
    current = datetime.now();
    return current;
def find_delta():
    current = datetime.now();
    year_c = current.year;

    if month == 12 and day <= 25 and hour <= 8:
        year_c += 1;

    try: date2 = datetime(day=25, month=12, year=int(year_c),
                         hour=int(hour_c));
    except: error("failed to convert date into intager");
    return date2;

def print_left(timedelta):
    try: print("Only {0} Day(s) and {1} Hour(s) Left!".format(timedelta.days,
                    round(timedelta.seconds/60/60, 2)));
    except: error("Failed to print time left");

def count_down():
    current = find_current();
    date2 = find_delta();
    countdelta = date2 - current;

    if verbose == True:
        countprint = "[*] Seconds left: ";
    else: countprint = "";

    verbose("Count Down To Crhistmas Started");
    while (current.second - countdelta.seconds) != 0:
        current = datetime.now();
        countdelta = date2 - current;

        #if countdelta.days < 1:
        print("{0}".format(countdelta));
        print("{0}{1}".format(countprint, countdelta.seconds));

        time.sleep(0.1);
        print("\033[3A");

    print_left(countdelta);
    verbose("Count Down To Christmas Started");
    sys.exit()


to_verbose = False;
if length != 1:
    for x in range(1, length):
        if arguments[x] == "-v":
            to_verbose = True;
            positive("Verbose Enabled");
        elif arguments[x] in ("-c",  "--count-down"):
            count_down();
        elif arguments[x] in ("-h", "--hour"):
            try:
                hour_c = int(arguments[x+1]);
                verbose("User specified hour");
            except:
                warning("Hour input violation defaulting to 8");
                hour_c = 8;
        elif arguments[x] in ("-i", "--interval"):
            try:
                count_intraval = int(arguments[x+1]);
                verbose("User Specified Count Down Interval");
            except:
                warning("Input violation defaulting to 1");
                hour_c = 1;
        elif arguments[x] in ("-help", "--help"):
            help();
        elif arguments[x] == "-d":
            positive("cmd arguments enabled");
            break;



# vvv



def main():
    verbose_true("");

    if prompt_user == True: error("Prompt User is not implemented");
    else:
        try:
            current = datetime.now();
            year_c = int(current.year);
        except:
            error("Failed to use default time"
                        .format(year_c));

    verbose("Current Year {}".format(year_c));

    date2 = find_delta();
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

    print_left(timedelta);



# Runs Main Function when all is loaded
if __name__ == "__main__":
    main();

# vim: textwidth=64
