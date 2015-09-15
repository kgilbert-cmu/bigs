from graph import Graph
from optparse import OptionParser

def parse_prefs(pref_file):
    prefs = {}
    with open(pref_file, 'r') as pf:
        lines = [line.rstrip() for line in pf]
        header = [i for i, x in enumerate(lines) if "\t" not in x]
        header.append(len(lines))
        for f, l in zip(header[:-1], header[1:]):
            nested = lines[(f + 1):l]
            prefs[lines[f]] = [x.lstrip() for x in nested]
    return prefs

def init_parser():
    parser = OptionParser()
    parser.add_option("-b", "--bachelors", dest = "Men", type = "string", help = "")
    parser.add_option("-p", "--houses", dest = "Women", type = "string", help = "")
    (options, args) = parser.parse_args()  # user input is stored in "options"
    return options

def main():
    options = init_parser()
    men = parse_prefs(options.Men)
    women = parse_prefs(options.Women)
    graph = Graph(men, women)
    bipartite = graph.perfectMatching()
    for pair in bipartite:
        print pair, "...", bipartite[pair]

if __name__ == "__main__":
    main()

