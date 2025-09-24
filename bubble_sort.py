###########################################################################################################
# Bubble Sort Algorithm
# By: Cameron Abo
# Due Date: 09/30/2025
# Take an array as input and sort the array in ascending order.
#     Count the number of comparisons and swaps made during the sorting process.
#     Return the sorted array, number of comparisons, and number of swaps.
###########################################################################################################

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    
    return arr, comparisons, swaps