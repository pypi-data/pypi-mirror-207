#!/usr/bin/env python

import socket

from twnet_parser.packet import TwPacket, parse7
from twnet_parser.messages7.control.token import CtrlToken
from twnet_parser.messages7.control.connect import CtrlConnect
from twnet_parser.messages7.system.info import MsgInfo

# TODO: import twnet_parser.constants.NET_MAX_PACKETSIZE
NET_MAX_PACKETSIZE = 1400

host = 'localhost'
port = 8303
dest_srv = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))

my_token = b'\xff\xaa\xbb\xee'
srv_token = b'\xff\xff\xff\xff'

def send_msg(messages):
    global srv_token
    if not isinstance(messages, list):
        messages = [messages]
    packet = TwPacket()
    packet.header.token = srv_token
    for msg in messages:
        packet.messages.append(msg)
    print(f"sending {packet.pack()}")
    sock.sendto(packet.pack(), dest_srv)

# TODO: we should be able to set this
# ctrl_token = CtrlToken(we_are_a_client = True)
ctrl_token = CtrlToken()
ctrl_token.response_token = my_token
send_msg(ctrl_token)

while True:
    data, addr = sock.recvfrom(NET_MAX_PACKETSIZE)
    packet = parse7(data)
    print(packet)

    for msg in packet.messages:
        if msg.message_name == 'token':
            srv_token = msg.response_token
            print(f"got server token {srv_token}")

            ctrl_connect = CtrlConnect()
            ctrl_connect.response_token = my_token
            send_msg(ctrl_connect)
        if msg.message_name == 'accept':
            # TODO: make these default values
            send_msg(MsgInfo(
                    version = "0.7 802f1be60a05665f",
                    client_version = 1797
            ))
            print("got accept")
