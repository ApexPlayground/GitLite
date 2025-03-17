import argparse
import os
from . import data

def main():
    user_argument = parse_arguments()
    user_argument.func(user_argument)

def parse_arguments():
    # create parser argument
    parser = argparse.ArgumentParser()

    sub_commands = parser.add_subparsers(dest='command')# Add subcommands
    sub_commands.required = True # make sure sub command is required

    # create init subcommand parser
    init_parser = sub_commands.add_parser('init')
    init_parser.set_defaults(func=init)# When 'init' is used, call the 'init' function

    # hash object parser for file
    hash_object_parser = sub_commands.add_parser ('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument ('file')
    
    return parser.parse_args()


def init(args: any):
    data.init() # calls the init function from data.py
    print(f'Initialized  empty gitlite repository in {os.path.join(os.getcwd(), data.GIT_DIR)}')

def hash_object(args: any):
    with open(args.file, 'rb') as file:
        # prints the newly hashed file
        print(data.hash_object(file.read()))