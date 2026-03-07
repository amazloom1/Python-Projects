import socket
import threading
from concurrent.futures import ThreadPoolExecutor

hostIP = input("Enter IP address: ")
sPort = int(input("Enter start port: "))
ePort = int(input("Enter end port: "))

servDict = {
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    67: "dhcp-server",
    68: "dhcp-client",
    69: "tftp",
    80: "http",
    110: "pop3",
    111: "rpcbind/portmapper",
    119: "nntp",
    123: "ntp",
    135: "msrpc",
    137: "netbios-ns",
    138: "netbios-dgm",
    139: "netbios-ssn",
    143: "imap",
    161: "snmp",
    162: "snmptrap",
    389: "ldap",
    443: "https",
    445: "microsoft-ds (smb)",
    465: "smtps",
    500: "ike/isakmp",
    514: "syslog",
    587: "smtp (submission)",
    631: "ipp",
    636: "ldaps",
    873: "rsync",
    993: "imaps",
    995: "pop3s",
    1194: "openvpn",
    1433: "ms-sql-s",
    1521: "oracle",
    1900: "ssdp",
    2049: "nfs",
    3306: "mysql",
    3389: "rdp",
    4500: "ipsec-nat-t",
    5353: "mdns",
    5432: "postgresql",
    5900: "vnc",
    6379: "redis",
    8080: "http-alt",
    8443: "https-alt",
    9200: "elasticsearch (http)",
    27017: "mongodb",
    51820: "wireguard"
}


def scan(h, p):
    addr = (h, p)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(addr)
    if result == 0:
        if p in servDict:
            print(f'{h} is open on port: {p} ({servDict[p]})')
        else:
            print(f'{h} is open on port: {p}')
    sock.close()


def thread():
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(sPort, ePort + 1):
            executor.submit(scan, hostIP, i)


thread()
