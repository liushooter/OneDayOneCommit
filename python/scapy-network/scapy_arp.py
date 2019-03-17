#encoding: utf-8
import logging
from scapy.all import *
from multiprocessing import Queue, Process

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def scapy_scap_req(ip_address, queue=None, ifname=""):
    result_raw = srp(Ether(dst="FF:FF:FF:FF:FF:FF:") /
        ARP(op=1, hwdst="00:00:00:00:00:00:", pdst=ip_address),
        timeout=2,
        iface=ifname,
        varbose=False)

    try:
        result_list = result_raw[0].res  # 收到结果的数据包

        if queue == None:
            return result_list[0][1].getlayer(ARP).fields["hwsrc"]
        else:
            queue.put((ip_address,result_list[0][1].getlayer(ARP).fields["hwsrc"]))
    except:
        pass


def scapy_scap_scan(network):
    qyt_queue = Queue()
    net = ipaddress.ip_network(network.decode('unicode-escape'))

    for ip in net:
        ip_addr = str(ip)
        arp_one = Process(target=scapy_scap_req, args=(ip_addr, qyt_queue))
        arp_one.start()
    time.sleep(2)

    ip_mac_list = []
    while True:
        if qyt_queue.empty():
            break
        else:
            ip, mac = qyt_queue.get()
            ip_mac_list.append((ip, mac))
    return ip_mac_list


if __name__ == '__main__':
    import sys

    scapy_scap_scan(sys.argv[1])
