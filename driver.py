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
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

def generate_random_array(size, min=0, max=10000):
    """Generate an array of random integers."""
    return [random.randint(min, max) for _ in range(size)]

def generate_sorted_array(size, order=0):
    """Generate a sorted array of integers. Order: 0 for ascending, 1 for descending."""
    return list(range(size)) if order == 0 else list(range(size, 0, -1))



def main():
    array_size = 10
    random_array = generate_random_array(array_size)
    
    print("Original Array:", random_array)
    
    # Test Bubble Sort
    bubble_sorted_array, bubble_comparisons, bubble_swaps = bubble_sort(random_array.copy())
    print("\nBubble Sort:")
    print("Sorted Array:", bubble_sorted_array)
    print("Comparisons:", bubble_comparisons)
    print("Swaps:", bubble_swaps)
    
    # Test Insertion Sort
    insertion_sorted_array, insertion_comparisons, insertion_swaps = insertion_sort(random_array.copy())
    print("\nInsertion Sort:")
    print("Sorted Array:", insertion_sorted_array)
    print("Comparisons:", insertion_comparisons)
    print("Swaps:", insertion_swaps)


if __name__ == "__main__":
    main()
