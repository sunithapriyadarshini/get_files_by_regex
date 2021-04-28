#!/usr/bin/env python
""" Return a list of files whose names match a regex in a given directory
"""
import argparse
import os
import re
import time


def get_files_by_regex(input_dir, regex):
    """ Returns list of files whose names match the given regex in a given directory.
    Args:
        param1: directory to be searched recursively
        param2: regex to match
    Returns:
        List of filenames.
    """
    matched_files = []

    if regex:
        print("Getting list of files for directory " +
              input_dir + " and regex " + regex + ":\n")
    else:
        print("Getting list of all files for directory " + input_dir + ":\n")


    for dirpath, dirnames, filenames in os.walk(input_dir):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            if re.match(regex, f):
                print(filepath)
                matched_files.append(filepath)

    return matched_files


def main(args):
    """
    Args:
        param1: command line arguments for directory and regex.
    Returns:
        Returns either all files if no regex provided, files that match a regex if regex provided
    """
    input_dir = os.getcwd()
    regex = ''

    if args.input_dir is not None:
        input_dir = os.path.abspath(args.input_dir) + '/'

    if args.regex is not None:
        regex = args.regex

    return get_files_by_regex(input_dir, regex)


if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", action='store', dest="input_dir",
                        help="Pass directory to search for files")
    parser.add_argument("-r", "--regex", action='store', dest="regex",
                        help="Pass regex to match file names")

    arguments = parser.parse_args()
    main(arguments)
    print("\n Execution Time: %s seconds" % (time.time() - start_time))
