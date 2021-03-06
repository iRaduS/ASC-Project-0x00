#!/usr/bin/python3
from sys import argv
from itertools import cycle

if len(argv) != 4:
    print('USAGE: python3 project.py <password> <input_file> <output_file>')
    exit()

if not (argv[1].isalnum()):
    print('ERROR: Password must be a string with lowercase or uppercase letters or numbers.')
    exit()

if len(argv[1]) < 10 or len(argv[1]) > 15:
    print('ERROR: Password must have between 10-15 characters.')
    exit()

def xor(contents, passphrase) -> bytes:
    return bytes(content ^ passchr for content, passchr in zip(contents, cycle(passphrase)))

with open(str(argv[2]), 'rb') as input_file, open(str(argv[3]), 'wb') as output_file:
    output_file.write(xor(input_file.read(), str.encode(str(argv[1]))))