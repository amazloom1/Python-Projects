from scapy.all import sniff, IP, TCP, UDP


ip = ''
protocolFilter = input('What protocol would you like to filter (TCP, UDP, or BOTH): ')
ipFilter = input('Would you like to filter for a specific IP address (YES or NO): ')
if ipFilter == 'YES':
    ip = input('Please enter the IP address you want to filter by: ')


def packetRead(packet):
    src = ''
    dst = ''
    protocol = ''
    sPort = ''
    dPort = ''

    if packet.haslayer(IP):
        src = packet.src
        dst = packet.dst
    if packet.haslayer(TCP):
        protocol = 'TCP'
        sPort = packet[TCP].sport
        dPort = packet[TCP].dport
    if packet.haslayer(UDP):
        protocol = 'UDP'
        sPort = packet[UDP].sport
        dPort = packet[UDP].dport

    if packet.haslayer(IP) and (ip == '' or (packet.haslayer(IP) and (packet[IP].src == ip or packet[IP].dst == ip))) and (protocolFilter == 'BOTH' or (protocolFilter == 'TCP' and packet.haslayer(TCP)) or (protocolFilter == 'UDP' and packet.haslayer(UDP))):
        print(f'Source IP: {src} | Destination IP: {dst} | {protocol} source port: {
              sPort} | {protocol} destination port: {dPort}')


sniff(iface='en0', prn=packetRead, count=100)
