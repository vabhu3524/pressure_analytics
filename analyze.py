#! /usr/bin/env python3

import json
import sys

def count_contractions(pressure_data):
    """
    Count the number of contractions for a pressure curve

    :param pressure_data: a list of pressure points
    :return: The total number of contractions
    """
    # FIXME
    return 0

def contractions_per_sec(pressure_data):
    """
    Calculate the mean contractions / secs for a pressure curve

    :param pressure_data: a list of pressure points
    :return: The mean frequency of contraction / secs
    """
    # FIXME
    return 0

def main():
    pressure_file = sys.argv[1]
    n = 0 # FIXME
    f = 0 # FIXME
    print("---")
    print("For {}:".format(pressure_file))
    print("* Number of contraction = {}".format(n))
    print("* Contraction / s = {}".format(n))

    return 0

if __name__ == '__main__':
    sys.exit(main())
