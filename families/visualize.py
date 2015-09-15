from optparse import OptionParser
import sys
import graph

def init_parser():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest = "File", type = "string", help = "")
    parser.add_option("-o", "--output", dest = "Output", type = "string", help = "")
    (options, args) = parser.parse_args()  # user input is stored in "options"
    return options

def main():
    options = init_parser()
    if options.File == None:
        print "Error: Did not specify input file."
        sys.exit(1)
    if options.Output == None:
        print "Warning: Did not specify output file. Defaulting to 'image.pdf'"
        options.Output = "image"
    
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
    image = graph.Graph(mapping)
    image.render(options.Output)

if __name__ == "__main__":
    main()

