#######################################
# Matt Miller
# CMIT-235-45: Advanced Python
# April 23, 2023
#
# Week 1 Assignment
# =================
# This program demonstrates basic use of lists, loops, and slicing along with
# the popular third-party NumPy library's arrays. It also demonstrates basic
# modularity by storing input data in a package separate from this module.
#
# Note: I would not normally include some of the very obvious comments you'll
# see below, but figured it would probably better to go a little overboard with
# the documentation initially. If you'd prefer I scale that back in future
# assignments, I'll be more than happy to do so.
#
# Week 2 Assignment
# =================
# In the second week, much of the functionality added in the first week is now
# replicated in the context of a new NetworkCheck class added to the
# CMIT235_Package package. That class does not actually handle print the data
# but instead returns it, leaving it to this module to handle output.
# Also, a new print_weekly_heading function was added so clearly delineate the
# output for this and subsequent weeks.
#
# Week 3 Assignment
# =================
# In the third week, we begin to parse packet capture data using new methods
# added in the NetworkCheck class. We also tinker a bit with distinctions
# between private, protected, and member attributes.
#
# Week 4 Assignment
# =================
# This week adds a NewNetworkCheck that tweaks the metrics analyzed. It also
# adds some csv-parsing methods to the original NetworkCheck to analyze the
# distribution of values in various columns (aka features).
#
# Week 5 Assignment
# =================
# This week adds the AddedNetworkCheck class derived from NewNetworkCheck. It
# includes a new getPingCount method which is called and printed. To demonstrate
# inheritance, we also call through to some methods introduced in previous
# weeks in the parent classes.
#
# Week 6 Assignment
# =================
# This week introduces logging and some additional error/exception handling.
#######################################

import sys
import logging
# we'll need the numpy package so we can use its array class and functions
import numpy as np
# for now, there isn't much in this package, but we need to import the tools
# module since that's where our source data is stored
import CMIT235_Package.CMIT235_Tools as cm
# and, in week 2, we start using the new NetworkCheck module
import CMIT235_Package.NetworkCheck as nc
# and week 4 introduced the NewNetworkCheck module
from CMIT235_Package.NewNetworkCheck import NewNetworkCheck
from CMIT235_Package.AddedNetworkCheck import AddedNetworkCheck


logging.basicConfig(filename="CMIT235_Network.log", level=logging.DEBUG)

logging.info("starting MyTest ...")


def abort(message, exit_code=1):
    """Prints and logs and error message then exits. Exits with code 1 unless overridden by caller."""
    logging.error(message)
    print(f"\nERROR - {message} - ABORTING")
    sys.exit(exit_code)


def print_weekly_heading(week):
    """Prints a slightly stylized heading to clearly separate weeks."""
    print(f"\n{'=' * 20} Week {week} {'=' * 20}\n")


def print_heading(title):
    """Prints a slightly stylized heading to clearly separate sections."""
    print(f"\n{'-' * 20} {title} {'-' * 20}\n")


def analyze_combined(combined):
    """Performs basic analysis on the combined list of sublists."""

    # we'll convert the list into a numpy array to make use of some of its
    # built-in tools (i.e., min, max, and unique)
    array = np.array(combined)

    # start by displaying the combined list itself
    print_heading("Combined List")
    print(combined)

    # numpy provides functions to determine the highest and lowest numbers in
    # the array, which saves me the effort of having to calculate it myself
    print_heading("Max/Min")
    print("The highest number is", np.max(array))
    print("The lowest number is", np.min(array))

    # it's built-in unique function also saves quite a bit of effort though
    # unlike min and max, unique is not a member function of the array itself
    # but rather a function of the numpy module itself so the array is passed in
    print_heading("Unique Numbers")
    print(np.unique(array))


def analyze_array(array):
    """Performs basic analysis on the provided numpy array."""

    # we'll start with some basic dimensional information
    print_heading("Array, Shape, and Dimensions")
    print("The array is:\n", array)
    print(f"It is a {array.ndim}-dimensional array with shape {array.shape}.")

    # then a bit of slicing
    print_heading("Slices")
    # here we just want the item in the last column of the last row
    print("Last item is", array[-1, -1])
    # and here we pass : first to fetch all rows, but then select only column 0
    print("Column 0 is", array[:, 0])
    # using array[1, :] also works, but the second parameter is implied
    print("Second row is", array[1])


print_weekly_heading(1)

# we'll start by combining the sublists from the companion package and doing
# some analysis (there several ways to combine these lists - I briefly used
# list comprehension to do it, but simple concatenation seems to be the much
# less cumbersome and more readable)
combined_list = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
if not isinstance(combined_list, list):
    abort(f"combined_list should be a list but is of type {type(combined_list)}")

analyze_combined(combined_list)

# next we'll do some slightly different analysis on the individual sublists
# after first converting them to numpy arrays
for sublist in (cm.mySubList1, cm.mySubList2, cm.mySubList3):
    analyze_array(np.array(sublist))

###########################################################
# Week 2
###########################################################

networkCheck = nc.NetworkCheck()
if not isinstance(networkCheck, nc.NetworkCheck):
    abort(f"networkCheck should be a NetworkCheck but is of type {type(networkCheck)}")

logging.info("created NetworkCheck instance")

week2combined = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
week2array = networkCheck.convertList2NpArray(week2combined)

print_weekly_heading(2)

week2min = networkCheck.getMin(week2array)
if week2min < -100:
    raise RuntimeError(f"invalid min {week2min} - should be at least -100")

week2max = networkCheck.getMax(week2array)
if week2max > 100:
    raise RuntimeError(f"invalid max {week2max} - should be no more than 100")

print("minimum value =", week2min)
print("maximum value =", week2max)
print("unique values =", networkCheck.getUniqueValues(week2array))

print("\ndescriptive info:")

week2info = networkCheck.getDescriptiveInfo(cm.mySubList1, cm.mySubList2, cm.mySubList3)
if not isinstance(week2info, dict):
    abort(f"week2info should be a dict but is of type {type(week2info)}")

for key, value in week2info.items():
    print("  {} = {}".format(key, value))

###########################################################
# Week 3
###########################################################

print_weekly_heading(3)

# these attempts to directly access the private __message1 attribute should
# fail since Python mangled its name
try:
    message1 = networkCheck.message1
except AttributeError:
    print("unable to access message1")

try:
    message1 = networkCheck.__message1
except AttributeError:
    print("unable to access __message1")

# so I'll need to use the accessor
message1 = networkCheck.getMessage1()

# while I could access the protected attribute, it is frowned on
# so opting for the accessor there as well
message2 = networkCheck.getMessage2()

# and this one is public
message3 = networkCheck.message3

print(f"\nMessage1:{message1:>25}\tMessage2:{message2:>25}\tMessage3:{message3:>25}")

print_heading("Packet Data")

# search the packet data for the provided source IP address
try:
    networkCheck.setSourceMacCount(cm.pcap, cm.mac_address)
except Exception as e:
    abort(f"unable to parse {cm.pcap}: {e}")

source_mac_count = networkCheck.getSourceMacCount()
if not isinstance(source_mac_count, int):
    abort(f"source mac count should be an int but is of type {type(source_mac_count)}")
print(f"Number of packets with source MAC address {cm.mac_address}: {source_mac_count}")

# search the packet data for the provided source port
try:
    networkCheck.setSourcePortCount(cm.pcap, cm.sport)
except Exception as e:
    abort(f"unable to parse {cm.pcap}: {e}")

source_port_count = networkCheck.getSourcePortCount()
if not isinstance(source_port_count, int):
    abort(f"source port count should be an int but is of type {type(source_port_count)}")
print(f"Number of UDP packets with source port {cm.sport}: {source_port_count}")

###########################################################
# Week 4
###########################################################

print_weekly_heading(4)

print("descriptive info:")

# we'll use the new class for this week
newNetworkCheck = NewNetworkCheck()
if not isinstance(newNetworkCheck, NewNetworkCheck):
    abort(f"newNetworkCheck should be a NewNetworkCheck but is of type {type(newNetworkCheck)}")

logging.info("created NewNetworkCheck instance")

# this will invoke the overridden getDescriptiveInfo method
week4info = newNetworkCheck.getDescriptiveInfo(cm.mySubList1, cm.mySubList2, cm.mySubList3)
for key, value in week4info.items():
    print("  {} = {}".format(key, value))

# even though we're still using an instance of the new class, we can call the
# new methods in the original class from which it is derived

print_heading("Individual Feature")
feature3counts = newNetworkCheck.checkCounts(cm.csv_data, cm.feature3)
print(f"{cm.feature3}:\n{feature3counts}")

print_heading("Multiple Feature")
allFeaturesCounts = newNetworkCheck.checkCounts(cm.csv_data, cm.feature1, cm.feature2, cm.feature3)
for feature, counts in allFeaturesCounts.items():
    print(f"{feature}:\n{counts}\n")

###########################################################
# Week 5
###########################################################

print_weekly_heading(5)

week5combined = cm.mySubList1 + cm.mySubList2 + cm.mySubList3
week5array = newNetworkCheck.convertList2NpArray(week5combined)

print("minimum value =", newNetworkCheck.getMin(week5array))
print("maximum value =", newNetworkCheck.getMax(week5array))
print("unique values =", newNetworkCheck.getUniqueValues(week5array))

addedNetworkCheck = AddedNetworkCheck()
if not isinstance(addedNetworkCheck, AddedNetworkCheck):
    abort(f"addedNetworkCheck should be a AddedNetworkCheck but is of type {type(addedNetworkCheck)}")

logging.info("created AddedNetworkCheck instance")

pingCount = addedNetworkCheck.getPingCount(cm.pcap)
if not isinstance(pingCount, int):
    abort(f"ping count should be an int but is of type {type(pingCount)}")
print(f"\nNumber of TCP packets with window size 4095: {pingCount}")

addedNetworkCheck.setSourceMacCount(cm.pcap, cm.mac_address)
print(f"\nNumber of packets with source MAC address {cm.mac_address}: {addedNetworkCheck.getSourceMacCount()}")

print(f"\n{cm.feature3}:\n{addedNetworkCheck.checkCounts(cm.csv_data, cm.feature3)}")
