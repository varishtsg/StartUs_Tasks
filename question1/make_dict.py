"""
Author: Varisht Ghedia
"""

def make_dict(list1, list2):
    """
    Makes a dictionary using the provided lists.
    Input:
    list1 (list): List to be used for keys.
    list2 (list): list to be used for values.
    Output:
    out_dict (dict): Dictionary using the input lists
    
    """
    out_dict = {}
    i = 0
    for item in list1:
        out_dict[item] = list2[i] if i < len(list2) else None
        i += 1
        
    return out_dict