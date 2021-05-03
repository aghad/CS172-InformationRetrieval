# This file should contain code to receive either a document-id or word or both and output the required metrics. See the assignment description for more detail.

import argparse
from parsing import process_commands

parser = argparse.ArgumentParser(description='Text retrieval program')
parser.add_argument('--doc', action='store', dest='doc', type=str, help='Lists document information')
parser.add_argument('--term', action='store', dest='term', type=str, help='Lists term information')
args = parser.parse_args()

if args.term and args.doc is not None:
    process_commands(term=args.term, doc=args.doc)
elif args.doc is not None:
    process_commands(doc=args.doc)
elif args.term is not None:
    process_commands(term=args.term)
else:
    # print help if no args
    parser.print_help()