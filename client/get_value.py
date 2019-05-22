#!/usr/bin/env python3

from base64 import b64decode
import pprint
from sys import argv

from dnslib.dns import DNSRecord, DNSHeader, DNSError, QTYPE, EDNS0

def catch_verification(QNAME: str) -> list:

    """Create and send dns query packet"""

    try:
        query_packet = DNSRecord.question(QNAME)
        response = query_packet.send(cache_resolver)
        assert str(resp.get_a().rdata) == LOCALADDR

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


class MessageError(Exception):
    def __init__(self):
        print("Can't "


if __name__ == '__main__':

    if len(argv) != 2:
        print("Usage:\n")
        print("    $ python3 encode_value.py <name server>")
        exit(1)
    else:
        HOST = argv[1]

    verification_line = catch_verification(HOST)

    if len(verification_line) == 0:
        print('')
        print('No verificaion\n')
        exit()
    else:
        response = to_dict(verification_line)

    answer = decode_value(response)
    pprint.pprint(answer)

