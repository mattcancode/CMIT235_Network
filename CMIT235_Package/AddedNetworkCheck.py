#######################################
# Matt Miller
# CMIT-235-45: Advanced Python
# April 28, 2023
#
# This module contains the AddedNetworkCheck class, which derives from the
# NewNetworkCheck class add adds the getPingCount method to count the number
# of pcap TCP packets with window property 4095.
#
# In week 7, we add a callGrandparent() method to call the getMax() method
# in the grandparent class.
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

    def callGrandparent(self, alist):
        """
        Calls the grandparent class's getMax() method and prints the result.
        :param alist: the input list
        :return: nothing (it would make sense to return the result of getMax()
        but that was not part of the assignment specification)
        """
        # it seems a little unnecessary use super() to make this call since
        # this neither this class nor the parent NewNetworkCheck class defines
        # an overriding getMax() method so simply calling getMax() directly
        # would have the same effect, but the whole point of this particular
        # change was to use super()
        #
        # note that in this case we don't just call super() because we want to
        # leapfrog the parent class and go straight to the base NetworkCheck
        # (it seems a little unintuitive to pass the immediate parent - class
        # NewNetworkCheck - rather than the grandparent NetworkCheck in which
        # the getMax() method is defined, but the super() method search begins
        # after the specified class)
        maximum = super(NewNetworkCheck, self).getMax(self.convertList2NpArray(alist))
        print(f"in AddedNetworkCheck.callGrandparent - maximum is {maximum}")
