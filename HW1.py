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
    if (type(lst) != list):
        #return None
        return None
    #edge case 2: if the input list is empty
    if (len(lst) == 0):
        #return an empty list
        return []
    #create a deep copy of the original list - so as not to edit the actual original
    original_list_copy = deepcopy(lst)
    #create a result list
    result = []
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
    if (type(d) is not dict):
        #return none
        return None
    #if the input is empty
    if (len(d) == 0):
        #return an empty list
        return []
    #first sort the dictionary by values
    sorted_by_keys = sorted(d, key=d.get)
    #create a result list
    resultList = []
    #iterate over the sorted list of keys
    for currkey in sorted_by_keys:
        #create a tuple for each key, val pair from the dictionary
        currentpair = (currkey, d[currkey])
        #append this tuple to the list
        resultList.append(currentpair)
    #return the list of key val tuples
    return resultList

"""
O: generator that yields all prefixes of a given sequence
I: sequence - could be any datatype?
C: none
E: empty sequence?
"""
def prefixes(seq):
    ''' Create a generator that yields all the prefixes of a
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    #iterate over the range of the length of the seq
    for i in range(len(seq) + 1):
        #yield the sequence from 0 up to the current element
        yield seq[0 : i]


def suffixes(seq):
    ''' Create a generator that yields all the suffixes of a
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    # #every time we yield, we want to add a new letter starting from the back
    #iterate over the range of the length of the seq
    for j in range(len(seq) + 1):
        #yield the sequence from the back of the seq down to the first element
        yield seq[len(seq) - j : len(seq)]


"""
O: all the slices of a given sequence
I: arbitrary sequence (datatype not known)
C: none
E: sequence is empty? What do we return??
"""
def slices(seq):
    ''' Create a generator that yields all the slices of a
    given sequence. Extra credit will be rewarded for doing this
    in a single line.
    '''
    #if the sequence is empty
    if (len(seq) == 0):
        #return the sequence
        return seq
    #iterate over the range of the length of the sequence
    for i in range(len(seq)):
        #iterate over the range of the length of the sequence again
        for j in range(i + 1, len(seq)):
            #if i is 0 and j is 1 --> to take care of having an empty case
            if (i == 0 and j == 1):
                yield seq[0:0]
            #yield the sequence from the current i letter to the j letter - the slice of the sequence
            yield seq[i:j]

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
    return [f(x) for x in l if p(x)]


"""
O: a single value reduced
I:  function of 2 elements, an iterable, and a possible initializer value
C: l must be iterable
E: if initializer is given, then start the reduce with this value
If initializer is not given and sequence contains only one item,
    the first item is returned. You may assume that if no initializer is given, the sequence will not
    be empty
"""
def my_reduce(function, l, initializer=None):
    '''Apply function of two arguments cumulatively to the items of list l, from left to right,
    so as to reduce l to a single value. This is equivalent to the 'fold' function from CIS 120.
    If the optional initializer is present, it is placed before the items of l in the calculation,
    and serves as a default when the sequence is empty.
    If initializer is not given and sequence contains only one item,
    the first item is returned. You may assume that if no initializer is given, the sequence will not
    be empty.
    '''
    #if there is an initializer and the sequence is empty
    if (initializer and len(l) == 0):
        #return the initializer
        return initializer
    #if no intializer and sequence contains only one element
    if (initializer == None and len(l) == 1):
        #return the first item
        return l[0]
    #iterate over the list
    for i in range(len(l)):
        #if there is an initializer present and its the first element in the iterable
        if (initializer and i == 0):
            #set accumulator var equal to the result of function call on initializer and first item in the list
            accumulator = function(initializer, l[i])
        #elsif there is no initializer and we're on the first item
        elif (initializer == None and i == 0):
            #set accumulator to the first element
            accumulator = l[i]
        #else
        else:
            #call the function on the accumulator and the current element in the list
            accumulator = function(l[i], accumulator)
    #return the accumulator
    return accumulator


class BSTree(object):
    ''' Implement a binary search tree.
    See here: http://en.wikipedia.org/wiki/Binary_search_tree
    or https://www.cis.upenn.edu/~cis120/current/files/120notes.pdf

    Each method you need to implement has its own docstring
    with further instruction. You'll want to move most of the
    implementation details to the Node class below.
    '''

    def __init__(self):
        #define a root Node for the tree
        self.root = None
        #define a count var for the tree
        self.count = 0

    def __str__(self):
        ''' Return a representation of the tree as (left, elem, right)
        where elem is the element stored in the root, and left and right
        are the left and right subtrees (which print out similarly).
        Empty trees should be represented by underscores. Do not include spaces.
        '''
        pass

    """
    O: integer num
    I: none...well I guess the tree that its being called on
    C: none
    E: none
    """
    def __len__(self):
        ''' Returns the number of nodes in the tree.'''
        #just return the self.count var
        return self.count

    """
    O: boolean whether the item was found or not
    I: integer element to be found
    C: none
    E: if the tree is empty, return false
    """
    def __contains__(self, element):
        ''' Finds whether a given element is in the tree.
        Returns True if the element is found, else returns False.
        '''
        #create inner function - contains_rec(current_node)
        def contains_rec(current_node):
            #if the current node is None
            if (current_node == None):
                #return false
                return False
            #elif the element is equal to the current node's value
            elif (current_node.value == element):
                #return true
                return True
            #elif the element is less than the current node's value
            elif (element < current_node.value):
                #return contains_rec on the left tree
                return contains_rec(current_node.left)
            #else (the element is greater than the current node's value)
            elif (element > current_node.value):
                #return contains_rec on the right tree
                return contains_rec(current_node.right)
        #call and return the inner function on the rootNode (passing in the rootNode)
        return contains_rec(self.root)

    """
    O: no output
    I: element to be added in the tree
    C: element must be in the param list
    E: none
    """
    def insert(self, element):
        ''' Insert a given value into the tree.
        Our implementation will allow duplicate nodes. The left subtree
        should contain all elements <= to the current element, and the
        right subtree will contain all elements > the current element.
        '''
        #create a new Node
        new_node = Node(element)
        #multiple cases: if there is no root Node yet
        if (self.root == None):
            #set the val of the root node
            self.root = new_node
            #increment the node count by one
            self.count += 1
            #return
            return
        #otherwise (root node has been created)
        else:
            #inner recursive function - insert_rec(curr_node)
            def insert_rec(curr_node):
                #if the currentNode is none,
                if (curr_node == None):
                    #set the curr_node equal to the element to be added
                    curr_node = new_node
                    #increment the node count by one
                    self.count += 1
                    #return
                    return
                #elif the element to be added is less than the curr_node's value
                elif (element < curr_node.value):
                    #return insert_rec function on the left tree
                    return insert_rec(curr_node.left)
                #elif the element to be added is greater than or equal to the curr_node's value
                elif (element >= curr_node.value):
                    #return insert_rec function on the right tree
                    return insert_rec(curr_node.right)
            #call and return the inner recursive function on the root node
            insert_rec(self.root)


    """
    O: list of elements in the Tree
    I: no inputs, function called on its own self
    C: none
    E: tree is empty (no insertions yet), then just return empty list
    """
    def elements(self):
        ''' Return a list of the elements visited in an inorder traversal:
        http://en.wikipedia.org/wiki/Tree_traversal
        Note that this should be the sorted order if you've inserted all
        elements using your previously defined insert function.
        '''
        #if the root node is None (meaning there is nothing in the tree yet)
        if (self.root == None):
            #return empty list
            return []
        #create a result list
        result_of_elements = []
        #create inner recursive function - elements_rec(curr_node)
        def elements_rec(curr_node):
            #if node has something
            if (curr_node):
                #if there's a left child
                if (curr_node.left):
                    #call the function on the left child
                    elements_rec(curr_node.left)
                #push the value of the node to the result list
                result_of_elements.append(curr_node.value)
                #if there's a right child
                if (curr_node.right):
                    #call the function on the right child
                    elements_rec(curr_node.right)
        #call the function on the root node
        elements_rec(self.root)
        #return the result list
        return result_of_elements

"""
O: Node of the BSTree with value, left, and right attributes
I: value of the node
C:
E: empty input??
"""
class Node(object):
    ''' A Node of the BSTree.
    Important data attributes: value (or element), left and right.
    '''
    #create constructor
    def __init__(self, value):
        #add attributes to the Node
        self.value = value
        self.left = None
        self.right = None

#Testing

#my_sort empty case
# print(my_sort([]))

# #my_sort regular case
# print(my_sort([5, 8, 3, 6, 2]))

# print(sort_dict({}))

# d = {"Jason": 70, "Bob": 10}
# print(sort_dict(d))

# pre = prefixes('cat')
# print(next(pre)) #''
# print(next(pre)) #'c'
# print(next(pre)) #'ca'
# print(next(pre)) #'cat'


# suffix = suffixes('yes')
# print(next(suffix)) #' '
# print(next(suffix)) # 's'
# print(next(suffix)) # 'es'
# print(next(suffix)) # 'yes'

# slices_name = slices('jas')
# print(next(slices_name)) # ' '
# print(next(slices_name)) # 'j'
# print(next(slices_name)) # 'ja'
# print(next(slices_name)) # 'jas'
# print(next(slices_name)) # 'a'
# print(next(slices_name)) # 'as'
# print(next(slices_name)) # 's'

#Testing my_reduce:
# def my_add(a, b):
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result

# numbers = [0, 1, 2, 3, 4]

# print(my_reduce(my_add, numbers))


# string = 'cat'
# print(string[0:0])
# print(string[0:1])
# print(string[0:2])
# print(string[0:3])
# print(string[2:3])
# print(string[3:3], 'hey')

