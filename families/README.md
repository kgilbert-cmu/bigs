# Families
Generate images of family trees in fraternity chapters

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


