#!/usr/bin/env python3

from base64 import b64decode
import pprint
from sys import argv

import dns.resolver

def print_usage():
    if len(argv) != 2:
        print("Usage:\n")
        print("    $ python3 encode_value.py <name server>")
        exit(1)
    else:
        return argv[1]


def query(dst):
    try:
        answer = dns.resolver.query(dst, "TXT")
        verification_line = [str(i).strip('"') for i in answer[:] if 'verification' in str(i)]
        if len(verification) = 0:
            print('No verication')
            exit()
        else:
            to_dict(verification_line)
    except:
        exit(1)


def to_dict(line):

    answer = {}
    for _ in line:
        key_value = _.sprit('=')
        if key_value[0] in answer.keys():
            key_value = key_value[0] + len(answer.keys())
            answer[key_value] = b64decode(key_value[1])
        else:
           answer[key_value[0]] = b64decode(key_value[1])

    pprint.pprint(answer)



if __name__ == '__main__':
    target_host = print_usage()
    
