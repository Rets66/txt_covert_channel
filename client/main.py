#!/usr/bin/env python3

from argparse import ArgumentParser
import base64
from sys import sys.argv

from scapy.all import *


if sys.argv != 3:

    print("")
    print("* Usage: python3 main.py argment domain")

    if sys.argv == 2:
        print("There aren't either text or domain")
    print("    $ python3 Some_text Auth_dns_server\n")
    sys.exit(1)


def handle_option():

    # parser = argparse.AugmentParser(description='This tool is ')
    # parser.add_argment('-f', action=)
    pass


def separate(qname, length=10):

    """
    - Encode the augument with base64
    - Separate the encoded character
    """

    encoded_char = base64.b64encode(b'{}'.format(qname))
    if len(encoded_char) != 10:
        domain = [encoded_char[i: i+length] for i in range(0, len(encoded_char), length)]
    else:
        domain = encoded_char

    return domain # domain = {'0asdfasdf9', '0asdfasdf9', '0asdfasdf9')


def query(subdomain):

    """ 
    - Query the contents of TXT record
    """

    DOMAIN = sys.argv[2]
    request = "{0}.{1}".format(subdomain, DOMAIN)

    answer = []
    for a in domain:
        answer = send(IP(_)/UDP(dport=53)/DNS(qd=DNSQR(qname=request, qtype=txt))
        answer.append()

    return answer

def parse():
    


def main(argv):

    QNAME = sys.argv[1]
    query(separate(QNAME))


if __name__ == '__main__':
    main()
