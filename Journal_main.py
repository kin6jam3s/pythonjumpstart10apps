"""
This is the Journal_main module.
"""

import os


def load(name):
    """
    This methos creates and loads a new jornal

    :param name: This base name of journal to load.
    :return: A new Journal data structure populated with file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    # print(os.path.abspath(filename)) # will show working folder path
    print('....saving to: {}'.format(filename))

    with open(filename, 'w') as fout:  # context manager for cleanup and flash buffer
        for entry in journal_data:
            fout.write(entry + '\n')

    # fout = open(filename, 'w')
    # fout.close()


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


# text = text ; journal_data = data
def add_entry(text, journal_data):
    journal_data.append(text)
