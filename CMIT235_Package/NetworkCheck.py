#######################################
# Matt Miller
# CMIT-235-45: Advanced Python
# March 26, 2023
#
# This module contains the NetworkCheck class, which includes some methods to
# analyze lists and numpy arrays.
#######################################

import numpy as np


class NetworkCheck:

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
