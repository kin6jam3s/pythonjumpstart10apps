import Journal_main


# from Journal_main import load, save
# from Journal_main import *


def main():
    print_header()
    run_event_loop()


# Function for showing the header
def print_header():
    print('-----------------------')
    print(' Journal App')
    print('-----------------------')


# Function for getting input from user and event loop while x is not press
def run_event_loop():
    # Show the message 'What do you want to do with your journal?'
    print('What do you want to do with your journal?')
    # user cmd initial value is 'EMPTY' which is not equals to 'x'
    cmd = 'EMPTY'
    # Journal file name
    journal_name = 'default'
    # Journal data which is imported fom Journal_main and use the function 'load'
    # journal_name will be the variable to be used on function load
    journal_data = Journal_main.load(journal_name)  # [] # list () # this is the return data from load function

    # Look to get user input while cmd != x and cmd is blank/empty str
    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it:  ')  # user input
        cmd = cmd.lower().strip()  # str input converted to lower case
        if cmd == 'l':
            # Function for listing sending journal_data as data
            list_entries(journal_data)
            # Function for adding sending journal_data as data
        elif cmd == 'a':
            add_entry(journal_data)
            # If user input 'x' or blank str it will close and save the program
        elif cmd != 'x' and cmd:
            print("Sorry, We dont understant '{}'.".format(cmd))

    print('Done, Goodbye!')
    # sending variable journal_name and journal_data to function named save from Journal_main
    Journal_main.save(journal_name, journal_data)


# data = journal_data
def list_entries(data):
    # data save to variable entries in reverse
    entries = reversed(data)
    # Get index number using enumerate and entry on reverse data
    for idx, i in enumerate(entries):
        print(idx + 1, i)
    # print(data)


# Function for adding an entry data = journal_data
def add_entry(data):
    # user input to add any string
    text = input('Type your entry, <enter> to exit: ')
    # data and text will be use as variable for add_entry function on Journal_main program/module
    Journal_main.add_entry(text, data)
    # data.append(text)


print('__file__' + __file__)
print('__name__' + __name__)

if __name__ == '__main__':
    main()
