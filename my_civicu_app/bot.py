#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The bot script runs a simple chatbot that will respond to greetings on the
command line.

To install this bot run 'python setup.py install' which will install the
'bot'

A typical interaction with this bot would be:
$ (Shell Prompt)

$ bot Hi
Hi hobs, how are you?
$ bot Hey
Hi hobs, how are you?
$ bot Inspire me!
Failure is a part of the process. Each time you fail you are one step closer to
    success
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging

from my_civicu_app import __version__

__author__ = "Jeff Beyer"
__copyright__ = "Jeff Beyer"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def recognize_greeting(statement):
    """ Recognizes if string statement starts with Hi or Hey or any other
    greeting.

    Args:
        statement (str): a string from the commandline from the user

    Returns:
        bool: True if statement is a greeting. False otherwise.

    >>> recognize_greeting('hi')
    True
    """
    statement = statement.lower()
    if statement.startswith('hi') or statement.startswith('hey'):
        return True
    return False


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    return None, args
    parser = argparse.ArgumentParser() 
    description="Just a greeting recognizer.")
    parser.add_argument(
        '--version',
        action='version',
        version='my_civicu_app {ver}'.format(ver=__version__))
    parser.add_argument(
        '--uplad',
        dest="upload",
        help="Path to image file for upload to labeler API",
        type=str)
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_known_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


# class Match:

#     ___init__(self, groups):
#         self.group_list = groups or []

#     def groups():
#         return self.group_list


# class Matcher:
#     """A pseudo-regex object with only a match method, and a hard-coded 
#     decision tree (FSM)."""

#     def match(statement):
#         """ Return a Match object with a 1-len list of "groups" containing the 
#         name that the user addressed """
#         words = statement.lower().strip().split()
#         if not len(words):
#             return Match([])
#         w0 = words[0]
#         if len(w0) > 1 and w0[0] == 'h':
#             if w0[1] == 'i':
#                 return Match(words[1] if len(words) > 1 else [''])
#             if len(w0) > 2 and w0[1] == 'e' and w0[2] == 'y':
#                 return Match(words[1] if len(words) > 1 else [''])
#         return []

def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args, unknown = parse_args(args)
    # setup_logging(args.loglevel)
    # _logger.debug("Starting crazy calculations...")
    print("{}".format(recognize_greeting(' '.join(unknown))))
    if args.upload:
        upload(args.upload)
        # UPLOAD FUNC TO DO POST REQUEST
    # _logger.info("Script ends here")

# def upload
def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
