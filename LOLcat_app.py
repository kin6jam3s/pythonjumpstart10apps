import os
import platform
import subprocess
import cat_service


def main():
    # print the header function
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created a folder: ' '\n' + folder)

    # download cats to folder
    download_cats(folder)
    # display cats using function display_cats and sending folder variable
    display_cats(folder)

    print('hello from main')


# Function for creating the header
def print_header():
    print('------------------')
    print('     CAT FACTORY')
    print('------------------')


def get_or_create_output_folder():
    # __file__ <- /Users/ronelordonio/dciv2-code/mypython/pythonjumpstart10apps/LOLcat_app.py
    # os.path.dirname(__file__) <- /Users/ronelordonio/dciv2-code/mypython/pythonjumpstart10apps
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    # full_path <- /Users/ronelordonio/dciv2-code/mypython/pythonjumpstart10apps/cat_pictures
    full_path = os.path.join(base_folder, folder)
    # verify if folder
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at: \n{}'.format(full_path))
        os.mkdir(full_path)  # creating folder(full_path)

    return full_path  # If full_path folder or directory already exists


# Function for downloading a image of cats in a folder using cat_service module
def download_cats(folder):
    print('Contacting server to download cats')
    # 8 image of cats will be downloaded
    cat_count = 8
    # for loop for appending the number on lolcat_
    for i in range(1, cat_count + 1):  # + 1 increase count to 8
        name = 'lolcat_{}'.format(i)  # generating the 'name' variable
        print('Downloading cat..' + name)
        # print(name, end=',')
        # use another module name cat_service and import get_cat function, sending folder and name variable
        cat_service.get_cat(folder, name)

    print('Done')


# Function for displaying the image on folder per OS
def display_cats(folder):
    # Identifying OS version using platform module and using .system
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        # opening folder base on OS version using subprocess module and using .call
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
        # subprocess.call(['start', folder. shell=True])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('We dont support your OS ' + platform.system())

    # 'open' Darwin/OS X  |   'start' Windows | 'xdg-open' Linux'


if __name__ == '__main__':
    main()
