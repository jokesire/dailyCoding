#!/user/bin/env python3 -tt
"""
Module documentation.
"""

# Imports
import sys
#import os

# Global variables

# Class declarations
class Node:
    def __init__(self, val , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Function declarations
def serialize(root):
    if root is None:
        return 'None'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == 'None':
            return None
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

# Main body
if __name__ == '__main__':
    main()
