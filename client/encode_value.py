#!/usr/bin/env python3

import base64
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
            pass

    except:
        exit(1)



if __name__ == '__main__':
    target_host = print_usage()
    main()
