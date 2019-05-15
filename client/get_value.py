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

        return verification_line

    except:
        print("")
        print("[No record] : This domain looks no verification value.\n")
        exit(1)


def to_dict(line: list) -> dict:
    response = {}
    for i in line:
        _ = str(i).strip("'[]").split("=")
        key = _[0]
        value = _[1]

        if key in response.keys():
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
    target_host = print_usage()
    verification_line = catch_verification(target_host)

    if len(verification_line) == 0:
        print('')
        print('No verificaion\n')
        exit()
    else:
        response = to_dict(verification_line)

    answer = decode_value(response)
    pprint.pprint(answer)

