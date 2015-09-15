from optparse import OptionParser
import sys

def init_parser():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest = "File", type = "string", help = "")
    (options, args) = parser.parse_args()  # user input is stored in "options"
    return options

def main():
    options = init_parser()
    if options.File == None:
        print "Error: Did not specify input file."
        sys.exit(1)
    
    pairs = []
    with open(options.File, 'r') as input_file:
        for line in input_file:
            pairs.append(line.strip())
    mapping = {}
    for p in pairs:
        (parent, children) = p.split(":")
        if parent not in mapping:
            mapping[parent] = []
        mapping[parent].extend(children.split(","))

if __name__ == "__main__":
    main()

