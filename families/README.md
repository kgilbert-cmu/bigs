# Families
Generate images of family trees in fraternity chapters

## Dependencies

You will need to install `pydot` and `graphviz`. Unfortunately, `graphviz` has some pretty nasty \$PATH bugs and you will very likely run into this issue even after you've installed both programs:

    RuntimeError: failed to execute [some command], make sure the Graphviz executables are on your systems' path

As far as I can tell, it's just a problem with the order in which you install the dependencies (I did graphviz then pydot, for example...). On a Mac, I recommend:

    pip install pydot
    brew install graphviz

## Setup
You will need to specify the connected pairs as (key, value) pairs. The acceptable format is a comma-separated list of Littles paired after each Big by a colon, as in the following example:

    Big:Little1,Little2,Little3

It is also OK to list each `Big:Little` pair on separate lines as in:

    Big:Little1
    Big:Little2
    Big:Little3

## Usage
Run the `visualize.py` program to generate an output PDF file.

Input the list of big/little pairs with the `--file` parameter and the name of the output file with the `--output` parameter.

Use the "`--help`" parameter to see the *Help* dialogue.

    $ > python visualize.py --help
    Usage: visualize.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -f FILE, --file=FILE
      -o OUTPUT, --output=OUTPUT


