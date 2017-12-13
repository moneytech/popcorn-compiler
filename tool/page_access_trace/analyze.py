#!/usr/bin/python3

'''
Analyze a page access trace (PAT) file.
'''

import sys
from sys import float_info
import argparse
from os import path
import pat
import metisgraph

###############################################################################
# Parsing
###############################################################################

def parseArguments():
    parser = argparse.ArgumentParser(
        description="Run various analyses on page access trace (PAT) files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    config = parser.add_argument_group("Configuration Options")
    config.add_argument("-i", "--input", type=str, required=True,
                        help="Input page access trace file")
    config.add_argument("-s", "--start", type=float, default=-1.0,
            help="Only analyze trace entries with timestamps after this time")
    config.add_argument("-e", "--end", type=float, default=float_info.max,
            help="Only analyze trace entries with timestamps before this time")
    config.add_argument("-v", "--verbose", action="store_true",
                        help="Print status updates & verbose files")

    placement = parser.add_argument_group("Thread Placement Options")
    placement.add_argument("-p", "--partition", action="store_true",
        help="Run the graph partitioning algorithm to place threads")
    placement.add_argument("-n", "--nodes", type=int, default=1,
        help="Number of nodes over which to distribute threads")
    placement.add_argument("--gpmetis", type=str, default="gpmetis",
        help="Location of the 'gpmetis' graph partitioning executable")
    placement.add_argument("--save-partitioning", action="store_true",
        help="Save intermediate files generated by partitioning process")

    # TODO make partitioning selectable from command line
    # TODO get binaries, add option to dump which symbols cause most page faults

    return parser.parse_args()

def sanityCheck(args):
    args.input = path.abspath(args.input)
    assert path.isfile(args.input), \
        "Invalid page access trace file '{}'".format(args.input)
    assert args.start < args.end, \
        "Start time must be smaller than end time (start: {}, end: {})" \
        .format(args.start, args.end)

    if args.partition:
        assert args.nodes >= 1, \
            "Number of nodes must be >= 1 ({})".format(args.nodes)

###############################################################################
# Driver
###############################################################################

if __name__ == "__main__":
    args = parseArguments()
    sanityCheck(args)

    if args.partition:
        graph = pat.parsePATtoGraph(args.input, args.start, args.end,
                                    args.verbose)
        metisgraph.placeThreads(graph, args.nodes, args.gpmetis,
                                args.save_partitioning, args.verbose)
