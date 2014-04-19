FCA-Python
==========

Formal concept analysis lattice generation and query in Python.

## Dependencies
* [NetworkX](http://networkx.github.io/)
* [matplotlib](http://matplotlib.org/)

## Usage

For the following context 



      | 1   |   2   |   3   |   4   |
    --|-----|-------|-------|-------|--
    a | 1   |   0   |   1   |   0   |
    --|-----|-------|-------|-------|--
    b | 1   |   1   |   0   |   1   |
    --|-----|-------|-------|-------|--
    c | 1   |   0   |   1   |   0   |
    --|-----|-------|-------|-------|--
    d | 0   |   1   |   0   |   1   |
    --|-----|-------|-------|-------|--

First input to the script would be the objects:

    a b c d

Second would be the attributes:

    1 2 3 4 5

and third input would be the matrix, in row major order. One row per line:

    1 0 1 0
    1 1 0 1
    1 0 1 0
    0 1 0 1

A file named **lattice.png** would be generated containing the representation of the concept lattice. And you can query the concepts i.e. extent for a given intent or intent for a given extent in terminal.



## Authors
* Pankaj Kumar (me@panks.me)
* Ayesha Siddiqa (m.ayeshasiddiqa@gmail.com)

