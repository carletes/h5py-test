#!/usr/bin/env python

"""Dumps the requested dataset of an HDF5 file."""

import argparse
import sys

from contextlib import closing

import h5py


def dump_dataset(input_file, dataset):
    with closing(h5py.File(input_file, "r")) as f:
        try:
            ds = f[dataset]
        except KeyError:
            print >> sys.stderr, "No dataset '%s'" % (dataset,)
            return 1

        for elem in ds:
            print elem


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=str, help="Input file")
    parser.add_argument("dataset", type=str, help="Dataset to dump")
    args = parser.parse_args()
    return dump_dataset(args.input, args.dataset)


if __name__ == "__main__":
    sys.exit(main())
