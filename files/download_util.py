import shutil
import requests
import os


# defaults the filename to None to be overwritten if there is no original name
def download_file_from_url(url, directory_path, url_filename=None):
    if url_filename == None:
        # returns the tail end of the path
        url_filename = os.path.basename(url)
        # updated path using filename from url
    file_path = os.path.join(directory_path, url_filename)
    os.makedirs(directory_path, exist_ok=True)
    # keep the request open until the entire block ends
    with requests.get(url, stream=True) as r:
        with open(file_path, 'wb') as f:
            # shutil.copyfileobj() method in Python is used to copy the contents of a file-like object to another file-like object.
            shutil.copyfileobj(r.raw, f)
    return file_path  # return the path to the downloaded file
