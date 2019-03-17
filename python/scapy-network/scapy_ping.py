#encoding: utf-8

import sys
import os
import ipaddress
import multiprocessing
from scapy.all import *

from scapy_ping_one import scapy_ping_one

def scapy_ping_scan(network):
    net = ipaddress.ip_network(network.decode('unicode-escape'))
    ip_processes = {}
    for ip in net:
        ip_addr = str(ip)
        ping_one = multiprocessing.Process(target=scapy_ping_one, args=(ip_addr, ))
        ping_one.start()
        ip_processes[ip_addr] = ping_one

    ip_list = []

    for ip, process in ip_processes.items():
        if process.exitcode == 3:  # 退出码为3 表示ping成功
            ip_list.append(ip)
        else:
            process.terminate()

    return sorted(ip_list)


if __name__ == '__main__':
    import time

    t1 = time.time()
    active_ip = scapy_ping_scan(sys.argv[1])
    print("活动的IP地址如下:")

    for ip in active_ip:
        print(ip)
    t2 = time.time()
    print(t2 - t1)
