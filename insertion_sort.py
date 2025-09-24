###########################################################################################################
# Insertion Sort Algorithm 
# By: Cameron Abo
# Due Date: 09/30/2025
# Take an array as input and sort the array in ascending order.
#     Count the number of comparisons and swaps made during the sorting process.
#     Return the sorted array, number of comparisons, and number of swaps.
###########################################################################################################

def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        swaps += 1
    
    return arr, comparisons, swaps