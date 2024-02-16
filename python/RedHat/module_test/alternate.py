# !/usr/bin/env python3
from reusable import *


def main():
    print("Module name is: " + __name__)
    print(square(5), cube(5))

# The * wildcard used above does not actually import all of the module's symbols into the top level symbol table.
#
# It ignores any symbols that start with an underscore.
#
# If a list of strings named __all__ is found in the module
# only the symbols named in the list are imported into the namespace.


if __name__ == "__main__":
    main()
