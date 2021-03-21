"""
Test script using pytest for make_dict

Author: Varisht Ghedia
"""


from make_dict import make_dict

def test_same_size():
    """
    Test that it can make dictionaries from lists of same size.
    """
    list1 = ['a', 'b', 'c']
    list2 = [1,3,3]

    assert make_dict(list1, list2) == {'a': 1, 'b': 3, 'c': 3}

def test_large_list2():
    """
    Test that it can make dictionaries when list of values is larger than list of keys.
    """
    list1 = ['a', 'b', 'c']
    list2 = [1,3,3,4]

    assert make_dict(list1, list2) == {'a': 1, 'b': 3, 'c': 3}

def test_large_list1():
    """
    Test that it can make dictionaries when list of keys is larger than list of values.
    """
    list1 = ['a', 'b', 'c', 'd']
    list2 = [1,3,4]

    assert make_dict(list1, list2) == {'a': 1, 'b': 3, 'c': 4, 'd': None}

