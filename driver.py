###########################################################################################################
# Project 01: Sorting Algorithms
# Course: CPSC 335, Fall 2025
# By: Cameron Abo
# Due Date: 09/30/2025
# Take an array as input and sort the array in ascending order.
#     Count the number of comparisons and swaps made during the sorting process.
#     Return the sorted array, number of comparisons, and number of swaps.
###########################################################################################################

import random
import time
from collections import namedtuple
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort


def generate_random_array(size, max = 10, min = 0):
    """Generate an array of random integers."""
    
    return list(random.randint(min, max) for _ in range(size))

def generate_sorted_array(size, order=0):
    """Generate a sorted array of integers. Order: 0 for ascending, 1 for descending."""
    
    return list(range(size)) if order == 0 else list(range(size, 0, -1))

def main():
    """Main function to test sorting algorithms."""
    
    array_size = 1000

    random = generate_random_array(array_size, array_size)
    ascending = generate_sorted_array(array_size)
    descending = generate_sorted_array(array_size, 1)
    unsorted_arrays = [random, ascending, descending]

    # print('Random Array: ', random)
    # print('Ascending Array:', ascending)
    # print('Descending Array: ', descending)
    # Loop for bubble sort
    for unsorted_array in unsorted_arrays:
        # Set initial time before bubble sort
        start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
 
        # Test Bubble Sort
        bubble_sorted_array, bubble_comparisons, bubble_swaps = bubble_sort(unsorted_array.copy())
        
        # Get final time after bubble sort
        bubble_sort_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - start_time

        print("\nBubble Sort:")
        #print("Sorted Array:", bubble_sorted_array)
        print("Array Size = ", array_size)
        print("Comparisons:", bubble_comparisons)
        print("Swaps:", bubble_swaps)
        print("Time in nanoseconds: ", bubble_sort_time)
    
    # print("\nRandom Array:", random)
    # print("Sorted Array:", ascending)
    # print("Worst Case Array:", descending)
    # Test Insertion Sort
    for unsorted_array in unsorted_arrays:
        # Set initial time before bubble sort
        start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
 
        # Test Bubble Sort
        bubble_sorted_array, bubble_comparisons, bubble_swaps = insertion_sort(unsorted_array.copy())
        
        # Get final time after bubble sort
        bubble_sort_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC) - start_time

        print("\nInsertion Sort:")
        #print("Sorted Array:", bubble_sorted_array)
        print("Array Size = ", array_size)
        print("Comparisons:", bubble_comparisons)
        print("Swaps:", bubble_swaps)
        print("Time in nanoseconds: ", bubble_sort_time)


if __name__ == "__main__":
    main()
