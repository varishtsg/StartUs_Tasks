"""
Author: Varisht Ghedia
"""

import re, string

def validate(password):
    """
    Validates password using regexp.
    Input:
    password (string): Password to validate
    Output:
    (boolean): bool if password is valid or not
    """
    regexp = re.compile('^(?=.{1,20}$)(?=[a-zA-Z\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff])[a-zA-Z0-9.-\u00C0-\u00D6\u00D8-\u00f6\u00f8-\u00ff]+(?<![-.])$')
    if regexp.match(password) is not None:
        return True
    else:
        return False



def validate_if(password):
    """
    Validates password using if - else.
    Input:
    password (string): Password to validate
    Output:
    (boolean): bool if password is valid or not
    """

    # Replace - & . with empty string as we need it
    invalid_chars = set(string.punctuation.replace("-", "").replace(".",""))

    if not (0 < len(password) < 21):
        return False
    # Check if password starts with latin characters
    elif not password[0].isalpha():
        return False
    # Check if password ends in special characters
    elif not password[-1].isalnum():
        return False
    # Check if password contains any special characters
    elif any(char in invalid_chars for char in password):
        return False
    else:
        return True

