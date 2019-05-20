#!/usr/bin/env python3

import dns.zone
import socketserver

PORT=9999
HOST='localhost'

# -- Resource Record --
RTYPE_A=1
RTYPE_CNAME=5
RTYPE_MX=15
RTYPE_TXT=16
RTYPE_AAAA=28

class EventHandler(socketserver.BaseRequestHandler):
    """
    - Listen
    - Encode text
    """

    def __init__(self):
        pass

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]

class CreateZone():
    """
    - Extract a line from command.txt
    - Encode the line by some encoding methods such as Base64, etc
    - Put on the prefix to the encoded lien
    """

    def __init__(self):
        pass
    zone = dns.zone.from_text()

    def get_file():
        pass


if __name__ == '__main__':
    pass
