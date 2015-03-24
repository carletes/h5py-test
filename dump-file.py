#!/usr/bin/env python

"""Dumps the contents of an HDF5 file."""

import argparse
import sys

from contextlib import closing

import h5py


def dump_item(name, obj):
    print "%s: %s" % (name, obj)


def dump_file(input_file):
    with closing(h5py.File(input_file, "r")) as f:
        f.visititems(dump_item)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=str, help="Input file")
    args = parser.parse_args()
    return dump_file(args.input)


if __name__ == "__main__":
    sys.exit(main())
