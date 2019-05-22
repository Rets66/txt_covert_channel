#!/usr/bin/env python3

import socketserver
from dnslib.dns import DNSRecord
from dnslib.server import DNSServer, DNSHandler, DNSResolver

"""
- Listen at ramdom port
- Parse the queries
- Get the subdomain
"""

def handle():
    resolver = BaseResolver()


class CreateZone():
    """
    - Extract a line from command.txt
    - Encode the line by some encoding methods such as Base64, etc
    - Put on the prefix to the encoded lien
    * Ceate lebel file from : https://github.com/TheRook/subbrute
    """

    def __init__(self):
        zone = dns.zone.from_text()

    def get_file():
        with open('label.txt', 'r') as f:
            data = f.read()

    def fake_verification(self):
        return "facebool-verification:"

    def create_answer(self, query, payload):
        answer_packet = query_packet.reply()
        rdata = payload
        answer_packet.add_answer(RR(QNAME, QTYPE, rdata=A()ttl=5)


if __name__ == '__main__':
    host, port = 'localhost', 9999
    with socketserver.UDPServer((host, port), EventHandler) as server:
        server.serve_forever()
