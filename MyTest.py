#######################################
# Matt Miller
# CMIT-235-45: Advanced Python
# March 18, 2023
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
#######################################

# we'll need the numpy package so we can use its array class and functions
import numpy as np
# for now, there isn't much in this package, but we need to import the tools
# module since that's where our source data is stored
import CMIT235_Package.CMIT235_Tools as cm


def print_heading(title):
    """Prints a slightly stylized heading to clearly separate sections."""
    print(f"{'-' * 20} {title} {'-' * 20}")


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
    print("The highest number is", array.max())
    print("The lowest number is", array.min())

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


# we'll start by combining the sublists from the companion package and doing
# some analysis (there several ways to combine these lists - I briefly used
# list comprehension to do it, but simple concatenation seems to be the much
# less cumbersome and more readable)
analyze_combined(cm.mySubList1 + cm.mySubList2 + cm.mySubList3)

# next we'll do some slightly different analysis on the individual sublists
# after first converting them to numpy arrays
for sublist in (cm.mySubList1, cm.mySubList2, cm.mySubList3):
    analyze_array(np.array(sublist))
