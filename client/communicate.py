#!/usr/bin/env python3

import argparse
import base64
from sys import argv

import dns.resolver


SUBDOMAIN={1:'www', 0:'mail'}


def query(qname: str) -> list:
    response = dns.resolver.query(qname, 'TXT')
    verification_line = [str(i).split('=') for i in response[:]\
                        if 'verification' in str(i)]
    return verificaion_line

def create_qname(message: str, length: int=10) -> list:

    cipher = base64.b64encode(message.encode()).decode()
    return [cipher[i: i+length] for i in range(0, len(cipher), length)]


def request(subdomain: list) -> list:

    """ 
    - Query the contents of TXT record
    - Handle the value if the value's line is multi
    """

    for _ in subdomain:
        value = []
        domain = "{0}.{1}".format(_, DOMAIN)
        response = list(dns.resolver.query(domain, 'TXT'))

        pass
        answer.append(res)

    return answer

def decipher(answer: list) -> str:

    """
    - Gather the TXT query's domain authentication value
    - Extract the value of domain verification
    - Decode the strings when the string is decode by base64
    """

    subdomain = [str(i).split('=')[1] for i in answer]
    subdomain = [i.strip(DOMAIN) for i in answer]
    value = [base64.b64decode(i.decode()) for i in _subdomain]

    pass

def main(qname: str) -> str:

    query = create_query(qname)
    answer = request(query)
    print(answer)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                    usage='communicate.py [-h] [-s(specific) | -r(random)]'\
                          '[-d(decode_type) |-i(interval)]',\
                    description='Get the value of domain verification')
    parser.add_argument('-s', '--specific', help='specific domain', \
                        action='store_true')
    parser.add_argument('-r', '--random', help='use randomly generated domain', \
                        action='store_true')
    parser.add_argument('-d', '--decode_type', help='difine the type of decode', \
                        action='store_true')
    parser.add_argument('-i', '--interval', help='difine the interval time of \
                        request packet', action='store_true')

    args = parser.parse_args()
    if args.specific:
        domain = args.domain
        # call function
    if args.random:
        # call randomly generate query
        pass
    if args.decode_type:
        decode = args.decode_type
    if args.interval:
        interval = args.interval
