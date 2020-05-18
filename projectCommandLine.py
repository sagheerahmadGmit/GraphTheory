#import the packages and class
import argparse
import project

#add the argument parser
parser = argparse.ArgumentParser(add_help=False)
#add the arguments to the parser
parser.add_argument("--instructions", help="In order to run this program, please use the following command 'python3 project.py'. Then follow the instructions on the screen to test your regular expression")
parser.add_argument("--infix", required=True, help="This is the infix that will be compared to the string",type=str)
parser.add_argument("--string", required=True, help="This is the string that will be matched to the infix",type=str)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Default Help Message of Project Command line')

args = parser.parse_args()

#run the match function from the project class
print(" Result:", project.match(str(args.infix), str(args.string)))
