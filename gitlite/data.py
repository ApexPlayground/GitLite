import os
import hashlib

GIT_DIR = '.gitlite'

def init():
    if not os.path.exists(GIT_DIR):
        os.makedirs(GIT_DIR)

        # Create the objects directory inside the .gitlite directory
        os.makedirs(os.path.join(GIT_DIR, 'objects'), exist_ok=True)
    else:
        print(f'The directory {GIT_DIR} already exist')

def hash_object(data: any):

    # if data is str, convert to byte
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Perform sha1 hashing and convert to hexadecimal
    object_ID = hashlib.sha1(data).hexdigest()

    # path to write tha data to
    file_path = os.path.join(GIT_DIR, 'objects', object_ID)

     # Ensure the directory exists before writing to it
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the data to the file
    with open(file_path, 'wb') as out:
        out.write(data)
    
    return object_ID
