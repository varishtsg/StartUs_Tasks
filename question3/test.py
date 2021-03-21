"""
Test script using pytest for make_dict

Author: Varisht Ghedia
"""


from top_ips import top_ip

def test_ips():
    """
    Test that it can make dictionaries from lists of same size.
    """
    file_path = '/home/senpai/Documents/Startus Task/question3/access.log'

    assert top_ip(file_path) == ['66.249.73.135', '46.105.14.53', '130.237.218.86', '75.97.9.59', '50.16.19.13', '209.85.238.199', '68.180.224.225', '100.43.83.137', '208.115.111.72', '198.46.149.143']


