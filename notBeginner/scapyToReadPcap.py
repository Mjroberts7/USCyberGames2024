#!/bin/env python3

from scapy.all import rdpcap

packets = rdpcap("tickticktick.pcap")

for packet in packets:
   if 'NTP' in packet:
      timestamp = packet['NTP'].ts
      print(timestamp)


