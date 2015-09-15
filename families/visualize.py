from optparse import OptionParser

def init_parser():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest = "File", type = "string", help = "")
    (options, args) = parser.parse_args()  # user input is stored in "options"
    return options

def main():
    options = init_parser()

if __name__ == "__main__":
    main()

