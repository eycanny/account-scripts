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
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
