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


def catch_verification(dst: str) -> list:

    try:
        response = dns.resolver.query(dst, "TXT")
        verification_line = [str(i).strip('"') for i in response[:] if 'verification' in str(i)]

        return velification_line

    except:
        exit(1)


def to_dict(line: list) -> dict:

    response = {}
    for i in line:
        key_value = i.sprit('=')
        if key_value[0] in response.keys():
            key_value = key_value[0] + len(response.keys())
            response[key_value] = key_value[1]
        else:
            response[key_value[0]] = key_value[1]

    return response


def decode_value(answer: dict) -> dict:

    for key, value in answer.items():
        value = base64.b64decode(value.encode()).decode()
        answer[key] = value

    return answer


if __name__ == '__main__':
    target_host = print_usage()
    verification_line = catch_verification(target_host)

    if len(verification_line) = 0:
        print('No verificaion')
        exit()
    else:
        response = to_dict(verification_line)

    answer = decode_value(response)
    pprint.pprint(answer)

