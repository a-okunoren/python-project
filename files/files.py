# references: https://docs.python.org/3/library/functions.html#open
import os  # so you can use paths and stuff
import requests
from download_util import download_file_from_url

fname = 'files/test.txt'  # point to where the file is
# gives the absolute path of the file
this_file_path = os.path.abspath(__file__)
print(this_file_path)
# dirname gives the path to the folder of a file path you give (so one before)
BASE_DIR = os.path.dirname(this_file_path)
print(BASE_DIR)

files_dir = os.path.join(BASE_DIR, "images")
print(files_dir)
if not os.path.exists(files_dir):  # if this path does not exist
    print("This is not a valid path")


# Write to a file
# with open(fname, 'w') as f:  # 'r' is the character that specifies what you want to do with the file (in this case read)
#   f.write("Hello World! ")

# Read a file
with open(fname, 'r') as f:
    content = f.read()  # save the contents of the file in content
    print(content.format(name='Derin'))

my_images = range(0, 12)
# creates the directory if it doesnt exist
os.makedirs(files_dir, exist_ok=True)
######
# for i in my_images:
#    fname = f"{i}.jpeg"
# full path includes base path/images/fname
#    file_path = os.path.join(files_dir, fname)
#    if os.path.exists(file_path):  # if that file path already exists
#        print(f"{fname} already exists")
#        continue
# filepath has absolute path to the file which is better to avoid errors
#    with open(file_path, 'w') as f:
#        f.write("Hello Dee")

url = 'https://mintsnowboarding.com/wp-content/uploads/2018/05/Backcountry-snowboarding-fun-e1604327879909.jpg'
download_file_from_url(url, files_dir)
