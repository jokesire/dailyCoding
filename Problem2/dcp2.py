#!/user/bin/env python3 -tt
"""
Module documentation.
"""

# Imports
import sys
#import os

# Global variables

# Class declarations

# Function declarations
def productOfAll(lst):
    product = 1
    for num in lst:
        product = num * product
    return product

def productOfAllButi(lst):
    product = productOfAll(lst)
    index = 0
    for num in lst:
        np = product / num
        lst[index] = np
        index = index + 1
    return lst

def main():
    print(productOfAllButi([1,2,3,4,5]))


# Main body
if __name__ == '__main__':
    main()
