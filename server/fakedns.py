#!/usr/bin/env python3

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
    - Extract text file
    - Encode text
    - Add prefix
    - Input TXT the text
    """

    def __init__(self):
        pass

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]

class CreateContent():
    """
    - Extract a line from command.txt
    - Encode the line by some encoding methods such as Base64, etc
    - Put on the prefix to the encoded lien
    """

    def __init__(self):
        pass

    def get_file():
        pass


if __name__ == '__main__':
    pass
