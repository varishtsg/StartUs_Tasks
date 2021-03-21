"""
Test script using pytest for validator_if

Author: Varisht Ghedia
"""


from validator import validate_if

def test_size_one():
    """
    Test that password is of size 1.
    """
    assert validate_if("a") == True

def test_size_twentyone():
    """
    Test that password cannot be of size more than 20
    """
    assert validate_if("a"*21) == False


def test_size_twenty():
    """
    Test that password is of size 20.
    """
    assert validate_if("a"*20) == True

def test_latin_start():
    """
    Test that password starts with latin characters.
    """
    assert validate_if("éáíúópaodsipas") == True

def test_number_start():
    """
    Test that password doesn't starts with number.
    """
    assert validate_if("2éáíúópaodsipas") == False

def test_character_start():
    """
    Test that password doesn't starts with special characters.
    """
    assert validate_if("!éáíúópaodsipas") == False

def test_latin_end():
    """
    Test that password ends with latin characters.
    """
    assert validate_if("éáíúópaodsipas") == True

def test_number_end():
    """
    Test that password ends with number.
    """
    assert validate_if("éáíúópaodsipas2") == True

def test_character_end():
    """
    Test that password doesn't end with special characters.
    """
    assert validate_if("éáíúópaodsipas!") == False

def test_dot_minus():
    """
    Test that password can contain "." "-".
    """
    assert validate_if("éáíúóp.ds-ipas") == True

def test_special_chars():
    """
    Test that password cannot contain other special characters.
    """
    assert validate_if("éáíúópao!!dsipas") == False