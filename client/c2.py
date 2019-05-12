#!/usr/bin/env python3

import base64
from sys import argv

import dns.resolver


def check_option():

    if len(argv) != 3:
        print("")
        print("* Usage: python3 main.py argment domain")
        print("    $ python3 <covert message> <authentication_dns server>\n")
        exit(1)

    else:
        message=argv[1]
        domain=argv[2]
        return message, domain


def create_query(message: str, length: int=10) -> list:

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
    message, domain = check_option()
    main(message)
