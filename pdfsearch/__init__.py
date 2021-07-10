#!/usr/bin/python3

import sys
import getopt
import os


input_file = None

def usage():
    print("Usage: " + sys.argv[0] + " -i input-file")

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:d:p:')
except getopt.GetoptError:
    usage()
    sys.exit(2)

for o, a in opts:
    if o == '-i':  # input file
        input_file = a
    else:
        assert False, "unhandled option"

def usage():
    print(": " + sys.argv[0] + " -i directory-of-documents -d dictionary-file -p postings-file")

if input_file == None:
    usage()
    sys.exit(2)

