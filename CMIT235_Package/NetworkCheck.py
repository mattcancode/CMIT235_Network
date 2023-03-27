#######################################
# Matt Miller
# CMIT-235-45: Advanced Python
# March 26, 2023
#
# This module contains the NetworkCheck class, which includes some methods to
# analyze lists and numpy arrays.
#
# Week 3:
#   Added private, protected, and public message attributes.
#   Added attributes and methods to search pcap files for source IP and port.
#
# Week 4:
#   Added overloaded checkCounts methods to scan data in packet file to
#   collect the distribution of data values for features.
#######################################

import numpy as np
import pandas as pd
from scapy.utils import rdpcap
from scapy.layers.l2 import Ether
from scapy.layers.inet import UDP
from multipledispatch import dispatch

class NetworkCheck:

    def __init__(self):
        self.__ip_count = 0
        self.__sport_count = 0

        self.__message1 = "Welcome to message 1"
        self._message2 = "Welcome to message 2"
        self.message3 = "Welcome to message 3"

    def __checkCounts(self, csv_data, *features):
        counts = {}

        df = pd.read_csv(csv_data, sep=',')

        for feature in features:
            counts[feature] = df[feature].value_counts()

        return counts

    @dispatch(str, str)
    def checkCounts(self, csv_data, feature):
        df = pd.read_csv(csv_data, sep=",")
        return df[feature].value_counts()

    @dispatch(str, str, str, str)
    def checkCounts(self, csv_data, feature1, feature2, feature3):
        counts = {}

        df = pd.read_csv(csv_data, sep=',')

        for feature in (feature1, feature2, feature3):
            counts[feature] = df[feature].value_counts()

        return counts

    def getMessage1(self):
        """
        Returns the private welcome message.
        """
        return self.__message1

    def getMessage2(self):
        """
        Returns the protected welcome message.
        """
        return self._message2

    def getSourcePortCount(self):
        """
        Fetches the packet count with source port matches (which is
        set in setSourcePortCount).
        :return: the number of matching packets
        """
        return self.__sport_count

    def setSourcePortCount(self, pcap, port):
        """
        Parses the provided pcap file to count the UDP packets with the
        provided source port.
        The count can be retrieved by calling getSourcePortCount().
        :return: None
        """
        count = 0

        packets = rdpcap(pcap)
        for packet in packets:
            if packet.haslayer(UDP) and packet[UDP].sport == port:
                count += 1

        self.__sport_count = count

    def getSourceIPCount(self):
        """
        Fetches the packet count with source IP matches (which is
        set in setSourceIPCount).
        :return: the number of matching packets
        """
        return self.__ip_count

    def setSourceIPCount(self, pcap, ip):
        """
        Parses the provided pcap file to count the packets with the provided source IP.
        The count can be retrieved by calling getSourceIPCount().
        :return: None
        """
        print(f"searching for '{ip}'")
        count = 0

        packets = rdpcap(pcap)
        for packet in packets:
            if packet.haslayer(Ether) and packet[Ether].src == ip:
                count += 1

        self.__ip_count = count

    def convertList2NpArray(self, source) -> np.ndarray:
        """
        Converts a python list to a numpy array.
        :param source: the list to convert
        :return: np.ndarray the convert numpy array
        """
        return np.array(source)

    def getMax(self, nparray: np.ndarray):
        """
        Returns the maximum value in the array.
        :param nparray: the input array
        :return: the maximum value
        """
        return np.amax(nparray)

    def getMin(self, nparray: np.ndarray):
        """
        Returns the minimum value in the array.
        :param nparray: the input array
        :return: the minimum value
        """
        return np.amin(nparray)

    def getUniqueValues(self, nparray: np.ndarray):
        """
        Returns the unique values found in the array.
        :param nparray: the input array
        :return: the unique values (sorted)
        """
        return np.unique(nparray)

    def getDescriptiveInfo(self, *lists):
        """
        Analyzes lists and returns a dictionary of information about each,
        including dimension, shape, last physical value, first column, and
        last row. The dictionary keys will be prefixed with "list#", where #
        is the index of the lists provided starting with 1.
        [Note that I would prefer to return a list of dictionaries to avoid
        the awkward (and difficult to parse) key names, but the requirements
        called for a single dictionary.]
        :param lists: the lists to evaluate
        :return: dict of information about the lists
        """
        # the information will be collected and return in a dict
        info = {}

        # we iterate using enumerate since it returns an index so we don't
        # need to track some separate variable like a count
        for idx, lst in enumerate(lists, start=1):
            nparray = np.array(lst)

            # since all the information will be in a single dictionary, we'll
            # prefix the keys with the ordered number of the list
            prefix = "list{}_".format(idx)

            # and then collect the expected information
            info[prefix + "dimension"] = nparray.ndim
            info[prefix + "shape"] = nparray.shape
            info[prefix + "last_number"] = nparray[-1, -1]
            info[prefix + "column 0"] = nparray[:, 0]
            info[prefix + "second row"] = nparray[1]

        # done - return the information
        return info
