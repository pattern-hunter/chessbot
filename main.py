import sys
from parse import parse_data

function_name = sys.argv[1]

if function_name == "parse":
    filename = sys.argv[2]
    parse_data(filename)