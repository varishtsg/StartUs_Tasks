"""
Author: Varisht Ghedia

Script to find the most frequent IP's from a access.log. Uses pandas.
"""
import pandas as pd

def top_ip(filename):
    # Open the file
    with open(filename) as f:
        content = f.readlines()
        f.close()

    # The space in timezone causes trouble while loading the data in a dataframe. Thus remove it.
    content = [x.strip().replace(" +", '+') for x in content]

    # Save the data to a temp file to load in dataframe.
    with open('access_mod.log', 'w') as filehandle:
        for listitem in content:
            filehandle.write('%s\n' % listitem)
        filehandle.close()

    # Read to df
    df = pd.read_csv('access_mod.log',sep=" ", names=['IP','User','Group', "Time", "Request", "Status", "PID", "URL", "UA"], engine='python')

    IP_list = df['IP'].value_counts()[:10].index.tolist()

    return IP_list

# ['66.249.73.135', '46.105.14.53', '130.237.218.86', '75.97.9.59', '50.16.19.13', '209.85.238.199', '68.180.224.225', '100.43.83.137', '208.115.111.72', '198.46.149.143']