""" CIS 192 Python Programming
    Do not distribute. Collaboration is NOT permitted.
"""

from copy import deepcopy

# Pro tip: think long and hard about testing your code.
# In this assignment, we aren't giving you example function calls.

"""
O: a sorted copy of a list
I: list
C: no constraints
E: if input is not a list
If input is empty
"""
def my_sort(lst):
    ''' Return a sorted copy of a list. Do not modify the original list. Do
    not use Python's built in sorted method or [].sort(). You may use
    any sorting algorithm of your choice.
    '''
    #edge case 1: if the input is not a list
        #return None
    #edge case 2: if the input list is empty
    if (len(lst) == 0):
        #return an empty list
        return []
    #create a deep copy of the original list - so as not to edit the actual original
    original_list_copy = deepcopy(lst)
    #create a result list
    result = []
    breakpoint()
    #as long as the deep copy has items in it
    while (original_list_copy):
        #set the minimum value to be the first index
        min = original_list_copy[0]
        #iterate over the copy list
        for currentEl in original_list_copy:
            #if an item is less than the min
            if (currentEl < min):
                #set this new num to be the min
                min = currentEl
        #append the min value to the result list
        result.append(min)
        #remove the value from the deep copy list
        original_list_copy.remove(min)
    #return the result list
    return result


"""
O: return a list of key, value tuples --> [(key, val), (key, val), (key, val)]
I: dictionary
C: no constraints
E: if input is not a dictionary
If input is empty
"""
def sort_dict(d):
    ''' Sort a dictionary by value. The function should return
    (not print) a list of key, value tuples, in the form (key, value).
    '''
    #if the input is not a dictionary
        #return none
    #if the input is empty
        #return an empty list
    #first sort the dictionary by values

    #create a result list

    #iterate over the dictionary
        #create a tuple for each key, val pair
        #append this tuple to the list
    #return the list of key val tuples


def prefixes(seq):
    ''' Create a generator that yields all the prefixes of a
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    pass


def suffixes(seq):
    ''' Create a generator that yields all the suffixes of a
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    pass


def slices(seq):
    ''' Create a generator that yields all the slices of a
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    pass


# HALF WAY POINT! Wahoo!


def extract_and_apply(l, p, f):
    '''
    Implement the function below in a single line:

        def extract_and_apply(l, p, f):
            result = []
            for x in l:
                if p(x):
                    result.append(f(x))
            return result

    where l is a list, p is a predicate (boolean) and f is a function.
    '''
    pass


def my_reduce(function, l, initializer=None):
    '''Apply function of two arguments cumulatively to the items of list l, from left to right,
    so as to reduce l to a single value. This is equivalent to the 'fold' function from CIS 120.
    If the optional initializer is present, it is placed before the items of l in the calculation,
    and serves as a default when the sequence is empty.
    If initializer is not given and sequence contains only one item,
    the first item is returned. You may assume that if no initializer is given, the sequence will not
    be empty.
    '''
    pass


class BSTree(object):
    ''' Implement a binary search tree.
    See here: http://en.wikipedia.org/wiki/Binary_search_tree
    or https://www.cis.upenn.edu/~cis120/current/files/120notes.pdf

    Each method you need to implement has its own docstring
    with further instruction. You'll want to move most of the
    implementation details to the Node class below.
    '''

    def __init__(self):
        pass

    def __str__(self):
        ''' Return a representation of the tree as (left, elem, right)
        where elem is the element stored in the root, and left and right
        are the left and right subtrees (which print out similarly).
        Empty trees should be represented by underscores. Do not include spaces.
        '''
        pass

    def __len__(self):
        ''' Returns the number of nodes in the tree.'''
        pass

    def __contains__(self, element):
        ''' Finds whether a given element is in the tree.
        Returns True if the element is found, else returns False.
        '''

    def insert(self, element):
        ''' Insert a given value into the tree.
        Our implementation will allow duplicate nodes. The left subtree
        should contain all elements <= to the current element, and the
        right subtree will contain all elements > the current element.
        '''
        pass

    def elements(self):
        ''' Return a list of the elements visited in an inorder traversal:
        http://en.wikipedia.org/wiki/Tree_traversal
        Note that this should be the sorted order if you've inserted all
        elements using your previously defined insert function.
        '''
        pass


class Node(object):
    ''' A Node of the BSTree.
    Important data attributes: value (or element), left and right.
    '''
    pass


#Testing

#my_sort empty case
print(my_sort([]))

#my_sort regular case
print(my_sort([5, 8, 3, 6, 2]))