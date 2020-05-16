import argparse
import project

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--nfa", required=True, help="NFA",type=str)
parser.add_argument("--string", required=True, help="String to match to nfa",type=str)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Default Help Message of Project Command line')

args = parser.parse_args()

print(" Result:", match(str(args.nfa), str(args.string)))
