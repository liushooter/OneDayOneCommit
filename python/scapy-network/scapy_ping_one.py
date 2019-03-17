#encoding: utf-8
import sys
import os
import logging
from scapy.all import *
import ipaddress
from random import randint

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def scapy_ping_one(host):
    id_ip = randint(1, 65535)  #随机产生IP ID位置
    id_ping = randint(1, 65535)  #ping ID 位
    seq_ping = randint(1, 65535)  #ping 序列号位

    packet = IP(dst=host, ttl=1, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b"welcome"
    ping = sr1(packet, timeout=2, verbose=False)

    if ping:
        os._exists(3)

if __name__ == '__main__':
    scapy_ping_one(sys.argv[1])

# https://www.bilibili.com/video/av24229682
# https://wizardforcel.gitbooks.io/scapy-docs/content/3.html