Each `.pref` file should be a YAML-like file where nested lists are ordered with whitespace.

"Keys" should start at the beginning of the line. Each value associated with that key should proceed sequentially, separated by newlines, and starting with a tab (`\\t`).

Here is an example:

    key1
        value1
        value2
        value3
    key2
        value1
        ...


I am specifying this convention because:

1. it is easy to read
2. it is easy to edit
3. it is easy to parse

Two example `.pref` files for a graph of 6 people in two equal groups (thus there must be two 3x3 matrices) are given in `Men.pref.example` and `Women.pref.example`.
