#######################################
# Matt Miller
# CMIT-235-45: Advanced Python
# April 16, 2023
#
# This module contains the AddedNetworkCheck class, which derives from the
# NewNetworkCheck class add adds the getPingCount method to count the number
# of pcap TCP packets with window property 4095.
#######################################

from scapy.utils import rdpcap
from scapy.layers.inet import TCP

from CMIT235_Package.NewNetworkCheck import NewNetworkCheck


class AddedNetworkCheck(NewNetworkCheck):

    def __init__(self):
        super().__init__()

    def getPingCount(self, pcap):
        """
        Parses the provided pcap file to count the TCP packets with
        window property 4095.
        :return: number of TCP packets with window property 4095
        """
        count = 0

        for packet in rdpcap(pcap):
            if packet.haslayer(TCP) and packet[TCP].window == 4095:
                count += 1

        return count
