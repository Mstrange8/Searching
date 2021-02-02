""" Name: Matthew Strange
    Class: CS2420
    Date: 01/11/2021

    Description: This project implements the linear search,
    the binary search, and the jump search to compare their
    efficiency ins searching.
"""

from time import perf_counter
import math
import random

""" Linear search: Searches the given array in
sequence starting at position 0."""


def linear_search(lyst, target):
    """Searches array using linear search."""
    for i in range(len(lyst)):
        if lyst[i] == target:
            return True
    return False


""" Binary search: Often used for sorted array. Searches the given
array by dividing array in half and searching the
side that has the target."""


def binary_search(lyst, target):
    """Searches array using binary search."""
    low = 0
    high = len(lyst) - 1

    while low <= high:
        mid = (high + low) // 2

        if lyst[mid] < target:
            low = mid + 1

        elif lyst[mid] > target:
            high = mid - 1

        else:
            return True
    return False


""" Jump Search: Often used for sorted arrays: Searches the
given array by dividing it in blocks and searching each
block one at a time in sequence."""


def jump_search(lyst, target):
    """Searches array using jump search."""
    jump = int(math.sqrt(len(lyst)))
    prev = 0

    for i in range(0, len(lyst), jump):
        if lyst[i] < target:
            prev = i
        elif lyst[i] == target:
            return True
        else:
            break

    low = prev
    for x in lyst[prev:]:
        if x == target:
            return True
        low += 1

    return False


def main():
    """main function"""
    lyst = random.sample(range(100000000), k=10000000)

    # Linear search for first element
    start_time = perf_counter()
    linear_search(lyst, lyst[0])
    print("Linear search first element: {:8f} seconds".format(perf_counter() - start_time))

    # Linear search for middle element
    start_time = perf_counter()
    linear_search(lyst, lyst[int(len(lyst)/2)])
    print("Linear search middle element: {:8f} seconds".format(perf_counter() - start_time))

    # Linear search for end element
    start_time = perf_counter()
    linear_search(lyst, lyst[-1])
    print("Linear search end element: {:.8f} seconds".format(perf_counter() - start_time))

    # Linear search for NOT element
    start_time = perf_counter()
    linear_search(lyst, -1)
    print("Linear search NOT element: {:.8f} seconds\n".format(perf_counter() - start_time))

    # Binary search for first element
    start_time = perf_counter()
    binary_search(lyst, lyst[0])
    print("Binary search first element: {:.8f} seconds".format(perf_counter() - start_time))

    # Binary search for middle element
    start_time = perf_counter()
    binary_search(lyst, lyst[int(len(lyst)/2)])
    print("Binary search middle element: {:.8f} seconds".format(perf_counter() - start_time))

    # Binary search for end element
    start_time = perf_counter()
    binary_search(lyst, lyst[-1])
    print("Binary search end element: {:.8f} seconds".format(perf_counter() - start_time))

    # Binary search for NOT element
    start_time = perf_counter()
    binary_search(lyst, -1)
    print("Binary search NOT element: {:.8f} seconds\n".format(perf_counter() - start_time))

    # Jump search for first element
    start_time = perf_counter()
    jump_search(lyst, lyst[0])
    print("Jump search first element: {:.8f} seconds".format(perf_counter() - start_time))

    # Jump search for middle element
    start_time = perf_counter()
    jump_search(lyst, lyst[int(len(lyst)/2)])
    print("Jump search middle element: {:.8f} seconds".format(perf_counter() - start_time))

    # Jump search for end element"""
    start_time = perf_counter()
    jump_search(lyst, lyst[-1])
    print("Jump search end element: {:.8f} seconds".format(perf_counter() - start_time))

    # Jump search for NOT element
    start_time = perf_counter()
    jump_search(lyst, -1)
    print("Jump search NOT element: {:.8f} seconds\n".format(perf_counter() - start_time))


if __name__ == "__main__":
    main()
