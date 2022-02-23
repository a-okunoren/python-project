# references: https://www.geeksforgeeks.org/python-shutil-copyfileobj-method/
import requests
import shutil
import os

THIS_FILE_PATH = os.path.abspath(__file__)  # get absolute path of this file
# get path to base folder file is in
BASE_DIR = os.path.dirname(THIS_FILE_PATH)

DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")

# if DOWNLOADS_DIR doesnt exist make the directory
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

url = 'https://cdn.checkyeti.com/images/original/Surfing+%28c%29+Shutterstock.jpg'

# this whole thing good for small files
r = requests.get(url, stream=True)  # stream stops the response

# path to the file we just downloaded
downloaded_image_path = os.path.join(DOWNLOADS_DIR, "1.jpg")
url_filename = os.path.basename(url)  # returns the tail end of the path
# updated path using filename from url
updated_file_path = os.path.join(DOWNLOADS_DIR, url_filename)

with open(downloaded_image_path, 'wb') as f:  # wb is write AND binary mode selected
    # returns the contents of the response to the http call in bytes
    f.write(r.content)

# keep the request open until the entire block ends
with requests.get(url, stream=True) as r:
    with open(updated_file_path, 'wb') as f:
        # shutil.copyfileobj() method in Python is used to copy the contents of a file-like object to another file-like object.
        shutil.copyfileobj(r.raw, f)
