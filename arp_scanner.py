import optparse
import scapy.all as scapy

parser = optparse.OptionParser()
parser.add_option("-t","--target",dest="ipaddress",help="Enter target IP address or IP address range")
options,args = parser.parse_args()
ip_address = options.ipaddress

arp_request = scapy.ARP(pdst=ip_address)
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

arp_request_broadcast = broadcast/arp_request

answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]

print("IP\t\t\t\tMAC address")
print("----------------------------------------------------------------------")
for i in answered_list:
    print(f"{i[1].psrc}\t\t\t{i[1].hwsrc}")
