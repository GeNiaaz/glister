#!/usr/bin/python3

import sys
import getopt
import os
import logging

def main(input_file):
    ...


logger = logging.getLogger(__name__)

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

if input_file == None:
    usage()
    sys.exit(2)

main(input_file)
