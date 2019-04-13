#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import polib


def extract(args):
    #  extract texts from a source and write to PO file
    print "extract"


def inject(args):
    print "inject"


def main():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
                                     description="Extract text and inject translations.",
                                     epilog="...")

    subparsers = parser.add_subparsers()
    sp_extract = subparsers.add_parser('extract',
                                       help="Extract text from document to PO file.")
    sp_extract.set_defaults(func=extract)

    sp_inject = subparsers.add_parser('inject',
                                      help="Inject text from PO file into copy of document.")
    sp_inject.set_defaults(func=inject)

    parser.add_argument('source', type=str,
                        help='an OmniGraffle file')
    parser.add_argument('target', type=str,
                        help='a PO or POT file')

    parser.add_argument('--canvas', type=str,
                        help='select a canvas with given name')

    args = parser.parse_args()
    args.func(args)
