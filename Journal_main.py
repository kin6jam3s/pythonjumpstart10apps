"""
This is the Journal_main module.
"""

import os


# Function to load the file 'default' which is the value of journal_name and equal to (name)
def load(name):
    """
    This method creates and loads a new journal

    :param name: This base name of journal to load.
    :return: A new Journal data structure populated with file data.
    """
    data = []  # Initial value of data. Empty list
    # (name) which is equal o 'default' and sent as a variable on function get_full_pathname
    filename = get_full_pathname(name)

    if os.path.exists(filename):  # check if the filename
        with open(filename) as fin:  # with open - open and close the file
            for entry in fin.readlines():  # loop and read the lines
                data.append(entry.rstrip())  # append data on the file for each line - remove white space at the end

    return data  # return the data


# name = journal_name ; journal_data = journal_data
def save(name, journal_data):
    # Get pull path of name(journal_name) using get_full_pathname function
    filename = get_full_pathname(name)
    # print(os.path.abspath(filename)) # will show working folder path
    print('....saving to: {}'.format(filename))

    # opening file(default.jrl) and write all the loaded entry and new entry
    with open(filename, 'w') as fout:  # context manager for cleanup and flash buffer
        for entry in journal_data:  # go through each line of journal_data
            fout.write(entry + '\n')  # write each line and separate by newline

    # fout = open(filename, 'w')
    # fout.close()


# Function for getting the full path or location of the file 'default'
def get_full_pathname(name):
    # os.path.abspath = /Users/ronelordonio/dciv2-code/mypython/pythonjumpstart10apps
    # os.path.join = ./journals/default.jrl
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename  # return /Users/ronelordonio/dciv2-code/mypython/pythonjumpstart10apps/journals/default.jrl


# text = text ; journal_data = data
def add_entry(text, journal_data):
    # This function is only for appending the txt to the journal_data
    journal_data.append(text)
