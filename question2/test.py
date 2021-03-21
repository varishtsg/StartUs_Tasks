"""
Test script using pytest for validator

Author: Varisht Ghedia
"""


from validator import validate

def test_size_one():
    """
    Test that password is of size 1.
    """
    assert validate("a") == True

def test_size_twentyone():
    """
    Test that password cannot be of size more than 20
    """
    assert validate("a"*21) == False


def test_size_twenty():
    """
    Test that password is of size 20.
    """
    assert validate("a"*20) == True

def test_latin_start():
    """
    Test that password starts with latin characters.
    """
    assert validate("éáíúópaodsipas") == True

def test_number_start():
    """
    Test that password doesn't starts with number.
    """
    assert validate("2éáíúópaodsipas") == False

def test_character_start():
    """
    Test that password doesn't starts with special characters.
    """
    assert validate("!éáíúópaodsipas") == False

def test_latin_end():
    """
    Test that password ends with latin characters.
    """
    assert validate("éáíúópaodsipas") == True

def test_number_end():
    """
    Test that password ends with number.
    """
    assert validate("éáíúópaodsipas2") == True

def test_character_end():
    """
    Test that password doesn't end with special characters.
    """
    assert validate("éáíúópaodsipas!") == False

def test_dot_minus():
    """
    Test that password can contain "." "-".
    """
    assert validate("éáíúóp.ds-ipas") == True

def test_special_chars():
    """
    Test that password cannot contain other special characters.
    """
    assert validate("éáíúópao!!dsipas") == False