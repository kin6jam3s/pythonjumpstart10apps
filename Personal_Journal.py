import Journal_main
# from Journal_main import load, save
# from Journal_main import *

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------')
    print(' Journal App')
    print('-----------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = Journal_main.load(journal_name)  # [] # list ()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it:  ')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, We dont understant '{}'.".format(cmd))

    print('Done, Goodbye!')
    Journal_main.save(journal_name, journal_data)


# data = journal_data
def list_entries(data):
    entries = reversed(data)
    for idx,i in enumerate(entries):
        print(idx+1,i)
    # print(data)


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    Journal_main.add_entry(text, data)
    # data.append(text)


print('__file__' + __file__)
print('__name__' + __name__)

if __name__ == '__main__':
    main()
