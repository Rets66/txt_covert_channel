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

def to_dict(target: list) -> dict:

    response = {}
    for i in target:
        _ = i.split('=')
        key = _[0]
        value = _[1]

        if key in response.keys():
            counter = response.keys()
            key = key + len(reponse.keys())
            response[key] = value
        else:
            response[key] = value

    return response


def decode_value(answer: dict) -> dict:
    try:
        for key, value in answer.items():
            value = base64.b64decode(value.encode()).decode()
            answer[key] = value

        return answer

    except:
        print("")
        print("Can't decode the value file\n")
        exit(1)


if __name__ == '__main__':

    # parser = argparse.ArgumentParser(descriptoin='The manual'):
    # parser.add_argument('-q', type=str, 
    if len(argv) != 2:
        print("Usage:\n")
        print("    $ python3 encode_value.py <name server>")
        exit(1)
    else:
        qname = argv[1]

    verification_line = catch_verification(qname)
    pprint.pprint(verification_line)


    '''if len(verification_line) == []:
        print('')
        print('No verificaion\n')
        exit()
    else:

        response = to_dict(verification_line)'''
