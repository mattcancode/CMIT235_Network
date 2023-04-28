#######################################
# Matt Miller
# CMIT-235-45: Advanced Python
# April 28, 2023
#
# This module contains the NewNetworkCheck class, which derives from the
# NetworkCheck class but overrides the getDescriptiveInfo method to return
# different metrics about the passed lists.
#
# In week 7, we add a callSuper() method to call a method in a parent class.
#######################################

import numpy as np
from CMIT235_Package.NetworkCheck import NetworkCheck


class NewNetworkCheck(NetworkCheck):
    def __init__(self):
        super().__init__()

    def getDescriptiveInfo(self, *lists):
        """
        Analyzes lists and returns a dictionary of information about each,
        including dimension, shape, mean, median, and standard deviation.
        The dictionary keys will be prefixed with "list#", where #
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
            info[prefix + "mean"] = np.mean(nparray)
            info[prefix + "median"] = np.median(nparray)
            info[prefix + "standard_deviation"] = np.std(nparray)

        # done - return the information
        return info

    def callSuper(self, alist):
        """
        Calls the parent class's getMin() method and prints the result.
        :param alist: the list
        :return: nothing (it would make sense to return the result of getMin()
        but that was not part of the assignment specification)
        """
        # it seems a little unnecessary use super() to make this call since
        # this class does not define an overriding getMin() method so simply
        # calling getMin() directly would have the same effect, but the whole
        # point of this particular change was to use super()
        minimum = super().getMin(self.convertList2NpArray(alist))
        print(f"in NewNetworkCheck.callSuper - minimum is {minimum}")
