import requests
import os
import shutil


# Function for getting
def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    # print(data)
    # For saving use function save_image and send folder, name, and data
    save_image(folder, name, data)


# Function for getting the output from url and return data as binary
def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw  # output is in binary format <urllib3.response.HTTPResponse object at 0x10b3809d0>


# Function for saving file
def save_image(folder, name, data):
    # generate the fullpath of the image
    file_name = os.path.join(folder, name + '.jpg')
    # create and open file and save data as fout
    with open(file_name, 'wb') as fout:
        # shutil copy the binary data to fout
        # print(fout, type(fout))
        shutil.copyfileobj(data, fout)

