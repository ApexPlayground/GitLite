import os

GIT_DIR = '.gitlite'

def init():
    if not os.path.exists(GIT_DIR):
        os.makedirs(GIT_DIR)
    else:
        print(f'The directory {GIT_DIR} already exist')