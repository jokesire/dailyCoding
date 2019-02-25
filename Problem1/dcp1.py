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
def sumExists(lst , k):
    seen = set()
    for num in lst:
        d = k - num
        if d in seen:
            return True
        else:
            seen.add(num)
    return False





def main():
    print(sumExists([10,15,3,7], 17))
    print(sumExists([10,15,3,4], 17))
    print(sumExists([10,15,3,7,4,8,9], 12))
    print(sumExists([10,15,3,7,8], 12))

# Main body
if __name__ == '__main__':
    main()
