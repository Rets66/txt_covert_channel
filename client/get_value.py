#!/usr/bin/env python3

import argparse
from base64 import b64decode
import pprint
from sys import argv

import dns.resolver

SUBDOMAIN=['www', 'mail']

def catch_verification(qname: str) -> list:

    response = dns.resolver.query(qname, 'TXT')
    verification_line = [str(i).strip('"') for i in response[:] \
                         if 'verification' in str(i)]

    if verification_line != []:
        return verification_line
    elif verification_line == []:
        print("")
        print("[No record] : This domain looks no verification value.\n")
        exit(0)
    else:
        exit(1)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(usage='get_value.py <URL>')
    parser.add_argument('url')
    args = parser.parse_args()

    qname = args.url
    verification_line = catch_verification(qname)
    pprint.pprint(verification_line)
