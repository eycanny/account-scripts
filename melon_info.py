"""Print out all the melons in our inventory."""
import sys

from melons import melons

def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon in melons:
        print(melon.upper())
        for attribute, value in melons[melon].items():
            print(str(attribute) + ": " + str(value))
        print()
