"""Print out all the melons in our inventory."""
import sys

from melons import melons

def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attribute in melons.items():
        print(melon_name.upper())
        for attribute, value in attribute.items():
            print(f"{attribute}: {value}")
        print("=================================")
