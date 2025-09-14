from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto

        if packet.haslayer('TCP'):
            src_port = packet['TCP'].sport
            dst_port = packet['TCP'].dport
            print(f"Source: {src_ip}:{src_port} -> Destination: {dst_ip}:{dst_port} | Protocol: TCP")

        elif packet.haslayer('UDP'):
            src_port = packet['UDP'].sport
            dst_port = packet['UDP'].dport
            print(f"Source: {src_ip}:{src_port} -> Destination: {dst_ip}:{dst_port} | Protocol: UDP")

        else:
            print(f"Source IP: {src_ip} -> Destination IP: {dst_ip} | Protocol: {protocol}")

sniff(prn=packet_callback, store=False)